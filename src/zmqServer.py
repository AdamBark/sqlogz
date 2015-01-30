import zmq

class ServerTask(object):
    def __init__(self, port=5555):
        self.port = port
        self._stop = False
        self.callback = None

    def register_callback(self, callback_func):
        """Register a function to be called with received strings"""
        self.callback = callback_func

    def run(self):
        """Start the server thread"""
        context = zmq.Context()
        frontend = context.socket(zmq.ROUTER)
        frontend.bind('tcp://*:' + str(self.port))

        poll = zmq.Poller()
        poll.register(frontend, zmq.POLLIN)

        while not self._stop:
            sockets = dict(poll.poll())
            if frontend in sockets:
                ident, msg, data = frontend.recv_multipart()
                print('Server received %s id %s' % (msg, ident))
                print self.callback(data)

        frontend.close()
        context.term()
        pass

    def stop(self):
        self._stop = True


# Testing
if __name__ == '__main__':
    import serialize
    server = ServerTask()
    serializer = serialize.Serialize()
    server.register_callback(lambda x: serializer.deserialize(x))
    server.run()
