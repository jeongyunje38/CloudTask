from twisted.internet import reactor, protocol


from .slave_protocol import SlaveProtocol


class SlaveFactory(protocol.ClientFactory):

    def buildProtocol(self, addr: protocol.IAddress) -> protocol.Protocol | None:

        return SlaveProtocol(self)

    def clientConnectionFailed(self, connector, reason):

        print("Connection failed")
        reactor.stop()

    def clientConnectionLost(self, connector, reason):

        print("Connection lost")
        reactor.stop()
