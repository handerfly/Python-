import sys
from PyQt5.QtWidgets import QApplication,QWidget,QDesktopWidget

class Exsample(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.setGeometry(300,300,300,300)
        self.setWindowTitle("居中窗口测试")
        self.center()
        self.show()

    def center(self):

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()

        qr.moveCenter(cp)

        self.move(qr.topLeft())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Exsample()

    sys.exit(app.exec_())
        
        
