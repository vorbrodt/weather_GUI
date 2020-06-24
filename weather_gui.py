# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'weather_gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import requests
import base64
import pprint
from datetime import datetime, date

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(467, 574)
        MainWindow.setStyleSheet("background-color: rgb(34, 38, 56);")
        MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 20, 300, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)

        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("background-color: rgba(0,0,0,0%)");
        self.label.setStyleSheet("color: rgb(255, 255, 255)");
        self.label.setScaledContents(False)
        self.label.setObjectName("label")

        self.searchButton = QtWidgets.QPushButton(self.centralwidget)
        self.searchButton.setGeometry(QtCore.QRect(30, 85, 110, 33))
        self.searchButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.searchButton.setObjectName("searchButton")
        self.searchBox = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")

        self.searchBox.setGeometry(QtCore.QRect(200, 84, 241, 34))
        self.searchBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.searchBox.setText("")
        self.searchBox.setObjectName("searchBox")

        self.enterCity = QtWidgets.QLabel(self.centralwidget)
        self.enterCity.setStyleSheet("color: rgb(34, 38, 56);")
        self.enterCity.setGeometry(QtCore.QRect(140, 85, 61, 32))
        self.enterCity.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.enterCity.setObjectName("enterCity")
        font = QtGui.QFont()
        font.setFamily("Times New Roman")

        self.infoFrame = QtWidgets.QFrame(self.centralwidget)
        self.infoFrame.setGeometry(QtCore.QRect(30, 120, 411, 461))
        self.infoFrame.setStyleSheet("background-color: rgb(253, 250, 255);")
        self.infoFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.infoFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.infoFrame.setObjectName("infoFrame")

        self.weatherIcon = QtWidgets.QLabel(self.infoFrame)
        self.weatherIcon.setGeometry(QtCore.QRect(10, 10, 111, 111))
        self.weatherIcon.setText("")
        self.weatherIcon.setObjectName("weatherIcon")

        self.tempBox = QtWidgets.QLabel(self.infoFrame)
        self.tempBox.setGeometry(QtCore.QRect(125, 10, 131, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.tempBox.setFont(font)
        self.tempBox.setText("")
        self.tempBox.setScaledContents(True)
        self.tempBox.setObjectName("tempBox")

        self.detailedInfo = QtWidgets.QLabel(self.infoFrame)
        self.detailedInfo.setGeometry(QtCore.QRect(240, 10, 161, 141))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.detailedInfo.setFont(font)
        self.detailedInfo.setText("")
        self.detailedInfo.setObjectName("detailedInfo")

        self.cityName = QtWidgets.QLabel(self.infoFrame)
        self.cityName.setGeometry(QtCore.QRect(10, 0, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.cityName.setFont(font)
        self.cityName.setObjectName("CityName")

        self.day1_icon = QtWidgets.QLabel(self.infoFrame)
        self.day1_icon.setGeometry(QtCore.QRect(60, 300, 61, 61))
        self.day1_icon.setObjectName("day1_icon")
        self.day2_icon = QtWidgets.QLabel(self.infoFrame)
        self.day2_icon.setGeometry(QtCore.QRect(170, 300, 61, 61))
        self.day2_icon.setObjectName("day2_icon")
        self.day3_icon = QtWidgets.QLabel(self.infoFrame)
        self.day3_icon.setGeometry(QtCore.QRect(280, 300, 61, 61))
        self.day3_icon.setObjectName("day3_icon")

        self.day1_temp = QtWidgets.QLabel(self.infoFrame)
        self.day1_temp.setGeometry(QtCore.QRect(60, 360, 81, 31))
        self.day1_temp.setObjectName("day1_temp")
        self.day2_temp = QtWidgets.QLabel(self.infoFrame)
        self.day2_temp.setGeometry(QtCore.QRect(170, 360, 71, 31))
        self.day2_temp.setObjectName("day2_temp")
        self.day3_temp = QtWidgets.QLabel(self.infoFrame)
        self.day3_temp.setGeometry(QtCore.QRect(280, 360, 71, 31))
        self.day3_temp.setObjectName("day3_temp")

        self.day1_text = QtWidgets.QLabel(self.infoFrame)
        self.day1_text.setGeometry(QtCore.QRect(60, 390, 81, 31))
        self.day1_text.setObjectName("day1_text")
        self.day2_text = QtWidgets.QLabel(self.infoFrame)
        self.day2_text.setGeometry(QtCore.QRect(170, 390, 71, 31))
        self.day2_text.setObjectName("day2_text")
        self.day3_text = QtWidgets.QLabel(self.infoFrame)
        self.day3_text.setGeometry(QtCore.QRect(280, 390, 71, 31))
        self.day3_text.setObjectName("day3_text")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 467, 22))
        self.menubar.setObjectName("menubar")

        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)

        self.menuEdit.setObjectName("menuEdit")

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.searchButton.clicked.connect(self.searchCity)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Get weather of a city"))
        self.searchButton.setText(_translate("MainWindow", "Search"))
        self.enterCity.setText(_translate("MainWindow", " City:"))

        self.day1_icon.setText(_translate("MainWindow", ""))
        self.day2_icon.setText(_translate("MainWindow", ""))
        self.day3_icon.setText(_translate("MainWindow", ""))
        self.day1_temp.setText(_translate("MainWindow", ""))
        self.day2_temp.setText(_translate("MainWindow", ""))
        self.day3_temp.setText(_translate("MainWindow", ""))
        self.day1_text.setText(_translate("MainWindow", ""))
        self.day2_text.setText(_translate("MainWindow", ""))
        self.day3_text.setText(_translate("MainWindow", ""))

        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))

    def searchCity(self):
        city = self.searchBox.text()

        API_KEY = "87b9acae8fd62ab7bcbd18a7e305feb5" #make script which fetches this
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        Final_url = base_url + "appid=" + API_KEY + "&q=" + city + "&units=metric"
        json_response = requests.get(Final_url).json()
        self.get_weather_forecast(API_KEY, city)
        if json_response["cod"]==200:
            self.cityName.setText(json_response["name"])
            main = json_response["main"]
            current_temperature = main["temp"]
            self.tempBox.setText(str(current_temperature) + " °C")

            #setup icons given by the weather API
            self.get_icon_data(json_response, self.weatherIcon)

            wind = str(json_response["wind"]["speed"])
            humidity = str(main["humidity"])
            pressure = str(main["pressure"])
            self.detailedInfo.setText("Humidity: " + humidity + "%\n"
                + "Wind: " + wind + " m/s\n" + "Pressure: " + pressure + " hPa")

    def get_weather_forecast(self, api_key, city):
        base_url = "http://api.openweathermap.org/data/2.5/forecast?"
        Final_url = base_url + "appid=" + api_key + "&q=" + city + "&units=metric"
        json_response = requests.get(Final_url).json()
        current_date = str(datetime.date(datetime.now()))
        forecast_list = json_response["list"]
        forcast_dict = {"icon1": self.day1_icon, "icon2": self.day2_icon, "icon3": self.day3_icon,
            "temp1": self.day1_temp, "temp2": self.day2_temp, "temp3": self.day3_temp,
            "text1": self.day1_text, "text2": self.day2_text, "text3": self.day3_text}
        weekdays= ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        count = 0
        for i in forecast_list:
            found_date = str(i.get("dt_txt").partition(' ')[0])
            found_time = (str(i.get("dt_txt").split(' ')[1]))

            if current_date != found_date and "15:00:00"==found_time:
                count += 1
                temp = i["main"].get("temp")

                #set temp for coming days
                forcast_dict.get("temp"+str(count)).setText(str(temp) + " °C")

                #set icon for coming days
                widget = forcast_dict.get("icon" + str(count))
                self.get_icon_data(i, widget)

                #set day for coming weather

                year, month, day = (int(x) for x in found_date.split('-'))
                print (str(date(year, month, day).weekday()))
                forcast_dict.get("text"+str(count)).setText(weekdays[date(year, month, day).weekday()])

                if count == 3:
                    break

        #pprint.pprint (forecast_list)

    def get_icon_data(self, json_response, widget):
        icon_id = json_response['weather'][0]['icon']
        url = 'http://openweathermap.org/img/wn/{icon}.png'.format(icon=icon_id)
        response = requests.get(url, stream=True)
        icon_data= base64.encodebytes(response.raw.read())
        ba = QtCore.QByteArray.fromBase64(icon_data)
        pixmap = QtGui.QPixmap()
        if pixmap.loadFromData(ba, "PNG"):
            widget.setScaledContents(True)
            widget.setPixmap(pixmap)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
