from VTCPOpcode import VTCPOpcode
from VTCPClient import Client
from Message import Message
from Page import Ui_MainWindow
from PyQt5 import QtWidgets
import sys

class GUI:
    def __init__(self):
        self.is_connected = False
        self.client = Client(self.updateAutoTestLable, self.updateManulTestLabel1, self.updateManulTestLabel2, self.updateManulTestLabel3)
        self.app = QtWidgets.QApplication(sys.argv)
        self.ui = Ui_MainWindow()
        
    def initButtons(self):
        self.ui.auto_test_signal.connect(self.onAutoTestButtonClicked)
        self.ui.manual_test_signal.connect(self.onManualTestButtonClicked)
        self.ui.connect_signal.connect(self.onConnectButtonClicked)
        self.ui.disconnect_signal.connect(self.onDisconnectButtonClicked)
        self.ui.print_log.connect(self.ui.printLog)

    def runGui(self):
        self.ui.show()
        self.initButtons()
        sys.exit(self.app.exec_())

    def updateAutoTestLable(self, text :str):
        self.ui.print_log.emit(self.ui.auto_tests_log_text_browser, text)

    def updateManulTestLabel1(self, text : str):
        self.ui.print_log.emit(self.ui.softphone_log_text_browser_1, text)

    def updateManulTestLabel2(self, text : str):
        self.ui.print_log.emit(self.ui.softphone_log_text_browser_1, text)
    
    def updateManulTestLabel3(self, text : str):
        self.ui.print_log.emit(self.ui.softphone_log_text_browser_1, text)
        
    def onConnectButtonClicked(self, domain : str):
        if(self.is_connected):
            return
        
        print(f"onConnectButtonClicked {domain}")
        # try:
        self.client.connect(domain)
        self.is_connected = True
        message = Message()
        message.push_integer(VTCPOpcode.VTCP_CONNECT_REQ.value)
        self.client.send(message)
        # except:
        #     self.is_connected = False

    def onDisconnectButtonClicked(self):
        if(not self.is_connected):
            return

        print("onDisconnectButtonClicked")

        message = Message()
        message.push_integer(VTCPOpcode.VTCP_DISCONNECT_REQ.value)
        self.client.send(message)
        self.client.disconnect()
        self.is_connected = False

    def onManualTestButtonClicked(self, pbx_ip: str):
        print(f"onManualTestButtonClicked {pbx_ip}")
        if(not self.is_connected):
            return

        message = Message()
        message.push_integer(VTCPOpcode.VTCP_MANUAL_TEST_REQ.value)
        message.push_string(pbx_ip)
        self.client.send(message)

    def onAutoTestButtonClicked(self, pbx_ip: str, amount :str):
        print(f"onAutoTestButtonClicked {pbx_ip}, {amount}")
        if(not self.is_connected):
            return

        message = Message()
        message.push_integer(VTCPOpcode.VTCP_AUTO_TEST_REQ.value)
        message.push_string(pbx_ip)
        message.push_integer(int(amount))
        self.client.send(message)