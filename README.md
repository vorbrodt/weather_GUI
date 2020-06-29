# Weather application

- Get API key from "https://openweathermap.org/" through creating account. Sign in and API key will be found under the tab "API keys".
Then add the personal API key in the logic.py file.

- Run the logic.py file (keep the weather_gui.py file in the same directory)


## Creating desktop application with QT designer on macOS

```
pip3 install pyqt5
```

- Download QT creator (includes QT designer) from: https://www.qt.io/ (download the open-source online version)

- After installation, select "New File or Project" and select the veriant to "Qt design form"

- Once GUI have been created, save it to desired folder. The file is saved as a ".ui-file" so following command to turn it to Python code that can be run:

```
cd pathTo.ui
pyuic5 -x nameOf.ui -o desiredName.py
```

