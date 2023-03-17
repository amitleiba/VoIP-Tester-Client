from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(QtWidgets.QMainWindow):

    auto_test_signal = QtCore.pyqtSignal(str, str)
    manual_test_signal = QtCore.pyqtSignal(str)
    connect_signal = QtCore.pyqtSignal(str)
    disconnect_signal = QtCore.pyqtSignal()
    print_log = QtCore.pyqtSignal(QtWidgets.QTextBrowser, str)

    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.setObjectName("MainWindow")
        self.resize(1303, 845)
        self.setAutoFillBackground(False)
        self.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(250, 0, 1060, 850))
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.Auto_Tests = QtWidgets.QWidget()
        self.Auto_Tests.setObjectName("Auto_Tests")
        self.auto_tests_main_label = QtWidgets.QLabel(self.Auto_Tests)
        self.auto_tests_main_label.setGeometry(QtCore.QRect(80, 30, 471, 33))
        self.auto_tests_main_label.setObjectName("auto_tests_main_label")
        self.auto_tests_amout_edit_text = QtWidgets.QTextEdit(self.Auto_Tests)
        self.auto_tests_amout_edit_text.setGeometry(QtCore.QRect(430, 170, 261, 31))
        self.auto_tests_amout_edit_text.setObjectName("auto_tests_amout_edit_text")
        self.auto_tests_button = QtWidgets.QPushButton(self.Auto_Tests)
        self.auto_tests_button.setGeometry(QtCore.QRect(760, 140, 75, 23))
        self.auto_tests_button.setObjectName("auto_tests_button")
        self.auto_tests_pbx_ip_edit_text = QtWidgets.QTextEdit(self.Auto_Tests)
        self.auto_tests_pbx_ip_edit_text.setGeometry(QtCore.QRect(430, 100, 261, 31))
        self.auto_tests_pbx_ip_edit_text.setObjectName("auto_tests_pbx_ip_edit_text")
        self.auto_tests_pbx_ip_label = QtWidgets.QLabel(self.Auto_Tests)
        self.auto_tests_pbx_ip_label.setGeometry(QtCore.QRect(270, 100, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.auto_tests_pbx_ip_label.setFont(font)
        self.auto_tests_pbx_ip_label.setObjectName("auto_tests_pbx_ip_label")
        self.auto_tests_amout_label = QtWidgets.QLabel(self.Auto_Tests)
        self.auto_tests_amout_label.setGeometry(QtCore.QRect(270, 170, 112, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.auto_tests_amout_label.setFont(font)
        self.auto_tests_amout_label.setObjectName("auto_tests_amout_label")
        self.auto_tests_log_text_browser = QtWidgets.QTextBrowser(self.Auto_Tests)
        self.auto_tests_log_text_browser.setGeometry(QtCore.QRect(2, 260, 1045, 555))
        self.auto_tests_log_text_browser.setObjectName("auto_tests_log_text_browser")
        self.auto_tests_log_label = QtWidgets.QLabel(self.Auto_Tests)
        self.auto_tests_log_label.setGeometry(QtCore.QRect(10, 225, 89, 28))
        self.auto_tests_log_label.setObjectName("auto_tests_log_label")
        self.tabWidget.addTab(self.Auto_Tests, "")
        self.Manual_Tests = QtWidgets.QWidget()
        self.Manual_Tests.setObjectName("Manual_Tests")
        self.manual_tests_main_label = QtWidgets.QLabel(self.Manual_Tests)
        self.manual_tests_main_label.setGeometry(QtCore.QRect(130, 20, 773, 84))
        self.manual_tests_main_label.setObjectName("manual_tests_main_label")
        self.manual_tests_pbx_ip_edit_text = QtWidgets.QTextEdit(self.Manual_Tests)
        self.manual_tests_pbx_ip_edit_text.setGeometry(QtCore.QRect(270, 120, 481, 41))
        self.manual_tests_pbx_ip_edit_text.setObjectName("manual_tests_pbx_ip_edit_text")
        self.manual_tests_pbx_ip_label = QtWidgets.QLabel(self.Manual_Tests)
        self.manual_tests_pbx_ip_label.setGeometry(QtCore.QRect(210, 120, 41, 33))
        self.manual_tests_pbx_ip_label.setObjectName("manual_tests_pbx_ip_label")
        self.manual_tests_register_button = QtWidgets.QPushButton(self.Manual_Tests)
        self.manual_tests_register_button.setGeometry(QtCore.QRect(770, 120, 93, 41))
        self.manual_tests_register_button.setObjectName("manual_tests_register_button")
        self.softphone_1 = QtWidgets.QFrame(self.Manual_Tests)
        self.softphone_1.setGeometry(QtCore.QRect(0, 180, 350, 641))
        self.softphone_1.setFrameShape(QtWidgets.QFrame.Box)
        self.softphone_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.softphone_1.setObjectName("softphone_1")
        self.softphone_log_label_1 = QtWidgets.QLabel(self.softphone_1)
        self.softphone_log_label_1.setGeometry(QtCore.QRect(10, 390, 50, 16))
        self.softphone_log_label_1.setObjectName("softphone_log_label_1")
        self.softphone_log_text_browser_1 = QtWidgets.QTextBrowser(self.softphone_1)
        self.softphone_log_text_browser_1.setGeometry(QtCore.QRect(2, 410, 346, 230))
        self.softphone_log_text_browser_1.setObjectName("softphone_log_text_browser_1")
        self.softphone_call_button_1 = QtWidgets.QPushButton(self.softphone_1)
        self.softphone_call_button_1.setGeometry(QtCore.QRect(128, 220, 94, 28))
        self.softphone_call_button_1.setObjectName("softphone_call_button_1")
        self.softphone_answer_button_1 = QtWidgets.QPushButton(self.softphone_1)
        self.softphone_answer_button_1.setGeometry(QtCore.QRect(64, 320, 94, 28))
        self.softphone_answer_button_1.setObjectName("softphone_answer_button_1")
        self.softphone_reject_button_1 = QtWidgets.QPushButton(self.softphone_1)
        self.softphone_reject_button_1.setGeometry(QtCore.QRect(192, 320, 94, 28))
        self.softphone_reject_button_1.setObjectName("softphone_reject_button_1")
        self.softphone_id_label_1 = QtWidgets.QLabel(self.softphone_1)
        self.softphone_id_label_1.setGeometry(QtCore.QRect(0, 10, 350, 24))
        self.softphone_id_label_1.setObjectName("softphone_id_label_1")
        self.softphone_request_label_1 = QtWidgets.QLabel(self.softphone_1)
        self.softphone_request_label_1.setGeometry(QtCore.QRect(10, 120, 261, 51))
        self.softphone_request_label_1.setObjectName("softphone_request_label_1")
        self.softphone_dest_edit_text_1 = QtWidgets.QTextEdit(self.softphone_1)
        self.softphone_dest_edit_text_1.setGeometry(QtCore.QRect(40, 170, 271, 41))
        self.softphone_dest_edit_text_1.setObjectName("softphone_dest_edit_text_1")
        self.softphone_status_label = QtWidgets.QLabel(self.softphone_1)
        self.softphone_status_label.setGeometry(QtCore.QRect(10, 70, 55, 16))
        self.softphone_status_label.setObjectName("softphone_status_label")
        self.softphone_current_status_label_1 = QtWidgets.QLabel(self.softphone_1)
        self.softphone_current_status_label_1.setGeometry(QtCore.QRect(80, 70, 55, 16))
        self.softphone_current_status_label_1.setText("")
        self.softphone_current_status_label_1.setObjectName("softphone_current_status_label_1")
        self.softphone_2 = QtWidgets.QFrame(self.Manual_Tests)
        self.softphone_2.setGeometry(QtCore.QRect(350, 180, 350, 641))
        self.softphone_2.setFrameShape(QtWidgets.QFrame.Box)
        self.softphone_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.softphone_2.setObjectName("softphone_2")
        self.softphone_log_label_2 = QtWidgets.QLabel(self.softphone_2)
        self.softphone_log_label_2.setGeometry(QtCore.QRect(10, 390, 50, 16))
        self.softphone_log_label_2.setObjectName("softphone_log_label_2")
        self.softphone_log_text_browser_2 = QtWidgets.QTextBrowser(self.softphone_2)
        self.softphone_log_text_browser_2.setGeometry(QtCore.QRect(2, 410, 346, 230))
        self.softphone_log_text_browser_2.setObjectName("softphone_log_text_browser_2")
        self.softphone_call_button_2 = QtWidgets.QPushButton(self.softphone_2)
        self.softphone_call_button_2.setGeometry(QtCore.QRect(128, 220, 94, 28))
        self.softphone_call_button_2.setObjectName("softphone_call_button_2")
        self.softphone_answer_button_2 = QtWidgets.QPushButton(self.softphone_2)
        self.softphone_answer_button_2.setGeometry(QtCore.QRect(64, 320, 94, 28))
        self.softphone_answer_button_2.setObjectName("softphone_answer_button_2")
        self.softphone_reject_button_2 = QtWidgets.QPushButton(self.softphone_2)
        self.softphone_reject_button_2.setGeometry(QtCore.QRect(192, 320, 94, 28))
        self.softphone_reject_button_2.setObjectName("softphone_reject_button_2")
        self.softphone_id_label_2 = QtWidgets.QLabel(self.softphone_2)
        self.softphone_id_label_2.setGeometry(QtCore.QRect(0, 10, 350, 24))
        self.softphone_id_label_2.setObjectName("softphone_id_label_2")
        self.softphone_request_label_2 = QtWidgets.QLabel(self.softphone_2)
        self.softphone_request_label_2.setGeometry(QtCore.QRect(10, 120, 261, 51))
        self.softphone_request_label_2.setObjectName("softphone_request_label_2")
        self.softphone_dest_edit_text_2 = QtWidgets.QTextEdit(self.softphone_2)
        self.softphone_dest_edit_text_2.setGeometry(QtCore.QRect(40, 170, 271, 41))
        self.softphone_dest_edit_text_2.setObjectName("softphone_dest_edit_text_2")
        self.softphone_status_label_2 = QtWidgets.QLabel(self.softphone_2)
        self.softphone_status_label_2.setGeometry(QtCore.QRect(10, 70, 55, 16))
        self.softphone_status_label_2.setObjectName("softphone_status_label_2")
        self.softphone_current_status_label_2 = QtWidgets.QLabel(self.softphone_2)
        self.softphone_current_status_label_2.setGeometry(QtCore.QRect(80, 70, 55, 16))
        self.softphone_current_status_label_2.setText("")
        self.softphone_current_status_label_2.setObjectName("softphone_current_status_label_2")
        self.softphone_3 = QtWidgets.QFrame(self.Manual_Tests)
        self.softphone_3.setGeometry(QtCore.QRect(700, 180, 350, 641))
        self.softphone_3.setFrameShape(QtWidgets.QFrame.Box)
        self.softphone_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.softphone_3.setObjectName("softphone_3")
        self.softphone_log_label_3 = QtWidgets.QLabel(self.softphone_3)
        self.softphone_log_label_3.setGeometry(QtCore.QRect(10, 390, 50, 16))
        self.softphone_log_label_3.setObjectName("softphone_log_label_3")
        self.softphone_log_text_browser_3 = QtWidgets.QTextBrowser(self.softphone_3)
        self.softphone_log_text_browser_3.setGeometry(QtCore.QRect(2, 410, 346, 230))
        self.softphone_log_text_browser_3.setObjectName("softphone_log_text_browser_3")
        self.softphone_call_button_3 = QtWidgets.QPushButton(self.softphone_3)
        self.softphone_call_button_3.setGeometry(QtCore.QRect(128, 220, 94, 28))
        self.softphone_call_button_3.setObjectName("softphone_call_button_3")
        self.softphone_answer_button_3 = QtWidgets.QPushButton(self.softphone_3)
        self.softphone_answer_button_3.setGeometry(QtCore.QRect(64, 320, 94, 28))
        self.softphone_answer_button_3.setObjectName("softphone_answer_button_3")
        self.softphone_reject_button_3 = QtWidgets.QPushButton(self.softphone_3)
        self.softphone_reject_button_3.setGeometry(QtCore.QRect(192, 320, 94, 28))
        self.softphone_reject_button_3.setObjectName("softphone_reject_button_3")
        self.softphone_id_label_3 = QtWidgets.QLabel(self.softphone_3)
        self.softphone_id_label_3.setGeometry(QtCore.QRect(0, 10, 350, 24))
        self.softphone_id_label_3.setObjectName("softphone_id_label_3")
        self.softphone_request_label_3 = QtWidgets.QLabel(self.softphone_3)
        self.softphone_request_label_3.setGeometry(QtCore.QRect(10, 120, 261, 51))
        self.softphone_request_label_3.setObjectName("softphone_request_label_3")
        self.softphone_dest_edit_text_3 = QtWidgets.QTextEdit(self.softphone_3)
        self.softphone_dest_edit_text_3.setGeometry(QtCore.QRect(40, 170, 271, 41))
        self.softphone_dest_edit_text_3.setObjectName("softphone_dest_edit_text_3")
        self.softphone_status_label_3 = QtWidgets.QLabel(self.softphone_3)
        self.softphone_status_label_3.setGeometry(QtCore.QRect(10, 70, 55, 16))
        self.softphone_status_label_3.setObjectName("softphone_status_label_3")
        self.softphone_current_status_label_3 = QtWidgets.QLabel(self.softphone_3)
        self.softphone_current_status_label_3.setGeometry(QtCore.QRect(80, 70, 55, 16))
        self.softphone_current_status_label_3.setText("")
        self.softphone_current_status_label_3.setObjectName("softphone_current_status_label_3")
        self.tabWidget.addTab(self.Manual_Tests, "")
        self.History = QtWidgets.QWidget()
        self.History.setObjectName("History")
        self.tabWidget.addTab(self.History, "")
        self.Settings = QtWidgets.QWidget()
        self.Settings.setObjectName("Settings")
        self.tabWidget.addTab(self.Settings, "")
        self.About = QtWidgets.QWidget()
        self.About.setObjectName("About")
        self.tabWidget.addTab(self.About, "")
        self.VoIP_Tester_Label = QtWidgets.QLabel(self.centralwidget)
        self.VoIP_Tester_Label.setGeometry(QtCore.QRect(0, 0, 250, 250))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.VoIP_Tester_Label.setFont(font)
        self.VoIP_Tester_Label.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.VoIP_Tester_Label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.VoIP_Tester_Label.setAutoFillBackground(True)
        self.VoIP_Tester_Label.setScaledContents(True)
        self.VoIP_Tester_Label.setObjectName("VoIP_Tester_Label")
        self.connect_frame = QtWidgets.QFrame(self.centralwidget)
        self.connect_frame.setGeometry(QtCore.QRect(0, 250, 250, 600))
        self.connect_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.connect_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.connect_frame.setObjectName("connect_frame")
        self.connect_frame_Connect_button = QtWidgets.QPushButton(self.connect_frame)
        self.connect_frame_Connect_button.setGeometry(QtCore.QRect(80, 320, 75, 23))
        self.connect_frame_Connect_button.setObjectName("connect_frame_Connect_button")
        self.connect_frame_ip_edit_text = QtWidgets.QTextEdit(self.connect_frame)
        self.connect_frame_ip_edit_text.setGeometry(QtCore.QRect(30, 270, 181, 31))
        self.connect_frame_ip_edit_text.setObjectName("connect_frame_ip_edit_text")
        self.connect_frame_text_label = QtWidgets.QLabel(self.connect_frame)
        self.connect_frame_text_label.setGeometry(QtCore.QRect(20, 90, 221, 101))
        self.connect_frame_text_label.setObjectName("connect_frame_text_label")
        self.connect_frame_ip_label = QtWidgets.QLabel(self.connect_frame)
        self.connect_frame_ip_label.setGeometry(QtCore.QRect(30, 250, 47, 13))
        self.connect_frame_ip_label.setObjectName("connect_frame_ip_label")
        self.connect_frame_disconnect_button = QtWidgets.QPushButton(self.connect_frame)
        self.connect_frame_disconnect_button.setGeometry(QtCore.QRect(150, 560, 93, 28))
        self.connect_frame_disconnect_button.setObjectName("connect_frame_disconnect_button")
        self.setCentralWidget(self.centralwidget)

        self.retranslateUi()
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(self)

        self.auto_tests_button.clicked.connect(self.autoTestClicked)
        self.manual_tests_register_button.clicked.connect(self.manualTestClicked)
        self.connect_frame_Connect_button.clicked.connect(self.connectClicked)
        self.connect_frame_disconnect_button.clicked.connect(self.disconnectClicked)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.auto_tests_main_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">Please Enter the required details below:</span></p></body></html>"))
        self.auto_tests_amout_edit_text.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8.25pt;\"><br /></p></body></html>"))
        self.auto_tests_button.setText(_translate("MainWindow", "Send"))
        self.auto_tests_pbx_ip_label.setText(_translate("MainWindow", "PBX IP:"))
        self.auto_tests_amout_label.setText(_translate("MainWindow", "Amout of calls:"))
        self.auto_tests_log_text_browser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.auto_tests_log_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">Text log:</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Auto_Tests), _translate("MainWindow", "Auto Tests"))
        self.manual_tests_main_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">Please enter the IP of the PBX to which you would like the</span></p><p><span style=\" font-size:18pt;\">softphone to be registered</span></p></body></html>"))
        self.manual_tests_pbx_ip_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">IP:</span></p></body></html>"))
        self.manual_tests_register_button.setText(_translate("MainWindow", "Register"))
        self.softphone_log_label_1.setText(_translate("MainWindow", "Text log:"))
        self.softphone_call_button_1.setText(_translate("MainWindow", "Call"))
        self.softphone_answer_button_1.setText(_translate("MainWindow", "Answer"))
        self.softphone_reject_button_1.setText(_translate("MainWindow", "Reject"))
        self.softphone_id_label_1.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Softphone id: 1001</span></p></body></html>"))
        self.softphone_request_label_1.setText(_translate("MainWindow", "Enter the id of the sofphone you want to call:"))
        self.softphone_status_label.setText(_translate("MainWindow", "Status:"))
        self.softphone_log_label_2.setText(_translate("MainWindow", "Text log:"))
        self.softphone_call_button_2.setText(_translate("MainWindow", "Call"))
        self.softphone_answer_button_2.setText(_translate("MainWindow", "Answer"))
        self.softphone_reject_button_2.setText(_translate("MainWindow", "Reject"))
        self.softphone_id_label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Softphone id: 1002</span></p></body></html>"))
        self.softphone_request_label_2.setText(_translate("MainWindow", "Enter the id of the sofphone you want to call:"))
        self.softphone_status_label_2.setText(_translate("MainWindow", "Status:"))
        self.softphone_log_label_3.setText(_translate("MainWindow", "Text log:"))
        self.softphone_call_button_3.setText(_translate("MainWindow", "Call"))
        self.softphone_answer_button_3.setText(_translate("MainWindow", "Answer"))
        self.softphone_reject_button_3.setText(_translate("MainWindow", "Reject"))
        self.softphone_id_label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Softphone id: 1003</span></p></body></html>"))
        self.softphone_request_label_3.setText(_translate("MainWindow", "Enter the id of the sofphone you want to call:"))
        self.softphone_status_label_3.setText(_translate("MainWindow", "Status:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Manual_Tests), _translate("MainWindow", "Manual Tests"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.History), _translate("MainWindow", "History"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Settings), _translate("MainWindow", "Settings"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.About), _translate("MainWindow", "About"))
        self.VoIP_Tester_Label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:28pt;\">VoIP</span></p><p align=\"center\"><span style=\" font-size:28pt;\">Tester</span></p><p align=\"center\"><span style=\" font-size:28pt;\">Controller</span></p></body></html>"))
        self.connect_frame_Connect_button.setText(_translate("MainWindow", "Connect"))
        self.connect_frame_text_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"justify\"><span style=\" font-size:10pt; font-weight:600;\">Please enter IP and</span></p><p align=\"justify\"><span style=\" font-size:10pt; font-weight:600;\">the port of the server</span></p><p align=\"justify\"><span style=\" font-size:10pt; font-weight:600;\">inorder to use the tester</span></p></body></html>"))
        self.connect_frame_ip_label.setText(_translate("MainWindow", "IP:"))
        self.connect_frame_disconnect_button.setText(_translate("MainWindow", "Disconnect"))

    def autoTestClicked(self):
        self.auto_test_signal.emit(self.auto_tests_pbx_ip_edit_text.toPlainText(), self.auto_tests_amout_edit_text.toPlainText())
    
    def manualTestClicked(self):
        self.manual_test_signal.emit(self.manual_tests_pbx_ip_edit_text.toPlainText())
    
    def connectClicked(self):
        self.connect_signal.emit(self.connect_frame_ip_edit_text.toPlainText())
    
    def disconnectClicked(self):
        self.disconnect_signal.emit()

    def printLog(self, text_browser : QtWidgets.QTextBrowser, value : str):
        text_browser.setText(text_browser.toPlainText() + value)
