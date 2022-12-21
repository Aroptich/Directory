from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


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
    def creat_label(self):
        self.label_names = ['Имя', 'Фамилия', 'Номер телефона']
        for names in self.label_names:
            self.label = QLabel(names, self)
            self.label.setFont(QFont("Times", 11, QFont.Bold))#Задание шрифта виджета
            self.label.setGeometry(QRect(self.x, self.y, self.widht_widget, self.height_widget))#Задание положения и размеров поля виджета
            self.y += 50
        return self.label





    def creat_line_edit(self):
        self.y = 150
        self.line_edit_names = ['Введите Имя', 'Введите фамилию', 'Введите номер телефона']
        for names in self.line_edit_names:
            self.x = 200
            self.ledText = QLineEdit('', self)  # Создаем поля для ввода текста
            self.ledText.setPlaceholderText(names)#Задание текста в поле ввода
            self.ledText.setGeometry(QRect(self.x, self.y, self.widht_widget, self.height_widget)) #Задание положения и размеров поля виджета
            self.y +=50
        return self.ledText

