# -*- coding: utf-8 -*-
"""
Created on Fri Jan 13 16:26:30 2023

@author: Estudiante
"""

from UI_Creditos import Ui_Creditos


import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QAction, QFileDialog, QMainWindow, QMessageBox, QDialog
from PyQt5 import Qt

""" Se usa para actualizar la interface tras ediccion en QtD 
    pyuic5 acerca_de.ui > Ui_Ventana_creditos.py """

class Ui_Ventana_creditos(QDialog):
    def __init__(self, parent = None):
        
        #QtWidgets.QMainWindow.__init__(self, parent)
        QtWidgets.QWidget.__init__(self, parent)
        
        
        self.ui = Ui_Creditos()
        
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.salir)
        
        
        #self.show()
        
    def salir(self):
        self.close()
        
        
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    my_app = Ui_Ventana_creditos()
    my_app.show()
    sys.exit(app.exec_())
    
    
