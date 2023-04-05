from VTCPOpcode import VTCPOpcode
from VTCPClient import Client
from Message import Message
from Page import Ui_MainWindow
from PyQt5 import QtWidgets
import sys
import json

class GUI:
    def __init__(self):
        self.is_connected = False
        self.client = Client(self.updateAutoTestLable,
                            self.updateManulTestLabel1, self.updateManulTestLabel2,
                            self.updateManulTestLabel3, self.onVtcpHistoryHeaderResult,
                            self.onVtcpHistoryLogResult)
        self.app = QtWidgets.QApplication(sys.argv)
        self.ui = Ui_MainWindow(self.filterAutoTestLable)
        self.AutoTestText = ''
        
    def initButtons(self):
        self.ui.auto_test_signal.connect(self.onAutoTestButtonClicked)
        self.ui.manual_test_signal.connect(self.onManualTestButtonClicked)
        self.ui.connect_signal.connect(self.onConnectButtonClicked)
        self.ui.disconnect_signal.connect(self.onDisconnectButtonClicked)
        self.ui.print_log.connect(self.ui.printLog)
        self.ui.item_clicked_signal.connect(self.onItemClickedInHistoryList)
        self.ui.openPopupWindow_signal.connect(self.ui.openPopupWindow)

    def runGui(self):
        self.ui.show()
        self.initButtons()
        # self.onVtcpHistoryHeaderResult("")
        sys.exit(self.app.exec_())

    def updateAutoTestLable(self, text :str):
        self.AutoTestText = text
        self.ui.print_log.emit(self.ui.auto_tests_log_text_browser, text)

    def updateManulTestLabel1(self, text : str):
        self.ui.print_log.emit(self.ui.softphone_log_text_browser_1, text)

    def updateManulTestLabel2(self, text : str):
        self.ui.print_log.emit(self.ui.softphone_log_text_browser_1, text)
    
    def updateManulTestLabel3(self, text : str):
        self.ui.print_log.emit(self.ui.softphone_log_text_browser_1, text)

    def filterAutoTestLable(self, item_text):
        if self.AutoTestText == '':
            return
        if item_text == 'ALL':
            self.updateAutoTestLable(self.AutoTestText)
        else:
            json_list = json.loads(self.AutoTestText)
            filtered_list = []
            for json_item in json_list['data']:
                if json_item['type'] in self.ui.comboBox.selected_items:
                    filtered_list.append(json_item)
            json_list['data'] = filtered_list
            json_text = self.format_json(json.dumps(json_list))
            self.ui.print_log.emit(self.ui.auto_tests_log_text_browser, json_text)
    
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
    
    def onVtcpHistoryHeaderResult(self, data):
        # data = '{"creation-time": "2023-02-23 10-31-22", "data": [{"type": "info", "description-time": "10-31-22:492", "description": "SIP REGISTER OK from 9995@127.0.0.1"}]},{"creation-time": "2023-02-23 10-31-22", "data": [{"type": "info", "description-time": "10-31-22:492", "description": "SIP REGISTER OK from 9995@127.0.0.1"}]}'
        json_list = json.loads(data)
        for i in range(len(json_list['headers'])):
            self.ui.Log_History_List_Widget.addItem(self.format_json(json.dumps(json_list['headers'][i])))

                # '_id: ' + json_list['headers'][i]['_id'] +',\ncreation-time: ' + json_list['headers'][i]['creation-time'])
        # self.ui.Log_History_List_Widget.addItem(data)

    def onVtcpHistoryLogResult(self, data):
        formated_data = self.format_json(data)
        self.ui.openPopupWindow_signal.emit(formated_data)
    
    def onItemClickedInHistoryList(self, data: str):
        if(not self.is_connected):
            return
        
        message = Message()
        message.push_integer(VTCPOpcode.VTCP_HISTORY_LOG_REQ.value)
        json_list = json.loads(data)
        message.push_string(str(json_list['_id']))
        self.client.send(message)
        
    def onConnectButtonClicked(self, domain : str):
        if(self.is_connected):
            return
        
        print(f"onConnectButtonClicked {domain}")
        try:
            self.client.connect(domain)
            self.is_connected = True
            message = Message()
            message.push_integer(VTCPOpcode.VTCP_CONNECT_REQ.value)
            self.client.send(message)
        except:
            self.is_connected = False
            print('Connection error')

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