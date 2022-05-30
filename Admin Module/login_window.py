import sys
import requests
import json

from PyQt5 import QtGui
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QListView
from PyQt5.QtWidgets import QMessageBox, QListWidget, QLabel, QLineEdit

from app_window import AppWindow


class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "Admin Portal"
        self.icon_path = 'C:/Users/AKAY/Downloads/logo.png'
        self.width = 800
        self.height = 600
        self.URL = "http://localhost:8000"
        self.username = None
        self.password = None

        self.initialize()

    def initialize(self):
        self.setWindowIcon(QtGui.QIcon(self.icon_path))
        self.setWindowTitle(self.title)
        self.setFixedSize(self.width, self.height)
        self.get_username()
        self.get_password()
        self.get_forgotpassword()

        login_bt = QPushButton("Login", self)
        login_bt.move(350, 285)
        login_bt.clicked.connect(self.login)

        self.show()

    def get_username(self):
        username_label = QLabel(self)
        username_label.setText("USERNAME   ")
        username_label.move(250, 165)

        self.username = QLineEdit(self)
        self.username.move(370, 160)
        self.username.resize(160,35)
    
    def get_password(self):
        password_label = QLabel(self)
        password_label.setText("PASSWORD   ")
        password_label.move(250, 223)

        self.password = QLineEdit(self)
        self.password.setEchoMode(QLineEdit.Password)
        self.password.move(370, 220)
        self.password.resize(160,35)

    def get_forgotpassword(self):
        forgotpassword_label = QLabel(self)
        forgotpassword_label.setText("Forgot Password   ")
        forgotpassword_label.move(550, 470)
        forgotpassword_label.resize(180,20)

    
    def login(self):
        if not self.password.text() or not self.username.text():
            QMessageBox.about(self, "Error", "\nPlease fill all entries\t\n")
        else:
            try:
                login_status = requests.get(self.URL+'/login?username='+
                                        self.username.text()+
                                        '&password='+self.password.text())
                login_status = json.loads(login_status.text)
                if login_status.get('status', False):
                    self.app_window = AppWindow(user=self.username.text())
                else:
                    QMessageBox.about(self, "Login Failed", "\nPlease try again\t\n")
            except requests.exceptions.ConnectionError:
                QMessageBox.about(self, "Conenction Error", "\nDatabase is not running\t\n")


app = QApplication(sys.argv)
style = """
        QWidget{
            background: #232326;
        }
        QLabel{
            font: Big-john;
            font-size: 16px;
            font-weight: bold;
            color: #f70a61;
        }
        QListView
        {
            background: #7e959e;
            margin-top: 20px;
        }
        QLabel#round_count_label, QLabel#highscore_count_label{
            border: 1px solid #fff;
            border-radius: 8px;
            padding: 2px;
        }
        QPushButton
        {
            color: white;
            font-family: Big-john;
            background: #f70a61;
            border: 1px #DADADA solid;
            padding: 5px 10px;
            border-radius: 8px;
            font-weight: bold;
            font-size: 9pt;
            outline: none;
        }
        QPushButton:hover{
            border: 1px #C6C6C6 solid;
            color: #fff;
            background: #ad1a50;
        }
        QLineEdit {
            padding: 1px;
            width: 50px;
            color: #fff;
            font-weight: bold;
            font-size: 14px;
            border-style: solid;
            border: 2px solid #fff;
            border-radius: 8px;
        }
    """
app.setStyleSheet(style)
w = LoginWindow()
sys.exit(app.exec())
