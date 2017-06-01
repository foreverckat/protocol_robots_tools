#coding=utf8

'''
# 网络通讯中转服务器
@author: chengjie
'''
 
import threading
import Queue
import select
import copy
import time
import socket
#from robot_Actions import *
#from GlobalTextConfig import robotMsg
try:
    # 配合robotframework 改用其自带的logger输出，使用logging时，会出现意外的配置文件无法找到的情况。必须要写完整路径才可以使用，比较麻烦。
    from robot.api import logger11
except:
    # 若不使用robotframework的框架，则采用本地的logging模块，及对应的logging配置文件来管理日志输出和打印
    import logging
    import logging.config
    logging.config.fileConfig("logging.config")
    logger = logging.getLogger("simpleExample")


MINSocketHeaderLength = 16
SocketHeaderProtocol = ">iiii"
registerSocks = {None:None}
bg_thread_flag = True


def registerManager():
    """
    # 注册管理机
    # 当有外部的机器人，需要注册收包的sock时，需要将自己的sock通过注册管道传递到这里，添加到可使用的字典内。
    """
    logger.info(robotMsg.msg1)
    global bg_thread_lock, bg_thread_flag, registerSocks, registerSocks_Queue, UNregisterSocks_Queue
    registered = []
    while True:
        bg_thread_lock.acquire()
        """
        # 处理传入sock，注册到数据字典内
        """
        if not registerSocks_Queue.empty():
            newRegister_sock = registerSocks_Queue.get()
            logger.info(robotMsg.msg2 % newRegister_sock)
            registerSocks[newRegister_sock] = Queue.Queue()
            if None in registerSocks: del registerSocks[None]
        bg_thread_lock.release()
        
        """
        # 处理传入sock，从数据字典内删除
        """
        bg_thread_lock.acquire()
        if not UNregisterSocks_Queue.empty():
            delRegister_sock = UNregisterSocks_Queue.get()
            logger.info(robotMsg.msg3 % newRegister_sock)
            del registerSocks[delRegister_sock]
            registered.append(delRegister_sock)

        bg_thread_lock.release() 
        """
        # 检查是否已经有sock完成过工作状态，若已有sock完成工作，且管理器处于空闲，则退出管理器
        """
        if len(registered) > 0 and registerSocks_Queue.empty() and UNregisterSocks_Queue.empty():
            break
    logger.info(robotMsg.msg4)

def recvData(sock, data):
    """
    # 粘包处理代码，用于分解粘包、断包、合包的处理
    """
    def returnBroken(o = False, p = "", b = "", h = []):
        return {"ok": o, "packet": p, "BrokenPacket": b, "header":[]}
    
    
    packet, BrokenPacket = data["packet"], data["BrokenPacket"]
    # 合并断包数据
    if len(BrokenPacket):
        packet += BrokenPacket
        BrokenPacket = ""
    try:
        packet += sock.recv(1024)
        # 若接收、合并出来的是空包，则返回空数据结构
        if packet:
            logger.info(repr(packet))
    except:
        return returnBroken(b = packet)
       
    if len(packet) < MINSocketHeaderLength:# 其长度必须大于16，即至少包含最小的header数据
        return returnBroken(b = packet)
    # 分解包头数据     
    PackHeader, PackBody =  packet[:MINSocketHeaderLength], packet[MINSocketHeaderLength:]
    try:
        tag,  packetLength, systemID, protoID  = struct.unpack(SocketHeaderProtocol, PackHeader)
        header = tag,  packetLength, systemID, protoID
        packetLength -= MINSocketHeaderLength
        if packetLength <= 0:
            return returnBroken(b = packet)
    except:
        return returnBroken(b = packet)
        
    # 分析包体数据
    if packetLength == len(PackBody):
        #logger.info("PAKCAGEINFO : package length is %s -- received data length is -- %s" % (packetLength, len(packet)))
        return returnBroken(o = True, p = packet, h = header)
    elif packetLength < len(PackBody):
        PackData, BrokenPacket = PackBody[:packetLength], PackBody[packetLength:] 
        packet = PackHeader + PackData
        #logger.info("PACKAGEINFO : package is larger than definition, length is %s -- received data length is -- %s" % (packetLength, len(packet)))
        return returnBroken(o = True, p = packet, b = BrokenPacket, h = header)
    elif packetLength > len(PackBody):
        #logger.info("PACKAGEINFO : package is smaller than definition, length is %s -- received data length is -- %s" % (packetLength,len(PackBody)))
        return returnBroken(b = packet, h = header)
    else:
        logger.error("can't happen.")

def recvManager():
    """
    # 收包轮询管理
    """
    global bg_thread_lock, bg_thread_flag, registerSocks
    
    selectWaitTime = 0.0 
    sd = {}
    recvable = []
    logger.info(robotMsg.msg7)
    while bg_thread_flag:
        """bg_thread_lock.acquire()
        
        # 清理不存在的sock数据
        
        for ns in registerSocks.keys():
            try:
                ns.fileno()
            except:
                logger.info("sock [%s] not exists, delete it from registerSocks_Queue." % ns)
                del registerSocks[ns]
        bg_thread_lock.release()
        """
        if not len(registerSocks):# 若长度为空，则返回等待新数据过来
            continue
        if None not in registerSocks:
            try:
                recvable , sendable , exceptional = select.select(registerSocks.keys(), [], [], selectWaitTime)
            except:
                pass
            if len(recvable):
                for sock in recvable:
                    bg_thread_lock.acquire()
                    if sock not in sd:
                        logger.info(robotMsg.msg5 % sock)
                        sd[sock] = {"ok": False, "packet":"", "BrokenPacket": "", "header":[]}# 数据结构初始化
                    
                    #logger.info("sock [%s] receiving data." % sock)
                    #sd[sock] = {"ok": True, "packet":sock.recv(1024), "BrokenPacket": "", "header":[]}
                    sd[sock] = recvData(sock, sd[sock])
                    bg_thread_lock.release()
                    
                    if sd[sock]["ok"]:
                        bg_thread_lock.acquire()
                        #logger.info(sd[sock]["ok"])
                        logger.info("data is ready. sock [%s] " % sock)
                        #logger.info("data is [%s]" % repr(sd[sock]))
                        
                        sockdata = copy.deepcopy(sd[sock])
                        registerSocks[sock].put(sockdata)
                        
                        #logger.info("data is [%s]" % repr(sockdata))
                        sd[sock]["packet"] = ""
                        sd[sock]["ok"] = False
                        bg_thread_lock.release()
    logger.info(robotMsg.msg6)
  
class ConnectHandler(threading.Thread):
    def setConnect(self, connect):  
        self.server_agent = connect  
      
    def run(self):
        """
        # 中转服务器的单独代理连接线程
        # 处理数据转发、记录、和连接管理
        """
        while True:
            rd = self.server_agent.recv(128)  
        print "recv data:", rd
        from drpb import pb_pb2
        row = pb_pb2.RowProto()
        
        row.ParseFromString(rd)
        
        print "null_map:", row.null_map
        for x,y in enumerate(row.column):
            print "column%s:" % x, y
            
        
        self.connect.close()  
SERVER_AGENT_HOST = '127.0.0.1'
SERVER_AGENT_PORT = 9999

DEV_CLIENT_AGENT_HOST = ""
DEV_CLIENT_AGENT_PORT = ""
          
class TestServer:
    """
    # 中转测试服务器，真实的客户端会连接到这里，并由测试服务器中转数据给真实的服务器
    # 
    """
    
    def __init__(self):
        pass
      
    def start(self):          
        logger.info("test server agent start at ({0}:{1})...".format(SERVER_AGENT_HOST, SERVER_AGENT_PORT))  
        self.server_agent()

    def client_agent(self):
          
        return
        
        
    def server_agent(self):
        """
        """
        ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
        ss.bind((SERVER_AGENT_HOST, SERVER_AGENT_PORT))  
        ss.settimeout(60*60)  
        ss.listen(5)  
        
        while True:
            try:
                (client, address) = ss.accept()
                ch = server_agent_handler()  
                ch.setConnect(client)  
                ch.start()  
            except Exception,e:
                logger.error(e)
                break
        ss.close()  
        logger.info("TestServer close, bye-bye.")      
      
class server_agent_handler(threading.Thread):

    def setConnect(self, connect):  
        self.agent = connect 
        self.streamData = ""
        self.server_agent = ""

    def run(self):
        """
        # 中转服务器的单独代理连接线程
        # 处理数据转发、记录、和连接管理
        """
        while True:
            recvable , sendable , exceptional = select.select([self.agent,], [], [], 10)
            if len(recvable):
                logger.info(recvable)
                for _sock in recvable:
                    #logger.info(dir(_sock))
                    self.streamData += _sock.recv(1024)
                    logger.info("current streamdata length is %s" % self.streamData )
                    self.streamData = ""

        self.connect.close()  
if __name__ == "__main__":  
    ts = TestServer()  
    ts.start() 