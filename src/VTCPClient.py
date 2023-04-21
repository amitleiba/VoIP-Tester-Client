import threading

from SocketHandler import SocketHandler
from Message import Message
from ResultHandler import ResultHandler

class Client:
    def __init__(self, selfupdateAutoTestLable,
                updateManulTestLabel1, updateManulTestLabel2,
                updateManulTestLabel3, onVtcpHistoryHeaderResult,
                onVtcpHistoryLogResult):
        # self.port = 8080
        self.socket_handler = SocketHandler()
        self.result_handler = ResultHandler(selfupdateAutoTestLable,
                                            updateManulTestLabel1, updateManulTestLabel2,
                                            updateManulTestLabel3, onVtcpHistoryHeaderResult,
                                            onVtcpHistoryLogResult, self.send)
        self.is_connected = False

    def connect(self, host: str, port : int):
        self.socket_handler.connect(host, port)
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

    def isConnected(self):
        return self.is_connected