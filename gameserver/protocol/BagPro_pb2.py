# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import gameserver.protocol.Role_pb2

DESCRIPTOR = descriptor.FileDescriptor(
  name='gameserver.protocol/BagPro.proto',
  package='protocal.game.BagProto',
  serialized_pb='\n gameserver.protocol/BagPro.proto\x12\x16protocal.game.BagProto\x1a\x1egameserver.protocol/Role.proto\"2\n\x11\x42\x61gItemUseRequest\x12\x0e\n\x06itemId\x18\x01 \x02(\x05\x12\r\n\x05\x63ount\x18\x02 \x02(\x05\"H\n\x12\x42\x61gItemUseResponse\x12\x32\n\x08\x61\x64\x64Items\x18\x01 \x03(\x0b\x32 .protocal.game.RoleProto.BagItem\"3\n\x12\x42\x61gItemSellRequest\x12\x0e\n\x06itemId\x18\x01 \x02(\x05\x12\r\n\x05\x63ount\x18\x02 \x02(\x05\"5\n\x13\x42\x61gItemSellResponse\x12\x0e\n\x06softCu\x18\x01 \x02(\x05\x12\x0e\n\x06hardCu\x18\x02 \x02(\x05\" \n\x0eItemOutRequest\x12\x0e\n\x06itemId\x18\x01 \x02(\x05\"?\n\x0fItemOutResponse\x12,\n\x03out\x18\x01 \x03(\x0b\x32\x1f.protocal.game.BagProto.ItemOut\"2\n\x07ItemOut\x12\x0c\n\x04type\x18\x01 \x02(\x05\x12\n\n\x02id\x18\x02 \x02(\x05\x12\r\n\x05times\x18\x03 \x02(\x05*\x96\x01\n\x07ProtoID\x12\x14\n\x10\x42\x41G_ITEM_USE_REQ\x10\x01\x12\x19\n\x15\x42\x41G_ITEM_USE_RESPINSE\x10\x02\x12\x15\n\x11\x42\x41G_ITEM_SELL_REQ\x10\x03\x12\x1a\n\x16\x42\x41G_ITEM_SELL_RESPINSE\x10\x04\x12\x10\n\x0cITEM_OUT_REQ\x10\x05\x12\x15\n\x11ITEM_OUT_RESPONSE\x10\x06')

_PROTOID = descriptor.EnumDescriptor(
  name='ProtoID',
  full_name='protocal.game.BagProto.ProtoID',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='BAG_ITEM_USE_REQ', index=0, number=1,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='BAG_ITEM_USE_RESPINSE', index=1, number=2,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='BAG_ITEM_SELL_REQ', index=2, number=3,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='BAG_ITEM_SELL_RESPINSE', index=3, number=4,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='ITEM_OUT_REQ', index=4, number=5,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='ITEM_OUT_RESPONSE', index=5, number=6,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=478,
  serialized_end=628,
)


BAG_ITEM_USE_REQ = 1
BAG_ITEM_USE_RESPINSE = 2
BAG_ITEM_SELL_REQ = 3
BAG_ITEM_SELL_RESPINSE = 4
ITEM_OUT_REQ = 5
ITEM_OUT_RESPONSE = 6



_BAGITEMUSEREQUEST = descriptor.Descriptor(
  name='BagItemUseRequest',
  full_name='protocal.game.BagProto.BagItemUseRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='itemId', full_name='protocal.game.BagProto.BagItemUseRequest.itemId', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='count', full_name='protocal.game.BagProto.BagItemUseRequest.count', index=1,
      number=2, type=5, cpp_type=1, label=2,
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
  serialized_start=92,
  serialized_end=142,
)


_BAGITEMUSERESPONSE = descriptor.Descriptor(
  name='BagItemUseResponse',
  full_name='protocal.game.BagProto.BagItemUseResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='addItems', full_name='protocal.game.BagProto.BagItemUseResponse.addItems', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=144,
  serialized_end=216,
)


_BAGITEMSELLREQUEST = descriptor.Descriptor(
  name='BagItemSellRequest',
  full_name='protocal.game.BagProto.BagItemSellRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='itemId', full_name='protocal.game.BagProto.BagItemSellRequest.itemId', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='count', full_name='protocal.game.BagProto.BagItemSellRequest.count', index=1,
      number=2, type=5, cpp_type=1, label=2,
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
  serialized_start=218,
  serialized_end=269,
)


_BAGITEMSELLRESPONSE = descriptor.Descriptor(
  name='BagItemSellResponse',
  full_name='protocal.game.BagProto.BagItemSellResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='softCu', full_name='protocal.game.BagProto.BagItemSellResponse.softCu', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='hardCu', full_name='protocal.game.BagProto.BagItemSellResponse.hardCu', index=1,
      number=2, type=5, cpp_type=1, label=2,
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
  serialized_start=271,
  serialized_end=324,
)


_ITEMOUTREQUEST = descriptor.Descriptor(
  name='ItemOutRequest',
  full_name='protocal.game.BagProto.ItemOutRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='itemId', full_name='protocal.game.BagProto.ItemOutRequest.itemId', index=0,
      number=1, type=5, cpp_type=1, label=2,
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
  serialized_start=326,
  serialized_end=358,
)


_ITEMOUTRESPONSE = descriptor.Descriptor(
  name='ItemOutResponse',
  full_name='protocal.game.BagProto.ItemOutResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='out', full_name='protocal.game.BagProto.ItemOutResponse.out', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=360,
  serialized_end=423,
)


_ITEMOUT = descriptor.Descriptor(
  name='ItemOut',
  full_name='protocal.game.BagProto.ItemOut',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='type', full_name='protocal.game.BagProto.ItemOut.type', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='id', full_name='protocal.game.BagProto.ItemOut.id', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='times', full_name='protocal.game.BagProto.ItemOut.times', index=2,
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
  serialized_start=425,
  serialized_end=475,
)

_BAGITEMUSERESPONSE.fields_by_name['addItems'].message_type = gameserver.protocol.Role_pb2._BAGITEM
_ITEMOUTRESPONSE.fields_by_name['out'].message_type = _ITEMOUT
DESCRIPTOR.message_types_by_name['BagItemUseRequest'] = _BAGITEMUSEREQUEST
DESCRIPTOR.message_types_by_name['BagItemUseResponse'] = _BAGITEMUSERESPONSE
DESCRIPTOR.message_types_by_name['BagItemSellRequest'] = _BAGITEMSELLREQUEST
DESCRIPTOR.message_types_by_name['BagItemSellResponse'] = _BAGITEMSELLRESPONSE
DESCRIPTOR.message_types_by_name['ItemOutRequest'] = _ITEMOUTREQUEST
DESCRIPTOR.message_types_by_name['ItemOutResponse'] = _ITEMOUTRESPONSE
DESCRIPTOR.message_types_by_name['ItemOut'] = _ITEMOUT

class BagItemUseRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _BAGITEMUSEREQUEST
  
  # @@protoc_insertion_point(class_scope:protocal.game.BagProto.BagItemUseRequest)

class BagItemUseResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _BAGITEMUSERESPONSE
  
  # @@protoc_insertion_point(class_scope:protocal.game.BagProto.BagItemUseResponse)

class BagItemSellRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _BAGITEMSELLREQUEST
  
  # @@protoc_insertion_point(class_scope:protocal.game.BagProto.BagItemSellRequest)

class BagItemSellResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _BAGITEMSELLRESPONSE
  
  # @@protoc_insertion_point(class_scope:protocal.game.BagProto.BagItemSellResponse)

class ItemOutRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ITEMOUTREQUEST
  
  # @@protoc_insertion_point(class_scope:protocal.game.BagProto.ItemOutRequest)

class ItemOutResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ITEMOUTRESPONSE
  
  # @@protoc_insertion_point(class_scope:protocal.game.BagProto.ItemOutResponse)

class ItemOut(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ITEMOUT
  
  # @@protoc_insertion_point(class_scope:protocal.game.BagProto.ItemOut)

# @@protoc_insertion_point(module_scope)
