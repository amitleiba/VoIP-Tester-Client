from VTCPOpcode import VTCPOpcode
from VTCPClient import Client
from Page import Ui_MainWindow
from PyQt5 import QtWidgets
import sys

class GUI:
    def __init__(self):
        self.is_connected = False
        self.client = Client()
        self.app = QtWidgets.QApplication(sys.argv)
        self.ui = Ui_MainWindow()
        
    def initButtons(self):
        self.ui.auto_test_signal.connect(self.onAutoTestButtonClicked)
        self.ui.manual_test_signal.connect(self.onManualTestButtonClicked)
        self.ui.connect_signal.connect(self.onConnectButtonClicked)
        self.ui.disconnect_signal.connect(self.onDisconnectButtonClicked)

    def runGui(self):
        self.ui.show()
        self.initButtons()
        sys.exit(self.app.exec_())
        
    def onConnectButtonClicked(self, domain : str, port :str):
        if(self.is_connected):
            return
        
        print(f"onConnectButtonClicked {domain} , {port}")
        # try:
        self.client.connect(domain, int(port))
        self.is_connected = True
        self.client.send(VTCPOpcode.VTCP_CONNECT, "")
        # except:
        #     self.is_connected = False

    def onDisconnectButtonClicked(self):
        if(not self.is_connected):
            return

        print("onDisconnectButtonClicked")
        self.client.send(VTCPOpcode.VTCP_DISCONNECT, "")
        self.client.disconnect()

    def onManualTestButtonClicked(self, data: str):
        print(f"onManualTestButtonClicked {data}")
        if(not self.is_connected):
            return

        self.client.send(VTCPOpcode.VTCP_MANUAL_TEST, data)

    def onAutoTestButtonClicked(self, data: str):
        print(f"onAutoTestButtonClicked {data}")
        if(not self.is_connected):
            return

        self.client.send(VTCPOpcode.VTCP_AUTO_TEST, data)