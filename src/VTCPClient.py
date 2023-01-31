import threading

from SocketHandler import SocketHandler
from Message import Message
from ResultHandler import ResultHandler

class Client:
    def __init__(self):
        self.port = 5060
        self.socket_handler = SocketHandler()
        self.result_handler = ResultHandler()
        self.is_connected = False

    def connect(self, host: str):
        self.socket_handler.connect(host, self.port)
        self.is_connected = True
        self.start_listening()

    def disconnect(self):
        self.is_connected = False
        self.socket_handler.disconnect()

    def send(self, message: Message):
        message.push_size()
        self.socket_handler.send(message.get_payload())
    
    def start_listening(self):
        listen_thread = threading.Thread(target=self.listen)
        listen_thread.start()

    def listen(self):
        while(self.is_connected):
            message = self.socket_handler.receive()
            if message != None:
                self.result_handler.handle(message)