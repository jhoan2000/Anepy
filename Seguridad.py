# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 12:13:54 2023

@author: Estudiante
"""
import sys, os
from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt, QTimer)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5.QtWidgets import *



cont_2 = 0

class UiSeguridad(QMainWindow):
    def __init__(self, parent = None):
        QMainWindow.__init__(self, parent)
        self.ui = Ui_Seguridad()
        self.ui.setupUi(self)
        # Eliminar titulo de barra
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        
        self.ui.dial_d1.valueChanged.connect(self.digito_1)
        self.ui.dial_d2.valueChanged.connect(self.digito_2)
        self.ui.dial_d3.valueChanged.connect(self.digito_3)
        self.ui.dial_d4.valueChanged.connect(self.digito_4)
        
        # Drop shadow effect efecto sombra
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(30)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(79,93,116,70))
        self.ui.frame.setGraphicsEffect(self.shadow)
        
        
        # ==>Qtimer of load
        self.timer = QTimer()
        
        self.timer.timeout.connect(self.prueba_seguridad)
        # # Tiempo (ml)
        self.timer.start(35)
        # self.show()
    
        
    def digito_1(self):
        valor = self.ui.dial_d1.value()
        self.ui.lb_d1.setText(str(valor))
        self.prueba_seguridad()
    def digito_2(self):
        valor = self.ui.dial_d2.value()
        self.ui.lb_d2.setText(str(valor))
        self.prueba_seguridad()
    def digito_3(self):
        valor = self.ui.dial_d3.value()
        self.ui.lb_d3.setText(str(valor))
        self.prueba_seguridad()
    def digito_4(self):
        valor = self.ui.dial_d4.value()
        self.ui.lb_d4.setText(str(valor))
        self.prueba_seguridad()
    def prueba_seguridad(self):
        global cont
        valor_1 = self.ui.lb_d1.text()
        valor_2 = self.ui.lb_d2.text()
        valor_3 = self.ui.lb_d3.text()
        valor_4 = self.ui.lb_d4.text()
        valor = valor_1 + valor_2 + valor_3 + valor_4
        key = "1234"
        print(cont, valor)
        if valor==key:
            cont_2 += 1
            if cont == 25:
                self.ui.lb_mensaje.setText("BIENVENIDO")
                self.ui.lb_d1.setText("")
                self.ui.lb_d2.setText("")
                self.ui.lb_d3.setText("")
                self.ui.lb_d4.setText("")
        if self.ui.lb_mensaje.text() == "BIENVENIDO":
            cont += 1
        if cont_2 == 50:
                self.timer.stop()
                print("INGRESO EXITOSO!!!")
                self.close()
                
        
my_app = None     
if __name__ == '__main__':
    app = QApplication(sys.argv)
    #app.setWindowIcon(QtGui.QIcon(os.path.join(basedir, 'logo.ico')))
    my_app = UiSeguridad()
    my_app.show()
    sys.exit(app.exec())