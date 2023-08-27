# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(640, 437)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(0, 0, 641, 481))
        self.widget.setStyleSheet("background-color: rgb(148, 177, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(90, 120, 199, 246), stop:1 rgba(255, 255, 255, 255));")
        self.widget.setObjectName("widget")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setGeometry(QtCore.QRect(0, 50, 641, 431))
        self.widget_2.setStyleSheet("background-color: rgb(228, 228, 228);")
        self.widget_2.setObjectName("widget_2")
        self.fileList = QtWidgets.QListWidget(self.widget_2)
        self.fileList.setGeometry(QtCore.QRect(90, 0, 551, 391))
        self.fileList.setObjectName("fileList")
        self.deleteButton = QtWidgets.QPushButton(self.widget)
        self.deleteButton.setGeometry(QtCore.QRect(530, 20, 75, 23))
        self.deleteButton.setStyleSheet("background-color: rgb(197, 213, 170);")
        self.deleteButton.setObjectName("deleteButton")
        self.addButton = QtWidgets.QPushButton(self.widget)
        self.addButton.setGeometry(QtCore.QRect(440, 20, 75, 23))
        self.addButton.setStyleSheet("\n"
"background-color: rgb(199, 215, 171);")
        self.addButton.setObjectName("addButton")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(100, 10, 201, 31))
        self.label.setStyleSheet("font: 87 italic 14pt \"Segoe UI Black\";")
        self.label.setObjectName("label")
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setGeometry(QtCore.QRect(0, 0, 91, 441))
        self.widget_3.setStyleSheet("background-color: rgb(88, 81, 139);\n"
"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0.04, stop:0 rgba(88, 81, 139, 234), stop:1 rgba(99, 128, 202, 255));")
        self.widget_3.setObjectName("widget_3")
        self.openButton = QtWidgets.QPushButton(self.widget_3)
        self.openButton.setGeometry(QtCore.QRect(10, 60, 75, 23))
        self.openButton.setStyleSheet("\n"
"background-color: rgb(199, 215, 171);")
        self.openButton.setObjectName("openButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.deleteButton.setText(_translate("Dialog", "Delete"))
        self.addButton.setText(_translate("Dialog", "Add"))
        self.label.setText(_translate("Dialog", "E - B O O K S"))
        self.openButton.setText(_translate("Dialog", "Open"))
