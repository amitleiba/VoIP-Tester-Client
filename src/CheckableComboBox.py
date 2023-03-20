# importing libraries 
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 

# new check-able combo box 
class CheckableComboBox(QComboBox): 
    # constructor 
    def __init__(self, filterAutoTestLabel, parent = None): 
        super(CheckableComboBox, self).__init__(parent)
        self.selected_items = []
        self.view().pressed.connect(self.handleItemPressed) 
        self.setModel(QStandardItemModel(self)) 
        self.filterAutoTestLabel = filterAutoTestLabel

    # action called when item get checked 
    def do_action(self): 
        # window.browser.setText("Selected items : " + ", ".join(self.selected_items))
        pass

    # when any item get pressed 
    def handleItemPressed(self, index):
        self.items = [self.model().item(i) for i in range(self.count())]
        for item_in_list in self.items:
            if item_in_list.text() == 'ALL':
                all_item = item_in_list
                break

        # getting the item 
        item = self.model().itemFromIndex(index) 

        # checking if item is checked 
        if item.checkState() == Qt.Checked: 
            if item.text() == 'ALL':
                for item_in_list in self.items:
                    if item_in_list.checkState() == Qt.Checked:
                        item_in_list.setCheckState(Qt.Unchecked)
                        if item_in_list.text() != 'ALL':
                            self.selected_items.remove(item_in_list.text())
                            # self.do_action()

            else:
                # making it unchecked
                item.setCheckState(Qt.Unchecked)
                all_item.setCheckState(Qt.Unchecked)
                self.selected_items.remove(item.text())
                # self.do_action()
            self.filterAutoTestLabel('remove')

        # if not checked 
        else: 
            if item.text() == 'ALL':
                for item_in_list in self.items:
                    if item_in_list.checkState() != Qt.Checked:
                        item_in_list.setCheckState(Qt.Checked)
                        if item_in_list.text() != 'ALL':
                            self.selected_items.append(item_in_list.text())
                            # self.do_action()

            else:
                # making the item checked 
                item.setCheckState(Qt.Checked)
                all_item.setCheckState(Qt.Checked)
                for item_in_list in self.items:
                    if item_in_list.text() != 'ALL' and item_in_list.checkState() != Qt.Checked:
                        all_item.setCheckState(Qt.Unchecked)
                        break
                self.selected_items.append(item.text())

            # call the action 
            self.filterAutoTestLabel(item.text())