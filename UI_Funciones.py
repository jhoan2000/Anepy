"""
Created on Tue May 17 01:34:16 2022

@author: JHOANSMITHMOSQUERAPE
"""

from PyQt5 import QtWidgets
#from UI_Porticos import Ui_Porticos

class Ui_Funciones(QtWidgets.QMainWindow):
    
    
    def Fn_inicializar(self):
        #self.ui = Ui_Porticos()
        
        E  = 21000
        
        datos_Elem = [
            #Elem, Ni, Nf, b, h, E,
            ["1", 1, 2, 0.4, 0.4, E],
            ["2", 2, 3, 0.3, 0.3, E],
            ["3", 2, 5, 0.2, 0.5, E],
            ["4", 3, 6, 0.2, 0.5, E],
            ["5", 4, 5, 0.4, 0.4, E],
            ["6", 5, 6, 0.3, 0.3, E],
            ["7", 5, 7, 0.2, 0.5, E],
            ["8", 7, 9, 0.2, 0.5, E],
            ["9", 8, 9, 0.4, 0.4, E],
             ]
            
        row = len(datos_Elem)
        col = len(datos_Elem[0])
        
        self.ui.sp_nElem.setValue(row)
        
        for i in range(row):
            
            self.ui.tbl_Elem.insertRow(i) # Inserta una columna en la tabla
            for j in range(col):
                celda = QtWidgets.QTableWidgetItem(str(datos_Elem[i][j]))
                self.ui.tbl_Elem.setItem(i, j,celda )
                self.ui.tbl_Elem.update()
        
        
        datos_Nod = [
            #Nodo, cx, cy
            [1, 0, 0],
            [2, 0, 4],
            [3, 0, 7],
            [4, 5.2, 0],
            [5, 5.2, 4],
            [6, 5.2, 7],
            [7, 7.8, 4],
            [8, 10.1, 1.5],
            [9, 10.1, 4],
            ]
        
        row = len(datos_Nod)
        col = len(datos_Nod[0])
        
        self.ui.sp_nNo.setValue(row)
        
        for i in range(row):
            
            self.ui.tbl_Nod.insertRow(i) # Inserta una columna en la tabla
            for j in range(col):
                celda = QtWidgets.QTableWidgetItem(str(datos_Nod[i][j]))
                self.ui.tbl_Nod.setItem(i, j,celda )
                self.ui.tbl_Nod.update()
        
        
        datos_Fuer = [
            #Nod, fx, fy, Mz
            [2, 200, 0, 0],
            [3, 400, 0, 0],
            [7, 0, -20, 0],
            ]
        try:
            row = len(datos_Fuer)
            col = len(datos_Fuer[0])
            
            self.ui.sp_nFuer.setValue(row)
            
            for i in range(row):
                
                self.ui.tbl_Fuer.insertRow(i) # Inserta una columna en la tabla
                for j in range(col):
                    celda = QtWidgets.QTableWidgetItem(str(datos_Fuer[i][j]))
                    self.ui.tbl_Fuer.setItem(i, j,celda )
                    self.ui.tbl_Fuer.update()
        except IndexError: pass
                
        datos_FuerW = [
            # ["1", 0, ((10*4)/7)],
            # ["2",((10*4)/7), 10],
            ["3",-8, -8], #"""CASO ANALIZAR######################"""############################
            ["4",-8, -8],
            ["7",-8, -8,],
            ["8",-8, -8,],
            ]
        
        row = len(datos_FuerW)
        col = len(datos_FuerW[0])
        self.ui.sp_nFuer_W.setValue(row)
        for i in range(row):
            self.ui.tbl_Fuer_W.insertRow(i) # Inserta una columna en la tabla
            for j in range(col):
                celda = QtWidgets.QTableWidgetItem(str(datos_FuerW[i][j]))
                self.ui.tbl_Fuer_W.setItem(i, j, celda)
                self.ui.tbl_Fuer_W.update()
        
        
        
        datos_Rest = [
                #Tipo de Apoyo, Nodo
                # Simple
                # Articulado
                # Empotrado
            ["Empotrado", 1],
            ["Empotrado", 4,],
            ["Empotrado", 8,],
            ]
        row = len(datos_Rest)
        col = len(datos_Rest[0])
        
        self.ui.sp_nRest.setValue(row)
        attr  = ['Simple', 'Articulado', 'Empotrado']
        for i in range(row):
            
            self.ui.tbl_Rest.insertRow(i) # Inserta una columna en la tabla
            for j in range(col):
                
                celda = QtWidgets.QTableWidgetItem(str(datos_Rest[i][j]))
                self.ui.tbl_Rest.setItem(i, j,celda )
                
                comboBox = QtWidgets.QComboBox()
                
                comboBox.addItems(attr)
                comboBox.setCurrentText(str(datos_Rest[i][0]))
                self.ui.tbl_Rest.setCellWidget(i, 0, comboBox)
                self.ui.tbl_Rest.update()
                
        ####################################
        #DIBUJO DE RESTRICCIONES EN EL CANVAS
        #####################################
        self.ploteo = self.ui.wgt_Rest.canvas
        self.ploteo.ax.clear()

        
        #Apoyo libre
        
        self.ploteo.ax.plot(1, 0.5, 'og', ms = 10) # corx, cory, tipo, grosor
        self.ploteo.ax.text(0.9, 1.02, "Simple", color = "#364b4a", size = 9) # corx, cory, tipo, grosor
        #Apoyo articulado
        
        self.ploteo.ax.plot(2, 0.5, '^b', ms = 10) # corx, cory, tipo, grosor
        self.ploteo.ax.text(1.8, 1.02, "Articulado", color = "#364b4a", size = 9)
        
        #Apoyo empotrado
        
        self.ploteo.ax.plot(3, 0.5, marker = '$\U000025AC$', ms = 15, c = 'r' ) # corx, cory, tipo, grosor
        self.ploteo.ax.text(2.8, 1.02, "Empotrado", color = "#364b4a", size = 9)
        # Maximixar espacio
        # Max Ejes x y Y
        self.ploteo.ax.axis([0.5, 3.5, 0, 2 ])# Limitando el eje x
        self.ploteo.fig.subplots_adjust(0, 0, 1, 1)
        self.nombre_arch("Inicializador") # Mustra nombre de archivo en interfaz
      
        
        
    def Wgt_ComboBox(self):
        # Cambio de paginas
        self.ui.cb_elemento.currentTextChanged.connect(self.Fn_elementos)
        self.ui.cb_convertir_de.currentTextChanged.connect(self.Fn_Sistema_unidades)
        
        pass
    # Cuando se acciona un spinbox
    def Wgt_SpinBox(self):
        self.ui.sp_nElem.valueChanged.connect(lambda: self.AgregarRenglonSinCombo('E')) 
        self.ui.sp_nNo.valueChanged.connect(lambda: self.AgregarRenglonSinCombo('N'))
        self.ui.sp_nFuer.valueChanged.connect(lambda: self.AgregarRenglonSinCombo('F'))
        self.ui.sp_nRest.valueChanged.connect(lambda: self.AgregarRenglonConCombo('R'))
        self.ui.sp_nFuer_W.valueChanged.connect(lambda: self.AgregarRenglonSinCombo('FW'))

    def Wgt_PushBoton(self):
        self.ui.btn_analizar.clicked.connect(self.guardar)
        self.ui.btn_analizar.clicked.connect(self.Fn_visualizar_porticos)
        self.ui.btn_analizar.clicked.connect(self.Fn_MatricesRigidezGUI)
        self.ui.btn_analizar.clicked.connect(self.Fn_grado_delta_elemento_fuerzas_internas)
        
        # Bar sup
        self.ui.btn_nuevo.clicked.connect(self.nuevo)
        self.ui.btn_nuevo.setToolTip("Nuevo Archivo (Control + N)") # ventana emergente de informacion
        
        self.ui.btn_abrir.clicked.connect(self.abrir)
        self.ui.btn_abrir.setToolTip("Abrir Archivo (Control + O)") # ventana emergente de informacion
        
        self.ui.btn_guardar.clicked.connect(self.guardar)
        self.ui.btn_guardar.setToolTip("Guardar Archivo (Control + S)") # ventana emergente de informacion
        
        self.ui.btn_inicio.clicked.connect(lambda: self.cambiarPagina("INICIO"))
        self.ui.btn_inicio.setToolTip("Ventana de inicio ") # ventana emergente de informacion
        
        self.ui.btn_matrices.clicked.connect(lambda: self.cambiarPagina("MATRICES DE RIGIDEZ"))
        self.ui.btn_matrices.setToolTip("Matrices de Rigidez (Control + K)") # ventana emergente de informacion
        
        self.ui.btn_fuerzas.clicked.connect(lambda: self.cambiarPagina("FUERZAS"))
        self.ui.btn_fuerzas.setToolTip("Fuerzas Internas (Control + F)") # ventana emergente de informacion
        
        self.ui.btn_deformada.clicked.connect(lambda: self.cambiarPagina("DEFORMADA"))
        self.ui.btn_deformada.setToolTip("Deformada (Control + D)") # ventana emergente de informacion
        self.ui.btn_amp_deformada.clicked.connect(self.Fn_amplificar_deformada_2)
        self.ui.btn_amp_deformada.setToolTip("Escalar")
        
        self.ui.btn_delta_fuerza.clicked.connect(lambda: self.cambiarPagina("DESPLAZAMIENTOS-FUERZAS"))
        self.ui.btn_delta_fuerza.setToolTip("Desplazamientos y fuerzas")
        
        self.ui.btn_screen_deformada.clicked.connect(self.capturar_defromada)
        
        #self.ui..clicked.connect(self.)
        
    def Wgt_Slider(self):
        self.ui.slider_Elem.valueChanged.connect(self.Fn_grado_delta_elemento_fuerzas_internas)
        self.ui.slider_zoom_defor.valueChanged.connect(self.Fn_amplificar_deformada_1)
        #self.ui.slider_zoom_defor.valueChanged.connect(self.Fn_visualizar_deformada)
    def Wgt_Barra(self):
        self.ui.actionNuevo.triggered.connect(self.nuevo)
        self.ui.actionAbrir.triggered.connect(self.abrir)
        self.ui.actionGuardar.triggered.connect(self.guardar)
        self.ui.actionSalir.triggered.connect(self.salir)
        ##################################
        self.ui.actionTema_claro.triggered.connect(lambda:self.Fn_Cambiar_Tema('claro'))
        self.ui.actionTema_oscuro.triggered.connect(lambda:self.Fn_Cambiar_Tema('oscuro'))
        ######################33
        self.ui.actionInformacion.triggered.connect(self.ven_creditos)
        self.ui.actionManual_de_uso.triggered.connect(self.Fn_manual_de_uso)
        ###################################3
        
        self.ui.actionConversor_de_unidades.triggered.connect(self.ven_conversiones)
        
    
        
    