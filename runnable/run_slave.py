import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))


from twisted.internet import reactor


from slave.slave_factory import SlaveFactory


if __name__ == "__main__":

    reactor.connectTCP("localhost", 8000, SlaveFactory())
    print("Client started")
    reactor.run()
