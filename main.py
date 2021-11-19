import sys
import random
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPainter, QColor, QPen


class First(QMainWindow):  # Экран приветсвия
    def __init__(self):  # иницилизация
        super(QMainWindow, self).__init__()
        uic.loadUi('Ui.ui', self)  # загрузка макета
        self.flag = None
        self.press.clicked.connect(self.flag_on)

    def flag_on(self):
        self.flag = True
        self.update()

    def paintEvent(self, e):
        if self.flag is True:
            qp = QPainter()
            qp.begin(self)
            qp.setBrush(QColor(255, 255, 0))
            x = random.randint(5, 500)
            y = random.randint(5, 500)
            qp.drawEllipse(x, x, y, y)
            qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = First()
    w.show()  # открываем начальное окно - приветсвия
    sys.exit(app.exec_())

