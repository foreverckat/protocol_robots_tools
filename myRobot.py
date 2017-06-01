#coding=utf8

'''
#提供给rf使用的robot框架，用于模拟客户端对服务端进行协议通讯、数据交互模拟，并使用rf进行针对通讯协议的数据、次序等内容进行协议测试用例设计和自动化测试执行。
@author: chengjie
'''
 
import threading
import Queue
import select
import copy
import time
import socket
from robot_Actions import *
from GlobalTextConfig import robotMsg
try:
    # 配合robotframework 改用其自带的logger输出，使用logging时，会出现意外的配置文件无法找到的情况。必须要写完整路径才可以使用，比较麻烦。
    from robot.api import logger1111111111111111
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
max_robots = 1
bg_thread_lock = threading.Lock()
registerSocks_Queue = Queue.Queue()
UNregisterSocks_Queue = Queue.Queue()


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

def robotCheck(robots):
    global bg_thread_flag
    while bg_thread_flag:
        if len([robot for robot in robots if robot.isAlive()]) == 0:
            bg_thread_flag = False
    logger.info("all robots exited.")
    
def robotManager():
    """
    # 依次启动socket发包线程注册管理器，以及统一的socket收包管理线程
    """
    nt_registerManager = threading.Thread(target = registerManager)
    nt_registerManager.start()
    
    nt_receiverManager = threading.Thread(target = recvManager)
    nt_receiverManager.start()
    

def getData(sock):
    global bg_thread_lock
    while 1:
        #time.sleep(0.5)
        if sock not in registerSocks:
            continue
        elif not registerSocks[sock].empty():
            bg_thread_lock.acquire()
            data = registerSocks[sock].get()
            bg_thread_lock.release()
            return data
        


def dolaunch(_sock = None, _account ="yu6786878", _password ="121234561233", _device="1236578557321", _ip = "192.168.1.1"):
    _sock.send(encrypt_LaunchRequest_Pack(protobuf = (1, 2, 1), account = _account, password = _password, device= _device, ip = _ip ))
    data = getData(_sock)
    if data:
        return decrypt_LaunchRequest_Pack(data)
    else:
        return False



def closeRobot(sock):
    global bg_thread_lock
    bg_thread_lock.acquire()
    UNregisterSocks_Queue.put(sock)
    bg_thread_lock.release()
    sock.close()


def startRobot(_acc = "robot", _pwd = "robot", _dev = "RobotProtobuf", _ls = "http://192.168.1.134:8091/"):
    
    global bg_thread_lock, bg_thread_flag, registerSocks_Queue, UNregisterSocks_Queue

    _robot = doLaunch(_url = _ls, _data = {"serverId": 1,"systemId": 2,"protoId": 2,"data": {"account": _acc, "password": _pwd,"device": _dev}})
    sock = ConnectHandler(_robot.gateServer[0], int(_robot.gateServer[1]))
    logger.info(robotMsg.msg10 % sock)

    bg_thread_lock.acquire()
    registerSocks_Queue.put(sock)
    bg_thread_lock.release()
    
    #dolaunch(_sock = sock)

    #logger.info("send data")
    #logger.info( repr(getData(sock)))
    #closeRobot(sock)
    return



if __name__ == "__main__":
    """
    # 协议模拟工具的主体运行逻辑
    # 并发足够的线程启动，使用最简单的线程并发方式
    # 因受限GIL，会有并发性能问题
    """
    logger.error("tool started.")
    st = time.time()
    robotManager()
    t = []
    maxRobot = 1
    serverHost = "192.168.1.132"
    serverPort = 8091
    
    for n in range(maxRobot):
        nt = threading.Thread(target = startRobot, args = (serverHost, serverPort))
        nt.start()
        nt.join()

    bg_thread_flag = False
    logger.info("finished in %s" % (time.time() - st))