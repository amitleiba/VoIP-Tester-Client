from GUI import GUI

def main():
    gui = GUI()
    gui.runGui()

if __name__ == '__main__':
    main()

# import re
# from PyQt5.QtGui import QValidator
# from PyQt5.QtWidgets import QApplication, QLineEdit, QWidget, QVBoxLayout

# class NumberOrCharValidator(QValidator):
#     def validate(self, input_str, pos):
#         if re.match("^[a-zA-Z0-9]*$", input_str):
#             return QValidator.Acceptable, input_str, pos
#         elif input_str == "":
#             return QValidator.Intermediate, input_str, pos
#         else:
#             return QValidator.Invalid, input_str, pos

# app = QApplication([])
# window = QWidget()

# layout = QVBoxLayout()
# edit_text = QLineEdit()

# # Set validator to only allow numbers or characters
# validator = NumberOrCharValidator()
# edit_text.setValidator(validator)

# layout.addWidget(edit_text)
# window.setLayout(layout)
# window.show()

# app.exec_()

# app.exec_()
