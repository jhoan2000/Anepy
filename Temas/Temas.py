# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 14:36:48 2023

@author: Estudiante
"""
cbg_bar = 'rgb(4, 107, 153)'
bar = """background-color: {}.;"""
bar = bar.format(cbg_bar)

clbl_arch = "rgb(222, 222, 222)"
label_archivo = """QLabel[ background-color: None;
/*Letra*/font: 10pt \"Arial\" color: {color};]"""
label_archivo = label_archivo.format(color=clbl_arch)
label_archivo = label_archivo.replace("[", "{")
label_archivo = label_archivo.replace( "]","}")

cbg_btn = "rgb(2, 85, 120)"
chv_btn = "rgb(0, 207, 255)"
cpush_btn = "rgb(173, 238, 236)"
btn = """QPushButton[
                /* Color de fondo*/\
                background-color: {0}.;
                font: 75 12pt \"Bell MT\";
                border-radius : 4px;]
                /* Cambia color al estar sobre*/
                QPushButton:hover[
                background-color: {1} ;]
                /* Cambia color al dar click*/
                QPushButton:pressed[
                background-color: {2};]
                """
btn = btn.format(cbg_btn,chv_btn,cpush_btn)
btn = btn.replace("[", "{")
btn = btn.replace( "]","}")


cbg_pag = "rgb(23, 123, 189)"
cb_paginas = """
 background-color: ;""".format(cbg_pag)



cbor_groupbox = "rgb(255, 255, 255)"  
cfont_groubox = "rgb(255, 255, 255)"
groupBox = """QGroupBox[
/*Borde*/
border: 2px solid {};
"border-radius: 5px;
    /*Letra*/
    font: 15pt \"Impact\";
    color: {};
]"""

groupBox = groupBox.format(cbor_groupbox,cfont_groubox )
groupBox = groupBox.replace("[", "{")
groupBox = groupBox.replace( "]","}")


cbg_spn= "rgb(255, 255, 255)"
cbor_spn = "rgb(240, 240, 240)"
cfont_spn = "rgb(1, 1, 1)"
spn = """QSpinBox[
    /* Color de fondo*/
    background-color: {}; 
    /* borde*/
    border-radius : 5px;
    border : 2px solid  {};
    /* Color de letras*/
    color: {};
    font: 10pt \"Times New Roman\";
    ]
QComboBox:hover[border : 2px solid rgb(254, 251, 216);
]"""
spn = spn.format(cbg_spn,cbor_spn,cfont_spn )
spn = spn.replace("[", "{")
spn = spn.replace( "]","}")

cbg_tbl = "rgb(255, 255, 255)"
cfont_tbl = "rgb(0, 0, 0)"
cbghd_tbl = "rgb(0, 159, 195)"
cfonthd_tbl = "rgb(0, 0, 0)"
tbl = """QTableWidget[
    background-color:{} ;
    border-radius : 5px;
    color: {};
    font: 75 11pt \"Times New Roman\";
    ]
    QHeaderView::section[
        border-radius : 1px;
        background-color: {};
        color:{} ;
        font: 75 11pt \"Times New Roman\";
    ]
    """
tbl = tbl.format(cbg_tbl,cfont_tbl,cbghd_tbl, cfonthd_tbl )
tbl = tbl.replace("[", "{")
tbl = tbl.replace( "]","}")
  
    
    
cbg_wgt = "rgb(179, 239, 255)"
cbor_wgt = "rgb(205, 205, 205)"
wgt = """/* color de fondo*/
background-color: {};
/*borde redondo*/
border-radius : 10px;
/* linea de borde*/
border : 2px solid {};
""".format(cbg_wgt,cbor_wgt)




cbg_mnu = "rgb(255, 255, 255)"  
cfont_mnu = " rgb(0, 0, 0)" 
cbg_imnu = "rgb(129, 185, 182)"  
cfont_imnu = " rgb(255,255,255)"          
mnu = """
background-color:{} ; color: {};
QMenu::item:selected [
    background-color: {};
    color:{};
]"""

mnu = mnu.format(cbg_mnu,cfont_mnu, cbg_imnu,cfont_imnu)
mnu = mnu.replace("[", "{")
mnu = mnu.replace( "]","}")

cbg_frm = "rgb(4, 120, 170)"
frm= """
background-color: {};
border-radius: 5px;""".format(cbg_frm)