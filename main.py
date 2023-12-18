import sys
from PyQt5 import uic
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QDialog


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('MainWindowpy.ui', self)
        self.label.setPixmap(QPixmap.fromImage(QImage('back.jpg')))
        self.pushButton.clicked.connect(self.play)
        self.pushButton_2.clicked.connect(self.rules)

    def rules(self):
        pass

    def play(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
