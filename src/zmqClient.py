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
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.REQ)
        self.socket.connect("tcp://{}:{}".format(self.server, self.port))

    def close(self):
        self.socket.close()
        self.context.term()
