
# -*- coding: utf-8 -*-
"""
Created on Tue May 17 00:49:49 2022

@author: JHOANSMITHMOSQUERAPE
"""
# Importando librerias

# QTDESIGNER
from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,Qt, QTimer)
from PyQt5.QtGui import  (QRegExpValidator, QDoubleValidator,QColor,  QKeySequence)

#Tema
#from Tema import Temas
from PyQt5.QtWidgets import *

import sys, os
from PyQt5.QtWidgets import QApplication, QAction, QFileDialog, QShortcut
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QDialog
# from PyQt5 import Qt
from PyQt5.Qt import QRegExp


# Ventanas de interfaces graficas
# ==>Security Screen
# from Ui_seguridad import UI_Seguridad
# ==>Splash Screen
# =>
from UI_Porticos_1920x1080 import Ui_Porticos_1920x1080 

from win32api import GetSystemMetrics # Tamaño de pantalla


import matplotlib.pyplot as plt_o
# Variables globales
cont = 0
cont_2 = 0

basedir = os.path.dirname(__file__)

"""COGER ERROR
elementos, Desplazamientos_elementos,dic_sub_nodos, tbl_Elem, tbl_Rest, diccionarioN = self.elementos_MEF, self.Desplazamientos_elementos_MEF,self.dic_sub_nodos_MEF, self.tbl_Elem_MEF, self.tbl_Rest_MEF, self.diccionarioN_MEF

AttributeError: 'Ui_ANEPY' object has no attribute 'elementos_MEF
'"""


try:
    from ctypes import windll  # Only exists on Windows.
    myappid = 'mycompany.myproduct.subproduct.version'
    windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
except ImportError:
    pass

""" Se usa para actualizar la interface tras ediccion
   en QtDesigner: pyuic5 Porticos_v3.ui > UI_Porticos.py """
   
""" Se usa para agregar las imagnes o iconos, covierte de ,qrc>py   
   pyrcc5 Logo.qrc -o Logo_rc.py"""

class Ui_ANEPY(QMainWindow):

    def __init__(self, parent = None):
        
        #QtWidgets.QMainWindow.__init__(self, parent)
        QWidget.__init__(self, parent)
        self.w_screen =  GetSystemMetrics(0)# Ancho de ventana
        self.h_screen = GetSystemMetrics(1) # Altura de pantalla
        
        # self.ui = Ui_MatrizMultiCriterio()
        # self.ui.setupUi(self)
        # Establece el tamaño de los widgets de la GUI
        #print("W:",self.w_screen )
    
        self.ui = Ui_Porticos_1920x1080()
        self.ui.setupUi(self)
        self.resizeEvent = self.responsive
        self.show()
    def responsive(self, e):
        self.W = self.size().width()
        self.H = self.size().height()
        print("here", self.W )
        print("here 1", self.ui.scrollArea.width())
        # Bar de menú botones
        self.rpsv_bar_cb_pg(self.ui.bar_cb_pg)
        # Pag principal
        self.rpsv_stackedWidget(self.ui.bar_cb_pg, self.ui.stackedWidget, self.ui.groupBox_1)
        # Bar inferior
        self.rpsv_bar_cb_pg_2(self.ui.stackedWidget, self.ui.bar_cb_pg_2)
        self.update()

    def rpsv_bar_cb_pg(self, bar_cb_pg ):
        h = max(int(self.H*0.04 ),36)
        
        bar_cb_pg.setGeometry(0,0,self.W, h)
        bar_cb_pg.update()
    
    def rpsv_stackedWidget(self, referencia, stackedWidget, groupBox_1):
        stackedWidget.setGeometry(10,0,self.W-20, int(stackedWidget.height()))
        stackedWidget.update()

        def rpsv_groupBox_1(groupBox_1):
            groupBox_1.setGeometry(0,5,stackedWidget.width(), int(groupBox_1.height()))
            groupBox_1.update()

        rpsv_groupBox_1(groupBox_1)
        

    def rpsv_bar_cb_pg_2(self, referencia, bar_cb_pg_2):
        h = referencia.y() + referencia.height() - 41
        print(f"h:{h}")
        bar_cb_pg_2.setGeometry(0,h ,self.W-20, int(bar_cb_pg_2.height()))
        bar_cb_pg_2.update()
        

my_app = None     
if __name__ == '__main__':
    app = QApplication(sys.argv)
    #app.setWindowIcon(QtGui.QIcon(os.path.join(basedir, 'logo.ico')))
    my_app = Ui_ANEPY()
    my_app.show()
    sys.exit(app.exec_())