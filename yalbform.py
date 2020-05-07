# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'yalb.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
#from QtCore import Qsize

class Ui_MainWindow(object):
	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(1920, 1080)
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
		self.gridLayout_3.setObjectName("gridLayout_3")

		self.Tab1 = QtWidgets.QTabWidget(self.centralwidget)
		self.Tab1.setLocale(QtCore.QLocale(QtCore.QLocale.Russian, QtCore.QLocale.Russia))
		self.Tab1.setObjectName("Tab1")
		self.tab = QtWidgets.QWidget()
		self.tab.setObjectName("tab")
		self.gridLayout = QtWidgets.QGridLayout(self.tab)
		self.gridLayout.setObjectName("gridLayout")

		self.ButtonAddLeg = QtWidgets.QPushButton(self.tab)
		self.ButtonAddLeg.setObjectName("ButtonAddLeg")
		self.gridLayout.addWidget(self.ButtonAddLeg, 2, 1, 1, 1, QtCore.Qt.AlignLeft)

		self.pushButtonDelLeg = QtWidgets.QPushButton(self.tab)
		self.pushButtonDelLeg.setObjectName(u"pushButtonDelLeg")
		self.pushButtonDelLeg.setText(u"Del Leg")
		self.gridLayout.addWidget(self.pushButtonDelLeg, 3, 1, 1, 1, QtCore.Qt.AlignLeft)

		self.calendarWidget = QtWidgets.QCalendarWidget(self.tab)
		self.calendarWidget.setObjectName("calendarWidget")
		self.gridLayout.addWidget(self.calendarWidget, 0, 0, 6, 1, QtCore.Qt.AlignLeft)
		self.calendarWidget.setGridVisible(True)

		self.ButtonAddAC = QtWidgets.QPushButton(self.tab)
		self.ButtonAddAC.setObjectName("ButtonAddAC")
		self.gridLayout.addWidget(self.ButtonAddAC, 0, 1, 1, 1, QtCore.Qt.AlignLeft)

		self.pushButtonDelAC = QtWidgets.QPushButton(self.tab)
		self.pushButtonDelAC.setObjectName("pushButtonDelAC")
		self.pushButtonDelAC.setText(u"Del A/C")
		self.gridLayout.addWidget(self.pushButtonDelAC, 1, 1, 1, 1, QtCore.Qt.AlignLeft)

		self.buttonRecalc = QtWidgets.QPushButton(self.tab)
		self.buttonRecalc.setObjectName(u"buttonRecalc")
		self.buttonRecalc.setToolTip(u"")
		self.buttonRecalc.setStatusTip(u"")
		self.buttonRecalc.setWhatsThis(u"")
		self.buttonRecalc.setAccessibleName(u"")
		self.buttonRecalc.setAccessibleDescription(u"")
		self.buttonRecalc.setText(u"Recalc Time")
		self.gridLayout.addWidget(self.buttonRecalc, 4, 1, 1, 1, QtCore.Qt.AlignLeft)

		self.tableViewAcft = QtWidgets.QTableView(self.tab)
		self.tableViewAcft.setObjectName(u"tableViewAcft")
		self.gridLayout.addWidget(self.tableViewAcft, 0, 2, 6, 1, QtCore.Qt.AlignLeft)
		self.tableViewAcft.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
		self.tableViewAcft.horizontalHeader().setStretchLastSection(False)


		#self.horizontalSpacer = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
		#self.gridLayout.addItem(self.horizontalSpacer, 0, 3, 1, 1)

		self.model = QtGui.QStandardItemModel(self.tab)

		self.tableLog = QtWidgets.QTableView(self.tab)
		self.tableLog.setModel(self.model)
		self.tableLog.setObjectName("tableLog")
		self.gridLayout.addWidget(self.tableLog, 6, 0, 1, 5)
		self.tableLog.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
		self.tableLog.horizontalHeader().setStretchLastSection(False)
		self.tableLog.setSortingEnabled(True)
		self.tableLog.setAlternatingRowColors(True)

		self.Tab1.addTab(self.tab, "")
		self.tab_2 = QtWidgets.QWidget()
		self.tab_2.setObjectName("tab_2")
		self.Tab1.addTab(self.tab_2, "")
		self.gridLayout_3.addWidget(self.Tab1, 0, 0, 1, 1)
		MainWindow.setCentralWidget(self.centralwidget)
		self.menubar = QtWidgets.QMenuBar(MainWindow)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 1920, 30))
		self.menubar.setObjectName("menubar")
		MainWindow.setMenuBar(self.menubar)
		self.statusbar = QtWidgets.QStatusBar(MainWindow)
		self.statusbar.setObjectName("statusbar")
		MainWindow.setStatusBar(self.statusbar)

		self.lcdNumber = QtWidgets.QLCDNumber(self.tab)
		self.lcdNumber.setObjectName(u"lcdNumber")
		self.lcdNumber.setMinimumSize(QtCore.QSize(300, 0))
		self.lcdNumber.setDigitCount(8)
		self.gridLayout.addWidget(self.lcdNumber, 2, 4, 2, 1, QtCore.Qt.AlignLeft)

		self.lcdNumberBLK = QtWidgets.QLCDNumber(self.tab)
		self.lcdNumberBLK.setObjectName(u"lcdNumberBLK")
		self.lcdNumberBLK.setMinimumSize(QtCore.QSize(300, 0))
		self.lcdNumberBLK.setDigitCount(8)
		self.gridLayout.addWidget(self.lcdNumberBLK, 0, 4, 2, 1, QtCore.Qt.AlignLeft)

		self.lcdNumberNight = QtWidgets.QLCDNumber(self.tab)
		self.lcdNumberNight.setObjectName(u"lcdNumberNight")
		self.lcdNumberNight.setMinimumSize(QtCore.QSize(300, 0))
		self.lcdNumberNight.setDigitCount(8)
		self.gridLayout.addWidget(self.lcdNumberNight, 4, 4, 2, 1, QtCore.Qt.AlignLeft)

		self.label_3 = QtWidgets.QLabel(self.tab)
		self.label_3.setObjectName(u"label_3")
		self.label_3.setEnabled(True)
		font = QtGui.QFont()
		font.setPointSize(30)
		font.setBold(True)
		font.setWeight(75)
		self.label_3.setFont(font)
		self.label_3.setText(u"<html><head/><body><p>Night Time	</p></body></html>")
		self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
		self.gridLayout.addWidget(self.label_3, 4, 3, 1, 1, QtCore.Qt.AlignLeft)

		self.label_2 = QtWidgets.QLabel(self.tab)
		self.label_2.setObjectName(u"label_2")
		self.label_2.setFont(font)
		self.label_2.setText(u"<html><head/><body><p>Flight Time	</p></body></html>")
		self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
		self.gridLayout.addWidget(self.label_2, 2, 3, 2, 1, QtCore.Qt.AlignLeft)

		self.label = QtWidgets.QLabel(self.tab)
		self.label.setObjectName(u"label")
		self.label.setFont(font)
		self.label.setText(u"<html><head/><body><p>Block Time	</p></body></html>")
		self.label.setTextFormat(QtCore.Qt.AutoText)
		self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
		self.gridLayout.addWidget(self.label, 0, 3, 2, 1, QtCore.Qt.AlignLeft)


		self.retranslateUi(MainWindow)
		self.Tab1.setCurrentIndex(0)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("Yet Another Log Book", "Yet Another Log Book"))
		self.ButtonAddLeg.setText(_translate("MainWindow", "Add Leg"))
		self.ButtonAddAC.setText(_translate("MainWindow", "Add A/C"))
		self.Tab1.setTabText(self.Tab1.indexOf(self.tab), _translate("MainWindow", "Log Book"))
		self.Tab1.setTabText(self.Tab1.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
