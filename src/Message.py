class Message:
    def __init__(self, opcode, data):
        self.opcode = opcode
        self.data = data

    def getData(self):
        return self.data