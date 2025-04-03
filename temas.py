# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 15:52:45 2023

@author: Estudiante
"""
class Fn_Cambiar_Tema:
    def __init__(self,modo):
        if modo == "claro":
            self.tema = "rgb(213, 244, 230)"

            self.ui.tbl_Rest.update()
            self.modo_claro()
        if modo == "oscuro":
            self.modo_oscuro()
            self.tema = "#C1D4D9"
            
        self.update()
    def modo_claro(self):
        
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
        #self.ui.btn_analizar.setStyleSheet(stybotones)
        self.ui.btn_nuevo.setStyleSheet(stybotones)
        self.ui.btn_abrir.setStyleSheet(stybotones)
        self.ui.btn_guardar.setStyleSheet(stybotones)
        self.ui.btn_fuerzas.setStyleSheet(stybotones)
        self.ui.btn_matrices.setStyleSheet(stybotones)
        self.ui.btn_inicio.setStyleSheet(stybotones)
        self.ui.btn_deformada.setStyleSheet(stybotones)
        #self.ui.btn_amp_deformada.setStyleSheet(stybotones)
        
        #-------------------------------------------------------------------------------#
        cbg_tbl = "rgb(255, 255, 255)"
        cfont_tbl = "rgb(0, 0, 0)"
        cbghd_tbl = "rgb(0, 159, 195)"
        cfonthd_tbl = "rgb(0, 0, 0)"
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
        font: 87 20pt "Segoe UI Black";
        background-color: none;
        ]""".format(cbg_frm, cbg_qline, cfont_label )
        
        styframe_2 = styframe_2.replace("[", "{")
        styframe_2 = styframe_2.replace( "]","}")
        self.ui.frame_2.setStyleSheet(styframe_2)
    
    def modo_oscuro(self):
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
        QMenuBar[
        background-color:{} ; color: {};]
        
        QMenu::item:selected [
            background-color: {};
            color:{};
        ]
        
        QMenuBar::item [
            spacing: 3px;           
            padding: 2px 10px;
            background-color: {} ;
            color: {};  
        ]
        
        """

        mnu = mnu.format(cbg_mnu,cfont_mnu,cbg_is,cfont_is, cbg_imnu,cfont_imnu)
        mnu = mnu.replace("[", "{")
        mnu = mnu.replace( "]","}")
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