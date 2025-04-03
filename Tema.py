# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 00:32:42 2023

@author: Estudiante
"""
from PyQt5 import QtWidgets

class Temas(QtWidgets.QMainWindow):
    def __init__(self,parent = None):
        QMainWindow.__init__(self, parent)  
        self.ui = parent.ui
        self.color_fondo = "#384D59" #384D59
        self.color_lementos = "#D5FEFE"
        self.color_letras = "#006b30"
        self.color_x = "#DCFAA9"
        self.color_y = "#ADF8FE"
        self.color_z = "#FFE847"
        self.ui.wgt_deformada.canvas.ax.set_facecolor(self.color_fondo) 
        self.ui.wgt_FIE.canvas.ax.set_facecolor(self.color_fondo) 
        self.ui.wgt_GDL.canvas.ax.set_facecolor(self.color_fondo) 
        self.ui.wgt_Rest.canvas.ax.set_facecolor(self.color_fondo) 
        self.ui.wgt_porticos.canvas.ax.set_facecolor(self.color_fondo)
        self.oscuro()
        
    def oscuro(self):
        #--------------------------------------------------------------------#
        self.color_fondo = "#384D59" #384D59
        self.color_lementos = "#D5FEFE"
        self.color_letras = "#006b30"
        self.color_x = "#DCFAA9"
        self.color_y = "#ADF8FE"
        self.color_z = "#FFE847"
        self.ui.wgt_deformada.canvas.ax.set_facecolor(self.color_fondo) 
        self.ui.wgt_FIE.canvas.ax.set_facecolor(self.color_fondo) 
        self.ui.wgt_GDL.canvas.ax.set_facecolor(self.color_fondo) 
        self.ui.wgt_Rest.canvas.ax.set_facecolor(self.color_fondo) 
        self.ui.wgt_porticos.canvas.ax.set_facecolor(self.color_fondo)
        
        # Barra principal

        cbg_mnu = "#111C26"  
        cfont_mnu = "rgb(255, 255, 255)" 
        cbg_is = "#384D59"   # Seleccionado
        cfont_is = " rgb(255,255,255)"
        
        cbg_imnu = "#111C26"   # Items
        cfont_imnu = " rgb(255,255,255)"      
        
        mnu = """
        QMenuBar{
        background-color:%s ; color: %s;}
        
        QMenu::item:selected {
            background-color: %s;
            color:%s;
        }
        
        QMenuBar::item {
            spacing: 3px;           
            padding: 2px 10px;
            background-color: %s ;
            color: %s;  
        }
        
        """%(cbg_mnu,cfont_mnu,cbg_is,cfont_is, cbg_imnu,cfont_imnu)
        self.ui.menubar.setStyleSheet(mnu)
        self.ui.menubar.update()
        