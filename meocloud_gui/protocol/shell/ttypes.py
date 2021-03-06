#
# Autogenerated by Thrift Compiler (0.9.1)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py:new_style,slots
#

from thrift.Thrift import TType, TMessageType, TException, TApplicationException

from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None


class NotificationType(object):
  FILE_STATUS = 0

  _VALUES_TO_NAMES = {
    0: "FILE_STATUS",
  }

  _NAMES_TO_VALUES = {
    "FILE_STATUS": 0,
  }

class FileState(object):
  READY = 0
  SYNCING = 1
  IGNORED = 2
  ERROR = 3

  _VALUES_TO_NAMES = {
    0: "READY",
    1: "SYNCING",
    2: "IGNORED",
    3: "ERROR",
  }

  _NAMES_TO_VALUES = {
    "READY": 0,
    "SYNCING": 1,
    "IGNORED": 2,
    "ERROR": 3,
  }

class MessageType(object):
  SUBSCRIBE_PATH = 0
  SHARE = 1
  OPEN = 2
  FILE_STATUS = 3

  _VALUES_TO_NAMES = {
    0: "SUBSCRIBE_PATH",
    1: "SHARE",
    2: "OPEN",
    3: "FILE_STATUS",
  }

  _NAMES_TO_VALUES = {
    "SUBSCRIBE_PATH": 0,
    "SHARE": 1,
    "OPEN": 2,
    "FILE_STATUS": 3,
  }

class SubscribeType(object):
  SUBSCRIBE = 0
  UNSUBSCRIBE = 1

  _VALUES_TO_NAMES = {
    0: "SUBSCRIBE",
    1: "UNSUBSCRIBE",
  }

  _NAMES_TO_VALUES = {
    "SUBSCRIBE": 0,
    "UNSUBSCRIBE": 1,
  }

class ShareType(object):
  LINK = 0
  FOLDER = 1

  _VALUES_TO_NAMES = {
    0: "LINK",
    1: "FOLDER",
  }

  _NAMES_TO_VALUES = {
    "LINK": 0,
    "FOLDER": 1,
  }

class OpenType(object):
  BROWSER = 0

  _VALUES_TO_NAMES = {
    0: "BROWSER",
  }

  _NAMES_TO_VALUES = {
    "BROWSER": 0,
  }

class FileStatusType(object):
  REQUEST = 0
  RESPONSE = 1
  MULTI_REQUEST = 2
  MULTI_RESPONSE = 3

  _VALUES_TO_NAMES = {
    0: "REQUEST",
    1: "RESPONSE",
    2: "MULTI_REQUEST",
    3: "MULTI_RESPONSE",
  }

  _NAMES_TO_VALUES = {
    "REQUEST": 0,
    "RESPONSE": 1,
    "MULTI_REQUEST": 2,
    "MULTI_RESPONSE": 3,
  }


class SubscribeMessage(object):
  """
  Attributes:
   - type
   - path
  """

  __slots__ = [ 
    'type',
    'path',
   ]

  thrift_spec = (
    None, # 0
    (1, TType.I32, 'type', None, None, ), # 1
    (2, TType.STRING, 'path', None, None, ), # 2
  )

  def __init__(self, type=None, path=None,):
    self.type = type
    self.path = path

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.I32:
          self.type = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.path = iprot.readString();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('SubscribeMessage')
    if self.type is not None:
      oprot.writeFieldBegin('type', TType.I32, 1)
      oprot.writeI32(self.type)
      oprot.writeFieldEnd()
    if self.path is not None:
      oprot.writeFieldBegin('path', TType.STRING, 2)
      oprot.writeString(self.path)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, getattr(self, key))
      for key in self.__slots__]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    if not isinstance(other, self.__class__):
      return False
    for attr in self.__slots__:
      my_val = getattr(self, attr)
      other_val = getattr(other, attr)
      if my_val != other_val:
        return False
    return True

  def __ne__(self, other):
    return not (self == other)


class ShareMessage(object):
  """
  Attributes:
   - type
   - path
  """

  __slots__ = [ 
    'type',
    'path',
   ]

  thrift_spec = (
    None, # 0
    (1, TType.I32, 'type', None, None, ), # 1
    (2, TType.STRING, 'path', None, None, ), # 2
  )

  def __init__(self, type=None, path=None,):
    self.type = type
    self.path = path

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.I32:
          self.type = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.path = iprot.readString();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('ShareMessage')
    if self.type is not None:
      oprot.writeFieldBegin('type', TType.I32, 1)
      oprot.writeI32(self.type)
      oprot.writeFieldEnd()
    if self.path is not None:
      oprot.writeFieldBegin('path', TType.STRING, 2)
      oprot.writeString(self.path)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, getattr(self, key))
      for key in self.__slots__]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    if not isinstance(other, self.__class__):
      return False
    for attr in self.__slots__:
      my_val = getattr(self, attr)
      other_val = getattr(other, attr)
      if my_val != other_val:
        return False
    return True

  def __ne__(self, other):
    return not (self == other)


class OpenMessage(object):
  """
  Attributes:
   - type
   - path
  """

  __slots__ = [ 
    'type',
    'path',
   ]

  thrift_spec = (
    None, # 0
    (1, TType.I32, 'type', None, None, ), # 1
    (2, TType.STRING, 'path', None, None, ), # 2
  )

  def __init__(self, type=None, path=None,):
    self.type = type
    self.path = path

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.I32:
          self.type = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.path = iprot.readString();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('OpenMessage')
    if self.type is not None:
      oprot.writeFieldBegin('type', TType.I32, 1)
      oprot.writeI32(self.type)
      oprot.writeFieldEnd()
    if self.path is not None:
      oprot.writeFieldBegin('path', TType.STRING, 2)
      oprot.writeString(self.path)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, getattr(self, key))
      for key in self.__slots__]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    if not isinstance(other, self.__class__):
      return False
    for attr in self.__slots__:
      my_val = getattr(self, attr)
      other_val = getattr(other, attr)
      if my_val != other_val:
        return False
    return True

  def __ne__(self, other):
    return not (self == other)


class FileStatus(object):
  """
  Attributes:
   - path
   - state
  """

  __slots__ = [ 
    'path',
    'state',
   ]

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'path', None, None, ), # 1
    (2, TType.I32, 'state', None, None, ), # 2
  )

  def __init__(self, path=None, state=None,):
    self.path = path
    self.state = state

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.path = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.I32:
          self.state = iprot.readI32();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('FileStatus')
    if self.path is not None:
      oprot.writeFieldBegin('path', TType.STRING, 1)
      oprot.writeString(self.path)
      oprot.writeFieldEnd()
    if self.state is not None:
      oprot.writeFieldBegin('state', TType.I32, 2)
      oprot.writeI32(self.state)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, getattr(self, key))
      for key in self.__slots__]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    if not isinstance(other, self.__class__):
      return False
    for attr in self.__slots__:
      my_val = getattr(self, attr)
      other_val = getattr(other, attr)
      if my_val != other_val:
        return False
    return True

  def __ne__(self, other):
    return not (self == other)


class FileStatusMessage(object):
  """
  Attributes:
   - type
   - status
   - statuses
  """

  __slots__ = [ 
    'type',
    'status',
    'statuses',
   ]

  thrift_spec = (
    None, # 0
    (1, TType.I32, 'type', None, None, ), # 1
    (2, TType.STRUCT, 'status', (FileStatus, FileStatus.thrift_spec), None, ), # 2
    (3, TType.LIST, 'statuses', (TType.STRUCT,(FileStatus, FileStatus.thrift_spec)), None, ), # 3
  )

  def __init__(self, type=None, status=None, statuses=None,):
    self.type = type
    self.status = status
    self.statuses = statuses

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.I32:
          self.type = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRUCT:
          self.status = FileStatus()
          self.status.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.LIST:
          self.statuses = []
          (_etype3, _size0) = iprot.readListBegin()
          for _i4 in xrange(_size0):
            _elem5 = FileStatus()
            _elem5.read(iprot)
            self.statuses.append(_elem5)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('FileStatusMessage')
    if self.type is not None:
      oprot.writeFieldBegin('type', TType.I32, 1)
      oprot.writeI32(self.type)
      oprot.writeFieldEnd()
    if self.status is not None:
      oprot.writeFieldBegin('status', TType.STRUCT, 2)
      self.status.write(oprot)
      oprot.writeFieldEnd()
    if self.statuses is not None:
      oprot.writeFieldBegin('statuses', TType.LIST, 3)
      oprot.writeListBegin(TType.STRUCT, len(self.statuses))
      for iter6 in self.statuses:
        iter6.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, getattr(self, key))
      for key in self.__slots__]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    if not isinstance(other, self.__class__):
      return False
    for attr in self.__slots__:
      my_val = getattr(self, attr)
      other_val = getattr(other, attr)
      if my_val != other_val:
        return False
    return True

  def __ne__(self, other):
    return not (self == other)


class Message(object):
  """
  Attributes:
   - type
   - subscribe
   - share
   - open
   - fileStatus
  """

  __slots__ = [ 
    'type',
    'subscribe',
    'share',
    'open',
    'fileStatus',
   ]

  thrift_spec = (
    None, # 0
    (1, TType.I32, 'type', None, None, ), # 1
    (2, TType.STRUCT, 'subscribe', (SubscribeMessage, SubscribeMessage.thrift_spec), None, ), # 2
    (3, TType.STRUCT, 'share', (ShareMessage, ShareMessage.thrift_spec), None, ), # 3
    (4, TType.STRUCT, 'open', (OpenMessage, OpenMessage.thrift_spec), None, ), # 4
    (5, TType.STRUCT, 'fileStatus', (FileStatusMessage, FileStatusMessage.thrift_spec), None, ), # 5
  )

  def __init__(self, type=None, subscribe=None, share=None, open=None, fileStatus=None,):
    self.type = type
    self.subscribe = subscribe
    self.share = share
    self.open = open
    self.fileStatus = fileStatus

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.I32:
          self.type = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRUCT:
          self.subscribe = SubscribeMessage()
          self.subscribe.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRUCT:
          self.share = ShareMessage()
          self.share.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.STRUCT:
          self.open = OpenMessage()
          self.open.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.STRUCT:
          self.fileStatus = FileStatusMessage()
          self.fileStatus.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('Message')
    if self.type is not None:
      oprot.writeFieldBegin('type', TType.I32, 1)
      oprot.writeI32(self.type)
      oprot.writeFieldEnd()
    if self.subscribe is not None:
      oprot.writeFieldBegin('subscribe', TType.STRUCT, 2)
      self.subscribe.write(oprot)
      oprot.writeFieldEnd()
    if self.share is not None:
      oprot.writeFieldBegin('share', TType.STRUCT, 3)
      self.share.write(oprot)
      oprot.writeFieldEnd()
    if self.open is not None:
      oprot.writeFieldBegin('open', TType.STRUCT, 4)
      self.open.write(oprot)
      oprot.writeFieldEnd()
    if self.fileStatus is not None:
      oprot.writeFieldBegin('fileStatus', TType.STRUCT, 5)
      self.fileStatus.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, getattr(self, key))
      for key in self.__slots__]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    if not isinstance(other, self.__class__):
      return False
    for attr in self.__slots__:
      my_val = getattr(self, attr)
      other_val = getattr(other, attr)
      if my_val != other_val:
        return False
    return True

  def __ne__(self, other):
    return not (self == other)

