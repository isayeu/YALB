# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'yalb.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QGroupBox, QGridLayout, QButtonGroup, QRadioButton, QDateEdit, QPushButton, QFormLayout
from PyQt5.QtCore import Qt, QSize


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

		self.groupBoxButtons = QGroupBox(self.tab)
		self.groupBoxButtons.setObjectName(u"groupBoxButtons")
		self.groupBoxButtons.setMaximumSize(QSize(100, 16777215))
		self.formLayout = QFormLayout(self.groupBoxButtons)
		self.gridLayout.addWidget(self.groupBoxButtons, 0, 1, 6, 1)

		self.ButtonAddLeg = QtWidgets.QPushButton(self.groupBoxButtons)
		self.ButtonAddLeg.setObjectName("ButtonAddLeg")
		self.formLayout.setWidget(2, QFormLayout.LabelRole, self.ButtonAddLeg)


		self.pushButtonDelLeg = QtWidgets.QPushButton(self.groupBoxButtons)
		self.pushButtonDelLeg.setObjectName(u"pushButtonDelLeg")
		self.pushButtonDelLeg.setText(u"Del Leg")
		self.formLayout.setWidget(3, QFormLayout.LabelRole, self.pushButtonDelLeg)

		self.calendarWidget = QtWidgets.QCalendarWidget(self.tab)
		self.calendarWidget.setObjectName("calendarWidget")
		self.gridLayout.addWidget(self.calendarWidget, 0, 0, 6, 1, QtCore.Qt.AlignLeft)
		self.calendarWidget.setGridVisible(True)

		self.ButtonAddAC = QtWidgets.QPushButton(self.groupBoxButtons)
		self.ButtonAddAC.setObjectName("ButtonAddAC")
		self.formLayout.setWidget(0, QFormLayout.LabelRole, self.ButtonAddAC)

		self.pushButtonDelAC = QtWidgets.QPushButton(self.groupBoxButtons)
		self.pushButtonDelAC.setObjectName("pushButtonDelAC")
		self.pushButtonDelAC.setText(u"Del A/C")
		self.formLayout.setWidget(1, QFormLayout.LabelRole, self.pushButtonDelAC)

		self.tableViewAcft = QtWidgets.QTableView(self.tab)
		self.tableViewAcft.setObjectName(u"tableViewAcft")
		self.gridLayout.addWidget(self.tableViewAcft, 0, 2, 6, 1, QtCore.Qt.AlignLeft)
		self.tableViewAcft.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
		self.tableViewAcft.horizontalHeader().setStretchLastSection(False)
		self.tableViewAcft.setMaximumSize(QSize(210, 16777215))

		self.model = QtGui.QStandardItemModel(self.tab)

		self.tableLog = QtWidgets.QTableView(self.tab)
		self.tableLog.setModel(self.model)
		self.tableLog.setObjectName("tableLog")
		self.gridLayout.addWidget(self.tableLog, 6, 0, 1, 6)
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
		self.gridLayout.addWidget(self.lcdNumber, 2, 5, 2, 1, QtCore.Qt.AlignLeft)

		self.lcdNumberBLK = QtWidgets.QLCDNumber(self.tab)
		self.lcdNumberBLK.setObjectName(u"lcdNumberBLK")
		self.lcdNumberBLK.setMinimumSize(QtCore.QSize(300, 0))
		self.lcdNumberBLK.setDigitCount(8)
		self.gridLayout.addWidget(self.lcdNumberBLK, 0, 5, 2, 1, QtCore.Qt.AlignLeft)

		self.lcdNumberNight = QtWidgets.QLCDNumber(self.tab)
		self.lcdNumberNight.setObjectName(u"lcdNumberNight")
		self.lcdNumberNight.setMinimumSize(QtCore.QSize(300, 0))
		self.lcdNumberNight.setDigitCount(8)
		self.gridLayout.addWidget(self.lcdNumberNight, 4, 5, 2, 1, QtCore.Qt.AlignLeft)

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
		self.gridLayout.addWidget(self.label_3, 4, 4, 2, 1, QtCore.Qt.AlignLeft)

		self.label_2 = QtWidgets.QLabel(self.tab)
		self.label_2.setObjectName(u"label_2")
		self.label_2.setFont(font)
		self.label_2.setText(u"<html><head/><body><p>Flight Time	</p></body></html>")
		self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
		self.gridLayout.addWidget(self.label_2, 2, 4, 2, 1, QtCore.Qt.AlignLeft)

		self.label = QtWidgets.QLabel(self.tab)
		self.label.setObjectName(u"label")
		self.label.setFont(font)
		self.label.setText(u"<html><head/><body><p>Block Time	</p></body></html>")
		self.label.setTextFormat(QtCore.Qt.AutoText)
		self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
		self.gridLayout.addWidget(self.label, 0, 4, 2, 1, QtCore.Qt.AlignLeft)

		self.groupBoxFilters = QGroupBox(self.tab)
		self.groupBoxFilters.setObjectName(u"groupBoxFilters")

		self.groupBoxFilters.setToolTip(u"")
		self.groupBoxFilters.setStatusTip(u"")
		self.groupBoxFilters.setWhatsThis(u"")
		self.groupBoxFilters.setAccessibleName(u"")
		self.groupBoxFilters.setAccessibleDescription(u"")
		self.groupBoxFilters.setTitle(u"Filters")
		self.gridLayout_2 = QGridLayout(self.groupBoxFilters)
		self.gridLayout_2.setObjectName(u"gridLayout_2")
		self.gridLayout.addWidget(self.groupBoxFilters, 0, 3, 6, 1, QtCore.Qt.AlignLeft)

		self.radioButton12Month = QRadioButton(self.groupBoxFilters)
		self.buttonGroupFilter = QButtonGroup(MainWindow)
		self.buttonGroupFilter.setObjectName(u"buttonGroupFilter")
		self.buttonGroupFilter.addButton(self.radioButton12Month)
		self.radioButton12Month.setObjectName(u"radioButton12Month")
		self.radioButton12Month.setToolTip(u"")
		self.radioButton12Month.setStatusTip(u"")
		self.radioButton12Month.setWhatsThis(u"")
		self.radioButton12Month.setAccessibleName(u"")
		self.radioButton12Month.setAccessibleDescription(u"")
		self.radioButton12Month.setText(u"Last 12 Month")

		self.gridLayout_2.addWidget(self.radioButton12Month, 2, 1, 1, 1)

		self.radioButtonDateToDate = QRadioButton(self.groupBoxFilters)
		self.buttonGroupFilter.addButton(self.radioButtonDateToDate)
		self.radioButtonDateToDate.setObjectName(u"radioButtonDateToDate")
		self.radioButtonDateToDate.setToolTip(u"")
		self.radioButtonDateToDate.setStatusTip(u"")
		self.radioButtonDateToDate.setWhatsThis(u"")
		self.radioButtonDateToDate.setAccessibleName(u"")
		self.radioButtonDateToDate.setAccessibleDescription(u"")
		self.radioButtonDateToDate.setText(u"From Date To Date")

		self.gridLayout_2.addWidget(self.radioButtonDateToDate, 4, 1, 1, 1)

		self.radioButtonPrDay = QRadioButton(self.groupBoxFilters)
		self.buttonGroupFilter.addButton(self.radioButtonPrDay)
		self.radioButtonPrDay.setObjectName(u"radioButtonPrDay")
		self.radioButtonPrDay.setToolTip(u"")
		self.radioButtonPrDay.setStatusTip(u"")
		self.radioButtonPrDay.setWhatsThis(u"")
		self.radioButtonPrDay.setAccessibleName(u"")
		self.radioButtonPrDay.setAccessibleDescription(u"")
		self.radioButtonPrDay.setText(u"Previous Day")

		self.gridLayout_2.addWidget(self.radioButtonPrDay, 0, 0, 1, 1)

		self.radioButton30days = QRadioButton(self.groupBoxFilters)
		self.buttonGroupFilter.addButton(self.radioButton30days)
		self.radioButton30days.setObjectName(u"radioButton30days")
		self.radioButton30days.setToolTip(u"")
		self.radioButton30days.setStatusTip(u"")
		self.radioButton30days.setWhatsThis(u"")
		self.radioButton30days.setAccessibleName(u"")
		self.radioButton30days.setAccessibleDescription(u"")
		self.radioButton30days.setText(u"Last 30 Days")

		self.gridLayout_2.addWidget(self.radioButton30days, 0, 1, 1, 1)

		self.radioButtonPrYear = QRadioButton(self.groupBoxFilters)
		self.buttonGroupFilter.addButton(self.radioButtonPrYear)
		self.radioButtonPrYear.setObjectName(u"radioButtonPrYear")
		self.radioButtonPrYear.setToolTip(u"")
		self.radioButtonPrYear.setStatusTip(u"")
		self.radioButtonPrYear.setWhatsThis(u"")
		self.radioButtonPrYear.setAccessibleName(u"")
		self.radioButtonPrYear.setAccessibleDescription(u"")
		self.radioButtonPrYear.setText(u"Previous Year")

		self.gridLayout_2.addWidget(self.radioButtonPrYear, 4, 0, 1, 1)

		self.radioButtonPrMonth = QRadioButton(self.groupBoxFilters)
		self.buttonGroupFilter.addButton(self.radioButtonPrMonth)
		self.radioButtonPrMonth.setObjectName(u"radioButtonPrMonth")
		self.radioButtonPrMonth.setToolTip(u"")
		self.radioButtonPrMonth.setStatusTip(u"")
		self.radioButtonPrMonth.setWhatsThis(u"")
		self.radioButtonPrMonth.setAccessibleName(u"")
		self.radioButtonPrMonth.setAccessibleDescription(u"")
		self.radioButtonPrMonth.setText(u"Previous Month")

		self.gridLayout_2.addWidget(self.radioButtonPrMonth, 2, 0, 1, 1)

		self.dateEditFilterFrom = QDateEdit(self.groupBoxFilters)
		self.dateEditFilterFrom.setObjectName(u"dateEditFilterFrom")
		self.dateEditFilterFrom.setToolTip(u"")
		self.dateEditFilterFrom.setStatusTip(u"")
		self.dateEditFilterFrom.setWhatsThis(u"")
		self.dateEditFilterFrom.setAccessibleName(u"")
		self.dateEditFilterFrom.setAccessibleDescription(u"")
		self.dateEditFilterFrom.setSpecialValueText(u"")
		self.dateEditFilterFrom.setDisplayFormat(u"dd.MM.yyyy")
		self.dateEditFilterFrom.setCalendarPopup(True)
		self.dateEditFilterFrom.setTimeSpec(Qt.UTC)

		self.gridLayout_2.addWidget(self.dateEditFilterFrom, 5, 0, 1, 1)

		self.dateEditFilterTo = QDateEdit(self.groupBoxFilters)
		self.dateEditFilterTo.setObjectName(u"dateEditFilterTo")
		self.dateEditFilterTo.setToolTip(u"")
		self.dateEditFilterTo.setStatusTip(u"")
		self.dateEditFilterTo.setWhatsThis(u"")
		self.dateEditFilterTo.setAccessibleName(u"")
		self.dateEditFilterTo.setAccessibleDescription(u"")
		self.dateEditFilterTo.setSpecialValueText(u"")
		self.dateEditFilterTo.setDisplayFormat(u"dd.MM.yyyy")
		self.dateEditFilterTo.setCalendarPopup(True)
		self.dateEditFilterTo.setTimeSpec(Qt.UTC)

		self.gridLayout_2.addWidget(self.dateEditFilterTo, 5, 1, 1, 1)

		self.pushButtonAppFilter = QPushButton(self.groupBoxFilters)
		self.pushButtonAppFilter.setObjectName(u"pushButtonAppFilter")
		self.pushButtonAppFilter.setToolTip(u"")
		self.pushButtonAppFilter.setStatusTip(u"")
		self.pushButtonAppFilter.setWhatsThis(u"")
		self.pushButtonAppFilter.setAccessibleName(u"")
		self.pushButtonAppFilter.setAccessibleDescription(u"")
		self.pushButtonAppFilter.setText(u"Apply Filter")

		self.gridLayout_2.addWidget(self.pushButtonAppFilter, 7, 0, 1, 1)

		self.pushButtonResetFilter = QPushButton(self.groupBoxFilters)
		self.pushButtonResetFilter.setObjectName(u"pushButtonResetFilter")
		self.pushButtonResetFilter.setToolTip(u"")
		self.pushButtonResetFilter.setStatusTip(u"")
		self.pushButtonResetFilter.setWhatsThis(u"")
		self.pushButtonResetFilter.setAccessibleName(u"")
		self.pushButtonResetFilter.setAccessibleDescription(u"")
		self.pushButtonResetFilter.setText(u"Reset Filter")

		self.gridLayout_2.addWidget(self.pushButtonResetFilter, 7, 1, 1, 1)

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
