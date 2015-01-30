import zmq


class ClientTask(object):
    def __init__(self, server, port=5555):
        self.server = server
        self.port = port

    def send_log(self, log_item):
        """Sends a serialized object to the connected server"""
        self.socket.send_string(log_item)

    def connect(self):
        """Connects to remove logz server"""
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.REQ)
        self.socket.connect("tcp://{}:{}".format(self.server, self.port))

    def close(self):
        self.socket.close()
        self.context.term()


if __name__ == "__main__":
    import serialize
    serializer = serialize.Serialize()
    client = ClientTask("localhost")
    client.connect()
    print "Connected"
    client.send_log(serializer.serialize("A string"))
    print "Sent log"
