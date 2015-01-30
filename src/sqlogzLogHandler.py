import logging

class sqlogHandler (logging.NullHandler):
  """ comment """

  def emit(self, record):
    print record

  def handle(self, record):
    print record

