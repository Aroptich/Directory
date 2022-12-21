import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtGui
from UI_veiw import Widget
from PyQt5.QtCore import *



class DlgMain(QMainWindow, Widget): #Создаем класс DlgMain и наследуемся от класса Qdialog
    def __init__(self): # Функция инициализации класса
        super().__init__() #Вызываем конструктор класса родителя(QMainWindow)
        self.setWindowTitle('Справочник') #Назввние приложения
        self.setFixedSize(400,400) # фиксироваTypeError: __init__() missing 4 required positional argumentsнный размер окна в пикселях
        self.setWindowIcon(QtGui.QIcon('../Directory/icons-directory.png')) #Создание иконки приложения



        self.setStyleSheet('.DlgMain {background-image: url(m_directory-yellow.jpg);}') # Устанавливаем задний фон
        self.label = Widget.creat_label(self) # Создаем именованные лейблы на главном окне
        self.line_edit = Widget.creat_line_edit(self)  # Создаем именнованные поля ввода на главном окне
        self.btn = Widget() #Создаем кнопку на главном экране

        self.statusbar = self.statusBar()  # Создаем статус в нижнем углу экрана на главном окне для отображения сообщений
        self.statusbar.showMessage('Готово', 1000)  # Отображение сообщения статус бара и продолжительность в мс


if __name__ == '__main__':
    app = QApplication(sys.argv) #Создание приложения
    dlgMain = DlgMain() #Создаем объект класса
    dlgMain.show() #Отображение GUI
    sys.exit(app.exec_()) #Запуск приложения