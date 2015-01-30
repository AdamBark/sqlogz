import logging
import logging.handlers

class sqlogHandler(logging.handlers.NullHandler):
  """ comment """

  def emit(self, record):
    print record

  def handle(self, record):
    print record

