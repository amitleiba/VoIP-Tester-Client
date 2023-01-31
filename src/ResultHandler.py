from VTCPOpcode import VTCPOpcode
from Message import Message

class ResultHandler:
    def __init__(self):
        self.handler = {
            VTCPOpcode.VTCP_CONNECT_RES: self.onVtcpConnectResult,
            VTCPOpcode.VTCP_DISCONNECT_RES: self.onVtcpDisconnectResult,
            VTCPOpcode.VTCP_AUTO_TEST_RES: self.onVtcpAutoTestResult,
            VTCPOpcode.VTCP_MANUAL_TEST_RES: self.onVtcpManualTestResult,
        }

    def handle(self, result :Message):
        opcode = VTCPOpcode(result.read_integer())
        self.handler.get(opcode)(result)

    def onVtcpConnectResult(self, data : Message):
        print("The server returned result for the Connection")
        data_msg = data.read_string()
        print(data_msg)

    def onVtcpDisconnectResult(self, data : Message):
        print("The server returned result for the Disconnection")

    def onVtcpAutoTestResult(self, data : Message):
        print("The server returned result for the Auto Test")

    def onVtcpManualTestResult(self, data : Message):
        print("The server returned result for the Manual Test")