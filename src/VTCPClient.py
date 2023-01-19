import SocketHandler
import VTCPOpcode
import VTCPParser

class Client:
    def __init__(self):
        self.socket_handler = SocketHandler.SocketHandler()
        self.parser = VTCPParser.Parser()

    def connect(self, host: str, port: int):
        self.socket_handler.connect(host, port)

    def disconnect(self):
        self.socket_handler.disconnect()

    def send(self, opcode: VTCPOpcode.VTCPOpcodes, data: str):
        serialized_message = self.parser.serialize(opcode, data)
        self.socket_handler.send(serialized_message)
    

