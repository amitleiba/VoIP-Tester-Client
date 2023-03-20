import socket
from Message import Message

class SocketHandler:
    def __init__(self):
        self.is_connected = False
            
    def connect(self, host: str, port: int):
        if(not self.is_connected):
            self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self._host = host
            self._port = port
            self._socket.connect((self._host, self._port))
            self.is_connected = True

    def disconnect(self):
        if self.is_connected:
            self.is_connected = False
            self._socket.close()
    
    def send(self, serilized_message):
        if self._socket is not None and self.is_connected:
            self._socket.send(serilized_message)

    def receive(self):
        if self._socket is not None and self.is_connected:
            try:
                header = self._socket.recv(4)
                data_size = int.from_bytes(header, 'little', signed=False)
                print(f"Data size: {data_size}")
                # data = self._socket.recv(data_size)
                # print(f'Data len: {len(data)}')
                # print(f"Data: {data}")
                counter = 0
                all_data = b''
                
                while counter < data_size:
                    data =  self._socket.recv(1024)
                    if not data:
                        break
                    all_data += data
                    counter += len(data)
                    print(counter)
                # data =  self._socket.recv(1024)
                # all_data += data
                
                
                print(f'Data len: {len(all_data)}')
                print(all_data)
                return Message(all_data)
            except Exception as e:
                if not self.is_connected:
                    print("Session closed gracefully")
                else:
                    print(f"An exception occurred: {e}")
                    print("Receiver error")
                    self.disconnect()
                return None