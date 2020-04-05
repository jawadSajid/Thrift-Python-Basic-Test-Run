import sys
import aiml

sys.path.append('gen-py/')

from chatbot_message_tranfer2 import chatbot
from chatbot_message_tranfer2.ttypes import *
from chatbot_message_tranfer2.constants import *

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

import socket

class ChatbotServerHandler:

    def transportMessage(self, msg):
        print("Reply from Client: ", msg)
        #response = input("Enter a message: ")
        return response


handler = ChatbotServerHandler()
processor = chatbot.Processor(handler)
transport = TSocket.TServerSocket("172.16.95.195", port=30304)
tfactory = TTransport.TBufferedTransportFactory()
pfactory = TBinaryProtocol.TBinaryProtocolFactory()

server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)

print("Starting python server...")
server.serve()
print ("done!")