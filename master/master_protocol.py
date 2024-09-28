from twisted.internet import task
from twisted.protocols import basic
from twisted.python.failure import Failure


class MasterProtocol(basic.LineReceiver):

    def __init__(self, factory) -> None:

        self.factory = factory
        self.query_client_status_period = 5.0

    def connectionMade(self):

        print("New client connected")
        print(self.transport.getPeer())
        self.run()

    def connectionLost(self, reason: Failure):

        print("Client disconnected")

    def lineReceived(self, line):

        print(line.decode())

        if line == b"STATUS":
            self.send_status()

    def send_status(self):

        self.sendLine(b"IDLE")

    def query_client_status(self):

        self.sendLine(b"STATUS")

    def run(self):

        looping_call = task.LoopingCall(self.query_client_status)
        looping_call.start(self.query_client_status_period)
