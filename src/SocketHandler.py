import socket

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
            print(serilized_message)
            self._socket.send(serilized_message)