# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: connection.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10\x63onnection.proto\"]\n\x11\x43onnectionMessage\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x11\n\tperson_id\x18\x02 \x01(\x05\x12\x12\n\ncoordinate\x18\x03 \x01(\t\x12\x15\n\rcreation_time\x18\x04 \x01(\t2E\n\x11\x43onnectionService\x12\x30\n\x06\x43reate\x12\x12.ConnectionMessage\x1a\x12.ConnectionMessageb\x06proto3')



_CONNECTIONMESSAGE = DESCRIPTOR.message_types_by_name['ConnectionMessage']
ConnectionMessage = _reflection.GeneratedProtocolMessageType('ConnectionMessage', (_message.Message,), {
  'DESCRIPTOR' : _CONNECTIONMESSAGE,
  '__module__' : 'connection_pb2'
  # @@protoc_insertion_point(class_scope:ConnectionMessage)
  })
_sym_db.RegisterMessage(ConnectionMessage)

_CONNECTIONSERVICE = DESCRIPTOR.services_by_name['ConnectionService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CONNECTIONMESSAGE._serialized_start=20
  _CONNECTIONMESSAGE._serialized_end=113
  _CONNECTIONSERVICE._serialized_start=115
  _CONNECTIONSERVICE._serialized_end=184
# @@protoc_insertion_point(module_scope)
