# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='launch.protocol/SystemIndex.proto',
  package='launch.protocal',
  serialized_pb='\n!launch.protocol/SystemIndex.proto\x12\x0flaunch.protocal*2\n\nSystemType\x12\x0f\n\x0bSERVERERROR\x10\x01\x12\n\n\x06LAUNCH\x10\x02\x12\x07\n\x03LOG\x10\x03')

_SYSTEMTYPE = descriptor.EnumDescriptor(
  name='SystemType',
  full_name='launch.protocal.SystemType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='SERVERERROR', index=0, number=1,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='LAUNCH', index=1, number=2,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='LOG', index=2, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=54,
  serialized_end=104,
)


SERVERERROR = 1
LAUNCH = 2
LOG = 3



# @@protoc_insertion_point(module_scope)
