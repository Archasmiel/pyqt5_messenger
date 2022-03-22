from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QWidget
from PyQt5 import uic
from PyQt5 import QtCore

UIFile = r'assets/ui/info.ui'


class InfoUi(QWidget):

    def init_window(self):
        self.setWindowIcon(QIcon("assets/images/logo.png"))
        self.setWindowTitle('Info')
        self.setFixedSize(200, 90)

        self.label_2.setText('Server application')
        self.label_2.resize(150, 15)
        self.label_2.move(25, 5)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)

        self.label_3.setText('Created by Archasmiel')
        self.label_3.resize(150, 15)
        self.label_3.move(25, 35)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)

        self.label.setText("telegram: <a href=\"https://github.com/Archasmiel\">@archasmiel</a><br>"
                           "github: <a href=\"https://github.com/Archasmiel\">Archasmiel</a>")
        self.label.setOpenExternalLinks(True)
        self.label.resize(150, 35)
        self.label.move(25, 55)
        self.label.setAlignment(QtCore.Qt.AlignCenter)

    def __init__(self):
        super(InfoUi, self).__init__()
        uic.loadUi(UIFile, self)
        self.init_window()
