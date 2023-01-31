class Message:
    def __init__(self, payload=None):
        if payload is None:
            payload = bytearray()
        self._payload = payload
        self._index = 0

    def read_integer(self):
        if not self.can_read(4):
            raise ValueError("Cannot read an integer from the payload")
        value = int.from_bytes(self._payload[self._index:self._index+4], 'little')
        self._index += 4
        return value

    def read_string(self):
        size = self.read_integer()
        if not self.can_read(size):
            raise ValueError("Cannot read a string from the payload")
        value = self._payload[self._index:self._index+size].decode()
        self._index += size
        return value

    def read_byte(self):
        if not self.can_read(1):
            raise ValueError("Cannot read a byte from the payload")
        value = self._payload[self._index]
        self._index += 1
        return value

    def can_read(self, size):
        return size > 0 and self._index + size <= len(self._payload)

    def push_integer(self, integer : int):
        self._payload.extend(integer.to_bytes(4, byteorder='little'))

    def push_string(self, string :  str):
        self.push_integer(len(string))
        self._payload.extend(string.encode())

    def get_payload(self):
        return self._payload

    def get_index(self):
        return self._index

    def push_size(self):
        size = len(self._payload)
        self._payload[:] = size.to_bytes(4, byteorder='little') + self._payload