from logging import Handler

class SqlogHandler(Handler):
  """ comment """

  def emit(self, record):
    print record

  def handle(self, record):
    print record

