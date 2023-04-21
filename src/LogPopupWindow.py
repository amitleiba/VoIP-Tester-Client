from PyQt5.QtWidgets import QDialog, QTextBrowser, QVBoxLayout, QLabel

class LogPopupWindow(QDialog):
    def __init__(self, data):
        super().__init__()
        self.setWindowTitle('Log Window')
        self.setGeometry(100, 100, 500, 850)

        layout = QVBoxLayout()

        self.text_browser = QTextBrowser(self)
        self.text_browser.setGeometry(2, 0, 496, 648)
        self.text_browser.setPlainText(data)

        layout.addWidget(self.text_browser)
        self.setLayout(layout)