# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='Role.proto',
  package='protocal.game.RoleProto',
  serialized_pb='\n\nRole.proto\x12\x17protocal.game.RoleProto\"/\n\x10RoleLoginRequest\x12\r\n\x05token\x18\x01 \x02(\t\x12\x0c\n\x04hash\x18\x02 \x02(\t\"c\n\x11RoleLoginResponse\x12\x11\n\troleExist\x18\x01 \x02(\x08\x12;\n\x08roleInfo\x18\x02 \x01(\x0b\x32).protocal.game.RoleProto.RoleInfoResponse\"\xf1\x01\n\x10RoleInfoResponse\x12\x10\n\x08roleName\x18\x01 \x02(\t\x12\r\n\x05level\x18\x02 \x02(\x05\x12\n\n\x02id\x18\x03 \x02(\x03\x12\x12\n\nexperience\x18\x04 \x02(\x05\x12\r\n\x05power\x18\x05 \x02(\x05\x12\x14\n\x0csoftCurrency\x18\x06 \x02(\x05\x12\x14\n\x0chardCurrency\x18\x07 \x02(\x05\x12\x10\n\x08vipLevel\x18\x08 \x02(\x05\x12\x39\n\x0b\x65mployeList\x18\t \x03(\x0b\x32$.protocal.game.RoleProto.EmployeInfo\x12\x14\n\x0c\x62uyPowerTime\x18\n \x02(\x05\"\xd1\x01\n\x0b\x45mployeInfo\x12\x0b\n\x03uid\x18\x01 \x02(\x03\x12/\n\x04\x63\x61rd\x18\x02 \x02(\x0b\x32!.protocal.game.RoleProto.CardInfo\x12:\n\x06weapon\x18\x03 \x02(\x0b\x32*.protocal.game.RoleProto.EmployeWeaponInfo\x12\x35\n\x07\x63lothes\x18\x04 \x02(\x0b\x32$.protocal.game.RoleProto.ClothesInfo\x12\x11\n\tmoveSpeed\x18\x05 \x02(\x02\"<\n\x0b\x43lothesInfo\x12\x0f\n\x07\x61llList\x18\x01 \x03(\x05\x12\x0f\n\x07ownList\x18\x02 \x03(\x05\x12\x0b\n\x03use\x18\x03 \x02(\x05\"\xc2\x01\n\x08\x43\x61rdInfo\x12\x0b\n\x03uid\x18\x01 \x02(\x03\x12\n\n\x02id\x18\x02 \x02(\x05\x12\r\n\x05level\x18\x03 \x02(\x05\x12\r\n\x05\x66ight\x18\x04 \x02(\x05\x12\x0b\n\x03\x65xp\x18\x05 \x02(\x05\x12\n\n\x02hp\x18\x06 \x02(\x05\x12\n\n\x02mp\x18\x07 \x02(\x05\x12\x0e\n\x06\x61ttack\x18\x08 \x02(\x05\x12\x0f\n\x07\x64\x65\x66\x65nse\x18\t \x02(\x05\x12\x39\n\tskillList\x18\n \x03(\x0b\x32&.protocal.game.RoleProto.CardSkillInfo\"*\n\rCardSkillInfo\x12\n\n\x02id\x18\x01 \x02(\x05\x12\r\n\x05level\x18\x02 \x02(\x05\"O\n\x11\x45mployeWeaponInfo\x12\x0b\n\x03uid\x18\x01 \x02(\x03\x12\n\n\x02id\x18\x02 \x02(\x05\x12\r\n\x05level\x18\x03 \x02(\x05\x12\x12\n\ninensifyId\x18\x04 \x02(\x05\"%\n\x11\x43reateRoleRequest\x12\x10\n\x08roleName\x18\x01 \x02(\t\"\x17\n\x15RandomNickNameRequest\"*\n\x16RandomNickNameResponse\x12\x10\n\x08roleName\x18\x01 \x02(\t\"\x10\n\x0e\x42\x61gInfoRequest\"z\n\x0f\x42\x61gInfoResponse\x12\x32\n\x08itemList\x18\x01 \x03(\x0b\x32 .protocal.game.RoleProto.BagItem\x12\x33\n\x08\x63\x61rdList\x18\x02 \x03(\x0b\x32!.protocal.game.RoleProto.CardInfo\"$\n\x07\x42\x61gItem\x12\n\n\x02id\x18\x01 \x02(\x05\x12\r\n\x05\x63ount\x18\x02 \x02(\x05\"\x13\n\x11RoleLogoutRequest*\xda\x01\n\x07ProtoID\x12\x12\n\x0eROLE_LOGIN_REQ\x10\x01\x12\x17\n\x13ROLE_LOGIN_RESPONSE\x10\x02\x12\x13\n\x0f\x43REATE_ROLE_REQ\x10\x03\x12\x16\n\x12ROLE_INFO_RESPONSE\x10\x04\x12\x18\n\x14RANDOM_NICK_NAME_REQ\x10\x05\x12\x1d\n\x19RANDOM_NICK_NAME_RESPONSE\x10\x06\x12\x13\n\x0fROLE_LOGOUT_REQ\x10\x07\x12\x10\n\x0cROLE_BAG_REQ\x10\x08\x12\x15\n\x11ROLE_BAG_RESPONSE\x10\t')

_PROTOID = descriptor.EnumDescriptor(
  name='ProtoID',
  full_name='protocal.game.RoleProto.ProtoID',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='ROLE_LOGIN_REQ', index=0, number=1,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='ROLE_LOGIN_RESPONSE', index=1, number=2,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='CREATE_ROLE_REQ', index=2, number=3,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='ROLE_INFO_RESPONSE', index=3, number=4,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='RANDOM_NICK_NAME_REQ', index=4, number=5,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='RANDOM_NICK_NAME_RESPONSE', index=5, number=6,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='ROLE_LOGOUT_REQ', index=6, number=7,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='ROLE_BAG_REQ', index=7, number=8,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='ROLE_BAG_RESPONSE', index=8, number=9,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1339,
  serialized_end=1557,
)


ROLE_LOGIN_REQ = 1
ROLE_LOGIN_RESPONSE = 2
CREATE_ROLE_REQ = 3
ROLE_INFO_RESPONSE = 4
RANDOM_NICK_NAME_REQ = 5
RANDOM_NICK_NAME_RESPONSE = 6
ROLE_LOGOUT_REQ = 7
ROLE_BAG_REQ = 8
ROLE_BAG_RESPONSE = 9



_ROLELOGINREQUEST = descriptor.Descriptor(
  name='RoleLoginRequest',
  full_name='protocal.game.RoleProto.RoleLoginRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='token', full_name='protocal.game.RoleProto.RoleLoginRequest.token', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='hash', full_name='protocal.game.RoleProto.RoleLoginRequest.hash', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
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
  serialized_start=39,
  serialized_end=86,
)


_ROLELOGINRESPONSE = descriptor.Descriptor(
  name='RoleLoginResponse',
  full_name='protocal.game.RoleProto.RoleLoginResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='roleExist', full_name='protocal.game.RoleProto.RoleLoginResponse.roleExist', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='roleInfo', full_name='protocal.game.RoleProto.RoleLoginResponse.roleInfo', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=88,
  serialized_end=187,
)


_ROLEINFORESPONSE = descriptor.Descriptor(
  name='RoleInfoResponse',
  full_name='protocal.game.RoleProto.RoleInfoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='roleName', full_name='protocal.game.RoleProto.RoleInfoResponse.roleName', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='level', full_name='protocal.game.RoleProto.RoleInfoResponse.level', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='id', full_name='protocal.game.RoleProto.RoleInfoResponse.id', index=2,
      number=3, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='experience', full_name='protocal.game.RoleProto.RoleInfoResponse.experience', index=3,
      number=4, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='power', full_name='protocal.game.RoleProto.RoleInfoResponse.power', index=4,
      number=5, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='softCurrency', full_name='protocal.game.RoleProto.RoleInfoResponse.softCurrency', index=5,
      number=6, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='hardCurrency', full_name='protocal.game.RoleProto.RoleInfoResponse.hardCurrency', index=6,
      number=7, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='vipLevel', full_name='protocal.game.RoleProto.RoleInfoResponse.vipLevel', index=7,
      number=8, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='employeList', full_name='protocal.game.RoleProto.RoleInfoResponse.employeList', index=8,
      number=9, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='buyPowerTime', full_name='protocal.game.RoleProto.RoleInfoResponse.buyPowerTime', index=9,
      number=10, type=5, cpp_type=1, label=2,
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
  serialized_start=190,
  serialized_end=431,
)


_EMPLOYEINFO = descriptor.Descriptor(
  name='EmployeInfo',
  full_name='protocal.game.RoleProto.EmployeInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='uid', full_name='protocal.game.RoleProto.EmployeInfo.uid', index=0,
      number=1, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='card', full_name='protocal.game.RoleProto.EmployeInfo.card', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='weapon', full_name='protocal.game.RoleProto.EmployeInfo.weapon', index=2,
      number=3, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='clothes', full_name='protocal.game.RoleProto.EmployeInfo.clothes', index=3,
      number=4, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='moveSpeed', full_name='protocal.game.RoleProto.EmployeInfo.moveSpeed', index=4,
      number=5, type=2, cpp_type=6, label=2,
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
  serialized_start=434,
  serialized_end=643,
)


_CLOTHESINFO = descriptor.Descriptor(
  name='ClothesInfo',
  full_name='protocal.game.RoleProto.ClothesInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='allList', full_name='protocal.game.RoleProto.ClothesInfo.allList', index=0,
      number=1, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='ownList', full_name='protocal.game.RoleProto.ClothesInfo.ownList', index=1,
      number=2, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='use', full_name='protocal.game.RoleProto.ClothesInfo.use', index=2,
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
  serialized_start=645,
  serialized_end=705,
)


_CARDINFO = descriptor.Descriptor(
  name='CardInfo',
  full_name='protocal.game.RoleProto.CardInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='uid', full_name='protocal.game.RoleProto.CardInfo.uid', index=0,
      number=1, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='id', full_name='protocal.game.RoleProto.CardInfo.id', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='level', full_name='protocal.game.RoleProto.CardInfo.level', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='fight', full_name='protocal.game.RoleProto.CardInfo.fight', index=3,
      number=4, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='exp', full_name='protocal.game.RoleProto.CardInfo.exp', index=4,
      number=5, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='hp', full_name='protocal.game.RoleProto.CardInfo.hp', index=5,
      number=6, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='mp', full_name='protocal.game.RoleProto.CardInfo.mp', index=6,
      number=7, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='attack', full_name='protocal.game.RoleProto.CardInfo.attack', index=7,
      number=8, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='defense', full_name='protocal.game.RoleProto.CardInfo.defense', index=8,
      number=9, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='skillList', full_name='protocal.game.RoleProto.CardInfo.skillList', index=9,
      number=10, type=11, cpp_type=10, label=3,
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
  serialized_start=708,
  serialized_end=902,
)


_CARDSKILLINFO = descriptor.Descriptor(
  name='CardSkillInfo',
  full_name='protocal.game.RoleProto.CardSkillInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='protocal.game.RoleProto.CardSkillInfo.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='level', full_name='protocal.game.RoleProto.CardSkillInfo.level', index=1,
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
  serialized_start=904,
  serialized_end=946,
)


_EMPLOYEWEAPONINFO = descriptor.Descriptor(
  name='EmployeWeaponInfo',
  full_name='protocal.game.RoleProto.EmployeWeaponInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='uid', full_name='protocal.game.RoleProto.EmployeWeaponInfo.uid', index=0,
      number=1, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='id', full_name='protocal.game.RoleProto.EmployeWeaponInfo.id', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='level', full_name='protocal.game.RoleProto.EmployeWeaponInfo.level', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='inensifyId', full_name='protocal.game.RoleProto.EmployeWeaponInfo.inensifyId', index=3,
      number=4, type=5, cpp_type=1, label=2,
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
  serialized_start=948,
  serialized_end=1027,
)


_CREATEROLEREQUEST = descriptor.Descriptor(
  name='CreateRoleRequest',
  full_name='protocal.game.RoleProto.CreateRoleRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='roleName', full_name='protocal.game.RoleProto.CreateRoleRequest.roleName', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
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
  serialized_start=1029,
  serialized_end=1066,
)


_RANDOMNICKNAMEREQUEST = descriptor.Descriptor(
  name='RandomNickNameRequest',
  full_name='protocal.game.RoleProto.RandomNickNameRequest',
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
  serialized_start=1068,
  serialized_end=1091,
)


_RANDOMNICKNAMERESPONSE = descriptor.Descriptor(
  name='RandomNickNameResponse',
  full_name='protocal.game.RoleProto.RandomNickNameResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='roleName', full_name='protocal.game.RoleProto.RandomNickNameResponse.roleName', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
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
  serialized_start=1093,
  serialized_end=1135,
)


_BAGINFOREQUEST = descriptor.Descriptor(
  name='BagInfoRequest',
  full_name='protocal.game.RoleProto.BagInfoRequest',
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
  serialized_start=1137,
  serialized_end=1153,
)


_BAGINFORESPONSE = descriptor.Descriptor(
  name='BagInfoResponse',
  full_name='protocal.game.RoleProto.BagInfoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='itemList', full_name='protocal.game.RoleProto.BagInfoResponse.itemList', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='cardList', full_name='protocal.game.RoleProto.BagInfoResponse.cardList', index=1,
      number=2, type=11, cpp_type=10, label=3,
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
  serialized_start=1155,
  serialized_end=1277,
)


_BAGITEM = descriptor.Descriptor(
  name='BagItem',
  full_name='protocal.game.RoleProto.BagItem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='protocal.game.RoleProto.BagItem.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='count', full_name='protocal.game.RoleProto.BagItem.count', index=1,
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
  serialized_start=1279,
  serialized_end=1315,
)


_ROLELOGOUTREQUEST = descriptor.Descriptor(
  name='RoleLogoutRequest',
  full_name='protocal.game.RoleProto.RoleLogoutRequest',
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
  serialized_start=1317,
  serialized_end=1336,
)

_ROLELOGINRESPONSE.fields_by_name['roleInfo'].message_type = _ROLEINFORESPONSE
_ROLEINFORESPONSE.fields_by_name['employeList'].message_type = _EMPLOYEINFO
_EMPLOYEINFO.fields_by_name['card'].message_type = _CARDINFO
_EMPLOYEINFO.fields_by_name['weapon'].message_type = _EMPLOYEWEAPONINFO
_EMPLOYEINFO.fields_by_name['clothes'].message_type = _CLOTHESINFO
_CARDINFO.fields_by_name['skillList'].message_type = _CARDSKILLINFO
_BAGINFORESPONSE.fields_by_name['itemList'].message_type = _BAGITEM
_BAGINFORESPONSE.fields_by_name['cardList'].message_type = _CARDINFO
DESCRIPTOR.message_types_by_name['RoleLoginRequest'] = _ROLELOGINREQUEST
DESCRIPTOR.message_types_by_name['RoleLoginResponse'] = _ROLELOGINRESPONSE
DESCRIPTOR.message_types_by_name['RoleInfoResponse'] = _ROLEINFORESPONSE
DESCRIPTOR.message_types_by_name['EmployeInfo'] = _EMPLOYEINFO
DESCRIPTOR.message_types_by_name['ClothesInfo'] = _CLOTHESINFO
DESCRIPTOR.message_types_by_name['CardInfo'] = _CARDINFO
DESCRIPTOR.message_types_by_name['CardSkillInfo'] = _CARDSKILLINFO
DESCRIPTOR.message_types_by_name['EmployeWeaponInfo'] = _EMPLOYEWEAPONINFO
DESCRIPTOR.message_types_by_name['CreateRoleRequest'] = _CREATEROLEREQUEST
DESCRIPTOR.message_types_by_name['RandomNickNameRequest'] = _RANDOMNICKNAMEREQUEST
DESCRIPTOR.message_types_by_name['RandomNickNameResponse'] = _RANDOMNICKNAMERESPONSE
DESCRIPTOR.message_types_by_name['BagInfoRequest'] = _BAGINFOREQUEST
DESCRIPTOR.message_types_by_name['BagInfoResponse'] = _BAGINFORESPONSE
DESCRIPTOR.message_types_by_name['BagItem'] = _BAGITEM
DESCRIPTOR.message_types_by_name['RoleLogoutRequest'] = _ROLELOGOUTREQUEST

class RoleLoginRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ROLELOGINREQUEST
  
  # @@protoc_insertion_point(class_scope:protocal.game.RoleProto.RoleLoginRequest)

class RoleLoginResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ROLELOGINRESPONSE
  
  # @@protoc_insertion_point(class_scope:protocal.game.RoleProto.RoleLoginResponse)

class RoleInfoResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ROLEINFORESPONSE
  
  # @@protoc_insertion_point(class_scope:protocal.game.RoleProto.RoleInfoResponse)

class EmployeInfo(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _EMPLOYEINFO
  
  # @@protoc_insertion_point(class_scope:protocal.game.RoleProto.EmployeInfo)

class ClothesInfo(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CLOTHESINFO
  
  # @@protoc_insertion_point(class_scope:protocal.game.RoleProto.ClothesInfo)

class CardInfo(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CARDINFO
  
  # @@protoc_insertion_point(class_scope:protocal.game.RoleProto.CardInfo)

class CardSkillInfo(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CARDSKILLINFO
  
  # @@protoc_insertion_point(class_scope:protocal.game.RoleProto.CardSkillInfo)

class EmployeWeaponInfo(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _EMPLOYEWEAPONINFO
  
  # @@protoc_insertion_point(class_scope:protocal.game.RoleProto.EmployeWeaponInfo)

class CreateRoleRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CREATEROLEREQUEST
  
  # @@protoc_insertion_point(class_scope:protocal.game.RoleProto.CreateRoleRequest)

class RandomNickNameRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RANDOMNICKNAMEREQUEST
  
  # @@protoc_insertion_point(class_scope:protocal.game.RoleProto.RandomNickNameRequest)

class RandomNickNameResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RANDOMNICKNAMERESPONSE
  
  # @@protoc_insertion_point(class_scope:protocal.game.RoleProto.RandomNickNameResponse)

class BagInfoRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _BAGINFOREQUEST
  
  # @@protoc_insertion_point(class_scope:protocal.game.RoleProto.BagInfoRequest)

class BagInfoResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _BAGINFORESPONSE
  
  # @@protoc_insertion_point(class_scope:protocal.game.RoleProto.BagInfoResponse)

class BagItem(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _BAGITEM
  
  # @@protoc_insertion_point(class_scope:protocal.game.RoleProto.BagItem)

class RoleLogoutRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ROLELOGOUTREQUEST
  
  # @@protoc_insertion_point(class_scope:protocal.game.RoleProto.RoleLogoutRequest)

# @@protoc_insertion_point(module_scope)
