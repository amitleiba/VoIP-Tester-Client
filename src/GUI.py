from VTCPOpcode import VTCPOpcodes
from VTCPClient import Client

class GUI:
    def __init__(self):
        self.client = Client()

    def onConnectButtonClicked(self):
        host = "127.0.0.1"
        port = 5060
        self.client.connect(host, port)
        self.client.send(VTCPOpcodes.ON_VTCP_CONNECT_REQUEST, "")

    def onDisconnectButtonClicked(self):
        self.client.send(VTCPOpcodes.ON_VTCP_DISCONNECT_REQUEST, "")
        self.client.disconnect()

    def onSSPTestButtonClicked(self):
        self.client.send(VTCPOpcodes.ON_VTCP_SSP_REQUEST, "")

    def onSpamTestButtonClicked(self):
        self.client.send(VTCPOpcodes.ON_VTCP_TEST_REQUEST, "")