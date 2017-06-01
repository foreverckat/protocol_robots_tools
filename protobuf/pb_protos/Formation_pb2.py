# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='Formation.proto',
  package='protocal.game.FormationProto',
  serialized_pb='\n\x0f\x46ormation.proto\x12\x1cprotocal.game.FormationProto\",\n\x14\x46ormationInfoRequest\x12\x14\n\x0c\x66ormationNum\x18\x01 \x02(\x05\"_\n\x15\x46ormationInfoResponse\x12\x46\n\x11\x62\x61ttleEmployeList\x18\x01 \x03(\x0b\x32+.protocal.game.FormationProto.BattleEmploye\"2\n\rBattleEmploye\x12\x12\n\nemployeUid\x18\x01 \x02(\x03\x12\r\n\x05index\x18\x02 \x02(\x05\"^\n\x14\x46ormationSaveRequest\x12\x46\n\x11\x62\x61ttleEmployeList\x18\x01 \x03(\x0b\x32+.protocal.game.FormationProto.BattleEmploye\"\x17\n\x15\x46ormationSaveResponse*s\n\x07ProtoID\x12\x16\n\x12\x46ORMATION_INFO_REQ\x10\x01\x12\x1b\n\x17\x46ORMATION_INFO_RESPONSE\x10\x02\x12\x16\n\x12\x46ORMATION_SAVE_REQ\x10\x03\x12\x1b\n\x17\x46ORMATION_SAVE_RESPONSE\x10\x04')

_PROTOID = descriptor.EnumDescriptor(
  name='ProtoID',
  full_name='protocal.game.FormationProto.ProtoID',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='FORMATION_INFO_REQ', index=0, number=1,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='FORMATION_INFO_RESPONSE', index=1, number=2,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='FORMATION_SAVE_REQ', index=2, number=3,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='FORMATION_SAVE_RESPONSE', index=3, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=365,
  serialized_end=480,
)


FORMATION_INFO_REQ = 1
FORMATION_INFO_RESPONSE = 2
FORMATION_SAVE_REQ = 3
FORMATION_SAVE_RESPONSE = 4



_FORMATIONINFOREQUEST = descriptor.Descriptor(
  name='FormationInfoRequest',
  full_name='protocal.game.FormationProto.FormationInfoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='formationNum', full_name='protocal.game.FormationProto.FormationInfoRequest.formationNum', index=0,
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
  serialized_start=49,
  serialized_end=93,
)


_FORMATIONINFORESPONSE = descriptor.Descriptor(
  name='FormationInfoResponse',
  full_name='protocal.game.FormationProto.FormationInfoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='battleEmployeList', full_name='protocal.game.FormationProto.FormationInfoResponse.battleEmployeList', index=0,
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
  serialized_start=95,
  serialized_end=190,
)


_BATTLEEMPLOYE = descriptor.Descriptor(
  name='BattleEmploye',
  full_name='protocal.game.FormationProto.BattleEmploye',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='employeUid', full_name='protocal.game.FormationProto.BattleEmploye.employeUid', index=0,
      number=1, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='index', full_name='protocal.game.FormationProto.BattleEmploye.index', index=1,
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
  serialized_start=192,
  serialized_end=242,
)


_FORMATIONSAVEREQUEST = descriptor.Descriptor(
  name='FormationSaveRequest',
  full_name='protocal.game.FormationProto.FormationSaveRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='battleEmployeList', full_name='protocal.game.FormationProto.FormationSaveRequest.battleEmployeList', index=0,
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
  serialized_start=244,
  serialized_end=338,
)


_FORMATIONSAVERESPONSE = descriptor.Descriptor(
  name='FormationSaveResponse',
  full_name='protocal.game.FormationProto.FormationSaveResponse',
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
  serialized_start=340,
  serialized_end=363,
)

_FORMATIONINFORESPONSE.fields_by_name['battleEmployeList'].message_type = _BATTLEEMPLOYE
_FORMATIONSAVEREQUEST.fields_by_name['battleEmployeList'].message_type = _BATTLEEMPLOYE
DESCRIPTOR.message_types_by_name['FormationInfoRequest'] = _FORMATIONINFOREQUEST
DESCRIPTOR.message_types_by_name['FormationInfoResponse'] = _FORMATIONINFORESPONSE
DESCRIPTOR.message_types_by_name['BattleEmploye'] = _BATTLEEMPLOYE
DESCRIPTOR.message_types_by_name['FormationSaveRequest'] = _FORMATIONSAVEREQUEST
DESCRIPTOR.message_types_by_name['FormationSaveResponse'] = _FORMATIONSAVERESPONSE

class FormationInfoRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _FORMATIONINFOREQUEST
  
  # @@protoc_insertion_point(class_scope:protocal.game.FormationProto.FormationInfoRequest)

class FormationInfoResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _FORMATIONINFORESPONSE
  
  # @@protoc_insertion_point(class_scope:protocal.game.FormationProto.FormationInfoResponse)

class BattleEmploye(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _BATTLEEMPLOYE
  
  # @@protoc_insertion_point(class_scope:protocal.game.FormationProto.BattleEmploye)

class FormationSaveRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _FORMATIONSAVEREQUEST
  
  # @@protoc_insertion_point(class_scope:protocal.game.FormationProto.FormationSaveRequest)

class FormationSaveResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _FORMATIONSAVERESPONSE
  
  # @@protoc_insertion_point(class_scope:protocal.game.FormationProto.FormationSaveResponse)

# @@protoc_insertion_point(module_scope)