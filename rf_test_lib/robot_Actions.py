#coding=utf8

'''
@author: chengjie
'''
from robot.api import logger
import socket
from LGN import *
import struct
import ProtocolConfig
header_data_Type = ">5i"
header_length    = struct.calcsize(header_data_Type)
Action_Msg_03 = u"连接到服务器：【%s】"

def initConn(func):
    """
    decorator of socket connection
    
    """
    def __decorator(*argus):
        if len(argus) != 2 and type(argus[0]) != str and type(argus[1]) != int:
            logger.error(Action_Msg_01)
            return False
        sock = func(*argus)
        return sock
    return __decorator


 
@initConn
def ConnectHandler(*argus):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(2)
    
    host_IP, host_PORT = argus
    logger.info(Action_Msg_03 % ":".join([host_IP, str(host_PORT)]) )
    try:
        sock.connect((host_IP, int(host_PORT)))
    except Exception, e:
        logger.info(Action_Msg_03 % ":".join([host_IP, str(host_PORT)]) )
        sock.close()
        return None
    return sock




def encrypt_LaunchRequest_pb_Header(func):
    def __deco(**argus):
        package_length = argus["databuf"].ByteSize() + header_length
        header_data = struct.pack(header_data_Type, 1, package_length, *argus["protobuf"])
        argus["package"] = header_data + argus["databuf"].SerializeToString()
        return func(**argus)
    return __deco


def encrypt_LaunchRequest_pb_data(func):
    def __deco(**argus):
        LaunchPackage = getProtocolInfo(*argus["protobuf"])
        LaunchPackage.account = argus["account"]
        LaunchPackage.password = argus["password"]
        LaunchPackage.device = argus["device"]
        argus["databuf"] = LaunchPackage
        return func(**argus)
    
    return __deco

 
def getProtocolInfo(server_Index, protocl_ID, protobuf_ID):
    
    if not server_Index or not protocl_ID or not protobuf_ID:
        return None
    
    if server_Index not in ProtocolConfig.game_protobuf:
        return None
    
    if protocl_ID not in ProtocolConfig.game_protobuf[server_Index]:
        return None
    
    if protobuf_ID not in ProtocolConfig.game_protobuf[server_Index][protocl_ID]:
        return None
    return ProtocolConfig.game_protobuf[server_Index][protocl_ID][protobuf_ID]
    
def decrypt_pb_Header(func): 
    def __deco(data):
        if len(data) >= header_length:
            package_Sign, package_length, server_Index, protocl_ID, protobuf_ID = struct.unpack_from(header_data_Type, data, 0)
            
            if len(data) == package_length:
                pb = getProtocolInfo(server_Index, protocl_ID, protobuf_ID)
                return func(pb.FromString(data[header_length:]))
            else:
                print "error package."
                return False
        else:
            print "error package."
            return False
    return __deco


@encrypt_LaunchRequest_pb_data
@encrypt_LaunchRequest_pb_Header
def encrypt_LaunchRequest_Pack(**argu):
    return argu["package"]

@decrypt_pb_Header
def decrypt_LaunchRequest_Pack(data):
    print data
    return data

def getDataFromPB(data,tag):
    return getattr(data, tag)

def dolaunch(sock = None, account ="yu6786878", password ="121234561233", device="1236578557321"):
    sock.send(encrypt_LaunchRequest_Pack(protobuf = (1, 2, 1), account ="yu6786878", password ="121234561233", device="1236578557321" ))
    data = sock.recv(1024)
    if data:
        return decrypt_LaunchRequest_Pack(data)
    else:
        return False
#sock = ConnectHandler("120.25.152.35", 8091)
#sock.send(encrypt_LaunchRequest_Pack(protobuf = (1, 2, 1), account ="yu6786878", password ="121234561233", device="1236578557321" ))

#data = sock.recv(1024)
#data = '\x00\x00\x00\x01\x00\x00\x01k\x00\x00\x00\x01\x00\x00\x00\x02\x00\x00\x00\x02\n\xac\x01SdDHOVrExpuB7UxdWYIKXmIy60bVQPz6XXd3ko9J/r+JOYY2w03N1FsyQ4bxhU4bWF5AhnkbYNg/FSxAlfoZJlLt8OfL3mnOc4h7l14wHaDBJENoYJ+A341LyWNu0L5u5MiYJ+ZI0C9uOz23D8+KN4VT8a7XgRKMIkzi8J+lNJc=\x12 4feb3c706a494768a9f6906587469807\x18\x80\xa3\x05" 1a3f47148d3f8e222fb2702c9a13a492(\x002*\x08\x01\x12\x0c\xe5\xa4\x96\xe7\xbd\x91\xe6\xb5\x8b\xe8\xaf\x95\x18\x00"\x00*\x14\n\x12120.25.152.35:809320\x08\x02\x12\x07wanglei\x18\x01"\x0c\xe6\xad\xa3\xe5\x9c\xa8\xe7\xbb\xb4\xe6\x8a\xa4*\x13\n\x11192.168.1.36:8093'
#print repr(data)
#if data:
#    decrypt_LaunchRequest_Pack(data)
