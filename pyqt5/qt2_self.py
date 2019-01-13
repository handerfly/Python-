import sys
from PyQt5.QtWidgets import QWidget,QApplication
from PyQt5.QtGui import QIcon

class App(QWidget):

    def __init__(self):
        super().__init__()
        
        self.initUI()

    def initUI(self):
        self.setGeometry(300,300,300,220)
        self.setWindowTitle("窗口图标案例")
        self.setWindowIcon(QIcon('images/72.png'))

        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)

    ex = App()

    sys.exit(app.exec_())
        
