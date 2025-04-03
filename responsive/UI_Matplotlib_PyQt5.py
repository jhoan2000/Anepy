# -*- coding: utf-8 -*-
"""
Created on Wed May 18 23:58:45 2022

@author: JHOANSMITHMOSQUERAPE
"""

from PyQt5 import QtWidgets
#from matplotlib.figure import Figure
#from matplotlib.backends.backend_gtk4agg import FigureCanvasQTAgg as FigureCanvas

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

class MplCanvasLienzo(FigureCanvas):
    def __init__(self,):
        self.fig = Figure(facecolor = "#8AC6BF", figsize=[9,6], dpi = 80) #Color de fondo azul
        self.ax = self.fig.add_subplot(111) # Se crea un solo lienzo
        FigureCanvas.__init__(self, self.fig) # Ejecuta

class MatplotlibWidgetaLienzo(QtWidgets.QWidget):
    def __init__(self, parent =None):
        QtWidgets.QWidget.__init__(self, parent)
        self.canvas = MplCanvasLienzo()
        self.vbl =  QtWidgets.QVBoxLayout()
        self.vbl.addWidget(self.canvas)
        self.setLayout(self.vbl)
        
