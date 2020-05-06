#!/usr/bin/env python
import sys
from datetime import datetime
from datetime import timedelta

from PyQt5 import QtCore, QtWidgets, QtSql
from shapely.geometry import LineString

#from Sun import Sun
from addacft import Ui_Dialog2
from addleg import Ui_Dialog
from yalbform import Ui_MainWindow
import ephem
import math


class AddAcftWindow(QtWidgets.QDialog):
	def __init__(self):
		super(AddAcftWindow, self).__init__()
		self.acft = Ui_Dialog2()
		self.acft.setupUi(self)
		self.acft.pushButton.clicked.connect(self.newacft)
		self.db = None

	def setDatabase(self, db):
		self.db = db

	def newacft (self):
		typ = self.acft.lineEdit.text()
		acftid = self.acft.lineEdit_2.text()
		query = QtSql.QSqlQuery()
		query.prepare("INSERT INTO acfts ('ACFT Type', 'ACFT ID') VALUES (?,?)")
		query.bindValue(0, typ)
		query.bindValue(1, acftid)
		if query.exec_():
			self.db.commit()
		else:
			QtWidgets.QMessageBox.warning(None, "Database Error", query.lastError().text())


class AddlegWindow(QtWidgets.QDialog):
	def __init__(self):
		super(AddlegWindow, self).__init__()
		self.addi = Ui_Dialog()
		self.addi.setupUi(self)
		self.addi.dateEdit.setDate(QtCore.QDate.currentDate())
		self.addi.pushButton_2.clicked.connect(self.hide)
		self.addi.pushButton_3.clicked.connect(self.hide)

class MainWindow(QtWidgets.QMainWindow):
	def __init__(self):
		super(MainWindow, self).__init__()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.AddAcftWindow = AddAcftWindow()
		self.ui.ButtonAddAC.clicked.connect(self.addacftdialog)
		self.AddAcftWindow.acft.pushButton.clicked.connect(self.run)
		self.addlegwindow = AddlegWindow()
		self.addlegwindow.addi.pushButton.clicked.connect(self.newleg)
		self.ui.ButtonAddLeg.clicked.connect(self.addLeg)
		self.ui.tableLog.clicked.connect(self.onRowSelect)
		self.ui.tableViewAcft.clicked.connect(self.acftselect)
		self.ui.pushButtonDelLeg.clicked.connect(self.delrow)
		self.ui.pushButtonDelAC.clicked.connect(self.delac)
		self.ui.buttonRecalc.clicked.connect(self.recalc)
		self.db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
		self.db.setDatabaseName("log.db")
		self.db.open()
		self.query = QtSql.QSqlQuery(self.db)
		self.selectedAC = None
		self.selectedID = None
		self.AddAcftWindow.setDatabase(self.db)
		self.run()

	def run(self):
		t = datetime.utcnow()
		print('Обновили Таблицы ', t)

		# Fill Log Table
		self.ui.model.clear()
		model = QtSql.QSqlQueryModel()
		model.setQuery("SELECT * FROM log")
		proxy = QtCore.QSortFilterProxyModel()
		proxy.setSourceModel(model)
		self.ui.tableLog.setModel(proxy)
		self.ui.tableLog.resizeColumnsToContents()

		# Fill Flight Time LCD
		query = QtSql.QSqlQuery("select * from log")
		record = query.record()
		nameCol = record.indexOf("FlightTime")  # index of the field "name"
		totalraw = timedelta(00, 00)
		while query.next():
			tt = datetime.strptime(query.value(nameCol), "%H:%M")
			delta = timedelta(hours=tt.hour, minutes=tt.minute)
			totalraw += delta
			total = '%02d:%02d' % (totalraw.days * 24 + totalraw.seconds // 3600, (totalraw.seconds % 3600) // 60)
			self.ui.lcdNumber.display(str(total))

		# Fill Block Time LCD
		query = QtSql.QSqlQuery("select * from log")
		record = query.record()
		nameCol = record.indexOf("BlockTime")  # index of the field "name"
		totalraw = timedelta(00, 00)
		while query.next():
			tt = datetime.strptime(query.value(nameCol), "%H:%M")
			delta = timedelta(hours=tt.hour, minutes=tt.minute)
			totalraw += delta
			total = '%02d:%02d' % (totalraw.days * 24 + totalraw.seconds // 3600, (totalraw.seconds % 3600) // 60)
			self.ui.lcdNumberBLK.display(str(total))

		# Fill Aircraft Table
		model = QtSql.QSqlQueryModel()
		model.setQuery("SELECT * FROM acfts")
		self.ui.tableViewAcft.setModel(model)
		self.ui.tableViewAcft.resizeColumnsToContents()

		# Fill Aircraft Combobox
		model = QtSql.QSqlTableModel(self)
		model.setTable("acfts")
		model.select()
		self.addlegwindow.addi.comboBox.setModel(model)
		self.addlegwindow.addi.comboBox.setModelColumn(model.fieldIndex("ACFT ID"))
	# End Fill

	def addLeg(self):
		self.addlegwindow.show()

	def addacftdialog(self):
		self.AddAcftWindow.show()

	def acftselect(self, index):
		self.selectedAC = index.sibling(index.row(), 0).data()

	def delac(self):
		id = self.selectedAC
		self.query.prepare("DELETE FROM acfts WHERE id=:id")
		self.query.bindValue(":id", id)
		if self.query.exec_():
			self.db.commit()
		else:
			QtWidgets.QMessageBox.warning(None, "Database Error", self.query.lastError().text())
		self.run()

	def onRowSelect(self, index):
		self.selectedID = index.sibling(index.row(), 0).data()

	def rowselect(self, id, *args):
		self.query.exec("SELECT %s FROM log WHERE ID = %d" % (",".join(args), int(id)))
		r = QtSql.QSqlRecord()
		while self.query.next():
			r = self.query.record()
		return [r.value(i) for i in range(r.count())]

	def delrow(self):
		id = self.selectedID
		self.query.prepare("DELETE FROM log WHERE ID = :id")
		self.query.bindValue(":id", id)
		if self.query.exec_():
			self.db.commit()
		else:
			QtWidgets.QMessageBox.warning(None, "Database Error", self.query.lastError().text())
		self.run()

	def get_ap_coords(self, ap_icao):
		coords = (None, None)
		self.query.prepare("SELECT Latitude, Longitude FROM airports WHERE ICAO = '%s'" % ap_icao.upper())
		if not self.query.exec_():
			QtWidgets.QMessageBox.warning(None, "Database Error", self.query.lastError().text())
			return coords
		while self.query.next():
			coords = (float(self.query.value(0)), float(self.query.value(1)))
			print('get_ap_coords():', ap_icao, *coords)
		return coords

	def recalc(self):
		if not self.selectedID:
			return
		fromap, toap = self.rowselect(self.selectedID, "AirportDeparture", "AirportArrival")
		date, depFtime, arriveTime = self.rowselect(self.selectedID, "Date", "TakeOff", "Landing")

		to = datetime.fromisoformat(date + " " + depFtime)
		ldgt = datetime.fromisoformat(date + " " + arriveTime)

		if ldgt < to:
			ldgt += timedelta(days=1)


		coords_departure = self.get_ap_coords(fromap)
		coords_arrival = self.get_ap_coords(toap)

		departure_ap = ephem.Observer()
		departure_ap.lat = math.radians(coords_departure[0])
		departure_ap.lon = math.radians(coords_departure[1])
		arrival_ap = ephem.Observer()
		arrival_ap.lat = math.radians(coords_arrival[0])
		arrival_ap.lon = math.radians(coords_arrival[1])

		departure_ap.date = to
		arrival_ap.date = to + timedelta(days=(departure_ap.lon - arrival_ap.lon)/math.pi/12.0)
		a = float(departure_ap.date)

		print(a, ldgt)


		#prev_sr_dep = departure_ap.previous_rising(ephem.Sun()).datetime()
		#prev_ss_dep = departure_ap.previous_setting(ephem.Sun()).datetime()
		next_sr_dep = departure_ap.next_rising(ephem.Sun()).datetime()
		next_ss_dep = departure_ap.next_setting(ephem.Sun()).datetime()
		#prev_sr_arr = arrival_ap.previous_rising(ephem.Sun()).datetime()
		#prev_ss_arr = arrival_ap.previous_setting(ephem.Sun()).datetime()
		next_sr_arr = arrival_ap.next_rising(ephem.Sun()).datetime()
		next_ss_arr = arrival_ap.next_setting(ephem.Sun()).datetime()
		# ugly hack
		#if next_ss_arr < next_sr_arr:
		#	arrival_ap.date = next_ss_arr + timedelta(seconds=1)
		#	next_ss_arr = arrival_ap.next_setting(ephem.Sun()).datetime()


		startinday = False
		strt = 'At Nigt'
		if next_sr_dep > next_ss_dep:
			startinday = True
			strt = 'At Day'

		print('Take OFF', strt)
		#print('Departure', '\n', prev_sr_dep, '\n', prev_ss_dep, '\n', next_sr_dep, '\n', next_ss_dep, '\n')
		#print('Arrival', '\n', prev_sr_arr, '\n', prev_ss_arr, '\n', next_sr_arr, '\n', next_ss_arr, '\n')
		print('Departure SR:', next_sr_dep, '\tSS:', next_ss_dep)
		print('Arrival   SR:', next_sr_arr, '\tSS:', next_ss_arr)
		print()

		# TODO: move to func
		with open("debug.csv", "wb") as f:
			line = f"1,{to},{next_sr_dep},{next_ss_dep},{next_sr_dep},{next_ss_dep}\n"
			f.write(line.encode("utf-8"))
			line = f"0,{ldgt},{next_sr_arr},{next_ss_arr},{next_sr_arr},{next_ss_arr}\n"
			f.write(line.encode("utf-8"))

		s = ephem.Sun()
		plane = ephem.Observer()
		plane.date = to
		flight_time_minutes = int((ldgt - to).total_seconds() // 60)
		print("ldgt-to in minutes:", flight_time_minutes, "HH:MM :", timedelta(hours=flight_time_minutes/60.0))
		dlat = (arrival_ap.lat - departure_ap.lat) / flight_time_minutes
		dlon = (arrival_ap.lon - departure_ap.lon) / flight_time_minutes
		dt = timedelta(seconds=60)
		nt = 0
		for i in range(flight_time_minutes):
			plane.date = to + dt * float(i)
			plane.lat = departure_ap.lat + dlat * float(i)
			plane.lon = departure_ap.lon + dlon * float(i)
			if plane.next_rising(s) < plane.next_setting(s):
				nt += 1
		nt /= 60.0
		print("NightTime_hard:", nt, timedelta(hours=nt))

		# coordsDep = {'longitude' : lonDep, 'latitude' : latDep}
		# coordsArr = {'longitude' : lonArr, 'latitude' : latArr}
		# timeSRDep = self.sun.getSunriseTime(coordsDep)['dec_rel']
		# timeSSDep = self.sun.getSunsetTime(coordsDep)['decimal']
		# timeSRArr = self.sun.getSunriseTime(coordsArr)['dec_rel']
		# timeSSArr = self.sun.getSunsetTime(coordsArr)['decimal']
		# (h, m) = depFtime.strftime("%H:%M").split(':')
		# depDecimal = int(h) + int(m) / 60
		# (h, m) = str(fltTime)[:-3].split(':')
		# x_flight = int(h) + int(m) / 60
		# arrDecimal = depDecimal + x_flight
		# lineFlight = LineString([(depDecimal, 1), (arrDecimal, 0)])
		# lineSR = LineString([(timeSRDep, 1), (timeSRArr, 0)])
		# lineSS = LineString([(timeSSDep, 1), (timeSSArr, 0)])
		# lineSRnextDay = LineString([(timeSRDep + 24, 1), (timeSRArr + 24, 0)])
		# lineSSnextDay = LineString([(timeSSDep + 24, 1), (timeSSArr + 24, 0)])

		# z1 = lineFlight.intersection(lineSR)
		# z2 = lineFlight.intersection(lineSS)
		# z3 = lineFlight.intersection(lineSRnextDay)
		# z4 = lineFlight.intersection(lineSRnextDay)

		# x1 = lineFlight.crosses(lineSR)
		# x2 = lineFlight.crosses(lineSS)
		# x3 = lineFlight.crosses(lineSRnextDay)
		# x4 = lineFlight.crosses(lineSSnextDay)
		# print('xross or no ', x1, x2, x3, x4)
		# night_time = 0

		# if depDecimal > timeSRDep:
		#	night_time = 0 						# Takoff At Day, short flight
		# night_time = arrDecimal - depDecimal	 # Take Off At Night, short flight
		"""
		if x1 == True:
			if x2 == True:
				if x3 == True:
					if x4 == True:
						night_time = arrDecimal - float(z4.x) + float(z3.x) - float(z2.x)
					night_time = float(z3.x) - float(z2.x) + 
				night_time = arrDecimal - float(z2.x)
			night_time = float(z1.x) - depDecimal

		if x1 and x2 and x3 and x4 == False:
			if	depDecimal > timeSRDep:
				night_time = 0 						# Takoff At Day, short flight
			if depDecimal < timeSRDep:
				night_time = arrDecimal - depDecimal	 # Take Off At Night, short flight
		"""

	# print('вылет ',depDecimal ,'\n', 'SRDep', timeSRDep,'\n', 'SSdep', timeSSDep,'\n', ' посадка ', arrDecimal,'\n', 'SRArr', timeSRArr,'\n', 'SSArr', timeSSArr,'\n', 'Flight', arrDecimal - depDecimal)
	# print('Взлет', depDecimal, 'SRDep', timeSRDep, 'Flight', arrDecimal - depDecimal)
	# print('Ночь = ', night_time)

	# (y, cross0, x) = str(lineFlight.intersection(lineSR)).split(' ')
	# print('test ', cross0, y, x)
	# print('рассвет 1', cross0)
	# print('закат 1', lineFlight.intersection(lineSS))
	# print('рассвет 2', lineFlight.intersection(lineSRnextDay))
	# print('закат 2', lineFlight.intersection(lineSSnextDay))

	def newleg(self):
		"""get date from calendar"""
		addi = self.addlegwindow.addi
		rawDate = addi.dateEdit.date()
		nextdate = rawDate.addDays(1)
		#		date = (rawDate.toPyDate(), nextdate.toPyDate())
		date = rawDate.toPyDate()
		print('посылаемая дата в Sun ', date)
		# self.sun = Sun( (rawDate.year(), rawDate.month(), rawDate.day()) )

		flightno = addi.lineEdit.text()  # flight nuber
		acno = addi.comboBox.currentText()  # aircraft id
		fromap = addi.lineEdit_2.text()  # departure airport ID
		toap = addi.lineEdit_3.text()  # dest airport ID

		"""blk time"""
		rawOffblktime = addi.timeEdit.time()
		offblktime = datetime(rawDate.year(), rawDate.month(), rawDate.day(), rawOffblktime.hour(),
							  rawOffblktime.minute())
		rawOnblktime = addi.timeEdit_2.time()
		onblktime = datetime(rawDate.year(), rawDate.month(), rawDate.day(), rawOnblktime.hour(), rawOnblktime.minute())
		if rawOffblktime > rawOnblktime:  # Check next day
			onblktime += timedelta(days=1)
		blktime = onblktime - offblktime
		# print (rawOffblktime.toPyTime())
		# blktime = blktimee.total_seconds()//60

		"""Flt time"""
		rawDepFTime = addi.timeEdit_4.time()
		depFtime = datetime(rawDate.year(), rawDate.month(), rawDate.day(), rawDepFTime.hour(), rawDepFTime.minute())
		rawArriveTime = addi.timeEdit_3.time()
		arriveTime = datetime(rawDate.year(), rawDate.month(), rawDate.day(), rawArriveTime.hour(),
							  rawArriveTime.minute())
		if rawArriveTime < rawDepFTime:  # Check next day
			arriveTime += timedelta(days=1)
		fltTime = arriveTime - depFtime

		# Night Flight Time

		# Write Line to log.db
		dte = date.strftime("%d\\%m\\%Y")
		onbt = onblktime.strftime("%H:%M")
		tot = depFtime.strftime("%H:%M")
		lt = arriveTime.strftime("%H:%M")
		ofbt = offblktime.strftime("%H:%M")
		query = QtSql.QSqlQuery()
		query.prepare(
			"INSERT INTO log ('Date', 'FlightNumber', 'Aircraft', 'AirportDeparture', 'AirportArrival', 'OffBlock', 'TakeOff', 'Landing', 'OnBlock', 'FlightTime', 'BlockTime', 'NightTime') VALUES (?,?,?,?,?,?,?,?,?,?,?,?)")
		query.bindValue(0, rawDate)
		query.bindValue(1, flightno)
		query.bindValue(2, acno)
		query.bindValue(3, fromap.upper())
		query.bindValue(4, toap.upper())
		query.bindValue(5, ofbt)
		query.bindValue(6, tot)
		query.bindValue(7, lt)
		query.bindValue(8, onbt)
		query.bindValue(9, str(fltTime)[:-3])
		query.bindValue(10, str(blktime)[:-3])
		query.bindValue(11, 'Жопа Тут')
		if not query.exec_():
			QtWidgets.QMessageBox.warning(None, "Database Error", query.lastError().text())
			return
		self.db.commit()
		self.run()


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
