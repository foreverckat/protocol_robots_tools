#coding=utf8

'''
@author: chengjie
joker game / google protobuf
 |  should use protobuf Descriptor for python.
 |  
 |  Descriptor for an enum defined in a .proto file.
 |  
 |  An EnumDescriptor instance has the following attributes:
 |  
 |    name: (str) Name of the enum type.
 |    full_name: (str) Full name of the type, including package name
 |      and any enclosing type(s).
 |  
 |    values: (list of EnumValueDescriptors) List of the values
 |      in this enum.
 |    values_by_name: (dict str -> EnumValueDescriptor) Same as |values|,
 |      but indexed by the "name" field of each EnumValueDescriptor.
 |    values_by_number: (dict int -> EnumValueDescriptor) Same as |values|,
 |      but indexed by the "number" field of each EnumValueDescriptor.
 |    containing_type: (Descriptor) Descriptor of the immediate containing
 |      type of this enum, or None if this is an enum defined at the
 |      top level in a .proto file.  Set by Descriptor's constructor
 |      if we're passed into one.
 |    file: (FileDescriptor) Reference to file descriptor.
 |    options: (descriptor_pb2.EnumOptions) Enum options message or
 |      None to use default enum options.
'''

try:
    # 配合robotframework 改用其自带的logger输出，使用logging时，会出现意外的配置文件无法找到的情况。必须要写完整路径才可以使用，比较麻烦。
    from robot.api import logger11
except:
    # 若不使用robotframework的框架，则采用本地的logging模块，及对应的logging配置文件来管理日志输出和打印
    import logging
    import logging.config
    logging.config.fileConfig("logging.config")
    logger = logging.getLogger("simpleExample")
import requests,json  
import socket
import struct
from GlobalTextConfig import robotProto, robotMsg

header_data_Type = ">5i"
header_length   = struct.calcsize(header_data_Type)


from launch.protocol import *

def checkSystemProto(func):
    
    def __deco(systemID, protobufID, protoID):
        ## check proto
        if not systemID:
            logger.error(robotProto.msg1)
            return None
        
        if systemID == 1:
            ProtoIndex = SystemIndex_pb2
            
            if protobufID not in ProtoIndex._SYSTEMTYPE.values_by_number:
                logger.error(robotProto.msg2)
                return None
            
            return func(ProtoIndex, protobufID, protoID)
    return __deco
    
@checkSystemProto
def get_Launch_proto(ProtoIndex, protobufID, protoID):
    """
    # 获取指定协议标签的protobuf数据对象
    # 比如，指定服务器ID为1   -- 登陆服务器，即launchserver
    #       指定协议文件ID为2 -- 在systemindex描述中，即为launchserver的launch协议对象
    #       指定protoID为2    -- 在launch的协议描述中，为launchresponse的协议对象
    # 这样，就可以直接获得指定的协议对象，然后用于后续封装、解包数据结构
    """
    if protobufID == ProtoIndex.LAUNCH: # so the protobuf here is Launch_pb2
        
        if protoID not in Launch_pb2._PROTOID.values_by_number:
            logger.error(robotProto.msg2)
            return None
        
        if protoID == Launch_pb2.LAUNCH_REQ:
            return Launch_pb2.LaunchRequest()
            
        elif protoID == Launch_pb2.LAUNCH_RESPONSE:
            return Launch_pb2.LaunchResponse()
        
        else:
            logger.error(robotProto.msg2)
            return None
    

def encrypt_LaunchRequest_pb_Header(func):
    def __deco(**argus):
        package_length = argus["Body"].ByteSize() + header_length

        argus["header"] = struct.pack(header_data_Type, 1, package_length, *argus["protobuf"])
        
        return func(**argus)
    return __deco


def encrypt_LaunchRequest_pb_data(func):
    def __deco(**argus):
        
        argus["Body"] = get_Launch_proto(*argus["protobuf"])
        argus["Body"].account = argus["account"]
        argus["Body"].password = argus["password"]
        argus["Body"].device = argus["device"]
        argus["Body"].ip = argus["ip"]
        return func(**argus)
    
    return __deco
    
@encrypt_LaunchRequest_pb_data
@encrypt_LaunchRequest_pb_Header
def encrypt_LaunchRequest_Pack(**argus):
    return argus["header"] + argus["Body"].SerializeToString()


def decrypt_pb_Header(func): 
    def __deco(data):
        if len(data) >= header_length:
            package_Sign, package_length, server_Index, protocl_ID, protobuf_ID = struct.unpack_from(header_data_Type, data, 0)
            if len(data) == package_length:
                pb = getProtocolInfo(server_Index, protocl_ID, protobuf_ID)
                return func(pb.FromString(data[header_length:]))
            else:
                return False
        else:
            return False
    return __deco
    
    
@decrypt_pb_Header
def decrypt_LaunchRequest_Pack(data):
    logger.info( data)
    return data
 
#LP = get_Launch_proto(1,2,1)
#LP = Launch_pb2.LaunchRequest()
#LP.account = "12313"
#LP.password = "12313123"
#LP.device = "98494894"
#print 
#print dir(LP)
#print LP.ByteSize()
#data = sock.recv(1024)
#data = '\x00\x00\x00\x01\x00\x00\x01k\x00\x00\x00\x01\x00\x00\x00\x02\x00\x00\x00\x02\n\xac\x01SdDHOVrExpuB7UxdWYIKXmIy60bVQPz6XXd3ko9J/r+JOYY2w03N1FsyQ4bxhU4bWF5AhnkbYNg/FSxAlfoZJlLt8OfL3mnOc4h7l14wHaDBJENoYJ+A341LyWNu0L5u5MiYJ+ZI0C9uOz23D8+KN4VT8a7XgRKMIkzi8J+lNJc=\x12 4feb3c706a494768a9f6906587469807\x18\x80\xa3\x05" 1a3f47148d3f8e222fb2702c9a13a492(\x002*\x08\x01\x12\x0c\xe5\xa4\x96\xe7\xbd\x91\xe6\xb5\x8b\xe8\xaf\x95\x18\x00"\x00*\x14\n\x12120.25.152.35:809320\x08\x02\x12\x07wanglei\x18\x01"\x0c\xe6\xad\xa3\xe5\x9c\xa8\xe7\xbb\xb4\xe6\x8a\xa4*\x13\n\x11192.168.1.36:8093'
#print repr(data)
#if data:
#    decrypt_LaunchRequest_Pack(data)


def initConn(func):
    """
    decorator of socket connection
    """
    def __decorator(*argus):
        if len(argus) != 2 and type(argus[0]) != str and type(argus[1]) != int:
            logging.error(robotMsg.msg8)
            return False
        sock = func(*argus)
        return sock
    return __decorator
 
@initConn
def ConnectHandler(*argus):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(2)
    host_IP, host_PORT = argus
    try:
        sock.connect((host_IP, int(host_PORT)))
    except Exception, e:
        logging.error(robotMsg.msg9 % (":".join([host_IP, str(host_PORT)]), e))
        sock.close()
        return None
    return sock


def HttpRequest_Post(func):
    def _deco(**argus):
        return func(requests.post(argus["_url"], data = json.dumps(argus["_data"])))
    return _deco


class robotData:
    
    def __getattr__(self, name):
        return name

    def __setattr__(self, name, value):
        self.__dict__[name] = value


@HttpRequest_Post
def doLaunch(ret):
    """
    ret.json() = {
                    u'account': u'a22d56', 
                    u'hash': u'e45f64febdf8d23982b5fc1f94613b5b', 
                    u'uid': 1260, 
                    u'isNew': False, 
                    u'myServerList': [], 
                    u'token': u'Jlf8XQWl7Mwx16BJy/Gf84EgO+tHaeBmeXHL9ZwoPh2uaPkD7a3jDaGDBN5elq2IynVS/cCO2MrFO06uJsM9jUqE1lYEfEfGuIqeRn6SJVBE3K7WRdp1kVHMA/zvrJOOPV0D1a1jgXAlpdWjmAICejjcX55TtXskdGw62xFJHfs=', 
                    u'session': u'92bd4efbbd74427a9402b913aa3ad857', 
                    u'result': True, 
                    u'expire': 86400, 
                    u'serversList': [{
                                       u'serverName': u'stress', 
                                       u'serverStatus': 0, 
                                       u'statusInfo': u'', 
                                       u'serverId': 1, 
                                       u'gateServerList': [
                                                            {u'hostAddress': u'192.168.1.135:8093'}
                                                            ]}]}
    """
    for k, v in ret.json().items():
        setattr(robotData, k, v)
    
    if robotData.isNew:
        logger.info("new role")

    if len(robotData.serversList) <= 0:
        logger.error(robotMsg.msg11)
    else:
        testArea = 0
        testServer = 0
        
        gateServersList = robotData.serversList[testArea]
        #if gateServers["serverStatus"] != 0:
        
        gateServer = gateServersList["gateServerList"][testServer]
        logger.info(robotMsg.msg12 % (gateServersList["serverName"], gateServer["hostAddress"]))
        robotData.gateServer = gateServer["hostAddress"].split(":")
        return robotData
            
