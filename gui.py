__author__ = 'STORM'
# -*- coding: utf-8 -*-
import sys
import tkinter
from PyQt5.QtWidgets import QApplication, QWidget, QToolTip, QPushButton, QLineEdit, QInputDialog
from PyQt5.QtGui import*
from PyQt5.QtCore import*
from math import pi, sqrt
root = tkinter.Tk()
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def getpoint(self):
        return(self.x, self.y)
    def __str__ (self):
        return str(self.x) + ',' + str(self.y)
class Circle(object):
    def __init__ (self, rad=0, point=Point(), deg=0):
        self.rad = rad
        self.Center = point
        self.deg = deg
    def diameter(self):
        return 2*float(self.rad)
    def circlearea(self):
        return pi*(float(self.rad)**2)
    def length(self):
        return 2*pi*float(self.rad)
    def __str__ (self):
        return 'Radius = ' + str(self.rad) + '\n' + 'Center: ' + str(self.Center)+ '\n' + 'Area = ' + str(self.circlearea()) + '\n' + 'length = ' + str(self.length()) + '\n' + 'diameter = ' + str(self.diameter())
    def intersection(self, other):
        if sqrt((self.Center.x - other.Center.x)**2 + (self.Center.y - other.Center.y)**2) <= (self.rad + other.rad):
            return True
        else:
            return False
    def sectarea(self, deg):
        if abs(float(deg)) <= 360:
            return float(0.5*deg*(pi/180)*(self.rad**2))
        else:
            return (0.5*(float(deg*(pi/180))-2*pi*int(deg/pi)))*(self.rad**2)
    def sectlength (self, deg):
        if abs(float(deg)) <= 360:
            return float(self.rad*deg*pi/180)
        else:
            return float(self.rad*(deg*pi/180 - 2*pi*int(deg/pi)))
# x = float(input('enter x of the first circle center'))
# y = float(input('enter y of the first circle center'))
# q = Point(x,y)
# r = float(input('enter the radius of the first circle'))
# fc = Circle(r,q)
# se = float(input('set any sector of the 1st circle in degrees'))
# print(str(fc) + '\n' + 'Sector area = ' + str(fc.sectarea(se)) + '\n' + 'Sector length = ' + str(fc.sectlength(se)))
# ask = input('Do you wanna build another circle?(yes = press any key, no = press n)')
# if ask == 'n':
#     print('')
# else:
#     xx = float(input('enter x of the second circle center'))
#     yy = float(input('enter y of the second circle center'))
#     qq = Point(xx,yy)
#     rr = float(input('enter the radius of the second circle'))
#     sc = Circle(rr,qq)
#     see = float(input('set any sector of the 2nd circle in degrees'))
#     print(str(sc) + '\n' + 'Sector area = ' + str(sc.sectarea(see)) + '\n' + 'Sector length = ' + str(sc.sectlength(see)) + '\n' + 'Intersection = ' + str(fc.intersection(sc)))
class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()
    def initUi(self, a=0):
        self.btn = QPushButton('Намалювати коло', self)
        self.a = Circle(a)
        #btn.resize(qbtn.sizeHint())
        self.btn.move(height*0.375-50, 20)
        self.btn.clicked.connect(self.showDialog)
        self.btn.resize(100,30)
        self.setGeometry((width-height*0.75)/2, 0.125*height, height*0.75, height*0.75)
        self.setWindowTitle('CircleBuilder v.1.0')
        self.setWindowIcon(QIcon('cat.ico'))
        self.show()
    def showDialog(self):
        text, ok = QInputDialog.getText(self, 'Введіть параметри кола', 'Радіус:')
        if ok:
            self.a.rad = float(text)
        tex, okay = QInputDialog.getText(self, 'Введіть параметри кола', 'Координата центра x:')
        if okay:
            self.a.Center.x = float(tex)
        te, ook = QInputDialog.getText(self, 'Введіть параметри кола', 'Координата центра y:')
        if ook:
            self.a.Center.y = float(te)
    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        qp.setBrush(Qt.white)
        qp.drawRect(event.rect())
        rx = self.a.rad
        ry = self.a.rad
        qp.setPen(Qt.red)
        cc = QPoint(0.375*height+self.a.Center.x, 0.375*height-self.a.  Center.y)
        qp.drawEllipse(cc, rx, ry)
        qp.end()
        QToolTip.setFont(QFont('Arial', 10))
        self.setToolTip(str(self.a))
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())