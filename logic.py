import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.Qt import Qt
from weather_gui import Ui_MainWindow
from PyQt5 import QtWidgets, QtCore, QtGui
import requests
import base64
from datetime import datetime, date
import pprint

"""
Sublcass to Ui_MainWindow which handels all the logic for the GUI
Where QWidget = PyQtClass (This class depends on the design chosen)
and Ui_MainWindow = DesignClass (The name of the class that appears in your design)
See link: https://stackoverflow.com/questions/46544780/qtdesigner-changes-will-be-lost-after-redesign-user-interface
"""
class Logic(QMainWindow, Ui_MainWindow):
    """
    Inheritance from Ui_MainWindow and run setupUi
    """
    def __init__(self, *args, **kwargs):
        QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

    """
    If return tab pressed then search for city
    """
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return:
            self.searchCity()

    """
    Collects data about the weather through a GET request and run
    get_icon_data and get_weather_forecast function
    """
    def searchCity(self):
        try:
            city = self.searchBox.text()
<<<<<<< HEAD
            API_KEY = "87b9acae8fd62ab7bcbd18a7e305feb5"
=======
            API_KEY = "<api_key>"
>>>>>>> 9b81fb9cad064b7ab8c010918ee7e8573b41c341
            base_url = "http://api.openweathermap.org/data/2.5/weather?"
            Final_url = base_url + "appid=" + API_KEY + "&q=" + city + "&units=metric"
            json_response = requests.get(Final_url).json()
            if json_response["cod"]==200:
                self.get_weather_forecast(API_KEY, city)
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
            else:
                self.reset_all()
                self.weatherIcon.setText("Not a valid city")
        except Exception as e:
            self.reset_all()
            self.weatherIcon.setText("Not a valid city")
            print ("Errorwhile searching city: ")
            print (e)

    """
    Get the weather at 15:00:00 for the upcoming three days through GET request
    """
    def get_weather_forecast(self, api_key, city):
        try:
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

                    #set weekday for coming weather
                    year, month, day = (int(x) for x in found_date.split('-'))
                    forcast_dict.get("text"+str(count)).setText(weekdays[date(year, month, day).weekday()])

                    if count == 3:
                        break
        except Exception as e:
            print ("Error while getting weather forecast: ")
            print (e)

    """
    Get the weather icon at 15:00:00 for the upcoming three days through GET request
    """
    def get_icon_data(self, json_response, widget):
        try:
            icon_id = json_response['weather'][0]['icon']
            url = 'http://openweathermap.org/img/wn/{icon}.png'.format(icon=icon_id)
            response = requests.get(url, stream=True)
            icon_data= base64.encodebytes(response.raw.read())
            ba = QtCore.QByteArray.fromBase64(icon_data)
            pixmap = QtGui.QPixmap()
            if pixmap.loadFromData(ba, "PNG"):
                widget.setScaledContents(True)
                widget.setPixmap(pixmap)
        except Exception as e:
            print ("Error while getting icon: ")
            print (e)


    """
    Resets all widgets all widgets to be empty
    """
    def reset_all(self):
        try:
            empty_pixmap = QtGui.QPixmap()
            self.day1_icon.setPixmap(empty_pixmap)
            self.day2_icon.setPixmap(empty_pixmap)
            self.day3_icon.setPixmap(empty_pixmap)
            self.day1_temp.setText("")
            self.day2_temp.setText("")
            self.day3_temp.setText("")
            self.day1_text.setText("")
            self.day2_text.setText("")
            self.day3_text.setText("")
            self.weatherIcon.autoFillBackground()
            self.detailedInfo.setText("")
            self.tempBox.setText("")
            self.cityName.setText("")
        except Exception as e:
            print ("Error while resetting all widgets: ")
            print (e)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = Logic()
    w.show()
    sys.exit(app.exec_())
