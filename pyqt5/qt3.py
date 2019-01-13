import sys
from PyQt5.QtWidgets import QApplication,QWidget,QToolTip,QPushButton
from PyQt5.QtGui import QFont

class Exsample(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):


        QToolTip.setFont(QFont('SansSerif',10))
        self.setToolTip('This is a <b>QWidget</b> widget')

        btn = QPushButton('Button',self)
        btn.setToolTip('This is a <b>QpushButton</b> widget')
        btn.resize(btn.sizeHint())
        btn.move(20,20)
        
        self.setGeometry(300,300,300,300)
        self.setWindowTitle("测试文字提示")
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)

    ex = Exsample()

    sys.exit(app.exec_())
