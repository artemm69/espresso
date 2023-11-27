from PyQt5.QtWidgets import QApplication, QMainWindow, QHeaderView, QTableWidgetItem
from PyQt5 import uic as QInterface

import sqlite3
import sys


class AddCoffee(QMainWindow):
    def __init__(self):
        super(AddCoffee, self).__init__()
        QInterface('add_coffee_form.ui', self)

        self.bindUi()

    def bindUi(self):
        self.addButton.clicked.connect(self.addCoffee)

    def addCoffee(self):
        sort = self.sort.text()
        roasting = self.roasting.text()
        coffee = self.coffee.text()
        taste = self.taste.text()
        price = self.price.text()
        capacity = self.capacity.text()

        if not all([req for req in [sort, roasting, coffee, taste, price, capacity]]):
            self.statusBar().showMessage('Не удалось добавить новое кофе.')
            return

        if not roasting.isdigit():
            self.statusBar().showMessage('Не удалось добавить новое кофе.')
            return

        if not price.isdigit():
            self.statusBar().showMessage('Не удалось добавить новое кофе.')
            return

        if not capacity.isdigit():
            self.statusBar().showMessage('Не удалось добавить новое кофе.')
            return

        database = sqlite3.connect('coffee.sqlite')
        cursor = database.cursor()

        cursor.execute(
            f"""INSERT INTO coffees(sort, roasting, coffee, taste, price, capacity)
      VALUES('{sort}', {roasting}, '{coffee}', '{taste}', {price}, {capacity})"""
        )

        database.commit()


class CoffeeViewer(QMainWindow):
    def __init__(self):
        super(CoffeeViewer, self).__init__()
        QInterface.loadUi('main.ui', self)

        self.loadCoffeeData(self.tableWidget)

    def loadCoffeeData(self, parent):
        parent.setRowCount(0)
        headers = ['ID', 'Сорт', 'Обжарка', 'Кофе', 'Вкус', 'Цена кофе', 'Объем кофе']
        parent.setColumnCount(len(headers))
        parent.setHorizontalHeaderLabels(headers)
        parent.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        database = sqlite3.connect('coffee.sqlite')
        cursor = database.cursor()

        coffee_data = cursor.execute('SELECT * FROM coffees').fetchall()
        for y, coffee in enumerate(coffee_data):
            parent.setRowCount(parent.rowCount() + 1)
            for x, description in enumerate(coffee):
                parent.setItem(y, x, QTableWidgetItem(str(description)))

