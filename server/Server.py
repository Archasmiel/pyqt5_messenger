import sys
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtWidgets, uic


UIFile = 'ui/main.ui'


class ServerUi(QtWidgets.QMainWindow):

    def __init__(self):
        super(ServerUi, self).__init__()
        uic.loadUi(UIFile, self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = ServerUi()
    win.show()
    app.exec_()
