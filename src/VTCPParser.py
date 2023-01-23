from VTCPOpcode import VTCPOpcode

class Parser:
    def __init__(self):
        self.HEADER_LENGTH = 4
        self.OPCODE_LENGTH = 4

    def serialize(self, opcode : VTCPOpcode, data : str):
        serialized_message = str(len(data)).zfill(self.HEADER_LENGTH) + str(opcode).zfill(self.OPCODE_LENGTH) + data
        return serialized_message

    def deserialize(self, serialized_message : str):
        opcode = VTCPOpcode(int(serialized_message[:self.OPCODE_LENGTH]))
        data = serialized_message[self.OPCODE_LENGTH:]
        return opcode, data