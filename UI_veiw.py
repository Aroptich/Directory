from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class Widget(QWidget):
    def __init__(self, x=50, y=150, widht_widget=150, height_widget=20):
        self.x = x
        self.y = y
        self.widht_widget = widht_widget
        self.height_widget = height_widget
        super(Widget, self).__init__()

        self.btn2 = QPushButton('Создать контакт', self)  # Создаем кнопку на главном окне
        self.btn2.setFont(QFont("Times", 11, QFont.Bold))  # Задание шрифта виджета
        self.btn2.setGeometry(QRect(230, 330, 150, 50))  # Задание положения и размеров поля виджета
    def create_label(self):
        self.label_names = ['Имя', 'Фамилия', 'Номер телефона']
        for names in self.label_names:
            self.label = QLabel(names, self)
            self.label.setFont(QFont("Times", 11, QFont.Bold))#Задание шрифта виджета
            self.label.setGeometry(QRect(self.x, self.y, self.widht_widget, self.height_widget))#Задание положения и размеров поля виджета
            self.y += 50
        return self.label


    def create_menu(self):
        menuBar = self.menuBar()
        fileMenu = QMenu("Файл", self)
        menuBar.addMenu(fileMenu)
        list_contacts = fileMenu.addAction('Список контактов')
        # list_contacts.triggered.connect(lambda: Guitar_2())
        return menuBar


    def create_line_edit(self):
        self.y = 150
        self.line_edit_names = ['Введите Имя', 'Введите фамилию', 'Введите номер телефона']
        for names in self.line_edit_names:
            self.x = 200
            self.ledText = QLineEdit('', self)  # Создаем поля для ввода текста
            self.ledText.setPlaceholderText(names)#Задание текста в поле ввода
            self.ledText.setGeometry(QRect(self.x, self.y, self.widht_widget, self.height_widget)) #Задание положения и размеров поля виджета
            self.y +=50
        return self.ledText

# class Guitar_2(QWidget):
#     def __init__(self):
#         super().__init__()
#
#         self.setGeometry(250, 55, 1200, 800)
#         self.setWindowTitle('Гитара')
#
#         self.First_button = QPushButton('Первая струна(клавиша 1)', self)
#         self.First_button.resize(170, 50)
#         self.First_button.move(40, 100)
#
#         self.Second_button = QPushButton('Вторая струна(клавиша 2)', self)
#         self.Second_button.resize(170, 50)
#         self.Second_button.move(40, 200)
#         self.show()





