from logging import Handler
from serialize import Serialize
from zmqClient import ClientTask

class SqlogHandler(Handler):
  """ LogHandler to write to sqlite databases via a zmq network """

  def __init__(self, server, port):
    """ This is a comment """
    Handler.__init__(self)
    self.serializer = Serialize()
    self.zmq = ClientTask(server, port)
 
  def emit(self, record):
    """ This is a comment """
    # serrecord = self.serializer.serialize(record.__dict__)
    serrecord = self.serializer.serialize(record)
    self.zmq.send_log(serrecord)

  def format(self, record):
    """ There is to be no formatting """
    return record

  def flush(self):
    """ There is to be no flushing """
    return

  def close(self):
    """ This is a comment. Because good coding style. """
    try:
      self.zmq.close()
    except:
      pass
