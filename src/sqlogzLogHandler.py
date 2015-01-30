from logging import Handler
from serialize import Serialize
from zmqClient import ClientTask

class SqlogHandler(Handler):
  """ comment """

  def __init__(self, server, port):
    Handler.__init__(self)
    self.serializer = Serialize()
    self.zmq = ClientTask(server, port)
 
  def emit(self, record):
    serrecord = self.serializer.serialize(record.__dict__)
    print "emit  : %s\n" % serrecord

  def format(self, record):
    """ There is to be no formatting """
    return record

  def flush(self):
    print "flush\n"

  def close(self):
    print "close\n"
