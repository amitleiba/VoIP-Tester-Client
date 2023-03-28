from VTCPOpcode import VTCPOpcode
from Message import Message

class ResultHandler:
    def __init__(self, selfupdateAutoTestLable, updateManulTestLabel1,
                updateManulTestLabel2, updateManulTestLabel3,
                onVtcpHistoryHeaderResult, onVtcpHistoryLogResult, send):
        self._selfupdateAutoTestLable = selfupdateAutoTestLable
        self._updateManulTestLabel1 = updateManulTestLabel1
        self._updateManulTestLabel2 = updateManulTestLabel2
        self._updateManulTestLabel3 = updateManulTestLabel3
        self._send = send
        self._onVtcpHistoryHeaderResult = onVtcpHistoryHeaderResult
        self._onVtcpHistoryLogResult =onVtcpHistoryLogResult
        self.handler = {
            VTCPOpcode.VTCP_CONNECT_RES: self.onVtcpConnectResult,
            VTCPOpcode.VTCP_DISCONNECT_RES: self.onVtcpDisconnectResult,
            VTCPOpcode.VTCP_AUTO_TEST_RES: self.onVtcpAutoTestResult,
            VTCPOpcode.VTCP_MANUAL_TEST_RES: self.onVtcpManualTestResult,
            VTCPOpcode.VTCP_HISTORY_HEADER_RES: self.onVtcpHistoryHeaderResult,
            VTCPOpcode.VTCP_HISTORY_LOG_RES: self.onVtcpHistoryLogResult
        }

    def handle(self, result :Message):
        opcode = VTCPOpcode(result.read_integer())
        return self.handler.get(opcode)(result)

    def onVtcpConnectResult(self, data : Message):
        print("The server returned result for the Connection")
        message = Message()
        message.push_integer(VTCPOpcode.VTCP_HISTORY_HEADER_REQ.value)
        self._send(message)

    def onVtcpHistoryHeaderResult(self, data : Message):
        self._onVtcpHistoryHeaderResult(data.read_string())

    def onVtcpHistoryLogResult(self, data : Message):
        self._onVtcpHistoryLogResult(data.read_string())                

    def onVtcpDisconnectResult(self, data : Message):
        print("The server returned result for the Disconnection")

    def onVtcpAutoTestResult(self, data : Message):
        print("The server returned result for the Auto Test")
        self._selfupdateAutoTestLable(self.format_json(data.read_string()))

    def onVtcpManualTestResult(self, data : Message):
        print("The server returned result for the Manual Test")

    def format_json(self, data : str):
        formatted_str = data.replace(" {", "{")
        formatted_str = formatted_str.replace(",", ",\n")
        formatted_str = formatted_str.replace("{", "{\n")
        formatted_str = formatted_str.replace("}", "\n}")
        formatted_str = formatted_str.replace("[{", "[\n{")
        formatted_str = formatted_str.replace("} ]", "}\n]")
        formatted_str = formatted_str.replace("\"type\"", "   \"type\"")
        formatted_str = formatted_str.replace("\"description-time\"", "   \"description time\"")
        formatted_str = formatted_str.replace("\"description\"", "   \"description\"")
        formatted_str = formatted_str.replace("data : ", "data:\n")
        return formatted_str
