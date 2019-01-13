import sys
from PyQt5.QtWidgets import QApplication,QWidget,QToolTip,QPushButton
from PyQt5.QtGui import QFont


class Exsample(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        #设置提示字符串的字体
        QToolTip.setFont(QFont("SansSerif",10))
        
        #定义btn
        btn = QPushButton('鼠标移动看看有啥效果?',self)

        #设置tooltip
        btn.setToolTip("what ever")
        btn.resize(btn.sizeHint())
        btn.move(30,30)

        


        #显示窗口  (padx,pady,width,height)
        self.setGeometry(300,300,800,300)
        self.setWindowTitle("toolTip")
        self.show()


if __name__ == '__main__':
     app = QApplication(sys.argv)
     ex = Exsample()

     sys.exit(app.exec_())
