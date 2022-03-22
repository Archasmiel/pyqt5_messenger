import time
import sys

from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic
from PyQt5.QtGui import QIcon
from server.ui.InfoUI import InfoUi

UIFile = r'assets/ui/server.ui'


class ServerUi(QMainWindow):
    #
    #    utility methods
    #
    @staticmethod
    def get_dmyhms_time_now():
        return time.strftime(f"%d.%m.%Y_%H.%M.%S", time.localtime())

    @staticmethod
    def get_hms_time_now():
        return time.strftime(f"%H:%M:%S", time.localtime())

    def update_log(self, text, whom):
        self.server_log += f'<i><font color="grey">[{self.get_hms_time_now()}]</font> ' \
                           f'<font color="{self.users.get(whom)}">[{whom}]</font> >> </i>{text}<br/>\n'
        self.textEdit.setHtml(self.server_log)

    #
    #    action methods
    #
    def action_exit_window(self):
        if self.running:
            try:
                # Server TODO
                self.running = False
                self.update_log(f'Stopped server', 'Server')
            except Exception:
                self.update_log(f'Error server stopping', 'Error')

        with open(rf'logs/log_{self.get_dmyhms_time_now()}.html', 'w') as f:
            f.write(self.server_log)

        sys.exit(0)

    def action_start_server(self):
        if self.running:
            self.update_log(f'Sorry, but server is already running', 'Error')
        else:

            try:
                # Server TODO
                self.running = True
                self.update_log(f'Started server', 'Server')
            except Exception:
                self.update_log(f'Error server starting', 'Error')

    def action_stop_server(self):
        if not self.running:
            self.update_log(f'Sorry, but server is already stopped', 'Error')
        else:
            try:
                # Server TODO
                self.running = False
                self.update_log(f'Stopped server', 'Server')
            except Exception:
                self.update_log(f'Error server stopping', 'Error')

    def action_push_button(self):
        if self.running:
            command = self.lineEdit.text()
            self.update_log(f'Suggested command "{command}"', 'ServerCommand')
            self.lineEdit.setText('')
        else:
            self.update_log(f'Server is not running', 'Error')
            self.lineEdit.setText('')

    def action_info_show(self):
        self.info.show()

    #
    #    init methods
    #
    def init(self):
        self.init_window()
        self.init_menubar()
        self.init_elements()

    def init_window(self):
        # init window
        self.setWindowIcon(QIcon("assets/images/logo.png"))
        self.setWindowTitle('Server')
        self.setFixedSize(792, 602)

        # successful load message
        self.update_log(f'Application loaded', 'Initial')

    def init_elements(self):
        # init pushButton
        self.pushButton.setText('Push')
        self.pushButton.clicked.connect(self.action_push_button)
        self.pushButton.setShortcut('Return')

        # init textEdit
        self.textEdit.setReadOnly(True)

    def init_menubar(self):
        bar = self.menuBar()

        # Actions menu
        file = bar.addMenu('Actions')
        file_menu = [file.addAction('Start'), file.addAction('Stop'), file.addAction('Exit')]
        file_menu_actions = [self.action_start_server, self.action_stop_server, self.action_exit_window]

        for n, m in enumerate(file_menu):
            m.triggered.connect(file_menu_actions[n])

        # Info menu
        about = bar.addMenu('About')
        about_menu = [about.addAction('Info')]
        about_menu_actions = [self.action_info_show]

        for n, m in enumerate(about_menu):
            m.triggered.connect(about_menu_actions[n])

    def __init__(self):
        super(ServerUi, self).__init__()
        uic.loadUi(UIFile, self)

        self.users = {
            'Error': 'red',
            'ServerCommand': '#11468F',
            'Server': '#05595B',
            'Initial': '#FFB72B',
            'Client': 'black'
        }
        self.server_log = ''
        self.running = False
        self.info = InfoUi()

        self.statusBar().showMessage('Application started')
        self.init()
        self.show()
