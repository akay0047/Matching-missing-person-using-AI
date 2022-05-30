import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon, QPixmap

class QrCode(QWidget):

    def __init__(self, user: str):
        
        super().__init__()
        self.title = 'QR Code'
        self.setWindowIcon(QtGui.QIcon('C:/Users/AKAY/Downloads/logo.png'))
        self.left = 750
        self.top = 360
        self.width = 400
        self.height = 400
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
    
        label = QLabel(self)
        pixmap = QPixmap('QR.jpg')
        label.setPixmap(pixmap)
        self.resize(pixmap.width(),pixmap.height())
        
        self.show()

    def runscript():
        panel = QtGui.QWidget()
        layout = QtGui.QHBoxLayout(panel)
        return panel 

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = QrCode('abhinay')
    sys.exit(app.exec_())
