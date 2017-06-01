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
          
class TestServer:
    """
    # 中转测试服务器，真实的客户端会连接到这里，并由测试服务器中转数据给真实的服务器
    # 
    """
    CLIENT_LOCAL_HOST = 'localhost'
    CLIENT_LOCAL_PORT = 9999
    def __init__(self):
        self.ip = CLIENT_LOCAL_HOST  
        self.iPort = CLIENT_LOCAL_PORT  
      
    def start(self):          
        logger.info("test server agent start at ({0}:{1})...".format(self.ip, self.iPort))  
                  
        cc = 1          
        ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
        ss.settimeout(1000 * 10)  
        ss.bind((self.ip, self.iPort))  
        ss.listen(5)  
        
        while True:  
            (client, address) = ss.accept()
            cc+=1
            ch = ConnectHandler()  
            ch.setConnect(client)  
            ch.start()  
            
        ss.close()  
        logger.info("TestServer close, bye-bye.")      
      
      
if __name__ == "__main__":  
    ts = TestServer()  
    ts.start() 