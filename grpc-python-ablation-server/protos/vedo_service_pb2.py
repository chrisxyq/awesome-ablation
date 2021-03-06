# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: vedo_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='vedo_service.proto',
  package='protos',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x12vedo_service.proto\x12\x06protos\"*\n\x14GetMeshPointsRequest\x12\x12\n\nmesh_index\x18\x01 \x01(\x05\"3\n\x13GetMeshPointsResult\x12\x1c\n\x05point\x18\x01 \x03(\x0b\x32\r.protos.Point\"\x1b\n\x05Point\x12\x12\n\ncoordinate\x18\x01 \x03(\t\"-\n\x0fGetUsersRequest\x12\x1a\n\x04user\x18\x01 \x03(\x0b\x32\x0c.protos.User\"\x18\n\x04User\x12\x10\n\x08username\x18\x01 \x03(\x01\",\n\x0cShuzuRequest\x12\x1c\n\x05shuzu\x18\x01 \x03(\x0b\x32\r.protos.Shuzu\"\x14\n\x05Shuzu\x12\x0b\n\x03shu\x18\x01 \x03(\t2T\n\x04Vedo\x12L\n\rGetMeshPoints\x12\x1c.protos.GetMeshPointsRequest\x1a\x1b.protos.GetMeshPointsResult\"\x00\x62\x06proto3'
)




_GETMESHPOINTSREQUEST = _descriptor.Descriptor(
  name='GetMeshPointsRequest',
  full_name='protos.GetMeshPointsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='mesh_index', full_name='protos.GetMeshPointsRequest.mesh_index', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=30,
  serialized_end=72,
)


_GETMESHPOINTSRESULT = _descriptor.Descriptor(
  name='GetMeshPointsResult',
  full_name='protos.GetMeshPointsResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='point', full_name='protos.GetMeshPointsResult.point', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=74,
  serialized_end=125,
)


_POINT = _descriptor.Descriptor(
  name='Point',
  full_name='protos.Point',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='coordinate', full_name='protos.Point.coordinate', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=127,
  serialized_end=154,
)


_GETUSERSREQUEST = _descriptor.Descriptor(
  name='GetUsersRequest',
  full_name='protos.GetUsersRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='user', full_name='protos.GetUsersRequest.user', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=156,
  serialized_end=201,
)


_USER = _descriptor.Descriptor(
  name='User',
  full_name='protos.User',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='username', full_name='protos.User.username', index=0,
      number=1, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=203,
  serialized_end=227,
)


_SHUZUREQUEST = _descriptor.Descriptor(
  name='ShuzuRequest',
  full_name='protos.ShuzuRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='shuzu', full_name='protos.ShuzuRequest.shuzu', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=229,
  serialized_end=273,
)


_SHUZU = _descriptor.Descriptor(
  name='Shuzu',
  full_name='protos.Shuzu',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='shu', full_name='protos.Shuzu.shu', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=275,
  serialized_end=295,
)

_GETMESHPOINTSRESULT.fields_by_name['point'].message_type = _POINT
_GETUSERSREQUEST.fields_by_name['user'].message_type = _USER
_SHUZUREQUEST.fields_by_name['shuzu'].message_type = _SHUZU
DESCRIPTOR.message_types_by_name['GetMeshPointsRequest'] = _GETMESHPOINTSREQUEST
DESCRIPTOR.message_types_by_name['GetMeshPointsResult'] = _GETMESHPOINTSRESULT
DESCRIPTOR.message_types_by_name['Point'] = _POINT
DESCRIPTOR.message_types_by_name['GetUsersRequest'] = _GETUSERSREQUEST
DESCRIPTOR.message_types_by_name['User'] = _USER
DESCRIPTOR.message_types_by_name['ShuzuRequest'] = _SHUZUREQUEST
DESCRIPTOR.message_types_by_name['Shuzu'] = _SHUZU
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetMeshPointsRequest = _reflection.GeneratedProtocolMessageType('GetMeshPointsRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETMESHPOINTSREQUEST,
  '__module__' : 'vedo_service_pb2'
  # @@protoc_insertion_point(class_scope:protos.GetMeshPointsRequest)
  })
_sym_db.RegisterMessage(GetMeshPointsRequest)

GetMeshPointsResult = _reflection.GeneratedProtocolMessageType('GetMeshPointsResult', (_message.Message,), {
  'DESCRIPTOR' : _GETMESHPOINTSRESULT,
  '__module__' : 'vedo_service_pb2'
  # @@protoc_insertion_point(class_scope:protos.GetMeshPointsResult)
  })
_sym_db.RegisterMessage(GetMeshPointsResult)

Point = _reflection.GeneratedProtocolMessageType('Point', (_message.Message,), {
  'DESCRIPTOR' : _POINT,
  '__module__' : 'vedo_service_pb2'
  # @@protoc_insertion_point(class_scope:protos.Point)
  })
_sym_db.RegisterMessage(Point)

GetUsersRequest = _reflection.GeneratedProtocolMessageType('GetUsersRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETUSERSREQUEST,
  '__module__' : 'vedo_service_pb2'
  # @@protoc_insertion_point(class_scope:protos.GetUsersRequest)
  })
_sym_db.RegisterMessage(GetUsersRequest)

User = _reflection.GeneratedProtocolMessageType('User', (_message.Message,), {
  'DESCRIPTOR' : _USER,
  '__module__' : 'vedo_service_pb2'
  # @@protoc_insertion_point(class_scope:protos.User)
  })
_sym_db.RegisterMessage(User)

ShuzuRequest = _reflection.GeneratedProtocolMessageType('ShuzuRequest', (_message.Message,), {
  'DESCRIPTOR' : _SHUZUREQUEST,
  '__module__' : 'vedo_service_pb2'
  # @@protoc_insertion_point(class_scope:protos.ShuzuRequest)
  })
_sym_db.RegisterMessage(ShuzuRequest)

Shuzu = _reflection.GeneratedProtocolMessageType('Shuzu', (_message.Message,), {
  'DESCRIPTOR' : _SHUZU,
  '__module__' : 'vedo_service_pb2'
  # @@protoc_insertion_point(class_scope:protos.Shuzu)
  })
_sym_db.RegisterMessage(Shuzu)



_VEDO = _descriptor.ServiceDescriptor(
  name='Vedo',
  full_name='protos.Vedo',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=297,
  serialized_end=381,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetMeshPoints',
    full_name='protos.Vedo.GetMeshPoints',
    index=0,
    containing_service=None,
    input_type=_GETMESHPOINTSREQUEST,
    output_type=_GETMESHPOINTSRESULT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_VEDO)

DESCRIPTOR.services_by_name['Vedo'] = _VEDO

# @@protoc_insertion_point(module_scope)
