import sys
from PyQt5.QtWidgets import QApplication,QWidget


if __name__ == "__main__":
    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(450,150)
    w.move(800,300)
    w.setWindowTitle('超级运维管理系统第一个窗口')
    w.show()


    sys.exit(app.exec_())







