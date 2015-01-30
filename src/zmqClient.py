import zmq

class ClientTask(object):
    def __init__(self, server, port=5555):
        self.server = server
        self.port = port

    def send_log(self, log_item):
        """Sends a serialized object to the connected server"""
        pass

    def connect(self):
        """Connects to remove logz server"""
        pass
