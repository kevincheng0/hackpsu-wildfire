import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import Qt
import random

SPRAY_PARTICLES = 50
SPRAY_DIAMETER = 5
COLORS = [
# 17 undertones https://lospec.com/palette-list/17undertones
'#000000', '#141923', '#414168', '#3a7fa7', '#35e3e3', '#8fd970', '#5ebb49',
'#458352', '#dcd37b', '#fffee5', '#ffd035', '#cc9245', '#a15c3e', '#a42f3b',
'#f45b7a', '#c24998', '#81588d', '#bcb0c2', '#ffffff',
]

class QPaletteButton(QtWidgets.QPushButton):

    def __init__(self, color):
        super().__init__()
        self.setFixedSize(QtCore.QSize(24,24))
        self.color = color
        self.setStyleSheet(f"background-color: {color}")

class Canvas(QtWidgets.QLabel):

    def __init__(self):
        super().__init__()
        pixmap = QtGui.QPixmap(800, 400)
        pixmap.fill(QtGui.QColor("white"))
        self.setPixmap(pixmap)
        self.pen_color = QtGui.QColor('#000000')
        self.drawn = []

    def set_pen_color(self, c):
        print(self.drawn)
        self.drawn = []
        self.pen_color = QtGui.QColor(c)

    def mouseMoveEvent(self, e):

        painter = QtGui.QPainter(self.pixmap())
        p = painter.pen()
        p.setWidth(1)
        p.setColor(self.pen_color)
        painter.setPen(p)

        for n in range(SPRAY_PARTICLES):
            xo = int(random.gauss(0, SPRAY_DIAMETER))
            yo = int(random.gauss(0, SPRAY_DIAMETER))
            painter.drawPoint(e.x() + xo, e.y() + yo)
            self.drawn.append((e.x() + xo, e.y() + yo))

        painter.end()
        self.update()


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: brown;")
        self.setWindowTitle("Color") 

        self.canvas = Canvas()
        w = QtWidgets.QWidget()
        l = QtWidgets.QVBoxLayout()
        w.setLayout(l)
        l.addWidget(self.canvas)

        options = QtWidgets.QHBoxLayout()
        self.add_options_buttons(options)
        l.addLayout(options)

        self.setCentralWidget(w)

    def add_options_buttons(self, layout):
        for c in COLORS:
            b = QPaletteButton(c)
            b.pressed.connect(lambda c=c: self.canvas.set_pen_color(c))
            layout.addWidget(b)


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()