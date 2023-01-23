from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui_MainWindow(QtWidgets.QMainWindow):

    auto_test_signal = QtCore.pyqtSignal(str)
    manual_test_signal = QtCore.pyqtSignal(str)
    connect_signal = QtCore.pyqtSignal(str, str)
    disconnect_signal = QtCore.pyqtSignal()

    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.setObjectName("MainWindow")
        self.resize(1079, 752)
        self.setAutoFillBackground(False)
        self.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(220, 0, 861, 641))
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setObjectName("tabWidget")
        self.Auto_Tests = QtWidgets.QWidget()
        self.Auto_Tests.setObjectName("Auto_Tests")
        self.auto_tests_label = QtWidgets.QLabel(self.Auto_Tests)
        self.auto_tests_label.setGeometry(QtCore.QRect(111, 220, 641, 71))
        self.auto_tests_label.setObjectName("auto_tests_label")
        self.auto_tests_edit_text = QtWidgets.QTextEdit(self.Auto_Tests)
        self.auto_tests_edit_text.setGeometry(QtCore.QRect(300, 300, 261, 31))
        self.auto_tests_edit_text.setObjectName("auto_tests_edit_text")
        self.auto_tests_button = QtWidgets.QPushButton(self.Auto_Tests)
        self.auto_tests_button.setGeometry(QtCore.QRect(390, 340, 75, 23))
        self.auto_tests_button.setObjectName("auto_tests_button")
        self.tabWidget.addTab(self.Auto_Tests, "")
        self.Manual_Tests = QtWidgets.QWidget()
        self.Manual_Tests.setObjectName("Manual_Tests")
        self.manual_tests_label = QtWidgets.QLabel(self.Manual_Tests)
        self.manual_tests_label.setGeometry(QtCore.QRect(160, 210, 551, 81))
        self.manual_tests_label.setObjectName("manual_tests_label")
        self.manual_tests_edit_text = QtWidgets.QTextEdit(self.Manual_Tests)
        self.manual_tests_edit_text.setGeometry(QtCore.QRect(300, 300, 271, 31))
        self.manual_tests_edit_text.setObjectName("manual_tests_edit_text")
        self.manual_tests_button = QtWidgets.QPushButton(self.Manual_Tests)
        self.manual_tests_button.setGeometry(QtCore.QRect(400, 340, 75, 23))
        self.manual_tests_button.setObjectName("manual_tests_button")
        self.tabWidget.addTab(self.Manual_Tests, "")
        self.Settings = QtWidgets.QWidget()
        self.Settings.setObjectName("Settings")
        self.tabWidget.addTab(self.Settings, "")
        self.VoIP_Tseter_Controller = QtWidgets.QWidget()
        self.VoIP_Tseter_Controller.setObjectName("VoIP_Tseter_Controller")
        self.tabWidget.addTab(self.VoIP_Tseter_Controller, "")
        self.VoIP_Tester_Label = QtWidgets.QLabel(self.centralwidget)
        self.VoIP_Tester_Label.setGeometry(QtCore.QRect(0, 0, 211, 131))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.VoIP_Tester_Label.setFont(font)
        self.VoIP_Tester_Label.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.VoIP_Tester_Label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.VoIP_Tester_Label.setAutoFillBackground(True)
        self.VoIP_Tester_Label.setScaledContents(True)
        self.VoIP_Tester_Label.setObjectName("VoIP_Tester_Label")
        self.connect_frame = QtWidgets.QFrame(self.centralwidget)
        self.connect_frame.setGeometry(QtCore.QRect(0, 140, 221, 611))
        self.connect_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.connect_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.connect_frame.setObjectName("connect_frame")
        self.connect_frame_Connect_button = QtWidgets.QPushButton(self.connect_frame)
        self.connect_frame_Connect_button.setGeometry(QtCore.QRect(70, 360, 75, 23))
        self.connect_frame_Connect_button.setObjectName("connect_frame_Connect_button")
        self.connect_frame_ip_edit_text = QtWidgets.QTextEdit(self.connect_frame)
        self.connect_frame_ip_edit_text.setGeometry(QtCore.QRect(10, 240, 181, 31))
        self.connect_frame_ip_edit_text.setObjectName("connect_frame_ip_edit_text")
        self.connect_frame_text_label = QtWidgets.QLabel(self.connect_frame)
        self.connect_frame_text_label.setGeometry(QtCore.QRect(10, 110, 201, 81))
        self.connect_frame_text_label.setObjectName("connect_frame_text_label")
        self.connect_frame_ip_label = QtWidgets.QLabel(self.connect_frame)
        self.connect_frame_ip_label.setGeometry(QtCore.QRect(10, 220, 47, 13))
        self.connect_frame_ip_label.setObjectName("connect_frame_ip_label")
        self.connect_frame_port_label = QtWidgets.QLabel(self.connect_frame)
        self.connect_frame_port_label.setGeometry(QtCore.QRect(10, 290, 47, 13))
        self.connect_frame_port_label.setObjectName("connect_frame_port_label")
        self.connect_frame_port_edit_text = QtWidgets.QTextEdit(self.connect_frame)
        self.connect_frame_port_edit_text.setGeometry(QtCore.QRect(10, 310, 181, 31))
        self.connect_frame_port_edit_text.setObjectName("connect_frame_port_edit_text")
        self.log_text_label = QtWidgets.QLabel(self.centralwidget)
        self.log_text_label.setGeometry(QtCore.QRect(220, 640, 861, 111))
        self.log_text_label.setObjectName("log_text_label")
        self.setCentralWidget(self.centralwidget)

        self.retranslateUi()
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(self)

        self.auto_tests_button.clicked.connect(self.autoTestClicked)
        self.manual_tests_button.clicked.connect(self.manualTestClicked)
        self.connect_frame_Connect_button.clicked.connect(self.connectClicked)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.auto_tests_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">Please enter the number of calls you want to pass through the PBX </span></p><p align=\"center\"><span style=\" font-size:16pt;\">(Max. 512)</span></p></body></html>"))
        self.auto_tests_edit_text.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.auto_tests_button.setText(_translate("MainWindow", "Send"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Auto_Tests), _translate("MainWindow", "Auto Tests"))
        self.manual_tests_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">Please enter the number of softphones you want to create </span></p><p align=\"center\"><span style=\" font-size:16pt;\">(Max. 5)</span></p></body></html>"))
        self.manual_tests_button.setText(_translate("MainWindow", "Send"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Manual_Tests), _translate("MainWindow", "Manual Tests"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Settings), _translate("MainWindow", "Settings"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.VoIP_Tseter_Controller), _translate("MainWindow", "VoIP Tseter Controller"))
        self.VoIP_Tester_Label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:28pt;\">VoIP Tester</span></p></body></html>"))
        self.connect_frame_Connect_button.setText(_translate("MainWindow", "Connect"))
        self.connect_frame_text_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"justify\"><span style=\" font-size:10pt; font-weight:600;\">Please enter IP and</span></p><p align=\"justify\"><span style=\" font-size:10pt; font-weight:600;\">the port of the server</span></p><p align=\"justify\"><span style=\" font-size:10pt; font-weight:600;\">inorder to use the tester</span></p></body></html>"))
        self.connect_frame_ip_label.setText(_translate("MainWindow", "IP:"))
        self.connect_frame_port_label.setText(_translate("MainWindow", "Port:"))
        self.log_text_label.setText(_translate("MainWindow", "<html><head/><body><p>Log Text:</p></body></html>"))

    def autoTestClicked(self):
        self.auto_test_signal.emit(self.auto_tests_edit_text.toPlainText())
    
    def manualTestClicked(self):
        self.manual_test_signal.emit(self.manual_tests_edit_text.toPlainText())
    
    def connectClicked(self):
        self.connect_signal.emit(self.connect_frame_ip_edit_text.toPlainText(), self.connect_frame_port_edit_text.toPlainText())
    
    def disconnectClicked(self):
        self.disconnect_signal.emit()


