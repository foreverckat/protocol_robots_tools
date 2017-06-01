#coding=utf8

'''
@author: chengjie
'''
 
import threading
import Queue
import select
import robot_Actions
from robot.api import logger
import struct
import LGN
# 配合robotframework 改用其自带的logger输出，使用logging时，会出现意外的配置文件无法找到的情况。必须要写完整路径才可以使用，比较麻烦
#import logging
#import logging.config
#logging.config.fileConfig("logging.config")
#logger = logging.getLogger("simpleExample")
import copy
import time
registerSocks = {}
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
    global bg_thread_lock, bg_thread_flag, registerSocks, registerSocks_Queue, UNregisterSocks_Queue
    
    while bg_thread_flag:
        bg_thread_lock.acquire()
        """
        # 处理传入sock，注册到数据字典内
        # 这里的原子操作为：获取机器人客户端传入的待操作sock，并且，建立一个对应的数据书写管道，将管道的对象发送回客户端
        """
        if not registerSocks_Queue.empty():
            newRegister_sock = registerSocks_Queue.get()
            logger.info("get sock [%s] registered." % newRegister_sock)
            registerSocks[newRegister_sock] = Queue.Queue()
        bg_thread_lock.release()
        
        """
        # 处理传入sock，从数据字典内删除
        """
        bg_thread_lock.acquire()
        if not UNregisterSocks_Queue.empty():
            delRegister_sock = UNregisterSocks_Queue.get()
            logger.info("get sock [%s] unregistered." % newRegister_sock)
            del registerSocks[delRegister_sock]
        bg_thread_lock.release() 
    
    logger.info("registerManager exited")
    
def recvManager():
    
    """
    # 收包管理机
    """
    global bg_thread_lock, bg_thread_flag, registerSocks
    
    selectWaitTime = 0.0 
    sd = {}
    recvable = []
    def returnBroken(o = False, p = "", b = "", h = []):
        return {"ok": o, "packet": p, "BrokenPacket": b, "header":[]}
    
    def recvData(sock, data):
        MINSocketHeaderLength = 16
        SocketHeaderProtocol = ">iiii"
        packet, BrokenPacket = data["packet"], data["BrokenPacket"]
        # 合并断包数据
        if len(BrokenPacket):
            packet += BrokenPacket
            BrokenPacket = ""
        try:
            packet += sock.recv(1024)
            # 若接收、合并出来的是空包，则返回空数据结构
            if not len(packet):
                return returnBroken()
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
    
    
    while bg_thread_flag:
        """bg_thread_lock.acquire()
        """
        # 清理不存在的sock数据
        """
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
        
        recvable , sendable , exceptional = select.select(registerSocks.keys(), [], [], selectWaitTime)
        
        if len(recvable):
            for sock in recvable:
                bg_thread_lock.acquire()
                if sock not in sd:
                    logger.info("sock [%s] initialized" % sock)
                    sd[sock] = {"ok": False, "packet":"", "BrokenPacket": "", "header":[]}# 数据结构初始化
                
                #logger.info("sock [%s] receiving data." % sock)
                sd[sock] = recvData(sock, sd[sock])
                bg_thread_lock.release()
                
                if sd[sock]["ok"]:
                    bg_thread_lock.acquire()
                    #logger.info(sd[sock]["ok"])
                    #logger.info("data is ready. sock [%s] " % sock)
                    #logger.info("data is [%s]" % repr(sd[sock]))
                    
                    sockdata = copy.deepcopy(sd[sock])
                    registerSocks[sock].put(sockdata)
                    
                    #logger.info("data is [%s]" % repr(sockdata))
                    sd[sock]["packet"] = ""
                    sd[sock]["ok"] = False
                    bg_thread_lock.release()
    logger.info("manager thread exited.")

def robotCheck(robots):
    global bg_thread_flag
    while bg_thread_flag:
        if len([robot for robot in robots if robot.isAlive()]) == 0:
            bg_thread_flag = False
    logger.info("all robots exited.")


def StartRobot(Host, Port):
    global bg_thread_lock, bg_thread_flag, registerSocks_Queue, UNregisterSocks_Queue
    sock = robot_Actions.ConnectHandler(Host, Port)
    logger.info(LGN.Action_Msg_04 % sock)
    bg_thread_lock.acquire()
    registerSocks_Queue.put(sock)
    bg_thread_lock.release()
    return sock


def robotManager():
    
    global max_robots#bg_thread_lock, bg_thread_flag, registerSocks_Queue, UNregisterSocks_Queue
    
    nt_registerManager = threading.Thread(target = registerManager)
    nt_registerManager.start()
    nt_recvManager     = threading.Thread(target = recvManager)
    nt_recvManager.start()
    #nt_registerManager.join()
    #nt_recvManager.join()
    """
    #tt = []
    #from multiprocessing.dummy import Pool as ThreadPool
    logger.info("started")
    import threadpool
    pool = threadpool.ThreadPool(2)
    reqs = threadpool.makeRequests(robotworker, [])
    [ pool.putRequest(req) for req in reqs ]
    pool.wait()
     
class robotworker(object):
    global bg_thread_lock, bg_thread_flag, registerSocks_Queue, UNregisterSocks_Queue, max_robots
    
    def __init__(self):
        
        #self.sock = ConnectHandler("120.25.152.35", 8091)
        self.sock = ConnectHandler("192.168.1.119", 8091)
        logger.info("robot started. sock [%s]" % self.sock)
        bg_thread_lock.acquire()
        registerSocks_Queue.put(self.sock)
        
            
        bg_thread_lock.release()
        
        st = time.time()
        self.sock.send(encrypt_LaunchRequest_Pack(protobuf = (1, 2, 1), account = str(max_robots + 1), password ="121234561233", device="1236578557321" ))
        while 1:
            if registerSocks.has_key(self.sock) and not registerSocks[self.sock].empty():
                data = registerSocks[self.sock].get()
                #logger.info(registerSocks[self.sock].empty())
                #logger.info(data)
                cryptdata = decrypt_LaunchRequest_Pack(data["packet"])
                logger.info(time.time() - st)
                UNregisterSocks_Queue.put(self.sock)
                break"""


    