from twisted.protocols import basic
from twisted.python.failure import Failure


class SlaveProtocol(basic.LineReceiver):

    def __init__(self, factory):

        self.factory = factory

    def connectionMade(self):

        print("Connected to server")
        self.run()

    def connectionLost(self, reason: Failure = ...) -> None:

        print("Disconnected from server")

    def lineReceived(self, line):

        if line == b"STATUS":
            self.send_status()

    def send_status(self):

        self.sendLine(b"IDLE")

    def run(self):

        pass
