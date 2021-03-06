# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='gameserver.protocol/RunePro.proto',
  package='protocal.game.RuneProto',
  serialized_pb='\n!gameserver.protocol/RunePro.proto\x12\x17protocal.game.RuneProto\"F\n\x10RuneInlayRequest\x12\x12\n\nemployeUid\x18\x01 \x02(\x03\x12\x0f\n\x07runeUid\x18\x02 \x02(\x03\x12\r\n\x05index\x18\x03 \x02(\x05\"\x13\n\x11RuneInlayResponse\"E\n\x0fRuneTakeRequest\x12\x12\n\nemployeUid\x18\x01 \x02(\x03\x12\x0f\n\x07runeUid\x18\x02 \x02(\x03\x12\r\n\x05index\x18\x03 \x02(\x05\"\x12\n\x10RuneTakeResponse\"\'\n\x14RuneIntensifyRequest\x12\x0f\n\x07runeUid\x18\x01 \x02(\x03\"\x17\n\x15RuneIntensifyResponse*\x96\x01\n\x07ProtoID\x12\x12\n\x0eRUNE_INLAY_REQ\x10\x01\x12\x17\n\x13RUNE_INLAY_RESPONSE\x10\x02\x12\x11\n\rRUNE_TAKE_REQ\x10\x03\x12\x16\n\x12RUNE_TAKE_RESPONSE\x10\x04\x12\x16\n\x12RUNE_INTENSIFY_REQ\x10\x05\x12\x1b\n\x17RUNE_INTENSIFY_RESPONSE\x10\x06')

_PROTOID = descriptor.EnumDescriptor(
  name='ProtoID',
  full_name='protocal.game.RuneProto.ProtoID',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='RUNE_INLAY_REQ', index=0, number=1,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='RUNE_INLAY_RESPONSE', index=1, number=2,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='RUNE_TAKE_REQ', index=2, number=3,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='RUNE_TAKE_RESPONSE', index=3, number=4,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='RUNE_INTENSIFY_REQ', index=4, number=5,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='RUNE_INTENSIFY_RESPONSE', index=5, number=6,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=313,
  serialized_end=463,
)


RUNE_INLAY_REQ = 1
RUNE_INLAY_RESPONSE = 2
RUNE_TAKE_REQ = 3
RUNE_TAKE_RESPONSE = 4
RUNE_INTENSIFY_REQ = 5
RUNE_INTENSIFY_RESPONSE = 6



_RUNEINLAYREQUEST = descriptor.Descriptor(
  name='RuneInlayRequest',
  full_name='protocal.game.RuneProto.RuneInlayRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='employeUid', full_name='protocal.game.RuneProto.RuneInlayRequest.employeUid', index=0,
      number=1, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='runeUid', full_name='protocal.game.RuneProto.RuneInlayRequest.runeUid', index=1,
      number=2, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='index', full_name='protocal.game.RuneProto.RuneInlayRequest.index', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=62,
  serialized_end=132,
)


_RUNEINLAYRESPONSE = descriptor.Descriptor(
  name='RuneInlayResponse',
  full_name='protocal.game.RuneProto.RuneInlayResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=134,
  serialized_end=153,
)


_RUNETAKEREQUEST = descriptor.Descriptor(
  name='RuneTakeRequest',
  full_name='protocal.game.RuneProto.RuneTakeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='employeUid', full_name='protocal.game.RuneProto.RuneTakeRequest.employeUid', index=0,
      number=1, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='runeUid', full_name='protocal.game.RuneProto.RuneTakeRequest.runeUid', index=1,
      number=2, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='index', full_name='protocal.game.RuneProto.RuneTakeRequest.index', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=155,
  serialized_end=224,
)


_RUNETAKERESPONSE = descriptor.Descriptor(
  name='RuneTakeResponse',
  full_name='protocal.game.RuneProto.RuneTakeResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=226,
  serialized_end=244,
)


_RUNEINTENSIFYREQUEST = descriptor.Descriptor(
  name='RuneIntensifyRequest',
  full_name='protocal.game.RuneProto.RuneIntensifyRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='runeUid', full_name='protocal.game.RuneProto.RuneIntensifyRequest.runeUid', index=0,
      number=1, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=246,
  serialized_end=285,
)


_RUNEINTENSIFYRESPONSE = descriptor.Descriptor(
  name='RuneIntensifyResponse',
  full_name='protocal.game.RuneProto.RuneIntensifyResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=287,
  serialized_end=310,
)

DESCRIPTOR.message_types_by_name['RuneInlayRequest'] = _RUNEINLAYREQUEST
DESCRIPTOR.message_types_by_name['RuneInlayResponse'] = _RUNEINLAYRESPONSE
DESCRIPTOR.message_types_by_name['RuneTakeRequest'] = _RUNETAKEREQUEST
DESCRIPTOR.message_types_by_name['RuneTakeResponse'] = _RUNETAKERESPONSE
DESCRIPTOR.message_types_by_name['RuneIntensifyRequest'] = _RUNEINTENSIFYREQUEST
DESCRIPTOR.message_types_by_name['RuneIntensifyResponse'] = _RUNEINTENSIFYRESPONSE

class RuneInlayRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RUNEINLAYREQUEST
  
  # @@protoc_insertion_point(class_scope:protocal.game.RuneProto.RuneInlayRequest)

class RuneInlayResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RUNEINLAYRESPONSE
  
  # @@protoc_insertion_point(class_scope:protocal.game.RuneProto.RuneInlayResponse)

class RuneTakeRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RUNETAKEREQUEST
  
  # @@protoc_insertion_point(class_scope:protocal.game.RuneProto.RuneTakeRequest)

class RuneTakeResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RUNETAKERESPONSE
  
  # @@protoc_insertion_point(class_scope:protocal.game.RuneProto.RuneTakeResponse)

class RuneIntensifyRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RUNEINTENSIFYREQUEST
  
  # @@protoc_insertion_point(class_scope:protocal.game.RuneProto.RuneIntensifyRequest)

class RuneIntensifyResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RUNEINTENSIFYRESPONSE
  
  # @@protoc_insertion_point(class_scope:protocal.game.RuneProto.RuneIntensifyResponse)

# @@protoc_insertion_point(module_scope)
