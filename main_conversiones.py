# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 01:30:36 2023

@author: Estudiante
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Jan 13 16:26:30 2023

@author: Estudiante
"""

from UI_Conversor_Unidades import Ui_Convertidor


import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QAction, QFileDialog, QMainWindow, QMessageBox, QDialog
from PyQt5 import Qt

""" Se usa para actualizar la interface tras ediccion en QtD 
    pyuic5 convertidor_un.ui > UI_Conversor_Unidades.py """

class Ui_Conversor_Unidades(QDialog):
    def __init__(self, parent = None):
        
        #QtWidgets.QMainWindow.__init__(self, parent)
        QtWidgets.QWidget.__init__(self, parent)
        
        
        self.ui = Ui_Convertidor()
        
        self.ui.setupUi(self)
        self.ui.cb_tipo.currentTextChanged.connect(self.obtener_unidad)
        self.obtener_unidad()
        self.ui.bt_convertir.clicked.connect(self.convertir_unidades)
        
        self.ui.lb_resultado.setAlignment(Qt.Qt.AlignCenter)
        self.ui.lb_resultado.setTextInteractionFlags(Qt.Qt.TextSelectableByMouse)
        #self.show()
        
    def obtener_unidad(self):
        tipo = self.ui.cb_tipo.currentText()
        self.ui.lb_resultado.setText("0")
        self.ui.lb_resultado.setAlignment(Qt.Qt.AlignCenter)
        print(tipo)
        unidades = []
        
        if tipo == "Longitud":
            unidades = ["[mm]", "[cm]","[m]","[pie]","[pulg]"]
        elif tipo == "Área":
            unidades = ["[mm2]", "[cm2]","[m2]","[pie2]","[pulg2]"]
        elif tipo == "Fuerza":
            unidades = ["[g]","[Lb]","[Kg]","[Ton]","[N]", "[KN]","[MN]", "[GN]"]
        elif tipo == "Momento":
            unidades = ["[Kg-m]","[Ton-m]","[Lb-pie]","[Lb-pulg]","[N-m]", "[KN-m]"]
        elif tipo == "Presión":
            unidades = ["[Psi(Lb/in2)]", "[Kg/cm2]", "[Kg/m2]","[Ton/cm2]","[Ton/m2]","[Pa]","[KPa]","[MPa]","[GPa]"]
        self.ui.cb_convertir_de.clear()
        self.ui.cb_convertir_de.addItems(unidades)
        self.ui.cb_convertir_de.update()
        
        self.ui.cb_convertir_a.clear()
        self.ui.cb_convertir_a.addItems(unidades)
        self.ui.cb_convertir_a.update()

    def convertir_unidades(self):
        con_de = self.ui.cb_convertir_de.currentText()
        con_a = self.ui.cb_convertir_a.currentText()
        valor = self.ui.in_valor.text()
        self.ui.in_valor.setAlignment(Qt.Qt.AlignCenter)
        if valor == "":
            valor = "1"
            self.ui.in_valor.setText(valor)
        def longitud(valor):
            dato = 0
            if con_de == con_de:
                dato = float(valor)
                #["[mm]", "[cm]","[m]","[pie]","[pulg]"]
            #-------------------[mm]-----------------#
            if con_de == "[mm]" and  con_a == "[cm]":
                dato = float(valor)/10 
            elif con_de == "[mm]" and  con_a == "[m]":
                dato = float(valor)/1000
            elif con_de == "[mm]" and  con_a == "[pie]":
                dato = float(valor)/304.8
            elif con_de == "[mm]" and  con_a == "[pulg]":
                dato = float(valor)/25.4
            #-------------------[cm]-----------------#   
            elif con_de == "[cm]" and  con_a == "[mm]":
                dato = float(valor) * 10
            elif con_de == "[cm]" and  con_a == "[m]":
                dato = float(valor)/100
            elif con_de == "[cm]" and  con_a == "[pie]":
                dato = float(valor)/30.48
            elif con_de == "[cm]" and  con_a == "[pulg]":
                dato = float(valor)/2.54
            #-------------------[m]-----------------#
            elif con_de == "[m]" and  con_a == "[mm]":
                dato = float(valor) * 1000
            elif con_de == "[m]" and  con_a == "[cm]":
                dato = float(valor)*100
            elif con_de == "[m]" and  con_a == "[pie]":
                dato = float(valor)*3.28084
            elif con_de == "[m]" and  con_a == "[pulg]":
                dato = float(valor)*39.37
             #-------------------[pie]-----------------#   
            elif con_de == "[pie]" and  con_a == "[mm]":
                dato = float(valor) * 304.8
            elif con_de == "[pie]" and  con_a == "[cm]":
                dato = float(valor)*30.48
            elif con_de == "[pie]" and  con_a == "[m]":
                dato = float(valor)/3.28084
            elif con_de == "[pie]" and  con_a == "[pulg]":
                dato = float(valor)*12
            #-------------------[pulg]-----------------#
            elif con_de == "[pulg]" and  con_a == "[mm]":
                dato = float(valor) * 25.4
            elif con_de == "[pulg]" and  con_a == "[cm]":
                dato = float(valor)*2.54
            elif con_de == "[pulg]" and  con_a == "[m]":
                dato = float(valor)/39.37
            elif con_de == "[pulg]" and  con_a == "[pulg]":
                dato = float(valor)/12
                
            dato = str(round(dato,4))
            print(dato)
            self.ui.lb_resultado.setText(dato)
            
        
        def área(valor):
            dato = 0
            if con_de == con_de:
                dato = float(valor)
                #["[mm]", "[cm]","[m]","[pie]","[pulg]"]
            #-------------------[mm]-----------------#
            if con_de == "[mm2]" and  con_a == "[cm2]":
                dato = float(valor)/10**2 
            elif con_de == "[mm2]" and  con_a == "[m2]":
                dato = float(valor)/1000**2 
            elif con_de == "[mm2]" and  con_a == "[pie2]":
                dato = float(valor)/304.8**2
            elif con_de == "[mm2]" and  con_a == "[pulg2]":
                dato = float(valor)/25.4**2
            #-------------------[cm]-----------------#   
            elif con_de == "[cm2]" and  con_a == "[mm2]":
                dato = float(valor) * 10**2
            elif con_de == "[cm2]" and  con_a == "[m2]":
                dato = float(valor)/100**2
            elif con_de == "[cm2]" and  con_a == "[pie2]":
                dato = float(valor)/30.48**2
            elif con_de == "[cm2]" and  con_a == "[pulg2]":
                dato = float(valor)/2.54**2
            #-------------------[m]-----------------#
            elif con_de == "[m2]" and  con_a == "[mm2]":
                dato = float(valor) * 1000**2
            elif con_de == "[m2]" and  con_a == "[cm2]":
                dato = float(valor)*100**2
            elif con_de == "[m2]" and  con_a == "[pie2]":
                dato = float(valor)*3.28084**2
            elif con_de == "[m2]" and  con_a == "[pulg2]":
                dato = float(valor)*39.37**2
             #-------------------[pie]-----------------#   
            elif con_de == "[pie2]" and  con_a == "[mm2]":
                dato = float(valor) * 304.8**2
            elif con_de == "[pie2]" and  con_a == "[cm2]":
                dato = float(valor)*30.48**2
            elif con_de == "[pie2]" and  con_a == "[m2]":
                dato = float(valor)/3.28084**2
            elif con_de == "[pie2]" and  con_a == "[pulg2]":
                dato = float(valor)*12^2
            #-------------------[pulg]-----------------#
            elif con_de == "[pulg2]" and  con_a == "[mm2]":
                dato = float(valor) * 25.4**2
            elif con_de == "[pulg2]" and  con_a == "[cm2]":
                dato = float(valor)*2.54**2
            elif con_de == "[pulg2]" and  con_a == "[m2]":
                dato = float(valor)/(39.37**2)
            elif con_de == "[pulg2]" and  con_a == "[pie2]":
                dato = float(valor)/12**2
                
            dato = str(round(dato,4))
            print(dato)
            self.ui.lb_resultado.setText(dato)
            self.ui.lb_resultado.setAlignment(Qt.Qt.AlignCenter)
        
        def fuerza(valor):
            dato = 0
            if con_de == con_de:
                dato = float(valor)
                #["[mm]", "[cm]","[m]","[pie]","[pulg]"]
            #-------------------[Lb]-----------------#
            if con_de == "[Lb]" and  con_a == "[Kg]" :
                dato = float(valor) * 0.453592
            if con_de == "[Lb]" and  con_a == "[Ton]" :
                dato = float(valor) * 0.453592 / 1000
            elif con_de == "[Lb]" and  con_a == "[g]":
                dato = float(valor)  * 0.453592* 10**3
            elif con_de == "[Lb]" and  con_a == "[N]" :
                dato = float(valor)* 4.4482
            elif con_de == "[Lb]" and  con_a == "[KN]":
                dato = float(valor)* 4.4482/10**3
            elif con_de == "[Lb]" and  con_a == "[MN]":
                dato = float(valor)* 4.4482/10**6
            elif con_de == "[Lb]" and  con_a == "[GN]":
                dato = float(valor)* 4.4482/10**9
            
            #--------------- [Kg]  -----------------------#
            if con_de == "[Kg]" and  con_a == "[Lb]" :
                dato = float(valor)/ 0.453592
            if con_de == "[Kg]" and  con_a == "[Ton]" :
                dato = float(valor) / 1000
            elif con_de == "[Kg]" and  con_a == "[g]":
                dato = float(valor) * 1000
            elif con_de == "[Kg]" and  con_a == "[N]" :
                dato = float(valor) * 9.8067
            elif con_de == "[Kg]" and  con_a == "[KN]":
                dato = float(valor) * 9.8067/10**3
            elif con_de == "[Kg]" and  con_a == "[MN]":
                dato = float(valor) * 9.8067/10**6
            elif con_de == "[Kg]" and  con_a == "[GN]":
                dato = float(valor) * 9.8067/10**9
            #--------------- [Ton]  -----------------------#
            if con_de == "[Ton]" and  con_a == "[Lb]" :
                dato = float(valor)*2204.62
            if con_de == "[Ton]" and  con_a == "[Kg]" :
                dato = float(valor)* 10**3
            elif con_de == "[Ton]" and  con_a == "[g]":
                dato = float(valor) * 10**6
            elif con_de == "[Ton]" and  con_a == "[N]" :
                dato = float(valor)*9.8067*10**3
            elif con_de == "[Ton]" and  con_a == "[KN]":
                dato = float(valor)*9.8067
            elif con_de == "[Ton]" and  con_a == "[MN]":
                dato = float(valor)*9.8067/10**3
            elif con_de == "[Ton]" and  con_a == "[GN]":
                dato = float(valor)*9.8067/10**6
            #--------------- [g]  -----------------------#
            if con_de == "[g]" and  con_a == "[Lb]" :
                dato = float(valor) / (0.453592*1000)
            if con_de == "[g]" and  con_a == "[Kg]" :
                dato = float(valor) / 10**3
            elif con_de == "[g]" and  con_a == "[Ton]":
                dato = float(valor) / 10**6
            elif con_de =="[g]" and  con_a == "[N]" :
                dato = float(valor) * 9.8067/10**3
            elif con_de == "[g]" and  con_a == "[KN]":
                dato = float(valor)* 9.8067/10**6
            elif con_de == "[g]" and  con_a == "[MN]":
                dato = float(valor)* 9.8067/10**9
            elif con_de == "[g]" and  con_a == "[GN]":
                dato = float(valor)* 9.8067/10**12
            #---------------  [N] -----------------------#
            if con_de =="[N]"  and  con_a == "[Lb]" :
                dato = float(valor) / 4.4482
            if con_de == "[N]" and  con_a == "[Kg]" :
                dato = float(valor) / 9.8067
            elif con_de =="[N]"  and  con_a == "[Ton]":
                dato = float(valor)/(9.8067*10**3)
            elif con_de == "[N]" and  con_a == "[g]" :
                dato = (float(valor) / 9.8067)*10**3
            elif con_de =="[N]"  and  con_a == "[KN]":
                dato = float(valor)/ 10**3
            elif con_de =="[N]"  and  con_a == "[MN]":
                dato = float(valor) / 10**6
            elif con_de == "[N]" and  con_a == "[GN]":
                dato = float(valor) / 10**9
            #--------------- [KN]  -----------------------#
            if con_de == "[KN]" and  con_a == "[Lb]" :
                dato = float(valor)/ 4.4482 * 10**3
            if con_de == "[KN]" and  con_a == "[Kg]" :
                dato = float(valor)/ 9.8067 * 10**3
            elif con_de == "[KN]" and  con_a == "[Ton]":
                dato = float(valor)/(9.8067)
            elif con_de == "[KN]" and  con_a == "[g]" :
                dato = float(valor)/ 9.8067 * 10**6
            elif con_de == "[KN]" and  con_a == "[N]":
                dato = float(valor) * 10**3
            elif con_de == "[KN]" and  con_a == "[MN]":
                dato = float(valor)/ 10**6
            elif con_de =="[KN]"  and  con_a == "[GN]":
                dato = float(valor)/ 10**9
            #---------------[MN]   -----------------------#
            if con_de == "[MN]" and  con_a == "[Lb]" :
                dato = float(valor)/ 4.4482 * 10**6
            if con_de == "[MN]" and  con_a == "[Kg]" :
                dato = float(valor)/ 9.8067 * 10**6
            elif con_de == "[MN]" and  con_a == "[Ton]":
                dato = float(valor)/(9.8067)*10**3
            elif con_de == "[MN]" and  con_a == "[g]" :
                dato = float(valor)/ 9.8067 * 10**9
            elif con_de == "[MN]" and  con_a == "[N]":
                dato = float(valor) * 10**6
            elif con_de =="[MN]"  and  con_a == "[KN]":
                dato = float(valor)* 10**3
            elif con_de =="[MN]"  and  con_a == "[GN]":
                dato = float(valor)/ 10**3
            #---------------[GN]   -----------------------#
            if con_de == "[GN]" and  con_a == "[Lb]" :
                dato = float(valor)/ 4.4482 * 10**9
            if con_de == "[GN]" and  con_a == "[Kg]" :
                dato = float(valor)/ 9.8067 * 10**9
            elif con_de == "[GN]" and  con_a == "[Ton]":
                dato = float(valor)/(9.8067)*10**6
            elif con_de == "[GN]" and  con_a == "[g]" :
                dato = float(valor)/ 9.8067 * 10**12
            elif con_de == "[GN]" and  con_a == "[N]":
                dato = float(valor)*10**9
            elif con_de == "[GN]" and  con_a == "[KN]":
                dato = float(valor)*10**6
            elif con_de == "[GN]" and  con_a == "[MN]":
                dato = float(valor)*10**3

            dato = str(round(dato,4))
            print(dato)
            self.ui.lb_resultado.setText(dato)
            self.ui.lb_resultado.setAlignment(Qt.Qt.AlignCenter)
        
        def momento(valor):
            dato = 0
            if con_de == con_de:
                dato = float(valor)
                
                # ["[Kg-m]","[Ton-m]","[Lb-pie]","[Lb-pulg]","[N-m]", "[KN-m]"]
            # Kg-m------------------
            if con_de == "[Kg-m]" and  con_a == "[Ton-m]" :
                dato = float(valor)/1000
            if con_de == "[Kg-m]" and  con_a == "[Lb-pie]" :
                dato = float(valor)*7.23301
            if con_de == "[Kg-m]" and  con_a == "[Lb-pulg]" :
                dato = float(valor)*86.8
            if con_de == "[Kg-m]" and  con_a == "[N-m]" :
                dato = float(valor)*9.81
            if con_de == "[Kg-m]" and  con_a == "[KN-m]" :
                dato = float(valor)*0.00981
            # Ton-m -----------------------
            if con_de == "[Ton-m]" and  con_a == "[Kg-m]" :
                dato = float(valor)*1000
            if con_de == "[Ton-m]" and  con_a == "[Lb-pie]" :
                dato = float(valor)*7.23301*1000
            if con_de == "[Ton-m]" and  con_a == "[Lb-pulg]" :
                dato = float(valor)*86.8*1000
            if con_de == "[Ton-m]" and  con_a == "[N-m]" :
                dato = float(valor)*9.81*1000
            if con_de == "[Ton-m]" and  con_a == "[KN-m]" :
                dato = float(valor)*9.81
            # Lb-pie------------------------------------
            
            if con_de == "[Lb-pie]" and  con_a == "[Kg-m]" :
                dato = float(valor)*(1/7.23301)
            if con_de == "[Lb-pie]" and  con_a == "[Ton-m]" :
                dato = float(valor)*(1/(7.23301/1000))
            if con_de == "[Lb-pie]" and  con_a == "[Lb-pulg]" :
                dato = float(valor)*12
            if con_de == "[Lb-pie]" and  con_a == "[N-m]" :
                dato = float(valor)*1.3558
            if con_de == "[Lb-pie]" and  con_a == "[KN-m]" :
                dato = float(valor)*1.3558*1e-3
            # Lb-pulg----------------------------
            if con_de == "[Lb-pulg]" and  con_a == "[Kg-m]" :
                dato = float(valor)*(1/86.8)
            if con_de == "[Lb-pulg]" and  con_a == "[Ton-m]" :
                dato = float(valor)*(1/86.8/1000)
            if con_de == "[Lb-pulg]" and  con_a == "[Lb-pie]" :
                dato = float(valor)/12
            if con_de == "[Lb-pulg]" and  con_a == "[N-m]" :
                dato = float(valor)*0.11298
            if con_de == "[Lb-pulg]" and  con_a == "[KN-m]" :
                dato = float(valor)*0.11298/1000
            # N-m------------------------------------
            if con_de == "[N-m]" and  con_a == "[Kg-m]" :
                dato = float(valor)*(1/9.81)
            if con_de == "[N-m]" and  con_a == "[Ton-m]" :
                dato = float(valor)*(1/9.81/1000)
            if con_de == "[N-m]" and  con_a == "[Lb-pie]" :
                dato = float(valor)/1,3558
            if con_de == "[N-m]" and  con_a == "[Lb-pulg]" :
                dato = float(valor)/0,11298
            if con_de == "[N-m]" and  con_a == "[KN-m]" :
                dato = float(valor)/1000
            # KN-m------------------------------------
            if con_de == "[KN-m]" and  con_a == "[Kg-m]" :
                dato = float(valor)*(1/9.81)*1000
            if con_de == "[KN-m]" and  con_a == "[Ton-m]" :
                dato = float(valor)*(1/9.81)
            if con_de == "[KN-m]" and  con_a == "[Lb-pie]" :
                dato = float(valor)/1.3558*1000
            if con_de == "[KN-m]" and  con_a == "[Lb-pulg]" :
                dato = float(valor)/0.11298*1000
            if con_de == "[KN-m]" and  con_a == "[N-m]" :
                dato = float(valor)*1000
            dato = str(round(dato,9))
            print(dato)
            self.ui.lb_resultado.setText(dato)
            self.ui.lb_resultado.setAlignment(Qt.Qt.AlignCenter)
        
        def presión(valor):
            if con_de == con_de:
                dato = float(valor)
            #-------------------[Psi(Lb/in2]-----------------#
            if con_de == "[Psi(Lb/in2)]" and  con_a == "[Kg/cm2]":
                dato = float(valor)*0.07031
            if con_de == "[Psi(Lb/in2)]" and  con_a == "[Kg/m2]":
                dato = float(valor)*703.0696
            if con_de == "[Psi(Lb/in2)]" and  con_a == "[Ton/cm2]":
                dato = float(valor)*0.0703/1000
            if con_de == "[Psi(Lb/in2)]" and  con_a == "[Ton/m2]":
                dato = float(valor)*0.7031
            if con_de == "[Psi(Lb/in2)]" and  con_a == "[Pa]":
                dato = float(valor)*6894.7591
            if con_de == "[Psi(Lb/in2)]" and  con_a == "[KPa]":
                dato = float(valor)*6894.7591/10e3*10
            if con_de == "[Psi(Lb/in2)]" and  con_a == "[MPa]":
                dato = float(valor)*6894.7591/10e6*10
            if con_de == "[Psi(Lb/in2)]" and  con_a == "[MPa]":
                dato = float(valor)*6894.7591/10e6*10
                
            #-------------------[Kg/cm2]-----------------#
            if con_de == "[Kg/cm2]" and  con_a == "[Psi(Lb/in2)]":
                dato = float(valor)/0.0703
            if con_de == "[Kg/cm2]" and  con_a == "[Kg/m2]":
                dato = float(valor)*10000
            if con_de == "[Kg/cm2]" and  con_a == "[Ton/cm2]":
                dato = float(valor)/1000
            if con_de == "[Kg/cm2]" and  con_a == "[Ton/m2]":
                dato = float(valor)*10
            if con_de == "[Kg/cm2]" and  con_a == "[Pa]":
                dato = float(valor)*98066.520482
            if con_de == "[Kg/cm2]" and  con_a == "[KPa]":
                dato = float(valor)*98.0667
            if con_de == "[Kg/cm2]" and  con_a == "[MPa]":
                dato = float(valor)*0.09806
            if con_de == "[Kg/cm2]" and  con_a == "[GPa]":
                dato = float(valor)/0.10197*1e-9
            #-------------------[Kg/m2]-----------------#
            if con_de == "[Kg/m2]" and  con_a == "[Psi(Lb/in2)]":
                dato = float(valor)/703.0696
            if con_de == "[Kg/m2]" and  con_a == "[Kg/cm2]":
                dato = float(valor)/10000
            if con_de == "[Kg/m2]" and  con_a == "[Ton/cm2]":
                dato = float(valor)*1e-7
            if con_de == "[Kg/m2]" and  con_a == "[Ton/m2]":
                dato = float(valor)*0.001
            if con_de == "[Kg/m2]" and  con_a == "[Pa]":
                dato = float(valor)*9.81
            if con_de == "[Kg/m2]" and  con_a == "[KPa]":
                dato = float(valor)*9.81*1e-3
                print("here", dato)
            if con_de == "[Kg/m2]" and  con_a == "[MPa]":
                dato = float(valor)*9.81*1e-6
            if con_de == "[Kg/m2]" and  con_a == "[GPa]":
                dato = float(valor)*9.81*1e-9
            
            #-------------------[Ton/cm2]-----------------#
            if con_de == "[Ton/cm2]" and  con_a == "[Psi(Lb/in2)]":
                dato = float(valor)/(0.0703/1000)
            if con_de == "[Ton/cm2]" and  con_a == "[Kg/m2]":
                dato = float(valor)/1e-7
            if con_de == "[Ton/cm2]" and  con_a == "[Kg/cm2]":
                dato = float(valor)*1000
            if con_de == "[Ton/cm2]" and  con_a == "[Ton/m2]":
                dato = float(valor)*10000
            if con_de == "[Ton/cm2]" and  con_a == "[Pa]":
                dato = float(valor)*98066520.48
            if con_de == "[Ton/cm2]" and  con_a == "[KPa]":
                dato = float(valor)*98066520.48*1e-3
            if con_de == "[Ton/cm2]" and  con_a == "[MPa]":
                dato = float(valor)*98066520.48*1e-6
            if con_de == "[Ton/cm2]" and  con_a == "[GPa]":
                dato = float(valor)*98066520.48*1e-9
            #-------------------[Ton/m2]-----------------#
            if con_de == "[Ton/m2]" and  con_a == "[Psi(Lb/in2)]":
                dato = float(valor)/0.7031
            if con_de == "[Ton/m2]" and  con_a == "[Kg/m2]":
                dato = float(valor)*1000
            if con_de == "[Ton/m2]" and  con_a == "[Ton/cm2]":
                dato = float(valor)/10000
            if con_de == "[Ton/m2]" and  con_a == "[Kg/cm2]":
                dato = float(valor)*0.10
            if con_de == "[Ton/m2]" and  con_a == "[Pa]":
                dato = float(valor)*9806.6501
            if con_de == "[Ton/m2]" and  con_a == "[KPa]":
                dato = float(valor)*(9806.6501/1000)
            if con_de == "[Ton/m2]" and  con_a == "[MPa]":
                dato = float(valor)*(9806.6501)*1e-6
            if con_de == "[Ton/m2]" and  con_a == "[GPa]":
                dato = float(valor)*(9806.6501)*1e-9
            #-------------------[Pa]-----------------#
            if con_de == "[Pa]" and  con_a == "[Psi(Lb/in2)]":
                dato = float(valor)/6894.7591
            if con_de == "[Pa]" and  con_a == "[Kg/m2]":
                dato = float(valor)*0.10197
            if con_de == "[Pa]" and  con_a == "[Ton/cm2]":
                dato = float(valor)*1.12*10e-4
            if con_de == "[Pa]" and  con_a == "[Ton/m2]":
                dato = float(valor)/9806.6501
            if con_de == "[Pa]" and  con_a == "[Kg/cm2]":
                dato = float(valor)*0.00001
            if con_de == "[Pa]" and  con_a == "[KPa]":
                dato = float(valor)*1e-3
            if con_de == "[Pa]" and  con_a == "[MPa]":
                dato = float(valor)*1e-6
            if con_de == "[Pa]" and  con_a == "[GPa]":
                dato = float(valor)*1e-9
            #-------------------[KPa]-----------------#
            if con_de == "[KPa]" and  con_a == "[Psi(Lb/in2)]":
                dato = float(valor)*0.14504
            if con_de == "[KPa]" and  con_a == "[Kg/m2]":
                dato = float(valor)*101.97
            if con_de == "[KPa]" and  con_a == "[Ton/cm2]":
                dato = float(valor)/(980665*10e7 ) *10e3
            if con_de == "[KPa]" and  con_a == "[Ton/m2]":
                dato = float(valor)/(9806.6501*10e-4)
            if con_de == "[KPa]" and  con_a == "[Kg/cm2]":
                dato = float(valor)*0.10197*10e-2
            if con_de == "[KPa]" and  con_a == "[Pa]":
                dato = float(valor)*1e3
            if con_de == "[KPa]" and  con_a == "[MPa]":
                dato = float(valor)*1e-3
            if con_de == "[KPa]" and  con_a == "[GPa]":
                dato = float(valor)*1e-6
             #-------------------[MPa]-----------------#
            if con_de == "[MPa]" and  con_a == "[Psi(Lb/in2)]":
                dato = float(valor)/6894.7591*10e6
            if con_de == "[MPa]" and  con_a == "[Kg/m2]":
                dato = float(valor)*101.97*1e6
            if con_de == "[MPa]" and  con_a == "[Ton/cm2]":
                dato = float(valor)/(980665*10e7 ) *10e6
            if con_de == "[MPa]" and  con_a == "[Ton/m2]":
                dato = float(valor)/(9806.6501*10e6)
            if con_de == "[MPa]" and  con_a == "[Kg/cm2]":
                dato = float(valor)*0.00001*1e6
            if con_de == "[MPa]" and  con_a == "[Pa]":
                dato = float(valor)*1e6
            if con_de == "[MPa]" and  con_a == "[KPa]":
                dato = float(valor)*1e-3
            if con_de == "[MPa]" and  con_a == "[GPa]":
                dato = float(valor)*1e-6
            #-------------------[GPa]-----------------#
            if con_de == "[GPa]" and  con_a == "[Psi(Lb/in2)]":
                dato = float(valor)/6894.7591*1e9
            if con_de == "[GPa]" and  con_a == "[Kg/m2]":
                dato = float(valor)*101.97*1e9
            if con_de == "[GPa]" and  con_a == "[Ton/cm2]":
                dato = float(valor)/(980665*1e7 ) *1e9
            if con_de == "[GPa]" and  con_a == "[Ton/m2]":
                dato = float(valor)/(9806.6501*1e9)
            if con_de == "[GPa]" and  con_a == "[Kg/cm2]":
                dato = float(valor)*0.00001*1e9
            if con_de == "[GPa]" and  con_a == "[Pa]":
                dato = float(valor)*1e9
            if con_de == "[GPa]" and  con_a == "[KPa]":
                dato = float(valor)*1e6
            if con_de == "[GPa]" and  con_a == "[MPa]":
                dato = float(valor)*1e3
            print(dato)
            dato = str(round(dato,9))
            
            self.ui.lb_resultado.setText(dato)
            self.ui.lb_resultado.setAlignment(Qt.Qt.AlignCenter)
            
        if self.ui.cb_tipo.currentText() == "Longitud":
            longitud(valor)        
        if self.ui.cb_tipo.currentText() == "Área":
            área(valor)
        if self.ui.cb_tipo.currentText() == "Fuerza":
            fuerza(valor)
            
        if self.ui.cb_tipo.currentText() == "Momento":
            momento(valor)
        
        if self.ui.cb_tipo.currentText() == "Presión":
            presión(valor)
            
        self.update()
        
    def salir(self):
        self.close()
        
        
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    my_app = Ui_Conversor_Unidades()
    my_app.show()
    sys.exit(app.exec_())
    
    
