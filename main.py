import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtGui
from UI_veiw import Widget, Guitar_2
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QMenuBar



class DlgMain(QMainWindow, Widget, QMenuBar): #Создаем класс DlgMain и наследуемся от класса Qdialog
    def __init__(self): # Функция инициализации класса
        super().__init__() #Вызываем конструктор класса родителя(QMainWindow)
        self.setWindowTitle('Справочник') #Назввние приложения
        self.setFixedSize(400,400) # фиксироваTypeError: __init__() missing 4 required positional argumentsнный размер окна в пикселях
        self.setWindowIcon(QtGui.QIcon('../Directory/icons-directory.png')) #Создание иконки приложения



        self.setStyleSheet('.DlgMain {background-image: url(m_directory-yellow.jpg);}') # Устанавливаем задний фон
        self.label = Widget.create_label(self) # Создаем именованные лейблы на главном окне
        self.line_edit = Widget.create_line_edit(self)  # Создаем именнованные поля ввода на главном окне
        self.btn = Widget() #Создаем кнопку на главном экране
        self.menu = Widget.create_menu(self) # Создаем меню с встпылвающими подменю
        # self.win = Guitar_2()


        self.statusbar = self.statusBar()  # Создаем статус в нижнем углу экрана на главном окне для отображения сообщений
        self.statusbar.showMessage('Готово', 1000)  # Отображение сообщения статус бара и продолжительность в мс


if __name__ == '__main__':
    app = QApplication(sys.argv) #Создание приложения
    dlgMain = DlgMain() #Создаем объект класса
    dlgMain.show() #Отображение GUI
    sys.exit(app.exec_()) #Запуск приложения