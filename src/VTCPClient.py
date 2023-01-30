from SocketHandler import SocketHandler
from Message import Message

class Client:
    def __init__(self):
        self.port = 5060
        self.socket_handler = SocketHandler()
        
    def connect(self, host: str):
        self.socket_handler.connect(host, self.port)

    def disconnect(self):
        self.socket_handler.disconnect()

    def send(self, message: Message):
        message.push_size()
        self.socket_handler.send(message.get_payload())
    

