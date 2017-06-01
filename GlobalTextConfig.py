#-*- coding=utf8 -*-
"""
    all text msg that needed be shown in code or program
"""

class robotMsg:
    
    def __getattr__(self, name):
        return name

    def __setattr__(self, name, value):
        self.__dict__[name] = value

class robotProto:
    
    def __getattr__(self, name):
        return name

    def __setattr__(self, name, value):
        self.__dict__[name] = value
        
robotMsg.msg1 = "register Manager initialized."
robotMsg.msg2 = "get sock [%s] registered."
robotMsg.msg3 = "get sock [%s] unregistered."
robotMsg.msg4 = "register Manager exited"
robotMsg.msg5 = "sock [%s] initialized"
robotMsg.msg6 = "data receiving Manager exited."
robotMsg.msg7 = "data receiving Manager initialized."
robotMsg.msg8 = "host or port arguments error"
robotMsg.msg9 = "connect to %s failed, %s"
robotMsg.msg10 = u"login susscessfuly：%s"
robotMsg.msg11 = u"server list is empty, error server data got from launch request."
robotMsg.msg12 = u"choose to login server %s, %s"

robotProto.msg1 = u"protocol_ID or protobuf_ID error."
robotProto.msg2 = u"protocol not existed."

#robotMsg.msg3 = "host arguments error"
#robotMsg.msg4 = "connect to %s failed, %s"
#Action_Msg_03 = u"连接到服务器：【%s】"
#Action_Msg_04 = u"机器人就绪. sock [%s]"