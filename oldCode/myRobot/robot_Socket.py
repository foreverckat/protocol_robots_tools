#coding=utf8

'''
@author: chengjie
'''
import socket
import logging
import threading
import Queue
import select
import struct
import time
import random

class socketManager(threading.Thread):
    """
        发包的处理
        采用单独线程，通过select方法进行待收包的socket管理
    """
    def __init__(self):
        threading.Thread.__init__(self)
        self.lock = threading.Lock()
        self.recvSockets = []
        self.sockdata = {}
        self.setManagerFlag(True)
        self.closeSockets = []
        self.robotIDs = []
        
        
    def setManagerFlag(self, flag):
        self.managerFlag = flag
    
    def closeTcp(self, sock):
        self.lock.acquire()
        if sock in self.recvSockets:
            self.recvSockets.remove(sock)
            #logging.info("recvSockets removed sock [%s]" % sock)
        if sock in self.sendList:
            self.sendList.remove(sock)
            #logging.info("sendList removed sock [%s]" % sock)
        sock.close()
        self.closeSockets.append(sock)
        self.lock.release()
        
        #logging.info("sock closed - %s" % sock)
        
    def closeManager(self):
        self.setManagerFlag(False)
        
    
    
    def connectTcp(self, host):
        """
        connect to specified server through tcp connection.
        """
        
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        try:
            sock.connect(host)
            sock.settimeout(0.0)
            #logging.info("connect to %s successfully" % (":".join([str(x) for x in host])))
        except Exception, e:
            logging.info("connect to %s failed, %s" % (":".join([str(x) for x in host]), e))
            sock.close()
            return None
        self.lock.acquire()
        self.recvSockets.append(sock)
        self.lock.release()
        return sock
    
    def run(self):
        # select method, choose send or recv function.
        #logging.info("manager threading started, attached on sock[%s]" % sock)
        selectWaitTime = 0.0 
        sd = {}
        recvable = []
        self.sendList = []
        self.msg = {}
        while self.managerFlag:
            
            
            
            self.lock.acquire()
            for ns in self.recvSockets:
                try:
                    ns.fileno()
                except:
                    self.recvSockets.remove(ns)
            for ns in self.sendList:
                try:
                    ns.fileno()
                except:
                    self.sendList.remove(ns)
            self.lock.release()
            if not len(self.recvSockets):
                
                continue
            
            recvable , sendable , exceptional = select.select(self.recvSockets, self.sendList, [], selectWaitTime)
                        
            if len(sendable):
                
                for nsock in sendable:
                    self.lock.acquire()
                    
                    if self.msg.has_key(nsock) and not self.msg[nsock].empty():
                        sd[nsock] = self.msg[nsock].get_nowait()
                    if nsock in self.sendList: 
                        self.sendList.remove(nsock)
                        ##logging.info("sendlist removed sock [%s]" % nsock)
                    self.lock.release()
                    
            if len(recvable):
                for sock in recvable:
                    #logging.info("handled with sock -  [%s]" % sock)
                    try:
                        nt = threading.Thread(target = self.handleRECV, args=(sock, sd))
                        nt.start()
                        nt.join()
                    except:
                        self.lock.acquire()
                        self.recvSockets.remove(sock)
                        self.lock.release()
                    nt.join()
                    
        logging.info("manager thread exited.")

    def handleRECV(self, sock, sd):
        
        if sock not in sd:
            sd[sock] = {"ok": False, "packet":"", "BrokenPacket": "", "canParseLength":False}
        
        sd[sock] = recvData(sock, sd[sock])
        
        #logging.info("recv finished. result is %s, packet is [%s]" % (sd[sock]["ok"], sd[sock]["packet"]))
        self.lock.acquire()
        if sd[sock]["ok"]:
            # 将数据写会主线程监听队列
            if sock not in self.sockdata:
                self.sockdata[sock] = Queue.Queue()
            self.sockdata[sock].put(sd[sock]["packet"])
            # 处理循环数据
            sd[sock]["packet"] = ""
            if len(sd[sock]["BrokenPacket"]):
                sd[sock]["packet"] = sd[sock]["BrokenPacket"]
                sd[sock]["BrokenPacket"] = ""
            # 将数据写回select循环
        if sock not in self.msg:
            self.msg[sock] = Queue.Queue()
        self.msg[sock].put_nowait(sd[sock])    
        
        # 通知select，可以处理
        if sock not in self.closeSockets:
            #logging.info("sock died. [%s]" % sock)
            self.sendList.append(sock)
            
        self.lock.release()
       
def recvData(sock, sd):
    
    packet, BrokenPacket, canParseLength = sd["packet"], sd["BrokenPacket"], sd["canParseLength"]
    #if len(packet):
        #logging.info("started receiving data with packet [%s]" % packet)
    # 若sock没有对应的数据，则初始化一套
    MINSocketHeaderLength = 16
    #logging.info(sock)
    try:
        packet += sock.recv(1024)
    except:
        return {"ok": False, "packet": packet, "BrokenPacket": "", "canParseLength":False}
    #logging.info("packet is [%s]" %packet)
    if not len(packet):
        return {"ok": False, "packet": packet, "BrokenPacket": "", "canParseLength":False}
        
    if not len(BrokenPacket):# 如果是非断包、粘包，其长度必须大于12，即至少包含最小的header数据
        if len(packet) >= MINSocketHeaderLength:
            canParseLength = True
        else:
            return {"ok": False, "packet": packet, "BrokenPacket": "", "canParseLength":False}
    else:# 若是断包、粘包状态，则分情况处理
        if len(packet) >= MINSocketHeaderLength: # 粘包状态下，拼接后大于最小字节要求的，可以进行处理
            canParseLength = True
        else:# 粘包状态拼接后都不满足的，则不处理，重新尝试收包
            canParseLength = False
    if canParseLength:# 若可以处理包，则处理之
        PackHeader, PackBody =  packet[:MINSocketHeaderLength], packet[MINSocketHeaderLength:]
        try:
            tag,  packetLength, systemID, protoID  = struct.unpack(">iiii", PackHeader)
            packetLength -= MINSocketHeaderLength
        except:
            return {"ok": False, "packet": packet, "BrokenPacket": "", "canParseLength":False}
            
    else:
        return {"ok": False, "packet": packet, "BrokenPacket": "", "canParseLength":False}
        
    
    if packetLength <= 0:
        #logging.info("error data-packet length(data less than 0).")
        return {"ok": False, "packet": packet, "BrokenPacket": "", "canParseLength":False}
        
    else:
        if packetLength == len(PackBody):
            #logging.info("PAKCAGEINFO : package length is %s -- received data length is -- %s" % (packetLength, len(packet)))
            #logging.info("data is [%s]" % packet)
            return {"ok": True, "packet": packet, "BrokenPacket": "", "canParseLength":False}
        
        elif packetLength < len(PackBody):
            PackData, BrokenPacket = PackBody[:packetLength], PackBody[packetLength:] 
            packet = PackHeader + PackData
            #logging.info("PACKAGEINFO : package is larger than definition, length is %s -- received data length is -- %s" % (packetLength, len(packet)))
            #logging.info("data is [%s]" % packet)
            #logging.info("left data is %s" % BrokenPacket)
            return {"ok": True, "packet": packet, "BrokenPacket": BrokenPacket, "canParseLength":False}
            
            
        elif packetLength > len(PackBody):
            #logging.info("PACKAGEINFO : package is smaller than definition, length is %s -- received data length is -- %s" % (packetLength,len(PackBody)))
            #logging.info("data is [%s]" % packet)
            
            return {"ok": False, "packet": packet, "BrokenPacket": "", "canParseLength":False}