# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QWidget,QPushButton
from PyQt5.QtCore import QCoreApplication

class Example(QWidget):

    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):

        #添加一个按钮
        btn = QPushButton('Quit', self)
        btn.clicked.connect(QCoreApplication.instance().quit)
        #设定按钮大小和位置，使用推荐大小
        btn.resize(btn.sizeHint())
        btn.move(50, 50)

        #设置窗口的位置和宽高
        self.setGeometry(300, 300, 300, 300)
        #设置窗口标题
        self.setWindowTitle('quit')

        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    example = Example()
    sys.exit(app.exec_())