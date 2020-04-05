import sys

sys.path.append('gen-py/')

from chatbot_message_tranfer2 import chatbot
from chatbot_message_tranfer2.ttypes import *
from chatbot_message_tranfer2.constants import *

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

try:
    # Make socket
    transport = TSocket.TSocket('172.16.95.195',port=30304)
    transport2 = TSocket.TSocket('172.16.95.195',port=30305)

    # Buffering is critical. Raw sockets are very slow
    transport = TTransport.TBufferedTransport(transport)
    transport2 = TTransport.TBufferedTransport(transport2)

    # Wrap in a protocol
    protocol = TBinaryProtocol.TBinaryProtocol(transport)
    protocol2 = TBinaryProtocol.TBinaryProtocol(transport2)

    # Create a client to use the protocol encoder
    client = chatbot.Client(protocol)
    client2 = chatbot.Client(protocol2)

    # Connect!
    transport.open()
    transport2.open()
    while True:
        msg = input("Your message: ")
        fromServer = client.transportMessage(msg)
        fromServer2 = client2.transportMessage(msg)
        print("From server : ", fromServer)
        print("From server : ", fromServer2)

    transport.close()
    transport2.close()

except Thrift.TException as tx:
    print("%s" % (tx.message))