# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='jokersvr.protocol/JokerServer.proto',
  package='commonProtocal.JokerServerProto',
  serialized_pb='\n#jokersvr.protocol/JokerServer.proto\x12\x1f\x63ommonProtocal.JokerServerProto*O\n\nServerType\x12\x08\n\x04NONE\x10\x00\x12\x0e\n\nLAUNCH_SVR\x10\x01\x12\x0b\n\x07LOG_SVR\x10\x02\x12\x0c\n\x08GAME_SVR\x10\x03\x12\x0c\n\x08GATE_SVR\x10\x04')

_SERVERTYPE = descriptor.EnumDescriptor(
  name='ServerType',
  full_name='commonProtocal.JokerServerProto.ServerType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='NONE', index=0, number=0,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='LAUNCH_SVR', index=1, number=1,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='LOG_SVR', index=2, number=2,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='GAME_SVR', index=3, number=3,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='GATE_SVR', index=4, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=72,
  serialized_end=151,
)


NONE = 0
LAUNCH_SVR = 1
LOG_SVR = 2
GAME_SVR = 3
GATE_SVR = 4



# @@protoc_insertion_point(module_scope)
