# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tensorflow/core/protobuf/rewriter_config.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='tensorflow/core/protobuf/rewriter_config.proto',
  package='tensorflow',
  syntax='proto3',
  serialized_pb=_b('\n.tensorflow/core/protobuf/rewriter_config.proto\x12\ntensorflow\"0\n\x0eRewriterConfig\x12\x1e\n\x16optimize_tensor_layout\x18\x01 \x01(\x08\x42\x35\n\x18org.tensorflow.frameworkB\x14RewriterConfigProtosP\x01\xf8\x01\x01\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_REWRITERCONFIG = _descriptor.Descriptor(
  name='RewriterConfig',
  full_name='tensorflow.RewriterConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='optimize_tensor_layout', full_name='tensorflow.RewriterConfig.optimize_tensor_layout', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=62,
  serialized_end=110,
)

DESCRIPTOR.message_types_by_name['RewriterConfig'] = _REWRITERCONFIG

RewriterConfig = _reflection.GeneratedProtocolMessageType('RewriterConfig', (_message.Message,), dict(
  DESCRIPTOR = _REWRITERCONFIG,
  __module__ = 'tensorflow.core.protobuf.rewriter_config_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.RewriterConfig)
  ))
_sym_db.RegisterMessage(RewriterConfig)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\030org.tensorflow.frameworkB\024RewriterConfigProtosP\001\370\001\001'))
# @@protoc_insertion_point(module_scope)
