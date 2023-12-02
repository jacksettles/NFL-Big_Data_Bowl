# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: nfl_bdb.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rnfl_bdb.proto\"\xbf\x01\n\x10SnapshotMetadata\x12\x0f\n\x07game_id\x18\x01 \x01(\x03\x12\x0f\n\x07play_id\x18\x02 \x01(\x03\x12\x10\n\x08\x66rame_id\x18\x03 \x01(\x03\x12\t\n\x01x\x18\x04 \x01(\x02\x12\t\n\x01y\x18\x05 \x01(\x02\x12\x10\n\x08velocity\x18\x06 \x01(\x02\x12\x14\n\x0c\x61\x63\x63\x65leration\x18\x07 \x01(\x02\x12\x13\n\x0borientation\x18\x08 \x01(\x02\x12\x11\n\tdirection\x18\t \x01(\x02\x12\x11\n\ttimestamp\x18\n \x01(\t\"c\n\x0ePlayerSnapshot\x12#\n\x08metadata\x18\x01 \x01(\x0b\x32\x11.SnapshotMetadata\x12\x0e\n\x06nfl_id\x18\x02 \x01(\x03\x12\x0c\n\x04uuid\x18\x03 \x01(\t\x12\x0e\n\x06weight\x18\x04 \x01(\x02\"A\n\x0c\x42\x61llSnapshot\x12#\n\x08metadata\x18\x01 \x01(\x0b\x32\x11.SnapshotMetadata\x12\x0c\n\x04uuid\x18\x02 \x01(\t\"o\n\tPlayFrame\x12)\n\x10player_snapshots\x18\x01 \x03(\x0b\x32\x0f.PlayerSnapshot\x12$\n\rball_snapshot\x18\x02 \x01(\x0b\x32\r.BallSnapshot\x12\x11\n\ttimestamp\x18\x03 \x01(\t\"\xcc\x03\n\x04Play\x12\x0f\n\x07game_id\x18\x01 \x01(\x03\x12\x0f\n\x07play_id\x18\x02 \x01(\x03\x12\x0c\n\x04uuid\x18\x03 \x01(\t\x12\x1b\n\x13\x62\x61ll_carrier_nfl_id\x18\x04 \x01(\x03\x12\x1b\n\x13yards_to_first_down\x18\x05 \x01(\x03\x12\x14\n\x0cgame_quarter\x18\x06 \x01(\x03\x12\x11\n\tplay_down\x18\x07 \x01(\x03\x12\x12\n\ngame_clock\x18\x08 \x01(\t\x12%\n\x0bpass_result\x18\t \x01(\x0e\x32\x10.Play.PassResult\x12\x14\n\x0cyards_gained\x18\n \x01(\x03\x12\x12\n\nyards_lost\x18\x0b \x01(\x03\x12\x11\n\tyards_net\x18\x0c \x01(\x03\x12\x17\n\x0f\x65nded_in_tackle\x18\r \x01(\x08\x12\x16\n\x0emissed_tackles\x18\x0e \x01(\x03\x12\x16\n\x0etackle_assists\x18\x0f \x01(\x03\x12\x1a\n\x06\x66rames\x18\x10 \x03(\x0b\x32\n.PlayFrame\"T\n\nPassResult\x12\x0c\n\x08\x43OMPLETE\x10\x00\x12\x0e\n\nINCOMPLETE\x10\x01\x12\x08\n\x04SACK\x10\x02\x12\x10\n\x0cINTERCEPTION\x10\x03\x12\x0c\n\x08SCRAMBLE\x10\x04\" \n\x04\x44\x61ta\x12\x18\n\tnfl_plays\x18\x01 \x03(\x0b\x32\x05.Playb\x06proto3')



_SNAPSHOTMETADATA = DESCRIPTOR.message_types_by_name['SnapshotMetadata']
_PLAYERSNAPSHOT = DESCRIPTOR.message_types_by_name['PlayerSnapshot']
_BALLSNAPSHOT = DESCRIPTOR.message_types_by_name['BallSnapshot']
_PLAYFRAME = DESCRIPTOR.message_types_by_name['PlayFrame']
_PLAY = DESCRIPTOR.message_types_by_name['Play']
_DATA = DESCRIPTOR.message_types_by_name['Data']
_PLAY_PASSRESULT = _PLAY.enum_types_by_name['PassResult']
SnapshotMetadata = _reflection.GeneratedProtocolMessageType('SnapshotMetadata', (_message.Message,), {
  'DESCRIPTOR' : _SNAPSHOTMETADATA,
  '__module__' : 'nfl_bdb_pb2'
  # @@protoc_insertion_point(class_scope:SnapshotMetadata)
  })
_sym_db.RegisterMessage(SnapshotMetadata)

PlayerSnapshot = _reflection.GeneratedProtocolMessageType('PlayerSnapshot', (_message.Message,), {
  'DESCRIPTOR' : _PLAYERSNAPSHOT,
  '__module__' : 'nfl_bdb_pb2'
  # @@protoc_insertion_point(class_scope:PlayerSnapshot)
  })
_sym_db.RegisterMessage(PlayerSnapshot)

BallSnapshot = _reflection.GeneratedProtocolMessageType('BallSnapshot', (_message.Message,), {
  'DESCRIPTOR' : _BALLSNAPSHOT,
  '__module__' : 'nfl_bdb_pb2'
  # @@protoc_insertion_point(class_scope:BallSnapshot)
  })
_sym_db.RegisterMessage(BallSnapshot)

PlayFrame = _reflection.GeneratedProtocolMessageType('PlayFrame', (_message.Message,), {
  'DESCRIPTOR' : _PLAYFRAME,
  '__module__' : 'nfl_bdb_pb2'
  # @@protoc_insertion_point(class_scope:PlayFrame)
  })
_sym_db.RegisterMessage(PlayFrame)

Play = _reflection.GeneratedProtocolMessageType('Play', (_message.Message,), {
  'DESCRIPTOR' : _PLAY,
  '__module__' : 'nfl_bdb_pb2'
  # @@protoc_insertion_point(class_scope:Play)
  })
_sym_db.RegisterMessage(Play)

Data = _reflection.GeneratedProtocolMessageType('Data', (_message.Message,), {
  'DESCRIPTOR' : _DATA,
  '__module__' : 'nfl_bdb_pb2'
  # @@protoc_insertion_point(class_scope:Data)
  })
_sym_db.RegisterMessage(Data)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _SNAPSHOTMETADATA._serialized_start=18
  _SNAPSHOTMETADATA._serialized_end=209
  _PLAYERSNAPSHOT._serialized_start=211
  _PLAYERSNAPSHOT._serialized_end=310
  _BALLSNAPSHOT._serialized_start=312
  _BALLSNAPSHOT._serialized_end=377
  _PLAYFRAME._serialized_start=379
  _PLAYFRAME._serialized_end=490
  _PLAY._serialized_start=493
  _PLAY._serialized_end=953
  _PLAY_PASSRESULT._serialized_start=869
  _PLAY_PASSRESULT._serialized_end=953
  _DATA._serialized_start=955
  _DATA._serialized_end=987
# @@protoc_insertion_point(module_scope)