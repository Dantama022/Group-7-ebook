import sys
import os
import subprocess
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QPushButton, QListWidgetItem
from ui_mainbody import Ui_MainWindow
from ui_QDialog import Ui_Dialog
from ui_QDialogEd import Ui_Dialog
from ui_QDialogEnv import Ui_Dialog


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.button1.clicked.connect(self.show_dialog1)
        self.button2.clicked.connect(self.show_dialog2)
        self.button3.clicked.connect(self.show_dialog3)

    def show_dialog1(self):
        dialog = QDialog()
        ui_dialog = Ui_Dialog()
        ui_dialog.setupUi(dialog)
        ui_dialog.addButton.clicked.connect(lambda: self.upload_file(ui_dialog.fileList))
        ui_dialog.openButton.clicked.connect(lambda: self.open_selected_file(ui_dialog.fileList))
        ui_dialog.deleteButton.clicked.connect(lambda: self.delete_selected_files(ui_dialog.fileList))
        dialog.exec_()

    def show_dialog2(self):
        dialog = QDialog()
        ui_dialog = Ui_Dialog()
        ui_dialog.setupUi(dialog)
        ui_dialog.addButton.clicked.connect(lambda: self.upload_file(ui_dialog.fileList))
        ui_dialog.openButton.clicked.connect(lambda: self.open_selected_file(ui_dialog.fileList))
        ui_dialog.deleteButton.clicked.connect(lambda: self.delete_selected_files(ui_dialog.fileList))
        dialog.exec_()

    def show_dialog3(self):
        dialog = QDialog()
        ui_dialog = Ui_Dialog()
        ui_dialog.setupUi(dialog)
        ui_dialog.addButton.clicked.connect(lambda: self.upload_file(ui_dialog.fileList))
        ui_dialog.openButton.clicked.connect(lambda: self.open_selected_file(ui_dialog.fileList))
        ui_dialog.deleteButton.clicked.connect(lambda: self.delete_selected_files(ui_dialog.fileList))
        dialog.exec_()

    def upload_file(self, file_list_widget):
        file_path = QtWidgets.QFileDialog.getOpenFileName(self, "Select a file")[0]
        if file_path:
            file_item = QListWidgetItem(file_path)
            file_list_widget.addItem(file_item)

    def open_selected_file(self, file_list_widget):
        selected_items = file_list_widget.selectedItems()
        for item in selected_items:
            self.open_file_with_default_app(item.text())

    def open_file_with_default_app(self, file_path):
        subprocess.Popen([file_path], shell=True)
        print(f"start " + f"{file_path}")
    def delete_selected_files(self, file_list_widget):
        selected_items = file_list_widget.selectedItems()
        for item in selected_items:
            file_list_widget.takeItem(file_list_widget.row(item))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainbody = MainWindow()
    mainbody.show()
    sys.exit(app.exec_())