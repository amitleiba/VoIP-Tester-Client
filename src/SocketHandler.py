import socket
from Message import Message

class SocketHandler:
    def __init__(self):
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            
    def connect(self, host: str, port: int):
        self._host = host
        self._port = port
        self._socket.connect((self._host, self._port))

    def disconnect(self):
        self._socket.close()
    
    def send(self, serilized_message):
        if self._socket is not None:
            self._socket.send(serilized_message)

    def receive(self):
        if self._socket is not None:
            header = self._socket.recv(4)
            data_size = int.from_bytes(header, 'little', signed=False)
            print(f"Data size: {data_size}")
            data = self._socket.recv(data_size)
            print(f"Data: {data}")
            return Message(data)