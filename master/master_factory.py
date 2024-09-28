from twisted.internet import protocol


from .master_protocol import MasterProtocol


class MasterFactory(protocol.ServerFactory):

    def buildProtocol(self, addr: protocol.IAddress) -> protocol.Protocol | None:

        return MasterProtocol(self)
