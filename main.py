
# -*- coding: utf-8 -*-
"""
Created on Tue May 17 00:49:49 2022

@author: JHOANSMITHMOSQUERAPE
"""
# Importando librerias

# QTDESIGNER
from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,Qt, QTimer)
from PyQt5.QtGui import  (QRegExpValidator, QDoubleValidator,QColor,  QKeySequence, QIcon )

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
from Ui_splash_screen import Ui_SplashScreen
# =>
from UI_Porticos import Ui_Porticos
from UI_Porticos_1920x1080 import Ui_Porticos_1920x1080 
from main_conversiones import Ui_Conversor_Unidades
from Ui_Ventana_creditos_nuevo import Ui_Creditos
#from win32api import GetSystemMetrics # Tamaño de pantalla


# Manejo de funciones al accionar widgets de las GUI
from UI_Funciones import Ui_Funciones

# Manejo de fichero
from cvs_ficheros import abir_datos, guardar_datos
from os import path

# ANALISÍS  ESTRUCTURAL
from math import  sqrt, atan, pi
import numpy as np
import Analisis_porticos as AEM
import Vector_fuerzas as VF
from propiedades_elementos import Propiedades_elemento
from MEF import Sub_E_N_F_FW_R, nodo_ireal
from deformada import Deformada

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
    myappid = 'jsmp.myproduct.subproduct.version'
    windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
except ImportError:
    pass

""" Se usa para actualizar la interface tras ediccion
   en QtDesigner: pyuic5 Porticos_v3.ui > UI_Porticos.py """
   
""" Se usa para agregar las imagnes o iconos, covierte de ,qrc>py   
   pyrcc5 Logo.qrc -o Logo_rc.py"""

class Delegate(QItemDelegate):
    def createEditor(self, parent, option, index):     # self, parent, option, index    
       
        line = QLineEdit(parent)                       #  parent
        
        # try it:
        validador =QRegExp("[-0-9.0-9]*")
        ok = QRegExpValidator(validador, parent)
        line.setValidator(ok)
        return line 
    
class Creditos(QMainWindow):
    def __init__(self, parent = None):
        QMainWindow.__init__(self, parent)
        self.ui = Ui_Creditos()
        self.ui.setupUi(self)
        self.ui.btn_salir.clicked.connect(self.salir)
        
        # Eliminar titulo de barra
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        
        # Drop shadow effect efecto sombra
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(40)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor("#53fdef"))
        self.ui.btn_salir.setGraphicsEffect(self.shadow)

        
    def salir(self):
        self.close()
          
class Ui_ANEPY(QMainWindow):

    def __init__(self, parent = None):
        
        #QtWidgets.QMainWindow.__init__(self, parent)
        QWidget.__init__(self, parent)
        self.ui = None
        
        # self.ui = Ui_MatrizMultiCriterio()
        # self.ui.setupUi(self)
        # Establece el tamaño de los widgets de la GUI
        #print("W:",self.w_screen )
        # if self.w_screen <= 1366:
        #     self.ui = Ui_Porticos()
        #     self.ui.setupUi(self)
        # elif self.w_screen == 1920:
        #     print("here")
        self.ui = Ui_Porticos_1920x1080()        
        self.icon = QIcon(os.path.join(basedir, 'Logo.ico'))
        menu_tray = QMenu()
        mn_exit = menu_tray.addAction("Salir",)
        mn_exit.triggered.connect(self.salir)
        self.tray = QSystemTrayIcon()
        self.tray.setContextMenu(menu_tray)
        self.tray.setIcon(self.icon)
        self.tray.setToolTip("Gracias por Utilizar ANEPY")
        self.tray.show()
        

        self.ui.setupUi(self)

        self.resizeEvent = self.responsive
        self.show()

        self.con = 0 # contador
        self.Fuerzas_internas = 0 # Fuerzas internas por elementos
        self.g_delta_elem = 0 # Gradso y desplazamientos por elemento
        self.tema = "rgb(213, 244, 230)"# color del tema se inicializa
        self.comboBox = 0 # controla el tipo de restricciones
        
        self.Fn_Cambiar_Tema("claro")
        # Colores de elementos de graficos
        self.color_fondo = "#ffffff"
        self.color_lementos = "gray"
        self.color_letras = "#006b30"
        self.color_x = "#14C38E"
        self.color_y = "#1A3C40"
        self.color_z = "#2F8F9D"
        self.tamaño_letra = 9
        self.redon = 4 # redondea entradas 

        # Activas MEF
        self.f_amp = 0
        self.activar_mef = False
        
        # Valiciones de entradas
        self.ui.inline_amplificacion.setMaxLength(11)
        self.ui.inline_amplificacion.setValidator(QDoubleValidator(0, 9999999, 4))
        
        self.ui.tbl_Elem.setItemDelegate(Delegate())  # set delegate
        self.ui.tbl_Nod.setItemDelegate(Delegate())  # set delegate
        self.ui.tbl_Fuer.setItemDelegate(Delegate())  # set delegate
        self.ui.tbl_Fuer_W.setItemDelegate(Delegate())  # set delegate
        self.ui.tbl_Rest.setItemDelegate(Delegate())  # set delegate
        
        # Si se modifica alguna tabla
        self.ui.tbl_Elem.cellChanged.connect(self.arhivo_modificado)
        self.ui.tbl_Nod.cellChanged.connect(self.arhivo_modificado)
        self.ui.tbl_Fuer.cellChanged.connect(self.arhivo_modificado)
        self.ui.tbl_Fuer_W.cellChanged.connect(self.arhivo_modificado)
        self.ui.tbl_Rest.cellChanged.connect(self.arhivo_modificado)
        
        #if self.ui.tbl_Elem.tbl_Elem.item(0,0)
        #print("#-----------------------")
       
        #   Valores de inicializacion
        Ui_Funciones.Fn_inicializar(self)
        
        # Control renglones en tablas
        Ui_Funciones.Wgt_SpinBox(self)
        
        # Control boton
        Ui_Funciones.Wgt_PushBoton(self)
        
        # Control Wgt combox
        Ui_Funciones.Wgt_ComboBox(self)
        
        # Control Wgt slider
        Ui_Funciones.Wgt_Slider(self)
        
        # Control barra superior
        Ui_Funciones.Wgt_Barra(self)
        
        self.portapapeles = QApplication.clipboard()
        self.short_copiar = QShortcut(QKeySequence("Ctrl+C"), self)
        self.short_copiar.activated.connect(lambda shortcut_key = self.short_copiar.key().toString(): self.copiar())
        self.short_pegar = QShortcut(QKeySequence("Ctrl+V"), self)
        self.short_pegar.activated.connect(lambda shortcut_key = self.short_copiar.key().toString(): self.pegar())
        self.short_analizar = QShortcut(QKeySequence("Ctrl+Intro"), self)
        self.short_analizar.activated.connect(lambda shortcut_key = self.short_analizar.key().toString(): self.Fn_visualizar_porticos())
        self.short_analizar.activated.connect(lambda shortcut_key = self.short_analizar.key().toString(): self.Fn_MatricesRigidezGUI())
        self.no_visualizar_portico = False

        self.show()
      
        
    # Ventanas secundarias y emergentes
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
          
    def Fn_Cambiar_Tema(self, modo):
        def modo_claro():
            
            # Graficos
            #--------------------------------------------------------------------#
            self.color_fondo = "#ffffff"
            self.color_lementos = "gray"
            self.color_letras = "#006b30"
            self.color_x = "#14C38E"
            self.color_y = "#1A3C40"
            self.color_z = "#2F8F9D"
            self.ui.wgt_deformada.canvas.ax.set_facecolor(self.color_fondo) 
            self.ui.wgt_FIE.canvas.ax.set_facecolor(self.color_fondo) 
            self.ui.wgt_GDL.canvas.ax.set_facecolor(self.color_fondo) 
            self.ui.wgt_Rest.canvas.ax.set_facecolor(self.color_fondo) 
            self.ui.wgt_porticos.canvas.ax.set_facecolor(self.color_fondo)
            self.Fn_visualizar_porticos()
            self.Fn_visualizar_gdl()
            self.Fn_visualizar_fuerzas_internas()
            self.Fn_visualizar_deformada
            #Barra principal
            #--------------------------------------------------------------------#
            cbg_mnu = "rgb(30, 40, 255)"  
            cfont_mnu = " rgb(0, 0, 0)" 
            cbg_imnu = "rgb(4, 107, 153)"  
            cfont_imnu = " rgb(0,0,0)"          
            mnu = """
            /**background-color:{} ; color: {};**/
            QMenu::item:selected [
                background-color: {};
                color:{};
            ]            
            """
            

            mnu = mnu.format(cbg_mnu,cfont_mnu, cbg_imnu,cfont_imnu)
            mnu = mnu.replace("[", "{")
            mnu = mnu.replace( "]","}")
            self.ui.menubar.setStyleSheet(mnu)
            self.ui.menubar.update()
            #Fondo principal
            #-------------------------------------------------------------------------------#
            ccb_pag = "rgb(23, 123, 189)"
            cb_paginas = """
             background-color:{} ;""".format(ccb_pag)
            self.ui.cb_paginas.setStyleSheet(cb_paginas)
            #-------------------------------------------------------------------------------#
            cbg_bar = 'rgb(4, 107, 153)'
            bar = """background-color: {};"""
            bar = bar.format(cbg_bar)
            self.ui.bar_cb_pg.setStyleSheet(bar)
            #-------------------------------------------------------------------------------#
            # Botones
            cbg_btn = "none"
            cfont = "rgb(255,255,255)"
            cbg_hv = "#0385bc"
            cbg_pres = "#049edf"
            
            stybotones ="""QPushButton[
                /* Color de fondo*//**background-color: rgb(213, 244, 230);**/
                    background-color:{} ;
                    color:{} ;
                    font: 75 14px \"Bell MT\";
                    border-radius : 4px;]
                /* Cambia color al estar sobre*/
                QPushButton:hover[
                    background-color:{} ;]
                    /* Cambia color al dar click*/
                QPushButton:pressed[
                    background-color:{};]
                """
            stybotones = stybotones.format(cbg_btn, cfont, cbg_hv, cbg_pres)
            stybotones = stybotones.replace("[", "{")
            stybotones = stybotones.replace( "]","}")
            #self.ui.btn_analizar.setStyleSheet(stybotones)
            self.ui.btn_nuevo.setStyleSheet(stybotones)
            self.ui.btn_abrir.setStyleSheet(stybotones)
            self.ui.btn_guardar.setStyleSheet(stybotones)
            self.ui.btn_fuerzas.setStyleSheet(stybotones)
            self.ui.btn_matrices.setStyleSheet(stybotones)
            self.ui.btn_inicio.setStyleSheet(stybotones)
            self.ui.btn_deformada.setStyleSheet(stybotones)
            self.ui.btn_delta_fuerza.setStyleSheet(stybotones)
            #self.ui.btn_amp_deformada.setStyleSheet(stybotones)
            
            #-------------------------------------------------------------------------------#
            cbg_tbl = "rgb(255, 255, 255)"
            cfont_tbl = "rgb(0, 0, 0)"
            cbghd_tbl = "rgb(0, 159, 195)"
            cfonthd_tbl = "rgb(0, 0, 0)"
            sfont_tbl = "12"
            sfonthd_tbl = "12"
            cborhv_tbl = "rgb(0, 255, 255)"
            cborselec_tbl = "rgb(23, 123, 189);"
            tbl = """QTableWidget[
                background-color:{} ;
                border-radius : 5px;
                color: {};
                font: {}px \"Calibri\";
                ]
                QHeaderView::section[
                    border-radius : 1px;
                    background-color: {};
                    color:{} ;
                    font: 75 {}px \"Times New Roman\";
                ]
                
                QTableWidget:hover[

                    border : 2px solid  {};]
                
                QTableWidget:item:selected:focus[
                border : 2px solid  {};
                color: {};
                
                
                    
                    ]

                """
            tbl = tbl.format(cbg_tbl,cfont_tbl,sfont_tbl, cbghd_tbl, cfonthd_tbl,sfonthd_tbl, cborhv_tbl,cborselec_tbl,cfont_tbl  )
            tbl = tbl.replace("[", "{")
            tbl = tbl.replace( "]","}")
              
            
            self.ui.tbl_Elem.setStyleSheet(tbl)
            self.ui.tbl_Nod.setStyleSheet(tbl)
            self.ui.tbl_Fuer.setStyleSheet(tbl)
            self.ui.tbl_Fuer_W.setStyleSheet(tbl)
            self.ui.tbl_Rest.setStyleSheet(tbl)
            self.ui.tbl_MKG.setStyleSheet(tbl)
            self.ui.tbl_MKGE.setStyleSheet(tbl)
            self.ui.tbl_MKL.setStyleSheet(tbl)
            self.ui.tbl_g_delta.setStyleSheet(tbl)
            self.ui.tbl_g_delta_elem.setStyleSheet(tbl)
            self.ui.tbl_propiedades.setStyleSheet(tbl)
            self.ui.tbl_vec_F.setStyleSheet(tbl)
            
            # Graficos
            #-------------------------------------------------------#
            cbg_wgt = "rgb(179, 239, 255)"
            cbor_wgt = "#ffffff"
            wgt = """/* color de fondo*/
            background-color: {};
            /*borde redondo*/
            border-radius : 10px;
            /* linea de borde*/
            border : 5px solid {};
            """.format(cbg_wgt,cbor_wgt)
        
            
            
            
            # Frames
            #------------------------------------------------------#
            cbg_frm = "rgb(4, 120, 170)"
            frm= """
            background-color: {};
            border-radius: 5px;""".format(cbg_frm)
            
            self.ui.frame_2.setStyleSheet(frm)
            self.ui.frame_3.setStyleSheet(frm)
            self.ui.frame_4.setStyleSheet(frm)
            self.ui.frame_5.setStyleSheet(frm)
            
            # Frame pagina 4
            cbg_frm = "rgb(4, 120, 170)"
            cbg_qline = "rgb(255, 255, 255)"
            cfont_label = "rgb(255, 255, 255)"
            styframe_2 = """QSlider[
            background-color: {};
            border-radius: 5px;]
            QLineEdit[
            background-color: {};
            border-radius: 5px;
            ]
            QLabel[
            color: {};
            font: 87 24px "Segoe UI Black";
            background-color: none;
            ]""".format(cbg_frm, cbg_qline, cfont_label )
            
            styframe_2 = styframe_2.replace("[", "{")
            styframe_2 = styframe_2.replace( "]","}")
            self.ui.frame_2.setStyleSheet(styframe_2)
        
        def modo_oscuro():
            # Graficos
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
            self.Fn_visualizar_porticos()
            self.Fn_visualizar_gdl()
            self.Fn_visualizar_fuerzas_internas()
            self.Fn_visualizar_deformada
            #Barra principal
            #--------------------------------------------------------------------#
            
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
            
            
            
            # mnu = """
            # QMenuBar[
            # background-color:{} ; color: {};]
            
            # QMenu::item:selected [
            #     background-color: {};
            #     color:{};
            # ]
            
            # QMenuBar::item [
            #     spacing: 3px;           
            #     padding: 2px 10px;
            #     background-color: {} ;
            #     color: {};  
            # ]
            
            # """

            # mnu = mnu.format(cbg_mnu,cfont_mnu,cbg_is,cfont_is, cbg_imnu,cfont_imnu)
            # mnu = mnu.replace("[", "{")
            # mnu = mnu.replace( "]","}")
            self.ui.menubar.setStyleSheet(mnu)
            #Fondo principal
            #--------------------------------------------------------------------#
            ccb_pag = "#111C26"
            cb_paginas = """
             background-color: {};""".format(ccb_pag)
            self.ui.cb_paginas.setStyleSheet(cb_paginas)
            # Seleccionador
            # Barra sup cambio paginas
            #--------------------------------------------------------------------#
            cbg_bar = '#111C26'
            bar = """background-color: {};"""
            bar = bar.format(cbg_bar)
            self.ui.bar_cb_pg.setStyleSheet(bar)
            
            #-------------------------------------------------------------------------------#
            # Botones
            cbg_btn = "#111c26"
            cfont = "rgb(255,255,255)"
            cbg_hv = "#1f3446"
            cbg_pres = "#385d7d"
            
            stybotones ="""QPushButton[
                /* Color de fondo*//**background-color: rgb(213, 244, 230);**/
                    background-color:{} ;
                    color:{} ;
                    font: 75 12pt \"Bell MT\";
                    border-radius : 4px;]
                /* Cambia color al estar sobre*/
                QPushButton:hover[
                    background-color:{} ;]
                    /* Cambia color al dar click*/
                QPushButton:pressed[
                    background-color:{};]
                """
            stybotones = stybotones.format(cbg_btn, cfont, cbg_hv, cbg_pres)
            stybotones = stybotones.replace("[", "{")
            stybotones = stybotones.replace( "]","}")
            # self.ui.btn_analizar.setStyleSheet(stybotones)
            self.ui.btn_nuevo.setStyleSheet(stybotones)
            self.ui.btn_abrir.setStyleSheet(stybotones)
            self.ui.btn_guardar.setStyleSheet(stybotones)
            self.ui.btn_fuerzas.setStyleSheet(stybotones)
            self.ui.btn_matrices.setStyleSheet(stybotones)
            self.ui.btn_inicio.setStyleSheet(stybotones)
            self.ui.btn_deformada.setStyleSheet(stybotones)
            self.ui.btn_delta_fuerza.setStyleSheet(stybotones)
            # self.ui.btn_amp_deformada.setStyleSheet(stybotones)
            
            # Tablas
            #--------------------------------------------------------------------#
            color_tbl = "#384D59"
            color_tbl_h = "#4D6873"  # header
            color_let= "rgb(255, 255, 255)" # color letra
            
            cbg_tbl = "#384D59"
            cfont_tbl = "rgb(255, 255, 255)"
            cbghd_tbl = "#4D6873"
            cfonthd_tbl = "rgb(255, 255, 255)"
            sfont_tbl = "10"
            sfonthd_tbl = "11"
            cborhv_tbl = "rgb(0, 255, 255)"
            cborselec_tbl = "rgb(23, 123, 189);"
            
            tbl = """QTableWidget[
                background-color:{} ;
                border-radius : 5px;
                color: {};
                font: {}pt \"Calibri\";
                ]
                QHeaderView::section[
                    border-radius : 1px;
                    background-color: {};
                    color:{} ;
                    font: 75 {}pt \"Times New Roman\";
                ]
                
                QTableWidget:hover[

                    border : 2px solid  {};]
                
                QTableWidget:item:selected:focus[
                border : 2px solid  {};
                color: {};
                    
                    ]
                

                """
            tbl = tbl.format(cbg_tbl,cfont_tbl,sfont_tbl, cbghd_tbl, cfonthd_tbl,sfonthd_tbl, cborhv_tbl,cborselec_tbl,cfont_tbl  )
            tbl = tbl.replace("[", "{")
            tbl = tbl.replace( "]","}")
            
            self.ui.tbl_Elem.setStyleSheet(tbl)
            self.ui.tbl_Nod.setStyleSheet(tbl)
            self.ui.tbl_Fuer.setStyleSheet(tbl)
            self.ui.tbl_Fuer_W.setStyleSheet(tbl)
            self.ui.tbl_Rest.setStyleSheet(tbl)
            self.ui.tbl_MKG.setStyleSheet(tbl)
            self.ui.tbl_MKGE.setStyleSheet(tbl)
            self.ui.tbl_MKL.setStyleSheet(tbl)
            self.ui.tbl_g_delta.setStyleSheet(tbl)
            self.ui.tbl_g_delta_elem.setStyleSheet(tbl)
            self.ui.tbl_propiedades.setStyleSheet(tbl)
            self.ui.tbl_vec_F.setStyleSheet(tbl)
            # Frames
            
            cbg_frm = "rgb(34, 56, 76)"
            frm= """
            background-color: {};
            border-radius: 5px;""".format(cbg_frm)
            self.ui.frame_2.setStyleSheet(frm)
            self.ui.frame_3.setStyleSheet(frm)
            self.ui.frame_4.setStyleSheet(frm)
            self.ui.frame_5.setStyleSheet(frm)
            
            
            # Graficos

            cbg_wgt = "rgb(34, 56, 76)"
            cbor_wgt = "#636363"
            wgt = """/* color de fondo*/
            background-color: {};
            /*borde redondo*/
            border-radius : 10px;
            /* linea de borde*/
            border : 2px solid {};
            """.format(cbg_wgt,cbor_wgt)

            # Frame pagina 4
            cbg_frm = "rgb(4, 120, 170)"
            cbg_qline = "#384D59"
            cfont_qline = "rgb(255, 255, 255)"
            cfont_label = "rgb(0, 0, 0)"
            styframe_2 = """QSlider[
            background-color: {};
            border-radius: 5px;]
            QLineEdit[
            background-color: {};
            color: {};
            border-radius: 5px;
            ]
            QLabel[
            color: {};
            font: 87 20pt "Segoe UI Black";
            background-color: none;
            ]"""
            styframe_2 = styframe_2.format(cbg_frm, cbg_qline, cfont_qline, cfont_label )
            
            styframe_2 = styframe_2.replace("[", "{")
            styframe_2 = styframe_2.replace( "]","}")
            self.ui.frame_2.setStyleSheet(styframe_2)
            
        if modo == "claro":
            self.tema = "rgb(213, 244, 230)"

            self.ui.tbl_Rest.update()
            modo_claro()
        if modo == "oscuro":
            modo_oscuro()
            self.tema = "#C1D4D9"
            
        self.update()
    
    def ven_creditos(self):
        self.creditos = Creditos()
        self.creditos.show()
    def ven_conversiones(self):
        self.ventana = Ui_Conversor_Unidades()
        self.ventana.show()
    # Si la extencion del archivo no concuerda con .j&y
    def ven_emerg_tipo_arch(self): 
        mensaje = QMessageBox()
        mensaje.setWindowTitle("Error de archivo")
        mensaje.setText("El arhivo que está intentando cargar\n"+ "no es compatible con ANEPY!!")
        mensaje.setIcon(QMessageBox.Critical)  
        valor = mensaje.exec_()  
    # Archivo guardado
    def ven_mensajes(self, evento): 
        mensaje = QMessageBox()
        mensaje.setWindowTitle(evento[1])
        mensaje.setText(evento[2]) #'$\U00002192$'
        if evento[0] == 0: # Archivo guardado
            mensaje.setIcon(QMessageBox.Information)
        if evento[0] == 1: # Error al abrir
            mensaje.setIcon(QMessageBox.Warning)
        valor = mensaje.exec_()
    # Cierre del software
    def closeEvent(self, evento):
        pregunta = QMessageBox.question(self, "Salir", "¿Seguro que deseas salir?", QMessageBox.Yes | QMessageBox.No)
        #pregunta.setIcon(QMessageBox.Question)
        if pregunta == QMessageBox.Yes:
            evento.accept()
        else: evento.ignore()
    def salir(self):
        self.close()
    # Manejo de archivos
    def nuevo(self):
        # Tbl elem
        self.ui.tbl_Elem.clearContents() # Se limpia la tabla
        self.ui.tbl_Elem.setRowCount(0)
        self.ui.sp_nElem.setValue(0)
        
        
        # Tbl nod
        self.ui.tbl_Nod.clearContents() # Se limpia la tabla
        self.ui.tbl_Nod.setRowCount(0)
        self.ui.sp_nNo.setValue(0)
        
        # Tbl F
        self.ui.tbl_Fuer.clearContents() # Se limpia la tabla
        self.ui.tbl_Fuer.setRowCount(0)
        self.ui.sp_nFuer.setValue(0)
        
        # Tbl Fw
        self.ui.tbl_Fuer_W.clearContents() # Se limpia la tabla
        self.ui.tbl_Fuer_W.setRowCount(0)
        self.ui.sp_nFuer_W.setValue(0)
        
        # Tbl rest
        self.ui.tbl_Rest.clearContents() # Se limpia la tabla
        self.ui.tbl_Rest.setRowCount(0)
        self.ui.sp_nRest.setValue(0)
        
        self.ui.wgt_porticos.canvas.ax.clear()
        self.ui.wgt_porticos.canvas.update()
        
        self.nombre_arch("Nuevo") # Actualiza nombre de archivo
        self.cambiarPagina("INICIO") # lleva la pantalla a inicio 

    def abrir(self, archivo = None):
        print("Here", archivo)
        # Abre el archivo
        if archivo == False: 
            archivo, _ = QFileDialog.getOpenFileName(self, "Abrir Archivo", 'C:\\Users\Estudiante\Documents\Qtdesigner\Interface grafica\Manejo de ficheros', 'Documento ANEPY (*.j&y)')
        # with open(archivo[0], 'rt') as f:
        #     datos = f.read()
        #     print(datos)
        
        # Listas parciales de almacenamiento de los datos
        datos_Elem = [] 
        datos_Nod = [] 
        datos_Fuer = [] 
        datos_FuerW = []
        datos_Rest = []
        datos_unidades = "" 
        
        
        if archivo: # Pregunta si posee una direccion

            if '.j&y' in archivo: # Si esl archivo contiene la extension .j&y
                self.nuevo() # Limpia todo las tablas
                self.nombre_arch(archivo) # Actualiza nombre de archivo
                self.cambiarPagina("INICIO") # lleva la pantalla a inicio
                self.Fn_visualizar_porticos() # Actualiza el grafico de inicio
                datos_Elem, datos_Nod, datos_Fuer, datos_FuerW, datos_Rest, datos_unidades = abir_datos(archivo)
                
                #print(datos_Rest, "##########333")
                
                # Con los datos ya obtenidos se proceden a cargarse a GUI
                
                
                # Elementos
                try: 
                    row = len(datos_Elem)
                    col = len(datos_Elem[0])
                    
                    self.ui.sp_nElem.setValue(row)

                    for i in range(row):
                        
                        self.ui.tbl_Elem.insertRow(i) # Inserta una columna en la tabla
                        for j in range(col):
                            celda = QTableWidgetItem(str(datos_Elem[i][j])) # Informacion
                            self.ui.tbl_Elem.setItem(i, j,celda ) # Agrega a la fi y col
                            self.ui.tbl_Elem.update() # Actualiza la tabla
                    """Quita el duplicado de fila"""
                    self.ui.sp_nElem.setValue(row+1)
                    self.ui.sp_nElem.setValue(row)
                    
                except IndexError:
                    mensaje = (1, "Error ", "El archivo no contiene elementos") # Tipo de notoficacion, titulo y mensaje
                    self.ven_mensajes(mensaje)
                
                # Nodos
                try:
                    row = len(datos_Nod)
                    col = len(datos_Nod[0])
                    
                    self.ui.sp_nNo.setValue(row)
                    
                    for i in range(row):
                        
                        self.ui.tbl_Nod.insertRow(i) # Inserta una columna en la tabla
                        for j in range(col):
                            celda = QTableWidgetItem(str(datos_Nod[i][j]))
                            self.ui.tbl_Nod.setItem(i, j,celda )
                            self.ui.tbl_Nod.update()
                    """Quita el duplicado de fila"""
                    self.ui.sp_nNo.setValue(row+1)
                    self.ui.sp_nNo.setValue(row)
                
                except IndexError:
                    mensaje = (1, "Error ", "El archivo no contiene nodos") # Tipo de notoficacion, titulo y mensaje
                    self.ven_mensajes(mensaje)
                
                
                # Fuerzas
                try: # Se utiliza por si no hay este tipo de datos en el portico
                    row = len(datos_Fuer)
                    col = len(datos_Fuer[0])
                    
                    self.ui.sp_nFuer.setValue(row)
                    
                    for i in range(row):
                        
                        self.ui.tbl_Fuer.insertRow(i) # Inserta una columna en la tabla
                        for j in range(col):
                            celda = QTableWidgetItem(str(datos_Fuer[i][j]))
                            self.ui.tbl_Fuer.setItem(i, j,celda )
                            self.ui.tbl_Fuer.update()
                    """Quita el duplicado de fila"""
                    self.ui.sp_nFuer.setValue(row+1)
                    self.ui.sp_nFuer.setValue(row)
                except IndexError:
                    pass
                
                # Fuerzas Distribuidas
                try:
                    
                    row = len(datos_FuerW)
                    col = len(datos_FuerW[0])
                    self.ui.sp_nFuer_W.setValue(row)
                    for i in range(row):
                        self.ui.tbl_Fuer_W.insertRow(i) # Inserta una columna en la tabla
                        for j in range(col):
                            celda = QTableWidgetItem(str(datos_FuerW[i][j]))
                            self.ui.tbl_Fuer_W.setItem(i, j, celda)
                            self.ui.tbl_Fuer_W.update()
                    """Quita el duplicado de fila"""
                    self.ui.sp_nFuer_W.setValue(row+1)
                    self.ui.sp_nFuer_W.setValue(row)
                except IndexError:
                    pass
            
                # Nodos
                try:
                    row = len(datos_Rest)
                    col = len(datos_Rest[0])

                    attr  = ['Simple', 'Articulado', 'Empotrado']
                    for i in range(row):
                        #self.ui.tbl_Rest.insertRow(i) # Inserta una columna en la tabla
                        self.ui.sp_nRest.setValue(row)
                        for j in range(col):
                                
                            celda = QTableWidgetItem(str(datos_Rest[i][j]))
                            self.ui.tbl_Rest.setItem(i, j,celda )
                                
                            comboBox = QComboBox()
                                
                            comboBox.addItems(attr)
                            comboBox.setCurrentText(str(datos_Rest[i][0]))
                            self.ui.tbl_Rest.setCellWidget(i, 0, comboBox)
                            self.ui.tbl_Rest.update()
                    # """Quita el duplicado de fila"""
                    
                except IndexError:
                    mensaje = (1, "Error ", "El archivo no contiene restricciones") # Tipo de notoficacion, titulo y mensaje
                    self.ven_mensajes(mensaje)
                
                # Unidades
                # print((datos_unidades))
                if datos_unidades == "m, KN, MPa":
                    self.ui.cb_convertir_de.setItemText(0,"m, KN, MPa")
                    self.ui.cb_convertir_de.setItemText(1,"pulg, Lb, Psi")
                elif datos_unidades == "pulg, Lb, Psi":
                    self.ui.cb_convertir_de.setItemText(1,"m, KN, MPa")
                    self.ui.cb_convertir_de.setItemText(0,"pulg, Lb, Psi")
                    
                    self.ui.cb_convertir_de.update()
                    # print("#----------------")
                    # print(len(datos_unidades))
                    
                
            else:
                self.ven_emerg_tipo_arch()
                # print("ARCHIVO NO COMPATIBLE")     
    def guardar(self):
        [tbl_Elem, tbl_Nod, tbl_Fuer, tbl_Rest,tbl_Fuer_W, nElem] = self.Fn_ExtraerDatosTablas() # Obtiene nados de Fn_ExtraerDatosTablas
        
        #opciones = QFileDialog.options()
        # opciones = 0
        # opciones |= QFileDialog.DontUseNativeDialog
        #archivo, _ =  QtWidgets.QFileDialog.getSaveFileName(self, "Guardar Archivo", 'C:\\', 'Text files (*.txt)', options = opciones)
        archivo, _ = QFileDialog.getSaveFileName(self, "Guardar Archivo", 'C:\\', 'Documento ANEPY (*.j&y)')
        
        unidades = self.ui.cb_convertir_de.currentText()
        # Eliminar multiplicacion x 1000 para convertir a KPa
        
        
        if archivo != '':
            tbl_Elem_parcial = []
            if unidades == "m, KN, MPa":
                for i in tbl_Elem:
                    # print(i)
                    elem = i[0]
                    Ni = i[1]
                    Nf = i[2]
                    b = i[3]
                    h = i[4]
                    E = i[5]/1000
                    tbl_Elem_parcial.append([elem, Ni, Nf, b, h, E])
            tbl_Elem = tbl_Elem_parcial
            guardar_datos(archivo, tbl_Elem, tbl_Nod, tbl_Fuer,tbl_Fuer_W, tbl_Rest, unidades)
            mensaje = (0, "Archivo Guardado", "Guardado¡¡") # Tipo de notoficacion, titulo y mensaje
            self.ven_mensajes(mensaje)
            self.nombre_arch(archivo)
    def arhivo_modificado(self):
        self.editado = True
    def copiar(self):
        self.copia_tbl_Elem = self.ui.tbl_Elem.selectedIndexes()
        self.copia_tbl_Nod = self.ui.tbl_Nod.selectedIndexes()
        self.copia_tbl_Fuer = self.ui.tbl_Fuer.selectedIndexes()
        self.copia_tbl_Fuer_W = self.ui.tbl_Fuer_W.selectedIndexes()
        
        
        portapapeles = self.portapapeles
        # print("pi",portapapeles.text())
       # portapapeles.clear(mode=portapapeles.Clipboard)
        portapapeles.setText("") 
        # print("po",portapapeles.text(0))
         
        # print("#########33")
        copia_texto = '' # Variable que almacena la seleccion
        
        # Tabla de elementos
        texto_1 = self.ui.tbl_Elem.selectedIndexes() # Agrega los items seleccionados en la tbl
        texto_2 = self.ui.tbl_Nod.selectedIndexes()
        texto_3 = self.ui.tbl_Fuer.selectedIndexes()
        texto_4 = self.ui.tbl_Fuer_W.selectedIndexes()
        texto_5 = self.ui.tbl_Rest.selectedIndexes()
        texto_6 = self.ui.tbl_propiedades.selectedIndexes()
        texto_7 = self.ui.tbl_MKL.selectedIndexes()
        texto_8 = self.ui.tbl_MKG.selectedIndexes()
        texto_9 = self.ui.tbl_MKGE.selectedIndexes()
        texto_10 = self.ui.tbl_vec_F.selectedIndexes()
        texto_11 = self.ui.tbl_g_delta.selectedIndexes()
        texto_12 = self.ui.tbl_g_delta_elem.selectedIndexes()
        texto_13 = self.ui.tbl_fuerzas_internas.selectedIndexes()
        
        
        def copiar_informacion(copia_texto):
            if len(texto_1): # Comprueba que se haya selecxion
                num_col = texto_1[-1].column() # numero de columnas
                for c in texto_1:
                    copia_texto += self.ui.tbl_Elem.item(c.row(), c.column()).text()# Extrae el texto de cada items
                    if c.column() == num_col:# agrega los saltos
                        copia_texto += '\n' 
                    else:
                        copia_texto += '\t'
                portapapeles.setText(copia_texto)  
                        
            elif len(texto_2):
                #(texto)
                num_col = texto_2[-1].column()
                for c in texto_2:
                    copia_texto += self.ui.tbl_Nod.item(c.row(), c.column()).text()
                    if c.column() == num_col:
                        copia_texto += '\n'
                    else:
                        copia_texto += '\t'
    
                portapapeles.setText(copia_texto)  
            
            
            elif len(texto_3):
                #print(texto)
                # print("Tabla tbl_Fuer")
                num_col = texto_3[-1].column()
                for c in texto_3:
                    copia_texto += self.ui.tbl_Fuer.item(c.row(), c.column()).text()
                    if c.column() == num_col:
                        copia_texto += '\n'
                    else:
                        copia_texto += '\t'
    
                portapapeles.setText(copia_texto)  
                        
            
            elif len(texto_4):
                #print(texto)
                num_col = texto_4[-1].column()
                for c in texto_4:
                    copia_texto += self.ui.tbl_Fuer_W.item(c.row(), c.column()).text()
                    if c.column() == num_col:
                        copia_texto += '\n'
                    else:
                        copia_texto += '\t'
    
                portapapeles.setText(copia_texto)  
            
            
            elif len(texto_5):
                #print(texto)
                num_col = texto_5[-1].column()
                for c in texto_5:
                    copia_texto += self.ui.tbl_Rest.item(c.row(), c.column()).text()
                    if c.column() == num_col:
                        copia_texto += '\n'
                    else:
                        copia_texto += '\t'
                
                portapapeles.setText(copia_texto)  
            elif len(texto_6):
                # print(texto)
                num_col = texto_6[-1].column()
                for c in texto_6:
                    copia_texto += self.ui.tbl_propiedades.item(c.row(), c.column()).text()
                    if c.column() == num_col:
                        copia_texto += '\n'
                    else:
                        copia_texto += '\t'
                portapapeles.setText(copia_texto)  
            
            elif len(texto_7):
                # print(texto)
                num_col = texto_7[-1].column()
                for c in texto_7:
                    copia_texto += self.ui.tbl_MKL.item(c.row(), c.column()).text()
                    if c.column() == num_col:
                        copia_texto += '\n'
                    else:
                        copia_texto += '\t'
                portapapeles.setText(copia_texto)
                
            elif len(texto_8):
                # print(texto)
                num_col = texto_8[-1].column()
                for c in texto_8:
                    copia_texto += self.ui.tbl_MKG.item(c.row(), c.column()).text()
                    if c.column() == num_col:
                        copia_texto += '\n'
                    else:
                        copia_texto += '\t'
                        
                portapapeles.setText(copia_texto)  
                
            elif len(texto_9):
                # print(texto)
                num_col = texto_9[-1].column()
                for c in texto_9:
                    copia_texto += self.ui.tbl_MKGE.item(c.row(), c.column()).text()
                    if c.column() == num_col:
                        copia_texto += '\n'
                    else:
                        copia_texto += '\t'
                portapapeles.setText(copia_texto)  
                
            elif len(texto_10):
                # print(texto)
                num_col = texto_10[-1].column()
                for c in texto_10:
                    copia_texto += self.ui.tbl_vec_F.item(c.row(), c.column()).text()
                    if c.column() == num_col:
                        copia_texto += '\n'
                    else:
                        copia_texto += '\t'
                portapapeles.setText(copia_texto)         
            
            elif len(texto_11):
                # print(texto)
                num_col = texto_11[-1].column()
                for c in texto_11:
                    copia_texto += self.ui.tbl_g_delta.item(c.row(), c.column()).text()
                    if c.column() == num_col:
                        copia_texto += '\n'
                    else:
                        copia_texto += '\t'
    
                portapapeles.setText(copia_texto)     
            
            elif len(texto_12):
                # print(texto)
                num_col = texto_12[-1].column()
                for c in texto_12:
                    copia_texto += self.ui.tbl_g_delta_elem.item(c.row(), c.column()).text()
                    if c.column() == num_col:
                        copia_texto += '\n'
                    else:
                        copia_texto += '\t'
                        
                portapapeles.setText(copia_texto)
            
            elif len(texto_13):
                # print(texto)
                num_col = texto_12[-1].column()
                for c in texto_13:
                    copia_texto += self.ui.tbl_fuerzas_internas.item(c.row(), c.column()).text()
                    if c.column() == num_col:
                        copia_texto += '\n'
                    else:
                        copia_texto += '\t'
                        
                portapapeles.setText(copia_texto)
            
        copiar_informacion(copia_texto = '')
        
        # Deselección  de tablas 
        self.ui.tbl_Elem.clearSelection()
        self.ui.tbl_Nod.clearSelection()
        self.ui.tbl_Fuer.clearSelection()
        self.ui.tbl_Fuer_W.clearSelection()
        self.ui.tbl_Rest.clearSelection()
        self.ui.tbl_propiedades.clearSelection()
        self.ui.tbl_MKL.clearSelection()
        self.ui.tbl_MKG.clearSelection()
        self.ui.tbl_MKGE.clearSelection()
        self.ui.tbl_vec_F.clearSelection()
        self.ui.tbl_g_delta.clearSelection()
        self.ui.tbl_g_delta_elem.clearSelection()
        self.ui.tbl_fuerzas_internas.clearSelection()
        
    def pegar(self):
        
        # Tbl Elemetos
        try:
            row = self.ui.tbl_Elem.currentRow()
            col = self.ui.tbl_Elem.currentColumn()
            ran_row = row - self.copia_tbl_Elem[0].row()
            ran_col = col - self.copia_tbl_Elem[0].column()
            
            for celda in self.copia_tbl_Elem:
                dato = QTableWidgetItem(celda.data()) # Almacena valor de la matriz
                self.ui.tbl_Elem.setItem(celda.row() + ran_row, celda.column() + ran_col, dato)
        except IndexError: pass
    
        # Tbl Nodos
        try:
        
            row = self.ui.tbl_Nod.currentRow()
            col = self.ui.tbl_Nod.currentColumn()
            ran_row = row - self.copia_tbl_Nod[0].row()
            ran_col = col - self.copia_tbl_Nod[0].column()
            
            for celda in self.copia_tbl_Nod:
                dato = QTableWidgetItem(celda.data()) # Almacena valor de la matriz
                self.ui.tbl_Nod.setItem(celda.row() + ran_row, celda.column() + ran_col, dato)
        except IndexError: pass
    
        # Tbl Fuerzas
        try:  
            row = self.ui.tbl_Fuer.currentRow()
            col = self.ui.tbl_Fuer.currentColumn()
            ran_row = row - self.copia_tbl_Fuer[0].row()
            ran_col = col - self.copia_tbl_Fuer[0].column()
            
            for celda in self.copia_tbl_Fuer:
                dato = QTableWidgetItem(celda.data()) # Almacena valor de la matriz
                self.ui.tbl_Fuer.setItem(celda.row() + ran_row, celda.column() + ran_col, dato)
        except IndexError: pass
            
        # Tbl Fuerzas W
        try:  
            row = self.ui.tbl_Fuer_W.currentRow()
            col = self.ui.tbl_Fuer_W.currentColumn()
            ran_row = row - self.copia_tbl_Fuer_W[0].row()
            ran_col = col - self.copia_tbl_Fuer_W[0].column()
            
            for celda in self.copia_tbl_Fuer_W:
                dato = QTableWidgetItem(celda.data()) # Almacena valor de la matriz
                self.ui.tbl_Fuer_W.setItem(celda.row() + ran_row, celda.column() + ran_col, dato)
        except IndexError: pass
        # print("Pegado")
    # Muestra nombre de archivo en interfaz
    def nombre_arch(self, direc):
        if direc == "Inicializador":
            self.ui.label_archivo.setText("Archivo: Inicializador" )
        elif direc == "Nuevo":
            self.ui.label_archivo.setText("Archivo: Introduce y Guarda los datos" )
            
        else:
            nombre = path.split(direc)[1]
            self.ui.label_archivo.setText("Archivo: "+ nombre )
            
    def Fn_manual_de_uso(self):
        manual = 'MANUAL_DE_USO_DEL_SOFTWARE_ANEPY.pdf'
        os.system(manual)
    def Fn_Sistema_unidades(self):
        sistema_unidades = self.ui.cb_convertir_de.currentText()
        # print(sistema_unidades)
        if sistema_unidades == "m, KN, MPa":
            # Tbl elementos
            self.ui.lb_tbl_elem_B.setText("[m]")
            self.ui.lb_tbl_elem_B.setAlignment(Qt.AlignCenter)
            self.ui.lb_tbl_elem_h.setText("[m]")
            self.ui.lb_tbl_elem_h.setAlignment(Qt.AlignCenter)
            self.ui.lb_tbl_elem_E.setText("[Mpa]")
            self.ui.lb_tbl_elem_E.setAlignment(Qt.AlignCenter)
            # Tbl nodos
            self.ui.lb_tbl_nod_cx.setText("[m]")
            self.ui.lb_tbl_nod_cx.setAlignment(Qt.AlignCenter)
            self.ui.lb_tbl_nod_cy.setText("[m]")
            self.ui.lb_tbl_nod_cy.setAlignment(Qt.AlignCenter)
            # Tbl fuerzas
            self.ui.lb_tbl_f_fx.setText("[KN]")
            self.ui.lb_tbl_f_fx.setAlignment(Qt.AlignCenter)
            self.ui.lb_tbl_f_fy.setText("[KN]")
            self.ui.lb_tbl_f_fy.setAlignment(Qt.AlignCenter)
            self.ui.lb_tbl_f_m.setText("[KN-m]")
            self.ui.lb_tbl_f_m.setAlignment(Qt.AlignCenter)
            # Tbl fuerzas distribuidas
            self.ui.lb_tbl_fw_wi.setText("[KN/m]")
            self.ui.lb_tbl_fw_wi.setAlignment(Qt.AlignCenter)
            self.ui.lb_tbl_fw_wf.setText("[KN/m]")
            self.ui.lb_tbl_fw_wf.setAlignment(Qt.AlignCenter)
            
        elif sistema_unidades == "pulg, Lb, Psi":
            # Tbl elementos
            self.ui.lb_tbl_elem_B.setText("[pulg]")
            self.ui.lb_tbl_elem_B.setAlignment(Qt.AlignCenter)
            self.ui.lb_tbl_elem_h.setText("[pulg]")
            self.ui.lb_tbl_elem_h.setAlignment(Qt.AlignCenter)
            self.ui.lb_tbl_elem_E.setText("[Psi]")
            self.ui.lb_tbl_elem_E.setAlignment(Qt.AlignCenter)
            # Tbl nodos
            self.ui.lb_tbl_nod_cx.setText("[pulg]")
            self.ui.lb_tbl_nod_cx.setAlignment(Qt.AlignCenter)
            self.ui.lb_tbl_nod_cy.setText("[pulg]")
            self.ui.lb_tbl_nod_cy.setAlignment(Qt.AlignCenter)
            # Tbl fuerzas
            self.ui.lb_tbl_f_fx.setText("[Lb]")
            self.ui.lb_tbl_f_fx.setAlignment(Qt.AlignCenter)
            self.ui.lb_tbl_f_fy.setText("[Lb]")
            self.ui.lb_tbl_f_fy.setAlignment(Qt.AlignCenter)
            self.ui.lb_tbl_f_m.setText("[Lb-pulg]")
            self.ui.lb_tbl_f_m.setAlignment(Qt.AlignCenter)
            # Tbl fuerzas distribuidas
            self.ui.lb_tbl_fw_wi.setText("[Lb/pulg]")
            self.ui.lb_tbl_fw_wi.setAlignment(Qt.AlignCenter)
            self.ui.lb_tbl_fw_wf.setText("[Lb/pulg]")
            self.ui.lb_tbl_fw_wf.setAlignment(Qt.AlignCenter)
        self.update()
    
    # Manejo de tablas de datos
    def AgregarRenglonSinCombo(self, var):
        if var == 'E':
            val = self.ui.sp_nElem.value() # Se obtiene el valor del spinbox de tbl_elementos
            self.ui.tbl_Elem.setRowCount(val) # Se aumenta las filas con val
            for i in range(val):# Cambia el valor de los elementos de forma automatica
                celda = QTableWidgetItem(str(i+1))
                self.ui.tbl_Elem.setItem(i, 0, celda)
            self.ui.tbl_Elem.update() # Se actualiza la tabla 
        
        elif var == 'N':
            val = self.ui.sp_nNo.value() # Se obtiene el valor del spinbox  de tbl_nodos
            self.ui.tbl_Nod.setRowCount(val) # Se aumenta las filas con val
            for i in range(val): # Cambia el valor de los nodos de forma automatica
                celda = QTableWidgetItem(str(i+1))
                self.ui.tbl_Nod.setItem(i, 0, celda)
            self.ui.tbl_Nod.update() # Se actualiza la tabla
            
        elif var == 'F':
            val = self.ui.sp_nFuer.value() # Se obtiene el valor del spinbox  de tbl_fuerzas concentradas
            self.ui.tbl_Fuer.setRowCount(val) # Se aumenta las filas con val
            self.ui.tbl_Fuer.update() # Se actualiza la tabla
        
        elif var == 'FW':
            val = self.ui.sp_nFuer_W.value() # Se obtiene el valor del spinbox  de tbl_fuerzas distribuidas
            self.ui.tbl_Fuer_W.setRowCount(val) # Se aumenta las filas con val
            self.ui.tbl_Fuer_W.update() # Se actualiza la tabla  
    def AgregarRenglonConCombo(self, var):
        if var == 'R':
            val = self.ui.sp_nRest.value() # Se obtiene el valor del spinbox
            self.ui.tbl_Rest.setRowCount(val)
            
            tipos  = ['Simple', 'Articulado', 'Empotrado'] # Tpos de apoyos
            
            # Introducir ComboBox
            for i in range(val):
                self.comboBox = QComboBox()
                self.comboBox.addItems(tipos)
                color_tema =self.tema
                #self.comboBox.setStyleSheet("background-color: ;")
                
                self.ui.tbl_Rest.setCellWidget(i, 0, self.comboBox)
                self.ui.tbl_Rest.update()
    def Fn_ElementoComboBox (self):
        #Datos de tablas
        [tbl_Elem, tbl_Nod, tbl_Fuer, tbl_Rest,tbl_Fuer_W, nElem] = self.Fn_ExtraerDatosTablas() # Obtiene nados de Fn_ExtraerDatosTablas 
        
        # Agregando elementos a combobox de barras o elementos
        
        for i in range(nElem):
            index = self.ui.cb_elemento.findText(str(tbl_Elem[i][0])) #Extrae indices o elementos
            #Evita que los elementos se dupliquen cada vez que se cambie y abra la vantana
            self.ui.cb_elemento.removeItem(index)#
            self.ui.cb_elemento.addItem(str(tbl_Elem[i][0])) 

    # Cambiar paginas
    def cambiarPagina(self, val):
        
        if val == "INICIO": # Introducir datos
            self.ui.stackedWidget.setCurrentWidget(self.ui.pagina_1)
          
        elif val == "MATRICES DE RIGIDEZ":
            self.ui.stackedWidget.setCurrentWidget(self.ui.pagina_2)
            # Llamando funcion 
            self.Fn_ElementoComboBox()#***********************
            self.Fn_visualizar_gdl()
                
        elif val == "DESPLAZAMIENTOS-FUERZAS":
            self.ui.stackedWidget.setCurrentWidget(self.ui.pagina_3)
            self.Fn_visualizar_fuerzas_internas()
        
        elif val == "DEFORMADA":
            self.ui.stackedWidget.setCurrentWidget(self.ui.pagina_4)
            self.Fn_visualizar_deformada(0)
        elif val == "FUERZAS":
            self.ui.stackedWidget.setCurrentWidget(self.ui.pagina_5)
            self.Fn_visualizar_fuerzas_internas()
        
    # Extaccion de datos de tablas
    def Fn_ExtraerDatosTablas(self):
    
    # Diccionarios de elementos
        # Tabla de elementos
        tbl_Elem = []
        num_elem_tbl = self.ui.sp_nElem.value() # Obtenemos el numero de elementos
        elem  = 0
        for i in range(num_elem_tbl):
            try:
                elem = int(self.ui.tbl_Elem.item(i,0).text()) #Se extrae el elemento ingresado en la ITF
                Ni = int(self.ui.tbl_Elem.item(i,1).text())
                Nf = int(self.ui.tbl_Elem.item(i,2).text())
                b = round(float(self.ui.tbl_Elem.item(i,3).text()),self.redon)
                h = round(float(self.ui.tbl_Elem.item(i,4).text()),self.redon)
                sistama_unidades = self.ui.cb_convertir_de.currentText()
                if sistama_unidades == "m, KN, MPa":
                    E = round(float(self.ui.tbl_Elem.item(i,5).text()),self.redon)*1000 # Convierte en Mpa
                else:
                    E = round(float(self.ui.tbl_Elem.item(i,5).text()),self.redon)
                tbl_Elem.append([elem, Ni, Nf, b, h, E])
            except ValueError: #or AttributeError:
                T_msj = "Error de Entrada"
                msj = """Cambiar a numero enteros Elemento: {} y Nodos
                                  """.format(elem)
                                  
                tipo = 1
                event = (tipo, T_msj, msj)
                self.ven_mensajes(event)
                tbl_Elem = 0
                break

        # Tabla de nodos
        tbl_Nod = []
        num_elem_tbl = self.ui.sp_nNo.value() # Obtenemos el numero de elementos
        
        for i in range(num_elem_tbl):
            try:
                nodo = int(self.ui.tbl_Nod.item(i,0).text()) #Se extrae el elemento ingresado en la ITF
                cx = round(float(self.ui.tbl_Nod.item(i,1).text()),self.redon)
                cy = round(float(self.ui.tbl_Nod.item(i,2).text()),self.redon)
                tbl_Nod.append([nodo, cx, cy])
            except ValueError or AttributeError:
                T_msj = "Error de Entrada"
                msj = """Cambiar a  enteros los Nodos
                                  """
                tipo = 1
                event = (tipo, T_msj, msj)
                self.ven_mensajes(event)
                tbl_Nod = 0                
            
            
        # Tabla de fuerzas
        tbl_Fuer = []
        num_elem_tbl = self.ui.sp_nFuer.value() # Obtenemos el numero de elementos
        try:
            for i in range(num_elem_tbl):
                nodo = int(self.ui.tbl_Fuer.item(i,0).text()) #Se extrae el elemento ingresado en la ITF
                fx = round(float(self.ui.tbl_Fuer.item(i,1).text()),self.redon)
                fy = round(float(self.ui.tbl_Fuer.item(i,2).text()),self.redon)
                Mz = round(float(self.ui.tbl_Fuer.item(i,3).text()),self.redon)
                tbl_Fuer.append([nodo, fx, fy, Mz])
        except ValueError or AttributeError:
            T_msj = "Error de Entrada"
            msj = """Cambiar a  enteros los Nodos
                              """
            tipo = 1
            event = (tipo, T_msj, msj)
            self.ven_mensajes(event)
            tbl_Fuer = 0
            
        # Tabla de restricciones en nodos
        tbl_Rest = []
        num_elem_tbl = self.ui.sp_nRest.value() # Obtenemos el numero de elementos
        
        for i in range(num_elem_tbl):
            try:
                tipo = str(self.ui.tbl_Rest.cellWidget(i,0).currentText()) #Se extrae el elemento ingresado en la ITF
                nodo = int(self.ui.tbl_Rest.item(i,1).text())
                tbl_Rest.append([tipo, nodo])
                #print(tbl_Rest)
            except ValueError or AttributeError:
                T_msj = "Error de Entrada"
                msj = """Cambiar a  enteros los Nodos
                                  """
                tipo = 1
                event = (tipo, T_msj, msj)
                self.ven_mensajes(event)
                tbl_Rest = 0
         # Tabla de fuerzas distribuidas
        tbl_Fuer_W = []
        num_elem_tbl = self.ui.sp_nFuer_W.value() # Obtenemos el numero de elementos
        #print("Num", num_elem_tbl)
        
        for i in range(num_elem_tbl):
            try:
                elemento = int(self.ui.tbl_Fuer_W.item(i,0).text()) #Se extrae el elemento ingresado en la ITF
                wi = round(float(self.ui.tbl_Fuer_W.item(i,1).text()),self.redon)
                wf = round(float(self.ui.tbl_Fuer_W.item(i,2).text()),self.redon)
                tbl_Fuer_W.append([elemento, wi, wf])
            except ValueError or AttributeError:
                T_msj = "Error de Entrada"
                msj = """Cambiar a  enteros los Elementos
                                  """
                tipo = 1
                event = (tipo, T_msj, msj)
                self.ven_mensajes(event)
                tbl_Fuer_W = 0
        #print("TW", tbl_Fuer_W)
        
        return tbl_Elem, tbl_Nod, tbl_Fuer, tbl_Rest, tbl_Fuer_W, len(tbl_Elem)
    
    # Diccionario de entradas
    def Fn_diccionario_elementos(self, tbl_Elem):
        diccionarioE = {}
    
        for i in range(len(tbl_Elem)):
            Elem = tbl_Elem[i][0]
            Ni = tbl_Elem[i][1]
            Nf = tbl_Elem[i][2]
            b = tbl_Elem[i][3]
            h = tbl_Elem[i][4]
            E = tbl_Elem[i][5]   
            diccionarioE[Elem] = [Ni, Nf, b, h, E]
        return diccionarioE
    def Fn_diccionario_nodos(self, tbl_Nod):
        diccionarioN = {}
        #DICCIONARIOS DE NODOS Y COORDENADAS
        for i in range(len(tbl_Nod)):
            Nod = tbl_Nod[i][0]
            xi = tbl_Nod[i][1]
            yi = tbl_Nod[i][2]
            diccionarioN[Nod] = [xi, yi]
        return diccionarioN
    def Fn_diccionario_fuerzas(self, tbl_Fuer):
        dic_tf = {}
        for i in range(len(tbl_Fuer)):
            Nod = tbl_Fuer[i] #Escoge el nodo en funcion de la cantidad de tbl_Fuer
            fx = Nod[1] # Escoge Fx 
            fy = Nod[2] # Escoge Fy 
            Mz = Nod[3] # Escoge Mz 
            dic_tf[Nod[0]] = [fx, fy, Mz]
        return dic_tf
    def Fn_diccionario_gdl(self, tbl_Nod):
        
        GDL_nodos = {}
        for i in range(len(tbl_Nod)):
        
            nodo = tbl_Nod[i][0]
            gdl = [nodo*3-3, nodo*3-2, nodo*3-1]
            GDL_nodos[nodo] = gdl
        return GDL_nodos
    #def Fn_diccionario_fuerzas_W(self, tbl_Fuer_W):
    
    # ANALSISI ESTRUCTURAL
    def Fn_propiedades_elementos(self, tbl_Elem,tbl_Nod, diccionarioN):
        elementos = []
        diccionarioN = self.Fn_diccionario_nodos(tbl_Nod)
        for i in range(len(tbl_Elem)):
            b = tbl_Elem[i][3]
            h = tbl_Elem[i][4]
            E = tbl_Elem[i][5]
            Elem = tbl_Elem[i][0]
            #print(Elem)
            try:
                Ni = tbl_Elem[i][1]
                Nf = tbl_Elem[i][2]
                conexion = [Elem, Ni, Nf]
                cxi = diccionarioN[Ni][0]
                cyi = diccionarioN[Ni][1]
                cxf = diccionarioN[Nf][0]
                cyf = diccionarioN[Nf][1]
            except KeyError:
                T_msj = "Error de Entrada"
                msj = """Falta un nodo en la tabla"""
                tipo = 1
                event = (tipo, T_msj, msj)
                self.ven_mensajes(event)
                self.no_visualizar_portico = True
            try:    
                barra = Propiedades_elemento(Elem,b, h, E, cxi, cyi, 
                                             cxf, cyf, conexion)
                elementos.append(barra) # Almacena elemento
                self.no_visualizar_portico = False
            except ZeroDivisionError:
                T_msj = "Error de Entrada"
                msj = """Coordenada de nodo :{} repetida
                                  """.format(Ni)
                tipo = 1
                event = (tipo, T_msj, msj)
                self.ven_mensajes(event)
                self.no_visualizar_portico = True
        return elementos
    
    def Fn_visualizar_porticos(self):
        [tbl_Elem, tbl_Nod, tbl_Fuer, tbl_Rest,tbl_Fuer_W,nElem] = self.Fn_ExtraerDatosTablas() # Obtiene nados de Fn_ExtraerDatosTablas
        diccionarioN = self.Fn_diccionario_nodos(tbl_Nod)
        diccionarioE = self.Fn_diccionario_elementos(tbl_Elem)
        #print(diccionarioE)
        dic_tf =  self.Fn_diccionario_fuerzas(tbl_Fuer) # Obtiene datos de Fn_diccionario_fuerzas
        elementos = self.Fn_propiedades_elementos(tbl_Elem, tbl_Nod, diccionarioN)
        
        #print("here", tbl_Fuer_W)
        
        self.ploteo = self.ui.wgt_porticos.canvas
        self.ploteo.ax.clear()
        
        plt = self.ploteo.ax
        
        #######################
        #Delimitacion del dibujo
        ######################
        xmax = 0
        ymax = 0

        for key in diccionarioN:
            
            valor_x = diccionarioN[key][0]
            valor_y = diccionarioN[key][1]
                
            if xmax < valor_x:
                xmax = valor_x
                
            if ymax < valor_y:
                ymax = valor_y
                
        ##############################
        # DIBUJO DE BARRAS PORTICO
        #############################
        
        for i in range(len(tbl_Elem)):
            #i = 1
            id_elem = tbl_Elem[i][0]
            Ni = tbl_Elem[i][1]
            Nf = tbl_Elem[i][2]
            #print(Nf)
            xi = diccionarioN[Ni][0]
            yi = diccionarioN[Ni][1]
            xf = diccionarioN[Nf][0]
            yf = diccionarioN[Nf][1]
            #print(Ele,"({},{}),({},{})".format (xi, yi, xf, yf))
            #plt.plot([xi, xf], [yi, yf])
            
            
            #self.ploteo.ax.scatter([xi, xf], [yi, yf],marker = 'o', color = "y", s = 150) #Dibujo de nodos
            xm =xi+(xf-xi)/2 +xmax*0.001 # Posicion del dexto respecto a x xmedio
            ym = yi + (yf-yi)/2-ymax*0.05 # Posicion del dexto respecto a y ymedio
            
            #print('xi: ',xi,'yi: ',yi,'xf: ', xf,'yf: ',yf,'xm: ',xm, 'ym: ',ym)    
            plt.plot([xi, xf], [yi, yf],color = self.color_lementos,linewidth=2)
            plt.text(xm, ym, id_elem, color = self.color_letras, size = 10 )
            
        ###########################
        # Dibujando fuerzas 
        ###########################

        for i in range(len(tbl_Fuer)):
            
            fuerzas = tbl_Fuer[i]
            #print("fuerza: ", fuerzas)
            nodo = fuerzas[0]
            #print("nodo: ", nodo)
            cx = diccionarioN[nodo][0]
            cy = diccionarioN[nodo][1]

            fx = fuerzas[1]
            fy = fuerzas[2]
            Mz = fuerzas[3]
            
            # Grafica fuerza en x
            if fx > 0 :
                ####PENDIENTE POR INVESTICAR ANNOTATE
                co = self.color_x
                self.ploteo.ax.plot([cx-xmax*0.03],[cy], marker = '$\U00002192$', ms = 20, c =co) #
                self.ploteo.ax.text(cx-xmax*0.15, cy+ymax*0.04, str(fx), color = co, size =  self.tamaño_letra )
            elif fx < 0:
                co = self.color_x
                self.ploteo.ax.plot([cx-xmax*0.03],[cy], marker = '$\U00002190$', ms = 20, c =co) #
                self.ploteo.ax.text(cx-xmax*0.15, cy+ymax*0.04, str(fx), color = co, size =  self.tamaño_letra )  
                    
                
            # Grafica fuerza en y
            if fy > 0:
                co = self.color_y
                self.ploteo.ax.plot([cx- xmax*0.01],[cy+ymax*0.08], marker = '$\U00002191$', ms = 20, c =co) #U+2193
                self.ploteo.ax.text(cx + xmax*0.01, cy+ymax*0.1, str(fy), color = co, size =  self.tamaño_letra )
            if fy<0:
                co = self.color_y
                self.ploteo.ax.plot([cx- xmax*0.01],[cy+ymax*0.08], marker = '$\U00002193$', ms = 20, c =co) #U+2193
                self.ploteo.ax.text(cx + xmax*0.01, cy+ymax*0.1, str(fy), color = co, size =  self.tamaño_letra ) 
            
            # Grafica M en z
            if Mz > 0  or Mz < 0:
                co = self.color_z
                self.ploteo.ax.plot([cx+ xmax*0.02],[cy- ymax*0.05], marker = '$\U000021BA$', ms = 20, c = co) #U+21BA
                self.ploteo.ax.text(cx+ xmax*0.05, cy - ymax*0.2, str(Mz), color = co, size =  self.tamaño_letra )
        
        ###########################
        # Dibujando fuerzas W
        ###########################
        def dibuajar_w_rectangualar(cxi, cyi, cxf, cyf, W, ang):
            W_dibujo = 0
            L1= []
            L2 = []
            p0 = []
            p1 = []
            p2 = []
            # print("ang",ang)
            co = "b" #self.color_x
            cotext = "#1098ad"
            # print("##3 ",elem, ang, W)
            # print("cxi=",cxi)
            Lm = 0 # L/2
            texto = round(W, 2)
            if ang == 0:
                Lm = abs(cxf-cxi)/2
                W_dibujo = cyi+ymax*0.05
                # sentido de la carga
                cx_t = cxi + Lm
                cy_t = W_dibujo+0.005*ymax
                
                if W > 0: # Cargas positivas
                    W_dibujo = cyi-ymax*0.15
                    cx_t = cxi + Lm 
                    cy_t = W_dibujo*0.905
                p0 = [cxi,cyi]
                p1 = [cxi,W_dibujo]
                p2 = [cxf, W_dibujo]
                p3 = [cxf, cyf]
                self.ploteo.ax.text(cx_t, cy_t, str(texto), color = cotext, size =  self.tamaño_letra )
            
            elif abs(ang) == 90:
                Lm = abs(cyf-cyi)/2
                W_dibujo = cxi + xmax*0.13
                if ang == 90:
                    cx_t = W_dibujo
                    cy_t = cyi + Lm     
                else:
                    cx_t = W_dibujo
                    cy_t = cyi - Lm
                if W > 0: 
                    W_dibujo = cxi - xmax*0.13
                p0 = [cxi,cyi]
                p1 = [W_dibujo,cyi]
                p2 = [W_dibujo, cyf]
                p3 = [cxf, cyf]
                self.ploteo.ax.text(cx_t, cy_t, str(texto), color = co, size =  self.tamaño_letra )
                
            elif abs(ang) > 0 and abs(ang) <90:
                b = cxf - cxi
                a = cyf - cyi
                L = sqrt(a**2 + b**2)
                Lm = L/2
                W_dibujo_i = cyi + ymax*0.13
                W_dibujo_f = cyf + ymax*0.13
                cx_t = cxi + Lm*0.65
                cy_t = W_dibujo_i + (W_dibujo_i+W_dibujo_f)/2
                if W > 0: 
                    W_dibujo_i = cyi - ymax*0.13
                    W_dibujo_f = cyf - ymax*0.13
                    cx_t = cxi + Lm*0.65
                    cy_t = W_dibujo_i + (W_dibujo_i+W_dibujo_f)/2
                p0 = [cxi,cyi]
                p1 = [cxi, W_dibujo_i]
                p2 = [cxf, W_dibujo_f]
                p3 = [cxf, cyf]
                self.ploteo.ax.text(cx_t, cy_t, str(texto), color = co, size =  self.tamaño_letra )
                
                
            L1 = [[p0[0],p1[0]], [p0[1],p1[1]]]
                  
            L2 =  [[p1[0],p2[0]],[p1[1],p2[1]]]
                  
            L3 = [[p2[0],p3[0]],[p2[1],p3[1]]]
            
            self.ploteo.ax.plot(L1[0], L1[1], c =co, linewidth = 1) #
            self.ploteo.ax.plot(L2[0], L2[1], c =co,linewidth = 1)
            self.ploteo.ax.plot(L3[0], L3[1],c =co,linewidth = 1)
            
            yi = 0
            for i in range(10):
                # Angulo del elemento = 0
                if ang == 0:
                    L = Lm*2
                    s = L/10
                    x = cxi+s*i
                    #xf = L2[0][1]

                    self.ploteo.ax.plot([x,x], L1[1], c =co,linewidth = 1)
                # Angulo del elemento = 0
                elif ang == 90:
                    L = Lm*2
                    s = L/10
                    y = cyi+s*i
                    #print(s, y, L1[0])
                    self.ploteo.ax.plot(L1[0], [y, y], c = co,linewidth = 1)
                elif ang == -90:
                    L = Lm*2
                    s = L/10
                    y = cyi-s*i
                    #print(s, y, L1[0])
                    if W>0:
                        self.ploteo.ax.plot(L1[0], [y, y], c = co,linewidth = 1)
                    if W<0:
                        self.ploteo.ax.plot([cxi,W_dibujo], [y, y], c = co,linewidth = 1)
                    
                    
                elif abs(ang) > 0 and abs(ang)< 90:
                    L = abs(cxf-cxi)
                    
                    s = L/10
                    x = cxi + s*i
                    if i != 0:
                        
                        if W < 0:
                            yi = yi + a*s/b
                            yf = W_dibujo_i + yi  
                        else: 
                            yi = yi + a*s/b
                            yf = yi + W_dibujo_i
                        print(yi)
                        self.ploteo.ax.plot([x,x], [yi,yf], c =co,linewidth = 1)
                    
        def dibuajar_w_triangular(cxi, cyi, cxf, cyf, Wi, Wf, ang):
            co = "b" #self.color_x
            cotext = "#1098ad"
            L1= []
            L2 = []
            p0 = []
            p1 = []
            p2 = []
            m = 0
            texto = 0
            # Dibujo carga decreciente
            if abs(Wi) > 0:
                texto = round(Wi, 2)
                
                # Angulo del elemento = 0
                if ang == 0:
                    Wi_dibujo = cyi + ymax*0.15
                    cx_t = cxi
                    cy_t = Wi_dibujo*1.02
                    if Wi > 0: # sentido de la carga
                        Wi_dibujo = cyi - ymax*0.15
                        cx_t = cxi
                        cy_t = Wi_dibujo*0.85
                    Wf_dibujo = cyf
                    p0 = [cxi,cyi]
                    p1 = [cxi,Wi_dibujo]
                    p2 = [cxf, Wf_dibujo]
                    # pendiente
                    m = -((Wf_dibujo-Wi_dibujo)/(cxf-cxi))
                    self.ploteo.ax.text(cx_t, cy_t*1.02, str(texto), color = cotext, size =  self.tamaño_letra )
                
                # Angulo del elemento = 90
                elif abs(ang) == 90:
                    Wi_dibujo = cxi + xmax*0.15
                    
                    cx_t = Wi_dibujo*1.02
                    cy_t = cyi
                    if Wi > 0: # sentido de la carga
                        Wi_dibujo = cxi - xmax*0.15
                        cx_t = Wi_dibujo*0.7
                        cy_t = cyi
                    Wf_dibujo = cxf
                    p0 = [cxi,cyi]
                    p1 = [Wi_dibujo, cyi]
                    p2 = [cxf, cyf]
                    # pendiente
                    m = -((Wf_dibujo-Wi_dibujo)/(cyf-cyi))
                    self.ploteo.ax.text(cx_t, cy_t, str(texto), color = co, size =  self.tamaño_letra )
                
                #----------------------------------------
                if abs(ang) > 0 and abs(ang) <90:
                    Wi_dibujo = cyi + ymax*0.15
                    cx_t = cxi
                    cy_t = Wi_dibujo*1.02
                    if Wi > 0: # sentido de la carga
                        Wi_dibujo = cyi - ymax*0.15
                        cx_t = cxi
                        cy_t = Wi_dibujo*0.85
                    Wf_dibujo = cyf
                    p0 = [cxi,cyi]
                    p1 = [cxi,Wi_dibujo]
                    p2 = [cxf, Wf_dibujo]
                    # pendiente
                    m_d = ((Wf_dibujo-Wi_dibujo)/(cxf-cxi))
                    # print("md",m_d)
                    
                    self.ploteo.ax.text(cx_t, cy_t*1.02, str(texto), color = co, size =  self.tamaño_letra )
                
                
            # Dibujo carga creciente
            else:
                texto = round(Wf, 2)
                # Angulo del elemento = 0
                if ang == 0:
                    Wi_dibujo = cyi
                    Wf_dibujo = cyf + ymax*0.15
                    
                    # sentido de la carga
                    cx_t = cxf*1.01
                    cy_t = Wf_dibujo*1.02
                    
                    if Wf > 0: 
                        Wf_dibujo = cyf - ymax*0.15
                        cx_t = cxf*1.01
                        cy_t = Wf_dibujo*1.02
                    p0 = [cxi,cyi]
                    p1 = [cxf,Wf_dibujo]
                    p2 = [cxf, cyf]
                    # pendiente
                    m = ((Wf_dibujo-Wi_dibujo)/(cxf-cxi))
                    
                    self.ploteo.ax.text(cx_t, cy_t, str(texto), color = co, size =  self.tamaño_letra ) # Dibuja texto
                # Angulo del elemento = 0
                elif abs(ang) == 90:
                    Wi_dibujo = cxi 
                    Wf_dibujo = cxf + xmax*0.15
                    # coordenadas de texto 
                    cx_t = Wf_dibujo*0.9
                    cy_t = cyf*1.01
                    
                    # sentido de la carga
                    if Wf > 0: 
                        Wf_dibujo = cxf - xmax*0.15
                        cx_t = Wf_dibujo*0.751
                        cy_t = cyf*0.82

                    p0 = [cxi,cyi]
                    p1 = [Wf_dibujo, cyf]
                    p2 = [cxf, cyf]
                    # pendiente
                    m = -((Wf_dibujo-Wi_dibujo)/(cyf-cyi))
                    
                    self.ploteo.ax.text(cx_t, cy_t, str(texto), color = co, size =  self.tamaño_letra )
                    
                if abs(ang) > 0 and abs(ang) <90:
                    Wf_dibujo = cyf + ymax*0.15
                    cx_t = cxf
                    cy_t = Wf_dibujo*1.02
                    if Wf > 0: # sentido de la carga
                        Wf_dibujo = cyf - ymax*0.15
                        cx_t = cxf
                        cy_t = Wf_dibujo*0.85
                    Wi_dibujo = cyi
                    print(Wf_dibujo)
                    p0 = [cxi,cyi]
                    p1 = [cxf,Wf_dibujo]
                    p2 = [cxf, cyf]
                    # pendiente
                    m_d = ((Wf_dibujo-Wi_dibujo)/(cxf-cxi))
                    
                    self.ploteo.ax.text(cx_t, cy_t*1.02, str(texto), color = co, size =  self.tamaño_letra )
                
            # Dibuja cargas W
            L1 = [[p0[0],p1[0]], [p0[1],p1[1]]]
            L2 =  [[p1[0],p2[0]],[p1[1],p2[1]]]
            self.ploteo.ax.plot(L1[0], L1[1], c =co, linewidth = 1) #
            self.ploteo.ax.plot(L2[0], L2[1], c =co,linewidth = 1)
            
            # Distribucion
            
            y_base = 0
            for i in range(10):
                L = cxf-cxi
                s = round(L/10,4)
                #-------------------------------------
                # Angulo del elemento = 0
                if ang ==0:
                    x = cxi + s*i
                    
                    # Dibujo carga decreciente
                    if abs(Wi) > 0:
                        y = Wi_dibujo - m*x
                      
                        self.ploteo.ax.plot([x, x], [cyi, y], c = co,linewidth = 1)
                        #print(Wi_dibujo, x, y, m)
                    # Dibujo carga creciente
                    else:
                        y = Wi_dibujo + m*x
                        self.ploteo.ax.plot([x, x], [cyi, y], c = co,linewidth = 1)
                        #print(x, y, m)
                #-----------------------------------
                # Angulo del elemento = 90
                elif abs(ang) == 90:
                    L = cyf-cyi
                    s = round(L/10,4)
                    y = cyi + s*i
                    #print(cxi, s)
                    # Dibujo carga decreciente
                    if abs(Wi) > 0: # Comparacion de magnitud
                        x = Wi_dibujo - m*y
                            
                        self.ploteo.ax.plot([cxi, x], [y, y], c = co,linewidth = 1)
                        #print(Wi_dibujo, x, y, m)
                    # Dibujo carga decreciente
                    else: 
                        x = Wi_dibujo - m*y
                        # Cargas en (sentido) positivo
                        self.ploteo.ax.plot([cxi, x], [y, y], c = co,linewidth = 1)
                        #print(x, y, m)
                #--------------------------------------------
                if abs(ang) > 0 and abs(ang) <90:
                   
                    x = cxi + s*i
                    
                    # Dibujo carga decreciente
                    if Wi < 0:
                        
                        a = (cyf-cyi)
                        b = (cxf-cxi)
                        m = a/b
                        yn = m_d*s*i
                        yi = cyi + m*s*i
                        if i == 0: # altura de referencia para sumar con yn
                            y_base = yi + Wi_dibujo
                            
                        yf = y_base + yn
                        #yf = yf-Wi_dibujo
                        #yf = cyi + +s*(cyf-(cyi+Wi_dibujo))/(cxf-cxi)
                        self.ploteo.ax.plot([x, x], [yi, yf], c = co,linewidth = 1)
                        #print(Wi_dibujo, x, y, m)
                    # Dibujo carga creciente
                    else:
                        a = (cyf-cyi)
                        b = (cxf-cxi)
                        m = a/b
                        yn = m_d*s*i
                        yi = cyi + m*s*i
                        if i == 0: # altura de referencia para sumar con yn
                            y_base = yi - Wi_dibujo
                            
                        yf = y_base + yn
                        #yf = yf-Wi_dibujo
                        #yf = cyi + +s*(cyf-(cyi+Wi_dibujo))/(cxf-cxi)
                        self.ploteo.ax.plot([x, x], [yi, yf], c = co,linewidth = 1)

        #----------------------------------------------------------
        def dibuajar_w_trapezoidal(cxi, cyi, cxf, cyf, Wi, Wf):
            co = "b" #self.color_x
            cotext = "#1098ad"
            L1= []
            L2 = []
            p0 = []
            p1 = []
            p2 = []
            m = 0
            texto = 0
            Wi_dibujo = 0
            Wf_dibujo = 0
            # print(Wi, Wf)
            if abs(Wi) > abs(Wf):
                texto_1 = Wi
                texto_2 = Wf
                if ang == 0:
                    Wi_dibujo = cyi + ymax*0.15
                    Wf_dibujo = cyf + ymax*0.10
                    p0 = [cxi,cyi]
                    p1 = [cxi,Wi_dibujo]
                    p2 = [cxf, Wf_dibujo]
                    p3 = [cxf, cyf]
                    # pendiente
                    m = ((Wf_dibujo-Wi_dibujo)/(cxf-cxi))
                    self.ploteo.ax.text(cxi, Wi_dibujo*1.02, str(texto_1), color = cotext, size =  self.tamaño_letra )
                    self.ploteo.ax.text(cxf, Wf_dibujo*1.02, str(texto_2), color = cotext, size =  self.tamaño_letra )
                # Angulo del elemento = 90
                elif abs(ang) == 90:
                    Wi_dibujo = cxi + xmax*0.15
                    Wf_dibujo = cyf + ymax*0.10
                    
                    cx_t = Wi_dibujo*1.02
                    cy_t = cyi
                    if Wi > 0: # sentido de la carga
                        Wi_dibujo = cxi - xmax*0.15
                        cx_t = Wi_dibujo*0.7
                        cy_t = cyi
                    Wf_dibujo = cxf
                    p0 = [cxi,cyi]
                    p1 = [cxi,Wi_dibujo]
                    p2 = [cxf, Wf_dibujo]
                    p3 = [cxf, cyf]
                    # pendiente
                    m = -((Wf_dibujo-Wi_dibujo)/(cyf-cyi))
                    self.ploteo.ax.text(cx_t, cy_t, str(texto), cotext = co, size =  self.tamaño_letra )
                
            else:
                texto_1 = Wi
                texto_2 = Wf
                if ang ==0:
                    Wi_dibujo = cyi + ymax*0.10
                    Wf_dibujo = cyf + ymax*0.15
                    p0 = [cxi,cyi]
                    p1 = [cxi,Wi_dibujo]
                    p2 = [cxf, Wf_dibujo]
                    p3 = [cxf, cyf]
                    m = ((Wf_dibujo-Wi_dibujo)/(cyf-cyi))
                    
                elif abs(ang) == 90:
                    Wi_dibujo = cxi + xmax*0.10
                    Wf_dibujo = cxf + xmax*0.15
                    if (Wi_dibujo and Wf_dibujo) ==0:
                        Wi_dibujo = cxi - ymax*0.10
                        Wf_dibujo = cxf - ymax*0.15
                    
                    cx_t = Wi_dibujo*0.2
                    cy_t = cyi
                    if Wi > 0: # sentido de la carga
                        Wi_dibujo = cxi - xmax*0.15
                        Wf_dibujo = cxi - xmax*0.25
                        if (Wi_dibujo and Wf_dibujo) == 0:
                            Wi_dibujo = cxi - ymax*0.0010
                            Wf_dibujo = cxf - ymax*0.0015
                        cx_t = Wi_dibujo*0.7
                        cy_t = cyi
                    # print(Wi_dibujo, Wf_dibujo)
                    p0 = [cxi,cyi]
                    p1 = [Wi_dibujo, cyi]
                    p2 = [Wf_dibujo ,cyf]
                    p3 = [cxf,cyf]
                    # print(p0)
                    # print(p1)
                    # print(p2)
                    # print(p3)
                    # pendiente
                    m = ((Wf_dibujo-Wi_dibujo)/(cyf-cyi))
                    
                    self.ploteo.ax.text(Wi_dibujo, cyi, str(texto_1), color = cotext, size =  self.tamaño_letra ) # Dibuja texto
                    self.ploteo.ax.text(Wf_dibujo, cyf*1.02, str(texto_2), color = cotext, size =  self.tamaño_letra ) # Dibuja texto
            
            # Dibuja cargas W
            L1 = [[p0[0],p1[0]], [p0[1],p1[1]]]
            L2 =  [[p1[0],p2[0]],[p1[1],p2[1]]]
            L3 =  [[p2[0],p3[0]],[p2[1],p3[1]]]
            # print(L1)
            # print(L3)
            self.ploteo.ax.plot(L1[0], L1[1], c =co, linewidth = 1) #
            self.ploteo.ax.plot(L2[0], L2[1], c =co,linewidth = 1)
            self.ploteo.ax.plot(L3[0], L3[1], c =co,linewidth = 1)
            
            # Distribucion
            
            for i in range(10):
                
                #print(cxi, s)
                if ang == 0:
                    L = abs(cxf-cxi)
                    s = round(L/10,4)
                    x = cxi + s*i
                    if abs(Wi) > abs(Wi):
                        y = Wi_dibujo - m*x
                        self.ploteo.ax.plot([x, x], [cyi, y], c =co,linewidth = 1)
                        # print(x, y, m)
                    else:
                        y = Wi_dibujo + m*x
                        self.ploteo.ax.plot([x, x], [cyi, y], c =co,linewidth = 1)
                elif ang == 90:
                    L = abs(cyf-cyi)
                    s = round(L/10,4)
                    Ly = s*i
                    y = cyi + s*i
                    w = Wi_dibujo + m*s*i
                    # print("w: ",w)
                    self.ploteo.ax.plot([cxi, w], [y, y], c =co,linewidth = 1) 
                    
                elif ang == -90:
                    L = abs(cyf-cyi)
                    s = round(L/10,4)
                    y = cyf + s*i
                    self.ploteo.ax.plot([cxf, x], [y, y], c =co,linewidth = 1) 
          
        for i in range(len(tbl_Fuer_W)):
            
            fuerzas = tbl_Fuer_W[i]
            #print(fuerzas)
            elem = fuerzas[0]
            #print(fuerzas)
            Ni =  diccionarioE[elem][0]
            Nf =  diccionarioE[elem][1]
            #print("nodo: ", nodo)
            cxi = diccionarioN[Ni][0]
            cyi = diccionarioN[Ni][1]
            cxf = diccionarioN[Nf][0]
            cyf = diccionarioN[Nf][1]

            Wi = fuerzas[1]
            Wf = fuerzas[2]
            
            ang = 0
            try:
                ang = atan((cyf - cyi)/(cxf - cxi))*180/pi
            except ZeroDivisionError:
                # angulo = 90
                
                if cyi > cyf:
                    ang = -90 # Indica que si se traza el sistema de coordenadas en el Ni el elemento se desarrolla hacia abajo del eje x por ende genera un angulo de -90
                else: 
                    ang = 90
            
            # Llama funciones - Grafica fuerza W
            # Rectangular
            if Wi == Wf :
                # print("Rectangular")
                W = Wi
                dibuajar_w_rectangualar(cxi, cyi, cxf, cyf, W, ang)
            elif abs(Wi) > 0 and abs(Wf) == 0 or abs(Wi) == 0 and abs(Wf) > 0:
                # print("Triangular")
                dibuajar_w_triangular(cxi, cyi, cxf, cyf, Wi, Wf, ang)
            
            elif abs(Wf) > abs(Wi) or abs(Wf) < abs(Wi) and abs(Wf) !=0 and abs(Wi) !=0:
                # print("Trapezoidal")
                dibuajar_w_trapezoidal(cxi, cyi, cxf, cyf, Wi, Wf)
            
            
        #########################
        # Dibujo de  nodos
        #########################
        for i in range(len(tbl_Nod)):
            nodo = tbl_Nod[i][0]
            cx = diccionarioN[nodo][0]
            cy = diccionarioN[nodo][1]
            
            for rest in tbl_Rest:# Se recorreran los nodos restringidos para no dibujarlos
                self.color_l_nodos = "#808080"
                if nodo != rest[1]:
                    plt.plot(cx, cy,self.color_l_nodos,marker = "o", ms = 6)
                    plt.text(cx+xmax*0.015, cy+ymax*0.02, str(nodo), color = "k", size = 10 )
               
        
        #########################
        # Dibujo de apoyos nodos
        #########################
        for i in range(len(tbl_Rest)):
            nodo = tbl_Rest[i][1]
            rst = tbl_Rest[i][0]
            cx = diccionarioN[nodo][0]
            cy = diccionarioN[nodo][1]
            if rst == "Empotrado":
                plt.plot(cx, cy, marker = '$\U000025AC$', ms = 20, c ="r")
            elif rst == "Articulado" :
                plt.plot(cx, cy,"^b", ms = 12)
            elif rst == "Simple" :
                plt.plot(cx, cy,"og", ms = 10)
             
        # Max Ejes x y Y
        plt.axis([-0.30 * xmax,1.35 * xmax, -0.25 * ymax,1.25 * ymax])# Limitando el eje x
        # Maximixar espacio
        #self.ploteo.fig.subplots_adjust(0, 0, 1, 1)
        

        self.ploteo.draw()
    def Fn_visualizar_gdl(self):
        
        
        [tbl_Elem, tbl_Nod, tbl_Fuer, tbl_Rest,tbl_Fuer_W, nElem] = self.Fn_ExtraerDatosTablas() # Obtiene nados de Fn_ExtraerDatosTablas 
            
        #print(tbl_Nod)
           
        diccionarioN = self.Fn_diccionario_nodos(tbl_Nod) # Obtiene datos de Fn_diccionario_nodos
        dic_tf =  self.Fn_diccionario_fuerzas(tbl_Fuer) # Obtiene datos de Fn_diccionario_fuerzas
        
        dic_gdl = self.Fn_diccionario_gdl(tbl_Nod)
        
        self.ploteo = self.ui.wgt_GDL.canvas # Widget
        self.ui.wgt_GDL.canvas.update()
        self.ploteo.ax.clear()
            
        plt = self.ploteo.ax
        
        
        
        #######################
        #Delimitacion del dibujo
        ######################
        xmax = 0
        ymax = 0
       
        for clave in diccionarioN:
            
            valor_x = diccionarioN[clave][0]
            valor_y = diccionarioN[clave][1]
            # Maximos
            if xmax < valor_x:
                xmax = valor_x
                
            if ymax < valor_y:
                ymax = valor_y
                
            
            ##############################
            # DIBUJO DE BARRAS PORTICO
            #############################
            
        for i in range(len(tbl_Elem)):
            #i = 1
            Elemento = tbl_Elem[i][0]
            Ni = tbl_Elem[i][1]
            Nf = tbl_Elem[i][2]
            #print(Nf)
            xi = diccionarioN[Ni][0]
            yi = diccionarioN[Ni][1]
            xf = diccionarioN[Nf][0]
            yf = diccionarioN[Nf][1]
            #print(Ele,"({},{}),({},{})".format (xi, yi, xf, yf))e
            #plt.plot([xi, xf], [yi, yf])
            xm =xi+(xf-xi)/2 +xmax*0.001 # Posicion del dexto respecto a x xmedio
            ym = yi + (yf-yi)/2+ymax*0.01 # Posicion del dexto respecto a y ymedio
            
            #print('xi: ',xi,'yi: ',yi,'xf: ', xf,'yf: ',yf,'xm: ',xm, 'ym: ',ym)    
            plt.plot([xi, xf], [yi, yf],color = self.color_lementos,linewidth=2)
            plt.text(xm, ym, Elemento, color = self.color_letras, size = self.tamaño_letra )
            #self.ploteo.ax.scatter([xi, xf], [yi, yf],marker = 'o', color = "y", s = 150) #Dibujo de nodos
      
            #########################
            # Dibujo de apoyos nodos
            #########################
            for i in range(len(tbl_Rest)):
                nodo = tbl_Rest[i][1]
                rst = tbl_Rest[i][0]
                xi = diccionarioN[nodo][0]
                yi = diccionarioN[nodo][1]
                if rst == "Empotrado":
                    plt.plot([xi],[yi], marker = '$\U000025AC$', ms = 20, c ="r")
                elif rst == "Articulado" :
                    plt.plot([xi],[yi],"^b", ms = 12)
                elif rst == "Simple" :
                    plt.plot([xi],[yi],"og", ms = 10)
          
            ###########################
            # Dibujando fuerzas
            ###########################
            
            
            
            
            def mostrar_grados(direccion, cx, cy, cz,grado):
                size_marker = 15
                
                if direccion == "dx":
                    
                    co = "#14C38E"
                    plt.plot([cx-xmax*0.03],[cy], marker = '$\U00002192$', ms = size_marker, c =co) #
                    plt.text(cx-xmax*0.06, cy+ymax*0.04, str(grado), color = co, size = self.tamaño_letra )
                    
                if direccion == "dy":
                    co = "#1A3C40"
                    plt.plot([cx- xmax*0.01],[cy+ymax*0.08], marker = '$\U00002193$', ms = size_marker, c ="#1A3C40") #U+2193
                    plt.text(cx + xmax*0.01, cy+ymax*0.08, str(grado), color = co, size = self.tamaño_letra ) 
               
                if direccion == "dz":
                    co = "#2F8F9D"
                    plt.plot([cx+ xmax*0.02],[cy- ymax*0.05], marker = '$\U000021BA$', ms = size_marker, c = co) #U+21BA
                    plt.text(cx+ xmax*0.05, cy - ymax*0.05, str(grado), color = co, size = self.tamaño_letra )

                
            for i in range(len(tbl_Nod)):
                
                nodo = tbl_Nod[i][0]
                #print("nodo: ", nodo)
                c_x = diccionarioN[nodo][0]
                c_y = diccionarioN[nodo][1]
                c_z = sqrt(c_x**2+c_y**2)
                
                direc_x = 'dx'
                direc_y ='dy'
                direc_z = 'dz'
                gdl_x = dic_gdl[nodo][0]
                gdl_y = dic_gdl[nodo][1]
                gdl_z = dic_gdl[nodo][2]
                
                mostrar_grados(direc_x, c_x, c_y,c_z, gdl_x)
                mostrar_grados(direc_y, c_x, c_y,c_z, gdl_y)
                mostrar_grados(direc_z, c_x, c_y,c_z, gdl_z)
                
                
            """Crear el id del elemento en el grafico"""
            # Max Ejes x y Y
            plt.axis([-0.25 * xmax,1.25 * xmax, -0.25 * ymax,1.25 * ymax])# Limitando el eje x
            # Maximixar espacio
            self.ploteo.fig.subplots_adjust(0, 0, 1, 1)

            self.ploteo.draw()
    def Fn_visualizar_fuerzas_internas(self):
        
        [tbl_Elem, tbl_Nod, tbl_Fuer, tbl_Rest,tbl_Fuer_W,nElem] = self.Fn_ExtraerDatosTablas() # Obtiene nados de Fn_ExtraerDatosTablas
        diccionarioN = self.Fn_diccionario_nodos(tbl_Nod)
        diccionarioE = self.Fn_diccionario_elementos(tbl_Elem)
        # dic_tf =  self.Fn_diccionario_fuerzas(tbl_Fuer) # Obtiene datos de Fn_diccionario_fuerzas
        
        elementos = self.Fn_propiedades_elementos(tbl_Elem, tbl_Nod, diccionarioN)
        
        # Wigt Graficador
        self.ploteo = self.ui.wgt_FIE.canvas # Widget
        self.ploteo.ax.clear()
        plt = self.ploteo.ax

        # cxi = elemento.cxi
        # cyi = elemento.cyi
        # cxf = elemento.cxf
        # cyf = elemento.cyf
        # ang = elemento.ang
        # Elemento con sus fuerzas
        fxi = 0
        fvi = 0
        Mzi = 0
        fxf = 0
        fvf = 0
        Mzf = 0
        
        #######################
        #Delimitacion del dibujo
        ######################
        xmax = 0
        ymax = 0
       
        for clave in diccionarioN:
            
            valor_x = diccionarioN[clave][0]
            valor_y = diccionarioN[clave][1]
            # Maximos
            if xmax < valor_x:
                xmax = valor_x
                
            if ymax < valor_y:
                ymax = valor_y
        
        # Grafica de elemento
        for i in range(len(tbl_Elem)):
            #i = 1
            Elemento = tbl_Elem[i][0]
            Ni = tbl_Elem[i][1]
            Nf = tbl_Elem[i][2]
            #print(Nf)
            xi = diccionarioN[Ni][0]
            yi = diccionarioN[Ni][1]
            xf = diccionarioN[Nf][0]
            yf = diccionarioN[Nf][1]
            #print(Ele,"({},{}),({},{})".format (xi, yi, xf, yf))e
            #plt.plot([xi, xf], [yi, yf])
            xm =xi+(xf-xi)/2 +xmax*0.001 # Posicion del dexto respecto a x xmedio
            ym = yi + (yf-yi)/2+ymax*0.01 # Posicion del dexto respecto a y ymedio
            
            #print('xi: ',xi,'yi: ',yi,'xf: ', xf,'yf: ',yf,'xm: ',xm, 'ym: ',ym)    
            plt.plot([xi, xf], [yi, yf],color = self.color_lementos, linewidth=2)
            plt.text(xm, ym, Elemento, color = self.color_letras, size = 10 )
            #self.ploteo.ax.scatter([xi, xf], [yi, yf],marker = 'o', color = "y", s = 150) #Dibujo de nodos
        
        # Grafico nodos

        for i in range(len(tbl_Nod)):
            nodo = tbl_Nod[i][0]
            cx = diccionarioN[nodo][0]
            cy = diccionarioN[nodo][1]
            
            for rest in tbl_Rest:# Se recorreran los nodos restringidos para no dibujarlos
                
                if nodo != rest[1]:
                    plt.plot([cx],[cy],"ok", ms = 6)
                    plt.text(cx+xmax*0.012, cy+ymax*0.01, str(nodo), color = "green", size = self.tamaño_letra )
        

        # Dibujo de apoyos nodos
        self.nod_rest = []
        for i in range(len(tbl_Rest)):
            nodo = tbl_Rest[i][1]
            self.nod_rest.append(nodo)
            rst = tbl_Rest[i][0]
            xi = diccionarioN[nodo][0]
            yi = diccionarioN[nodo][1]
            if rst == "Empotrado":
                plt.plot([xi],[yi], marker = '$\U000025AC$', ms = 20, c ="r")
            elif rst == "Articulado" :
                plt.plot([xi],[yi],"^b", ms = 12)
            elif rst == "Simple" :
                plt.plot([xi],[yi],"og", ms = 10)
        
        # Grafico de fuerzas
        i_d = ""
        def mostrar_fuerzas(direccion, cx, cy, cz,fuerza):
            size_marker = 15 # Tamaño de marcadores
                
            if direccion == "fx":
                co = self.color_x
                if fuerza>0:
                    
                    # Cambia la direccion de la representacion de la fuerza en x
                    # for i in range(self.nod_rest):
                    #     nodo = i
                    #     cx_n = diccionarioN[nodo][0]
                    #     cy_n = diccionarioN[nodo][1]
                        
                    plt.plot([cx-xmax*0.03],[cy], marker = '$\U00002192$', ms = size_marker, c =co) #
                    
                    plt.text(cx-xmax*0.10, cy+ymax*0.025, str(fuerza)+i_d, color = co, size = self.tamaño_letra )
                    
                elif fuerza<0:
                    
                    plt.plot([cx-xmax*0.03],[cy], marker = '$\U00002190$', ms = size_marker, c =co) #
                    plt.text(cx-xmax*0.10, cy+ymax*0.025, str(fuerza)+i_d, color = co, size = self.tamaño_letra )
                
                
            if direccion == "fv":
                co = self.color_y
                if fuerza<0:
                    plt.plot([cx- xmax*0.01],[cy+ymax*0.08], marker = '$\U00002193$', ms = size_marker, c ="#1A3C40") #U+2193
                    plt.text(cx + xmax*0.01, cy+ymax*0.08, str(fuerza)+i_d, color = co, size = self.tamaño_letra ) 
                    
                elif fuerza>0:

                    plt.plot([cx- xmax*0.01],[cy+ymax*0.08], marker = '$\U00002191$', ms = size_marker, c ="#1A3C40") #U+2193
                    plt.text(cx + xmax*0.01, cy+ymax*0.08, str(fuerza)+i_d, color = co, size = self.tamaño_letra ) 
                    
            if direccion == "Mz":
                co = self.color_z
                if fuerza<0:
                    plt.plot([cx+ xmax*0.025],[cy- ymax*0.05], marker = '$\U000021BA$', ms = size_marker, c = co) #U+21BA
                    plt.text(cx+ xmax*0.04, cy - ymax*0.037, str(fuerza)+i_d, color = co, size = self.tamaño_letra )
                elif fuerza>0:
                    plt.plot([cx+ xmax*0.025],[cy- ymax*0.05], marker = '$\U000021BB$', ms = size_marker, c = co) #U+21BA
                    plt.text(cx+ xmax*0.04, cy - ymax*0.037, str(fuerza)+i_d, color = co, size = self.tamaño_letra )

        coord = [] # coordenadas repetidas
        nod = [] # nodod repetidos
        for i in range(len(elementos)):
            #print(elementos)
            elemento = elementos[i]
            i_d = " E"+str(elemento.Elem)
            ang = elemento.ang
            try:
                fuerzas = self.Fuerzas_internas[i]
                # print(fuerzas)
                if abs(ang) == 90:
                    fxi = round(fuerzas[1][0],3)
                    fvi = round(fuerzas[0][0],3)
                    Mzi = round(fuerzas[2][0],3)
                    fxf = round(fuerzas[4][0],3)
                    fvf = round(fuerzas[3][0],3)
                    Mzf = round(fuerzas[5][0],3)
                else:
                    fxi = round(fuerzas[0][0],3)
                    fvi = round(fuerzas[1][0],3)
                    Mzi = round(fuerzas[2][0],3)
                    fxf = round(fuerzas[3][0],3)
                    fvf = round(fuerzas[4][0],3)
                    Mzf = round(fuerzas[5][0],3)
                
            except TypeError:
                pass
                # print("Ejecute analizar en la primera pagina")
            Ni = elemento.conex[1]
            Nf = elemento.conex[2]
            cxi = elemento.cxi
            cyi = elemento.cyi
            czi = sqrt(cxi**2+cyi**2)
            cxf = elemento.cxf
            cyf = elemento.cyf
            czf = sqrt(cxf**2+cyf**2)
            
            
            
            fuerza_x = 'fx'
            fuerza_y ='fv'
            Momento_z = 'Mz'
            # gdl_x = dic_gdl[nodo][0]
            # gdl_y = dic_gdl[nodo][1]
            # gdl_z = dic_gdl[nodo][2]
            
            
            
            if elemento.conex[1] not in coord:
                mostrar_fuerzas(fuerza_x, cxi, cyi,czi, fxi)
                mostrar_fuerzas(fuerza_y, cxi, cyi,czi,fvi)
                mostrar_fuerzas(Momento_z, cxi, cyi,czi, Mzi)
            else:# Cuantas veces se repite
                nod.append(Ni)
                cxi_1 = cxi
                cyi = cyi + ymax*0.085*nod.count(Ni)
                cxi = cxi + xmax*0.035*nod.count(Ni)
                mostrar_fuerzas(Momento_z, cxi, cyi,czi, Mzi)
                mostrar_fuerzas(fuerza_x, cxi_1, cyi,czi, fxi)
                mostrar_fuerzas(fuerza_y, cxi_1, cyi,czi,fvi)
            
            if elemento.conex[2] not in coord:
                mostrar_fuerzas(fuerza_x, cxf, cyf,czf, fxf)
                mostrar_fuerzas(fuerza_y, cxf, cyf,czf,fvf)
                mostrar_fuerzas(Momento_z, cxf, cyf,czf, Mzf)
            else:
                nod.append(Nf)
                cxf_1 = cxf
                cyf = cyf + ymax*0.085*nod.count(Nf)
                cxf = cxf + xmax*0.035*nod.count(Nf)
                mostrar_fuerzas(Momento_z, cxf, cyf,czf, Mzf)
                #----------------------------
                mostrar_fuerzas(fuerza_x, cxf_1, cyf,czf, fxf)
                mostrar_fuerzas(fuerza_y, cxf_1, cyf,czf,fvf)
                
                
            coord.append(elemento.conex[1])
            coord.append(elemento.conex[2])

            
            
        """Crear el id del elemento en el grafico"""
        # Max Ejes x y Y
        plt.axis([-0.25 * xmax,1.25 * xmax, -0.25 * ymax,1.25 * ymax])# Limitando el eje x
        # Maximixar espacio
        self.ploteo.fig.subplots_adjust(0, 0, 1, 1)

        self.ploteo.draw()          
    def Fn_visualizar_deformada(self, f_amp):
        if self.activar_mef:
            try:
                elementos, Desplazamientos_elementos,dic_sub_nodos, tbl_Elem, tbl_Rest, diccionarioN = self.elementos_MEF, self.Desplazamientos_elementos_MEF,self.dic_sub_nodos_MEF, self.tbl_Elem_MEF, self.tbl_Rest_MEF, self.diccionarioN_MEF
                
                # Wigt Graficador
                self.ploteo_d = self.ui.wgt_deformada.canvas # Widget
                
                self.ploteo_d.ax.clear()
                plt = self.ploteo_d.ax 
                fig, ax = plt_o.subplots()
                plt_2 = ax
                datos_deformada = Deformada(elementos, Desplazamientos_elementos,f_amp)
                
                """ Para graficar se utilizan los datos originales sin MEF """
                # Delimitacion del dibujo
                xmax = 0
                ymax = 0
                for clave in diccionarioN:
                    
                    valor_x = diccionarioN[clave][0]
                    valor_y = diccionarioN[clave][1]
                    # Maximos
                    if xmax < valor_x:
                        xmax = valor_x
                        
                    if ymax < valor_y:
                        ymax = valor_y
                        
                # Grafica elementos
                for i in range(len(tbl_Elem)):
                    #i = 1
                    Ele = tbl_Elem[i][0]
                    Ni = tbl_Elem[i][1]
                    Nf = tbl_Elem[i][2]
                    #print(Ni)
                    #print(Nf)
                    xi = diccionarioN[Ni][0]
                    yi = diccionarioN[Ni][1]
                    xf = diccionarioN[Nf][0]
                    yf = diccionarioN[Nf][1]
                    #print(Ele,"({},{}),({},{})".format (xi, yi, xf, yf))
                    #plt.plot([xi, xf], [yi, yf])
                    
                    plt.plot([xi, xf], [yi, yf],color = self.color_lementos, linewidth=2)
                    plt_2.plot([xi, xf], [yi, yf],color = self.color_lementos, linewidth=2)
                    #plt.plot([xi, xf], [yi, yf],marker = "o",color = "#55aaff",  ms=10, )
                    
                # Grafica apoyos
             
                for i in range(len(tbl_Rest)):
                    nodo = tbl_Rest[i][1]
                    rst = tbl_Rest[i][0]
                    xi = diccionarioN[nodo][0]
                    yi = diccionarioN[nodo][1]
                    if rst == "Empotrado":
                        plt.plot([xi],[yi], marker = '$\U000025AC$', ms = 20, c ="r")
                        plt_2.plot([xi],[yi], marker = '$\U000025AC$', ms = 20, c ="r")
                    elif rst == "Articulado" :
                        plt.plot([xi],[yi],"^b", ms = 12)
                        plt_2.plot([xi],[yi],"^b", ms = 12)
                    elif rst == "Simple" :
                        plt.plot([xi],[yi],"og", ms = 10)
                        plt_2.plot([xi],[yi],"og", ms = 10)
                
                # Grafica deformada
                for i in range(len(elementos),):
                    Ni = elementos[i].conex[1]
                    Nf = elementos[i].conex[2]
                    
                    xi = datos_deformada.dic_deformada[Ni][0]
                    yi = datos_deformada.dic_deformada[Ni][1]
                    xf = datos_deformada.dic_deformada[Nf][0]
                    yf = datos_deformada.dic_deformada[Nf][1]
                    
                    #print(Ele,"({},{}),({},{})".format (xi, yi, xf, yf))
                    plt.plot([xi, xf], [yi, yf]) # Lineas con colores diferentes
                    plt_2.plot([xi, xf], [yi, yf]) # Lineas con colores diferentes
                    #plt.plot([xi, xf], [yi, yf],"b--",linewidth=2)
                    # plt.plot([xi, xf], [yi, yf],marker = "o",color = "#55aaff",  ms=1, ) # Para mostrar subdivisiones
                    #plt.plot([xi],[yi],"og", ms = 4)  # Nodos
                    
                    # Max Ejes x y Y
                    # Coreccion de desplazamiento en apoyo simple
                    
        
                # co = "#14C38E"
                # plt.plot([cx-xmax*0.03],[cy], marker = '$\U00002192$', ms = 20, c =co) #
                # plt.text(cx-xmax*0.06, cy+ymax*0.04, str(grado), color = co, size = 12 )
                
                # Obtiene nodos principales
                nodos_principales = []
                for i in range(len(tbl_Elem)):
                    Ni = tbl_Elem[i][1]
                    Nf = tbl_Elem[i][2]
                    
                    if Ni not in nodos_principales:
                        nodos_principales.append(Ni)
                        
                    if Nf not in nodos_principales:
                        nodos_principales.append(Nf)
                        
                for i in range(len(nodos_principales)):
                    nodo = nodos_principales[i]
                    sub_nodo = nodo_ireal(diccionarioN, dic_sub_nodos, nodo)
                    desplazamientos =  datos_deformada.Desplazamientos[sub_nodo]
                    cxi = datos_deformada.dic_deformada[sub_nodo][0]
                    cyi = datos_deformada.dic_deformada[sub_nodo][1]
                    ux = 0
                    uy = 0
                    gz = 0
                    
                    for i in range(len(tbl_Rest)):
                        nodo_rest = tbl_Rest[i][1]
                        rst = tbl_Rest[i][0]
                        xi = diccionarioN[nodo][0]
                        yi = diccionarioN[nodo][1]
                        sub_nodo = nodo_ireal(diccionarioN, dic_sub_nodos, nodo_rest)
                        if rst == "Simple" and nodo_rest == sub_nodo:
                           
                            ux = desplazamientos[0][0]
                            uy = desplazamientos[0][0]
                            gz = desplazamientos[2][0]
                            print("uy", uy)
                        else:
                    
                            ux = desplazamientos[0][0]
                            uy = desplazamientos[1][0]
                            gz = desplazamientos[2][0]
                    
                    # print(nodos_principales, ",", nodo, len(nodos_principales), nodos_principales[i])
                    #co = "#14C38E"
                    #plt.plot([cx-xmax*0.03],[cy], marker = '$\U00002192$', ms = 20, c =co) #
                    plt.text(cxi-xmax*0.06, cyi+ymax*0.010, "Ux"+str(nodo)+"= "+str(format(ux,'.4E')), color = self.color_x, size = self.tamaño_letra )
                    plt.text(cxi-xmax*0.06, cyi-ymax*0.030, "Uy"+str(nodo)+"= "+str(format(uy,'.4E')), color = self.color_y, size = self.tamaño_letra )
                    plt.text(cxi-xmax*0.06, cyi-ymax*0.065, "$\U000003B8$"+"z"+str(nodo)+"= "+str(format(gz,'.4E')), color = self.color_z, size = self.tamaño_letra )
                    
                    plt_2.text(cxi-xmax*0.06, cyi+ymax*0.010, "Ux"+str(nodo)+"= "+str(format(ux,'.4E')), color = self.color_x, size = self.tamaño_letra )
                    plt_2.text(cxi-xmax*0.06, cyi-ymax*0.030, "Uy"+str(nodo)+"= "+str(format(uy,'.4E')), color = self.color_y, size = self.tamaño_letra )
                    plt_2.text(cxi-xmax*0.06, cyi-ymax*0.065, "$\U000003B8$"+"z"+str(nodo)+"= "+str(format(gz,'.4E')), color = self.color_z, size = self.tamaño_letra )
                
                
                plt.axis([-0.25 * xmax,1.25 * xmax, -0.25 * ymax,1.25 * ymax])# Limitando el eje x
                plt_2.axis([-0.25 * xmax,1.25 * xmax, -0.25 * ymax,1.25 * ymax])# Limitando el eje x
                    # Maximixar espacio
                self.ploteo_d.fig.subplots_adjust(0, 0, 1, 1)
        
                self.ploteo_d.draw() 
            except TypeError:
                pass
    
    # AMPLIFICACIONES DE LA DEFORMADA
    def Fn_amplificar_deformada_2(self):
        # Write line
        self.f_amp = float(self.ui.inline_amplificacion.text())
        # print(type(self.f_amp),self.f_amp*2)
        self.Fn_visualizar_deformada(self.f_amp)
        
    def Fn_amplificar_deformada_1(self):
        # Slider de elementos
        self.ui.slider_zoom_defor.setMaximum(1000)
        
        self.ui.slider_zoom_defor.setMinimum(0)
        
        self.f_amp = self.ui.slider_zoom_defor.value()
        self.Fn_visualizar_deformada(self.f_amp)
        
    def guardado_parcial_MEF(self):
        #Almacena de manera parcial los valores de la deformada
        self.elementos_MEF, self.Desplazamientos_elementos_MEF,self.dic_sub_nodos_MEF, self.tbl_Elem_MEF, self.tbl_Rest_MEF, self.diccionarioN_MEF = self.Fn_MEF()
    
    def Fn_elementos(self):
        [tbl_Elem, tbl_Nod, tbl_Fuer, tbl_Rest,tbl_Fuer_W,nElem] = self.Fn_ExtraerDatosTablas() 
        diccionarioN = self.Fn_diccionario_nodos(tbl_Nod)
        diccionarioE = self.Fn_diccionario_elementos(tbl_Elem)
        # dic_tf =  self.Fn_diccionario_fuerzas(tbl_Fuer) # Obtiene datos de Fn_diccionario_fuerzas
        
        elementos = self.Fn_propiedades_elementos(tbl_Elem, tbl_Nod, diccionarioN)
        
        self.ui.cb_elemento.update()
        val = int(self.ui.cb_elemento.currentText())

        for i in range(nElem):

            if val ==  elementos[i].Elem:
                MK_local = elementos[i].KL
                MK_globale = elementos[i].KG
                L = elementos[i].L
                A = elementos[i].A
                ModE = elementos[i].E
                I = elementos[i].I
                Ang = elementos[i].ang

    
        # 1 propiedades
        Datos = [L, A, ModE, I, Ang]
        self.ui.tbl_propiedades.clearContents() # Se limpia la tabla
        self.ui.tbl_propiedades.setRowCount(0) # Cantidad de filas pasa a 0
        self.ui.cb_elemento.update()
        val = int(self.ui.cb_elemento.currentText())
        for i in range(nElem):
            if val ==  elementos[i].Elem:
                MK_local = elementos[i].KL
                MK_globale = elementos[i].KG
                L = elementos[i].L
                A = elementos[i].A
                ModE = elementos[i].E
                I = elementos[i].I
                Ang = elementos[i].ang

    
        # 1 propiedades
        Datos = [L, A, ModE, I, Ang]
        self.ui.tbl_propiedades.clearContents() # Se limpia la tabla
        self.ui.tbl_propiedades.setRowCount(0) # Cantidad de filas pasa a 0

        for n in range(1):
            self.ui.tbl_propiedades.insertRow(n)
            for j in range(5):
                #print(round(Datos[j],4))
                d = QTableWidgetItem(str(round(Datos[j],4))) # Almacena valor de la matriz
                self.ui.tbl_propiedades.setItem(n,j,d) # se lleva a la tabla
            
        # 2 tbl_MKL
        self.ui.tbl_MKL.clearContents() # Se limpia la tabla
        self.ui.tbl_MKL.setRowCount(0)
        # 3 tbl_MKGE
        self.ui.tbl_MKGE.clearContents() # Se limpia la tabla
        self.ui.tbl_MKGE.setRowCount(0)
        
        for i in range(6):
            self.ui.tbl_MKL.insertRow(i)
            self.ui.tbl_MKGE.insertRow(i)
            for j in range(6):
                #print(round(MK_local[i][j],4))

                tb = QTableWidgetItem(str(round(MK_local[i][j],4))) # Almacena valor de la matriz
                self.ui.tbl_MKL.setItem(i,j,tb) # se lleva a la tabla
                #print(round(MK_globale[i][j],4))
                tb = QTableWidgetItem(str(round(MK_globale[i][j],4))) # Almacena valor de la matriz
                self.ui.tbl_MKGE.setItem(i,j,tb) # se lleva a la tabla
                
        self.ui.tbl_MKL.resizeColumnToContents(10) # Ajusta la columna a el numero que le metamos a la casilla

    def capturar_defromada(self):
        direc, _ = QFileDialog.getSaveFileName(self, "Guardar Archivo", 'C:\\', 'IMAGEN ANEPY (*.png)')
        # print(direc)
        plt_o.figure(figsize=(9,6), dpi=80)
        #fig.subplots_adjust(0, 0, 1, 1)
        plt_o.savefig(direc, bbox_inches='tight')

    def Fn_MatricesRigidezGUI(self):
        self.update()
        if self.no_visualizar_portico == False:
            self.ui.tbl_g_delta_elem.update() 
            # Obtiene nados de Fn_ExtraerDatosTablas
            [tbl_Elem, tbl_Nod, tbl_Fuer, tbl_Rest,tbl_Fuer_W,nElem] = self.Fn_ExtraerDatosTablas() 
            diccionarioN = self.Fn_diccionario_nodos(tbl_Nod)
            diccionarioE = self.Fn_diccionario_elementos(tbl_Elem)
            # dic_tf =  self.Fn_diccionario_fuerzas(tbl_Fuer) # Obtiene datos de Fn_diccionario_fuerzas
            
            elementos = self.Fn_propiedades_elementos(tbl_Elem, tbl_Nod, diccionarioN)
            
            vector_fuerzas = VF.Vector_fuerzas_externas(elementos,[tbl_Elem, tbl_Nod, tbl_Fuer, tbl_Rest,
                                                                   tbl_Fuer_W,nElem], 
                                                        diccionarioN, diccionarioE)
            tbl_Fuer = vector_fuerzas.tbl_Fuer # Obtiene datos de Fn_diccionario_fuerzas
            
            
            dic_tf = vector_fuerzas.dic_tf
            dic_vecF_ext_Elem = vector_fuerzas.dic_vecF_ext_Elem
            aem = AEM.Analisis_matricial(tbl_Elem, tbl_Rest, tbl_Nod, dic_tf, diccionarioN, dic_vecF_ext_Elem)
            self.activar_mef = True # Activa el MEF
            #print("###### ",aem.gdlN)
            
            #Extrayendo propiedades de la clase
            #MRE = analisis.KG_elem()
            # 3 tbl_MKG 
            
            """ Nota se muestra la matriz de rigidez global con las restricciones"""
            
            MK_Global = aem.MGL # Matris de rigidez global 
            ngl = MK_Global.shape[0] #Grados de libertad libres
            #print("##############dimension: ",ngl )
            self.ui.tbl_MKG.clearContents() # Se limpia la tabla
            self.ui.tbl_MKG.setRowCount(0)
            self.ui.tbl_MKG.setColumnCount(0)
            
            cont = 0 
            for i in range(ngl):
                self.ui.tbl_MKG.insertRow(i)
                for j in range(ngl):
                    if cont < ngl:
                        self.ui.tbl_MKG.insertColumn(j)
                        cont += 1
                    #print(round(MK_Global[i][j],4))
                    tb = QTableWidgetItem(str(round(MK_Global[i][j],4))) # Almacena valor de la matriz
                    self.ui.tbl_MKG.setItem(i,j,tb) # se lleva a la tabla
                    
            # Bloquea la ediccion de estas tablas
            self.ui.tbl_propiedades.setEditTriggers(QAbstractItemView.NoEditTriggers)
            self.ui.tbl_MKL.setEditTriggers(QAbstractItemView.NoEditTriggers)
            self.ui.tbl_MKGE.setEditTriggers(QAbstractItemView.NoEditTriggers)
            self.ui.tbl_MKG.setEditTriggers(QAbstractItemView.NoEditTriggers)
            self.ui.tbl_vec_F.setEditTriggers(QAbstractItemView.NoEditTriggers)
            self.ui.tbl_g_delta.setEditTriggers(QAbstractItemView.NoEditTriggers)
            self.ui.tbl_g_delta_elem.setEditTriggers(QAbstractItemView.NoEditTriggers)
            
            self.ui.tbl_MKG.setEditTriggers(QAbstractItemView.NoEditTriggers)
            
            "Mostrar el vector de cargas en la interfaz"
            vec_Fuerzas = aem.F
            self.ui.tbl_vec_F.clearContents() # Se limpia la tabla
            self.ui.tbl_vec_F.setRowCount(0)
            row = len(vec_Fuerzas)
            #col = len(datos_FuerW[0])
            for i in range(row):
                self.ui.tbl_vec_F.insertRow(i) # Inserta una fila en la tabla
                celda = QTableWidgetItem(str(vec_Fuerzas[i][0]))
                self.ui.tbl_vec_F.setItem(i, 0, celda)
                self.ui.tbl_vec_F.update()
                
            #grafica los grados de libertad
            self.Fn_visualizar_gdl()
            "Mostrar grado-desplazamiento - en la interfaz"
            g_delta = aem.g_delta
    
            row = len(g_delta)
            col = len(g_delta[0])
            self.ui.tbl_g_delta.clearContents() # Se limpia la tabla
            self.ui.tbl_g_delta.setRowCount(0)
    
            for i in range(row):
                self.ui.tbl_g_delta.insertRow(i) # Inserta una fila en la tabla
                for j in range(col):
                    dato = g_delta[i][j]
                    if j == 0:
                        dato = int(dato)
                    else:
                        dato = round(dato, 9)
                    celda = QTableWidgetItem(str(dato))
                    self.ui.tbl_g_delta.setItem(i, j, celda)
                    self.ui.tbl_g_delta.update()
           
            #fuerzas internas por elemntos
            self.Fuerzas_internas = aem.F_Internas_E
            
            #print("#--------------------")
            #print(self.Fuerzas_internas)
            # Grados y desplazamiento por elemento
            self.g_delta_elem = aem.g_delta_elemento
            self.guardado_parcial_MEF()
        
    def Fn_grado_delta_elemento_fuerzas_internas(self):
        "Mostrar grado-desplazamiento - en la interfaz"
        
        [tbl_Elem, tbl_Nod, tbl_Fuer, tbl_Rest,tbl_Fuer_W,nElem] = self.Fn_ExtraerDatosTablas() # Obtiene nados de Fn_ExtraerDatosTablas
        diccionarioN = self.Fn_diccionario_nodos(tbl_Nod)
        diccionarioE = self.Fn_diccionario_elementos(tbl_Elem)
        # dic_tf =  self.Fn_diccionario_fuerzas(tbl_Fuer) # Obtiene datos de Fn_diccionario_fuerzas
        
        # Slider de elementos
        self.ui.slider_Elem.setMaximum(nElem-1)
        
        self.ui.slider_Elem.setMinimum(0)
        
        i_d = self.ui.slider_Elem.value()
        
        self.ui.n_Elem.setText(str(i_d+1))
        
        #--------------------------------------------------
        try:
            g_delta_elem = self.g_delta_elem[i_d]
            # print(self.g_delta_elem)
            
            self.ui.tbl_g_delta_elem.clearContents() # Se limpia la tabla
            self.ui.tbl_g_delta_elem.setRowCount(0)
            row = len(g_delta_elem)
            col = len(g_delta_elem[0])
            
            for i in range(6):
                self.ui.tbl_g_delta_elem.insertRow(i) # Inserta una fila en la tabla
                for j in range(col):
                    dato = g_delta_elem[i][j]
                    if j == 0:
                        dato = int(dato)
                    else: dato = round(dato,9)
                    celda = QTableWidgetItem(str(dato))
                    self.ui.tbl_g_delta_elem.setItem(i,j, celda)
            self.ui.tbl_g_delta_elem.update() 
            
            #----------------------------------------------
            # Tabla de fuerzas internas
            fuerzas = self.Fuerzas_internas[i_d]
            #self.ui.tbl_fuerzas_internas.clearContents() # Se limpia la tabla
            #self.ui.tbl_fuerzas_internas.setRowCount(0)
            row = len(fuerzas)
            col = len(fuerzas[0])
            
           
            #dato = 
            #self.ui.tbl_fuerzas_internas.clearContents() # Se limpia la tabla
            self.ui.tbl_fuerzas_internas.update()
            for i in range(row):
                self.ui.tbl_fuerzas_internas.insertRow(i) # Inserta una fila en la tabla
                for j in range(1):
                    dato = round(fuerzas[i][j], self.redon)
                    celda = QTableWidgetItem(str(dato))
                    self.ui.tbl_fuerzas_internas.setItem(i, j, celda)
            self.ui.tbl_fuerzas_internas.verticalHeader().hide()
            self.ui.tbl_fuerzas_internas.update()        
            
        except TypeError:
            pass
            
    def Fn_MEF(self):
        
        """ En una nueva version con esta funcion se podrá utilizar para:
            
            1) Graficar    Fx
            2)   "          V
            3)   "          M
        """

        """Aplicacion del método"""
        #if self.activar_MEF == True:
        if self.activar_mef == True:
            [tbl_Elem1, tbl_Nod, tbl_Fuer, tbl_Rest1, tbl_Fuer_W,nElem] = self.Fn_ExtraerDatosTablas() # Obtiene nados de Fn_ExtraerDatosTablas
            diccionarioN1 = self.Fn_diccionario_nodos(tbl_Nod)
            diccionarioE = self.Fn_diccionario_elementos(tbl_Elem1)
            elementos = self.Fn_propiedades_elementos(tbl_Elem1, tbl_Nod, diccionarioN1)
            sub = 10
            tbl_sub_elementos, dic_sub_elementos, tbl_sub_nodos, dic_sub_nodos,tbl_sub_Fuer, tbl_sub_F_W, tbl_sub_restricciones, sub_elementos, dic_nod_real_irreal = Sub_E_N_F_FW_R(elementos,sub, tbl_Elem1, tbl_Nod, tbl_Fuer, tbl_Fuer_W, tbl_Rest1, diccionarioE, diccionarioN1 )
            
            """Re-asignacion"""
            tbl_Elem = tbl_sub_elementos
            tbl_Nod = tbl_sub_nodos
            tbl_Fuer = tbl_sub_Fuer
            tbl_Fuer_W = tbl_sub_F_W 
            tbl_Rest = tbl_sub_restricciones
            diccionarioE = dic_sub_elementos
            diccionarioN = dic_sub_nodos
            elementos =  sub_elementos
            
            """Vector fuerza"""
            vector_fuerzas_ext = VF.Vector_fuerzas_externas(sub_elementos,[tbl_Elem, tbl_Nod, tbl_Fuer, tbl_Rest,tbl_Fuer_W,len(elementos)], 
                                                        diccionarioN, diccionarioE)
            
            tbl_Fuer = vector_fuerzas_ext.tbl_Fuer # Tabla de la suma de fuerzas que llegan al los nodos vector para corformacion del vector fuerzas
            dic_tf = vector_fuerzas_ext.dic_tf
            dic_vecF_ext_Elem = vector_fuerzas_ext.dic_vecF_ext_Elem
            
            """ Realiza analisis"""
            
            Portico = AEM.Analisis_matricial(tbl_Elem, tbl_Rest, tbl_Nod, dic_tf, diccionarioN, dic_vecF_ext_Elem)
            
            self.Desplazamientos_elementos = Portico.d_elem
            
            return elementos, self.Desplazamientos_elementos,diccionarioN, tbl_Elem1, tbl_Rest1, diccionarioN1

# # Security Screen
# class UiSeguridad(QMainWindow):
#     def __init__(self, parent = None):
#         QMainWindow.__init__(self, parent)
#         self.ui = UI_Seguridad()
#         self.ui.setupUi(self)
#         # Eliminar titulo de barra
#         self.setWindowFlag(Qt.FramelessWindowHint)
#         self.setAttribute(Qt.WA_TranslucentBackground)
        
#         self.ui.dial_d1.valueChanged.connect(self.digito_1)
#         self.ui.dial_d2.valueChanged.connect(self.digito_2)
#         self.ui.dial_d3.valueChanged.connect(self.digito_3)
#         self.ui.dial_d4.valueChanged.connect(self.digito_4)
        
#         # Drop shadow effect efecto sombra
#         self.shadow = QGraphicsDropShadowEffect(self)
#         self.shadow.setBlurRadius(30)
#         self.shadow.setXOffset(0)
#         self.shadow.setYOffset(0)
#         self.shadow.setColor(QColor(79,93,116,70))
#         self.ui.frame.setGraphicsEffect(self.shadow)
        
#         self.key = "0000"
#         # ==>Qtimer of load
#         self.timer = QTimer()
        
#         self.timer.timeout.connect(self.prueba_seguridad)
#         # # Tiempo (ml)
#         self.timer.start(50)
#         # self.show()
    
#     def digito_1(self):
#         valor = self.ui.dial_d1.value()
#         self.ui.lb_d1.setText(str(valor))
#         self.prueba_seguridad()
#     def digito_2(self):
#         valor = self.ui.dial_d2.value()
#         self.ui.lb_d2.setText(str(valor))
#         self.prueba_seguridad()
#     def digito_3(self):
#         valor = self.ui.dial_d3.value()
#         self.ui.lb_d3.setText(str(valor))
#         self.prueba_seguridad()
#     def digito_4(self):
#         valor = self.ui.dial_d4.value()
#         self.ui.lb_d4.setText(str(valor))
#         self.prueba_seguridad()
#     def prueba_seguridad(self):
#         global cont_2
#         valor_1 = self.ui.lb_d1.text()
#         valor_2 = self.ui.lb_d2.text()
#         valor_3 = self.ui.lb_d3.text()
#         valor_4 = self.ui.lb_d4.text()
#         valor = valor_1 + valor_2 + valor_3 + valor_4
#         if valor==self.key:
#             cont_2 += 1
#             if cont == 25:
#                 self.ui.lb_d1.setText("")
#                 self.ui.lb_d2.setText("")
#                 self.ui.lb_d3.setText("")
#                 self.ui.lb_d4.setText("")
#             if cont_2 == 50:
#                     self.timer.stop()
#                     self.splash = SplashScreen()
#                     self.splash.show()
#                     self.close()
  
# Splash Screen
class UiSplashScreen(QMainWindow):
    def __init__(self, parent = None):
        QMainWindow.__init__(self, parent)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)
        
        # UI ==> Codigo de interfaz
        #-----------------------------------
        
        # Eliminar titulo de barra
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        
        # Drop shadow effect efecto sombra
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0,0,0,60))
        self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)
        
        # ==>Qtimer of load
        self.timer = QTimer()
        self.timer.timeout.connect(self.progressBar)
        # Tiempo (ml)
        self.timer.start(35)
        
        # Inicial de descripcion
        self.ui.label_descripcion.setText("<strong>BIENVENIDO</strong> A MI APLICACIÓN")
        # Cambiar descripcion en el tiempo
        QTimer.singleShot(100, lambda: self.ui.label_descripcion.setText("<strong>LOADING</strong> ANÁLISIS PORTICOS.."))
        QTimer.singleShot(1250, lambda: self.ui.label_descripcion.setText("<strong>LOADING</strong> CORTANTE Y MEP.."))
        QTimer.singleShot(1500, lambda: self.ui.label_descripcion.setText("<strong>LOADING</strong> DEFORMADA..."))
        QTimer.singleShot(1750, lambda: self.ui.label_descripcion.setText("<strong>LOADING</strong> MAIN CONVERSIONES..."))
        QTimer.singleShot(2000, lambda: self.ui.label_descripcion.setText("<strong>LOADING</strong> MAIN CRÉDITOS..."))
        QTimer.singleShot(2250, lambda: self.ui.label_descripcion.setText("<strong>LOADING</strong> MEF"))
        QTimer.singleShot(2500, lambda: self.ui.label_descripcion.setText("<strong>LOADING</strong> PROPIEDADES DE ELE..."))
        QTimer.singleShot(2750, lambda: self.ui.label_descripcion.setText("<strong>LOADING</strong> TEMAS..."))
        QTimer.singleShot(3000, lambda: self.ui.label_descripcion.setText("<strong>LOADING</strong> FUNCIONES..."))
        QTimer.singleShot(3250, lambda: self.ui.label_descripcion.setText("<strong>LOADING</strong> MATPLOTLIB_PYQT5..."))
        QTimer.singleShot(3500, lambda: self.ui.label_descripcion.setText("<strong>LOADING</strong> VECTOR FUERZAS..."))
        # ==> Show Ventana principal
        #-----------------------------------
        
        self.show()
        # ==> End
        
        # ==>Funciones
        #-----------------------------------
    def progressBar(self):
        global cont
        # Set value to progressbar
        self.ui.progressBar.setValue(cont)
        # Close Splash Screen and apen APP
        if cont > 100:
            # Stop TimeOutError
            self.timer.stop()
            self.main = Ui_ANEPY()
            if len(sys.argv) > 1:
                dir_file = sys.argv[1]
                print("###########################",dir_file)
                self.main.abrir(dir_file)
            else:
                print("Uso: python main.py archivo.j&y")
            self.main.show()
            # Close Splash Screen
            self.close()
        # Incrementar contador
        cont += 1
 


my_app = None     
if __name__ == '__main__':
    app = QApplication(sys.argv)
    #app.setWindowIcon(QIcon(os.path.join(basedir, 'Logo.ico')))
    my_app = UiSplashScreen()
    my_app.show()
    sys.exit(app.exec_())