import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem
import io
from PyQt5 import uic
import sqlite3

template = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>981</width>
    <height>600</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QTableWidget" name="tableWidget">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>1</y>
      <width>981</width>
      <height>541</height>
     </rect>
    </property>
    <column>
     <property name="text">
      <string>ID</string>
     </property>
    </column>
    <column>
     <property name="text">
      <string>Сорт</string>
     </property>
    </column>
    <column>
     <property name="text">
      <string>Обжарка</string>
     </property>
    </column>
    <column>
     <property name="text">
      <string>Молотый/в зернах</string>
     </property>
    </column>
    <column>
     <property name="text">
      <string>Описание вкуса</string>
     </property>
    </column>
    <column>
     <property name="text">
      <string>Цена</string>
     </property>
    </column>
    <column>
     <property name="text">
      <string>Объем</string>
     </property>
    </column>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>981</width>
     <height>26</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
"""


class Coffee(QMainWindow):
    def __init__(self):
        super(Coffee, self).__init__()
        self.f = io.StringIO(template)
        uic.loadUi(self.f, self)
        self.open_table()

    def open_table(self):
        con = sqlite3.connect("coffee.sqlite")
        cur = con.cursor()
        data = cur.execute("SELECT * FROM coffe_info").fetchall()
        self.tableWidget.setRowCount(len(data))
        for i, row in enumerate(data):
            for j, elem in enumerate(row):
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(str(elem)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Coffee()
    ex.show()
    sys.exit(app.exec())