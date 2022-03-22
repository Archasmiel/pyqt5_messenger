import sys
from server.ui.ServerUI import ServerUi
from PyQt5.QtWidgets import QApplication


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = ServerUi()
    app.exec_()
