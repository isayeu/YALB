# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5.QtCore import (QMetaObject)
from PyQt5.QtWidgets import *

class Ui_Dialog2(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(194, 84)
        Dialog.setWindowTitle(u"New aircraft")
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lineEdit = QLineEdit(Dialog)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setPlaceholderText(u"Type")

        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)

        self.lineEdit_2 = QLineEdit(Dialog)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setPlaceholderText(u"ID")

        self.gridLayout.addWidget(self.lineEdit_2, 0, 1, 1, 1)

        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStatusTip(u"")
        self.pushButton.setText(u"Add")
        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 1)
        self.pushButton_2 = QPushButton(Dialog)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setText(u"Cancel")

        self.gridLayout.addWidget(self.pushButton_2, 1, 1, 1, 1)

        QMetaObject.connectSlotsByName(Dialog)
