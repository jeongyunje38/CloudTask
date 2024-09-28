import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))


from twisted.internet import reactor


from master.master_factory import MasterFactory


if __name__ == "__main__":

    factory = MasterFactory()
    reactor.listenTCP(8000, factory)
    print("Server started")
    reactor.run()
