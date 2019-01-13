import sys
from PyQt5.QtWidgets import QApplication,QMainWindow


class Exsample(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.statusBar().showMessage("hello")

        self.setGeometry(300,300,300,300)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Exsample()

    sys.exit(app.exec_())
