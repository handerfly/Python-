import sys
from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtGui import QIcon


class Exsample(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.setGeometry(300,300,300,100)
        self.setWindowTitle("测试窗口图标")
        self.setWindowIcon(QIcon("images/72.png"))

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    ex = Exsample()

    sys.exit(app.exec_())


        
