from logging import Handler

class sqlogHandler(Handler):
  """ comment """

  def emit(self, record):
    print record

  def handle(self, record):
    print record

