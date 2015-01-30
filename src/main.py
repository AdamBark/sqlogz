
import serialize
import zmqServer
import dbWriter
import logging

class Main:

    def __init__(self):
        self._opts = self.options()
        
    
    def event(self, blob):
        """Event callback on every received log message"""
        ser = serialize.Serialize()
        logrec = ser.deserialize(blob)
        self.dbw.insertRecord(logrec)
        
        self.dbw.commit()
    

    def options(self):
        # TODO: implement proper opt/arg parsing!!!
        return {'logfile': '/tmp/sqlogz.sqlite'}

    def run(self):
        self.dbw = dbWriter.DBWriter(self._opts['logfile'])
        self.server = zmqServer.ServerTask()
        self.server.register_callback(self.event)
        self.server.run()


if __name__=="__main__":
    main = Main()
    main.run()

        
        
