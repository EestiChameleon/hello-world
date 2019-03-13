import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import pyqtSlot


class App(QWidget):

    def __init__(self):
        super().__init__()

        self.title = 'Name'
        self.left = 500
        self.top = 300
        self.width = 200
        self.height = 100
        self.Xb = 65
        self.Yb = 40
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        b = QPushButton('TbIK', self)
        b.move(self.Xb, self.Yb)
        b.clicked.connect(self.on_click)

        self.show()

    @pyqtSlot()
    def on_click(self):
        print('TbIK clicked')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

