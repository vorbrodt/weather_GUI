# weather_GUI

## How to run on macOS

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
