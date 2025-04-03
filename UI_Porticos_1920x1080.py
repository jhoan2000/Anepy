# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Porticos_v3_1920x1080nyDeQW.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

import os

from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt, QTimer, )
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5.QtWidgets import *

from UI_Matplotlib_PyQt5 import MatplotlibWidgetaLienzo

basedir = os.path.dirname(__file__)
class Ui_Porticos_1920x1080(object):
    def setupUi(self, Porticos_1920x1080):
        if not Porticos_1920x1080.objectName():
            Porticos_1920x1080.setObjectName(u"Porticos_1920x1080")
        Porticos_1920x1080.resize(1464, 988)
        Porticos_1920x1080.setMaximumSize(QSize(16777215, 16777215))
       
        self.icon = QIcon(os.path.join(basedir, 'Logo.ico'))
        Porticos_1920x1080.setWindowIcon(self.icon)
        self.actionNuevo = QAction(Porticos_1920x1080)
        self.actionNuevo.setObjectName(u"actionNuevo")
        self.actionAbrir = QAction(Porticos_1920x1080)
        self.actionAbrir.setObjectName(u"actionAbrir")
        self.actionGuardar = QAction(Porticos_1920x1080)
        self.actionGuardar.setObjectName(u"actionGuardar")
        self.actionSalir = QAction(Porticos_1920x1080)
        self.actionSalir.setObjectName(u"actionSalir")
        self.actionTema_claro = QAction(Porticos_1920x1080)
        self.actionTema_claro.setObjectName(u"actionTema_claro")
        self.actionTema_oscuro = QAction(Porticos_1920x1080)
        self.actionTema_oscuro.setObjectName(u"actionTema_oscuro")
        self.actionConversor_de_unidades = QAction(Porticos_1920x1080)
        self.actionConversor_de_unidades.setObjectName(u"actionConversor_de_unidades")
        self.actionInformacion = QAction(Porticos_1920x1080)
        self.actionInformacion.setObjectName(u"actionInformacion")
        self.actionManual_de_uso = QAction(Porticos_1920x1080)
        self.actionManual_de_uso.setObjectName(u"actionManual_de_uso")
        self.centralwidget = QWidget(Porticos_1920x1080)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"")
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1462, 964))
        self.scrollAreaWidgetContents.setMinimumSize(QSize(0, 0))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_10 = QFrame(self.scrollAreaWidgetContents)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(1350, 720))
        self.frame_10.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.cb_paginas = QFrame(self.frame_10)
        self.cb_paginas.setObjectName(u"cb_paginas")
        self.cb_paginas.setEnabled(True)
        self.cb_paginas.setGeometry(QRect(0, 36, 16777215, 975))
        self.cb_paginas.setStyleSheet(u"/**background-color: rgb(4, 107, 153);**/\n"
"background-color: rgb(23, 123, 189);\n"
"\n"
"")
        self.cb_paginas.setFrameShape(QFrame.StyledPanel)
        self.cb_paginas.setFrameShadow(QFrame.Raised)
        self.stackedWidget = QStackedWidget(self.cb_paginas)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setEnabled(True)
        self.stackedWidget.setGeometry(QRect(9, -1, 1501, 901))
        self.stackedWidget.setMouseTracking(False)
        self.stackedWidget.setFrameShape(QFrame.NoFrame)
        self.pagina_1 = QWidget()
        self.pagina_1.setObjectName(u"pagina_1")
        self.groupBox_1 = QGroupBox(self.pagina_1)
        self.groupBox_1.setObjectName(u"groupBox_1")
        self.groupBox_1.setEnabled(True)
        self.groupBox_1.setGeometry(QRect(0, 10, 1341, 841))
        self.groupBox_1.setStyleSheet(u"QGroupBox{\n"
"/*Borde*/\n"
"border: 2px solid rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"\n"
"	/*Letra*/\n"
"	font: 26px \"Impact\";\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.tbl_Nod = QTableWidget(self.groupBox_1)
        if (self.tbl_Nod.columnCount() < 3):
            self.tbl_Nod.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tbl_Nod.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tbl_Nod.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tbl_Nod.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tbl_Nod.setObjectName(u"tbl_Nod")
        self.tbl_Nod.setGeometry(QRect(504, 84, 240, 251))
        self.tbl_Nod.setStyleSheet(u"QTableWidget{\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius : 5px;\n"
"color: rgb(0, 0, 0);\n"
"font: 75 16px \"Calibri\";\n"
"}\n"
"\n"
"QTableWidget:hover{\n"
"\n"
"border : 2px solid  rgb(0, 255, 255);\n"
"\n"
"}\n"
"\n"
"QHeaderView::section{\n"
"border-radius : 1px;\n"
"	background-color: rgb(0, 159, 195);\n"
"\n"
"color: rgb(0, 0, 0);\n"
"font: 75 16px \"Times New Roman\";\n"
"\n"
"}\n"
"\n"
"QTableWidget:hover{\n"
"\n"
"border : 2px solid  rgb(0, 255, 255);\n"
"\n"
"}\n"
"")
        self.tbl_Nod.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tbl_Nod.setRowCount(0)
        self.tbl_Nod.horizontalHeader().setMinimumSectionSize(42)
        self.tbl_Nod.horizontalHeader().setDefaultSectionSize(80)
        self.tbl_Nod.verticalHeader().setVisible(False)
        self.tbl_Nod.verticalHeader().setDefaultSectionSize(29)
        self.tbl_Fuer = QTableWidget(self.groupBox_1)
        if (self.tbl_Fuer.columnCount() < 4):
            self.tbl_Fuer.setColumnCount(4)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tbl_Fuer.setHorizontalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tbl_Fuer.setHorizontalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tbl_Fuer.setHorizontalHeaderItem(2, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tbl_Fuer.setHorizontalHeaderItem(3, __qtablewidgetitem6)
        self.tbl_Fuer.setObjectName(u"tbl_Fuer")
        self.tbl_Fuer.setGeometry(QRect(9, 398, 320, 180))
        self.tbl_Fuer.setStyleSheet(u"QTableWidget{\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius : 5px;\n"
"color: rgb(0, 0, 0);\n"
"font: 75 16px \"Calibri\";\n"
"}\n"
"\n"
"QTableWidget:hover{\n"
"\n"
"border : 2px solid  rgb(0, 255, 255);\n"
"\n"
"}\n"
"\n"
"QHeaderView::section{\n"
"border-radius : 1px;\n"
"	background-color: rgb(0, 159, 195);\n"
"\n"
"color: rgb(0, 0, 0);\n"
"font: 75 16px \"Times New Roman\";\n"
"\n"
"}\n"
"\n"
"QTableWidget:hover{\n"
"\n"
"border : 2px solid  rgb(0, 255, 255);\n"
"\n"
"}\n"
"")
        self.tbl_Fuer.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tbl_Fuer.setRowCount(0)
        self.tbl_Fuer.horizontalHeader().setMinimumSectionSize(42)
        self.tbl_Fuer.horizontalHeader().setDefaultSectionSize(80)
        self.tbl_Fuer.verticalHeader().setVisible(False)
        self.tbl_Fuer.verticalHeader().setMinimumSectionSize(20)
        self.tbl_Fuer.verticalHeader().setDefaultSectionSize(20)
        self.wgt_Rest = MatplotlibWidgetaLienzo(self.groupBox_1)
        self.wgt_Rest.setObjectName(u"wgt_Rest")
        self.wgt_Rest.setGeometry(QRect(368, 650, 331, 180))
        self.wgt_Rest.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius : 5px")
        self.wgt_porticos = MatplotlibWidgetaLienzo(self.groupBox_1)
        self.wgt_porticos.setObjectName(u"wgt_porticos")
        self.wgt_porticos.setGeometry(QRect(758, 80, 574, 481))
        self.wgt_porticos.setCursor(QCursor(Qt.ArrowCursor))
        self.wgt_porticos.setMouseTracking(False)
        self.wgt_porticos.setStyleSheet(u"/* color de fondo*/\n"
"\n"
"background-color: rgb(179, 239, 255);\n"
"/*borde redondo*/\n"
"border-radius : 10px;\n"
"/* linea de borde*/\n"
"border : 2px solid rgb(205, 205, 205);\n"
"")
        self.label_13 = QLabel(self.groupBox_1)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(9, 599, 269, 21))
        self.label_13.setStyleSheet(u"QLabel{\n"
"background-color: None;\n"
"	color: rgb(255, 255, 255);\n"
"font-size: 12px;\n"
"}")
        self.tbl_Rest = QTableWidget(self.groupBox_1)
        if (self.tbl_Rest.columnCount() < 3):
            self.tbl_Rest.setColumnCount(3)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tbl_Rest.setHorizontalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tbl_Rest.setHorizontalHeaderItem(1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tbl_Rest.setHorizontalHeaderItem(2, __qtablewidgetitem9)
        self.tbl_Rest.setObjectName(u"tbl_Rest")
        self.tbl_Rest.setGeometry(QRect(8, 650, 331, 180))
        self.tbl_Rest.setStyleSheet(u"QTableWidget{\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius : 5px;\n"
"color: rgb(0, 0, 0);\n"
"font: 75 16px \"Calibri\";\n"
"}\n"
"\n"
"QTableWidget:hover{\n"
"\n"
"border : 2px solid  rgb(0, 255, 255);\n"
"\n"
"}\n"
"\n"
"QHeaderView::section{\n"
"border-radius : 1px;\n"
"	background-color: rgb(0, 159, 195);\n"
"\n"
"color: rgb(0, 0, 0);\n"
"font: 75 16px \"Times New Roman\";\n"
"\n"
"}\n"
"\n"
"QTableWidget:hover{\n"
"\n"
"border : 2px solid  rgb(0, 255, 255);\n"
"\n"
"}\n"
"")
        self.tbl_Rest.setRowCount(0)
        self.tbl_Rest.horizontalHeader().setMinimumSectionSize(42)
        self.tbl_Rest.horizontalHeader().setDefaultSectionSize(110)
        self.tbl_Rest.horizontalHeader().setProperty("showSortIndicator", False)
        self.tbl_Rest.verticalHeader().setVisible(False)
        self.tbl_Rest.verticalHeader().setCascadingSectionResizes(False)
        self.tbl_Rest.verticalHeader().setMinimumSectionSize(20)
        self.tbl_Rest.verticalHeader().setDefaultSectionSize(25)
        self.tbl_Rest.verticalHeader().setHighlightSections(True)
        self.sp_nRest = QSpinBox(self.groupBox_1)
        self.sp_nRest.setObjectName(u"sp_nRest")
        self.sp_nRest.setGeometry(QRect(282, 605, 56, 16))
        self.sp_nRest.setCursor(QCursor(Qt.PointingHandCursor))
        self.sp_nRest.setStyleSheet(u"\n"
"QSpinBox{\n"
"\n"
"/* Color de fondo*/\n"
"background-color: rgb(255, 255, 255); \n"
"\n"
"/* borde*/\n"
"border-radius : 5px;\n"
"border : 2px solid  rgb(240, 240, 240);\n"
"\n"
"/* Color de letras*/\n"
"	color: rgb(1, 1, 1);\n"
"\n"
"	font: 10pt \"Times New Roman\";\n"
"}\n"
"\n"
"\n"
"QComboBox:hover{\n"
"\n"
"\n"
"border : 2px solid rgb(254, 251, 216);\n"
"\n"
"}\n"
"\n"
"")
        self.sp_nRest.setAlignment(Qt.AlignCenter)
        self.label_19 = QLabel(self.groupBox_1)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(372, 599, 191, 29))
        self.label_19.setStyleSheet(u"QLabel{\n"
"background-color: None;\n"
"	color: rgb(255, 255, 255);\n"
"font-size:16px;\n"
"}")
        self.btn_analizar = QPushButton(self.groupBox_1)
        self.btn_analizar.setObjectName(u"btn_analizar")
        self.btn_analizar.setGeometry(QRect(968, 582, 151, 31))
        self.btn_analizar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_analizar.setStyleSheet(u"QPushButton{\n"
"/* Color de fondo*/\n"
"/**background-color: rgb(213, 244, 230);**/\n"
"	background-color: rgb(11, 65, 116);\n"
"	color: rgb(255, 255, 255);\n"
"font: 75 18px \"Bell MT\";\n"
"border-radius : 4px;\n"
"/**border : 2px solid  rgb(240, 240, 240);**/\n"
"\n"
"}\n"
"\n"
"/* Cambia color al estar sobre*/\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(18, 90, 140);\n"
"\n"
"}\n"
"/* Cambia color al dar click*/\n"
"QPushButton:pressed{\n"
"\n"
"background-color:rgb(173, 238, 236);\n"
"\n"
"}\n"
"\n"
"\n"
"")
        self.tbl_Fuer_W = QTableWidget(self.groupBox_1)
        if (self.tbl_Fuer_W.columnCount() < 3):
            self.tbl_Fuer_W.setColumnCount(3)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tbl_Fuer_W.setHorizontalHeaderItem(0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tbl_Fuer_W.setHorizontalHeaderItem(1, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tbl_Fuer_W.setHorizontalHeaderItem(2, __qtablewidgetitem12)
        self.tbl_Fuer_W.setObjectName(u"tbl_Fuer_W")
        self.tbl_Fuer_W.setGeometry(QRect(369, 398, 320, 180))
        self.tbl_Fuer_W.setStyleSheet(u"QTableWidget{\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius : 5px;\n"
"color: rgb(0, 0, 0);\n"
"font: 75 16px \"Calibri\";\n"
"}\n"
"\n"
"QTableWidget:hover{\n"
"\n"
"border : 2px solid  rgb(0, 255, 255);\n"
"\n"
"}\n"
"\n"
"QHeaderView::section{\n"
"border-radius : 1px;\n"
"	background-color: rgb(0, 159, 195);\n"
"\n"
"color: rgb(0, 0, 0);\n"
"font: 75 16px \"Times New Roman\";\n"
"\n"
"}\n"
"\n"
"QTableWidget:hover{\n"
"\n"
"border : 2px solid  rgb(0, 255, 255);\n"
"\n"
"}\n"
"")
        self.tbl_Fuer_W.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tbl_Fuer_W.horizontalHeader().setDefaultSectionSize(112)
        self.tbl_Fuer_W.verticalHeader().setCascadingSectionResizes(False)
        self.tbl_Fuer_W.verticalHeader().setMinimumSectionSize(20)
        self.tbl_Fuer_W.verticalHeader().setDefaultSectionSize(25)
        self.tbl_Elem = QTableWidget(self.groupBox_1)
        if (self.tbl_Elem.columnCount() < 6):
            self.tbl_Elem.setColumnCount(6)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tbl_Elem.setHorizontalHeaderItem(0, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tbl_Elem.setHorizontalHeaderItem(1, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tbl_Elem.setHorizontalHeaderItem(2, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tbl_Elem.setHorizontalHeaderItem(3, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tbl_Elem.setHorizontalHeaderItem(4, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tbl_Elem.setHorizontalHeaderItem(5, __qtablewidgetitem18)
        self.tbl_Elem.setObjectName(u"tbl_Elem")
        self.tbl_Elem.setGeometry(QRect(7, 84, 480, 251))
        font = QFont()
        font.setFamilies([u"Calibri"])
        font.setBold(False)
        font.setItalic(False)
        self.tbl_Elem.setFont(font)
        self.tbl_Elem.setStyleSheet(u"QTableWidget{\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius : 5px;\n"
"color: rgb(0, 0, 0);\n"
"font: 75 12px \"Calibri\";\n"
"\n"
"}\n"
"\n"
"\n"
"QTableWidget:item:selected:focus{\n"
"border : 2px solid  rgb(23, 123, 189);\n"
"color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QTableWidget:hover{\n"
"\n"
"border : 2px solid  rgb(0, 255, 255);\n"
"\n"
"}\n"
"\n"
"QHeaderView::section{\n"
"border-radius : 1px;\n"
"	background-color: rgb(0, 159, 195);\n"
"\n"
"color: rgb(0, 0, 0);\n"
"font: 75 16px \"Times New Roman\";\n"
"\n"
"}\n"
"\n"
"QTableWidget:hover{\n"
"\n"
"border : 2px solid  rgb(0, 255, 255);\n"
"\n"
"}\n"
"")
        self.tbl_Elem.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tbl_Elem.setEditTriggers(QAbstractItemView.AnyKeyPressed|QAbstractItemView.DoubleClicked|QAbstractItemView.EditKeyPressed)
        self.tbl_Elem.setProperty("showDropIndicator", True)
        self.tbl_Elem.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.tbl_Elem.setRowCount(0)
        self.tbl_Elem.horizontalHeader().setMinimumSectionSize(42)
        self.tbl_Elem.horizontalHeader().setDefaultSectionSize(80)
        self.tbl_Elem.verticalHeader().setVisible(False)
        self.tbl_Elem.verticalHeader().setMinimumSectionSize(20)
        self.tbl_Elem.verticalHeader().setDefaultSectionSize(20)
        self.label_33 = QLabel(self.groupBox_1)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setGeometry(QRect(156, 624, 47, 19))
        self.label_33.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font-size: 12px;")
        self.label_34 = QLabel(self.groupBox_1)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setGeometry(QRect(46, 624, 47, 19))
        self.label_34.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font-size: 12px;")
        self.frame = QFrame(self.groupBox_1)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(8, 54, 735, 31))
        self.frame.setStyleSheet(u"background-color: none;\n"
"font-size: 12px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(99, 8, 47, 16))
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lb_tbl_elem_B = QLabel(self.frame)
        self.lb_tbl_elem_B.setObjectName(u"lb_tbl_elem_B")
        self.lb_tbl_elem_B.setGeometry(QRect(262, 8, 29, 16))
        self.lb_tbl_elem_B.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(19, 8, 47, 16))
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"")
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(179, 8, 47, 16))
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lb_tbl_elem_h = QLabel(self.frame)
        self.lb_tbl_elem_h.setObjectName(u"lb_tbl_elem_h")
        self.lb_tbl_elem_h.setGeometry(QRect(342, 8, 29, 16))
        self.lb_tbl_elem_h.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lb_tbl_elem_E = QLabel(self.frame)
        self.lb_tbl_elem_E.setObjectName(u"lb_tbl_elem_E")
        self.lb_tbl_elem_E.setGeometry(QRect(418, 8, 43, 16))
        self.lb_tbl_elem_E.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lb_tbl_nod_cy = QLabel(self.frame)
        self.lb_tbl_nod_cy.setObjectName(u"lb_tbl_nod_cy")
        self.lb_tbl_nod_cy.setGeometry(QRect(678, 8, 29, 16))
        self.lb_tbl_nod_cy.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(518, 8, 47, 16))
        self.label_8.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lb_tbl_nod_cx = QLabel(self.frame)
        self.lb_tbl_nod_cx.setObjectName(u"lb_tbl_nod_cx")
        self.lb_tbl_nod_cx.setGeometry(QRect(598, 8, 29, 16))
        self.lb_tbl_nod_cx.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.frame_6 = QFrame(self.groupBox_1)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(12, 374, 677, 23))
        self.frame_6.setStyleSheet(u"background-color:none;\n"
"font-size: 12px;")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.label_11 = QLabel(self.frame_6)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(16, 4, 47, 16))
        self.label_11.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lb_tbl_f_fy = QLabel(self.frame_6)
        self.lb_tbl_f_fy.setObjectName(u"lb_tbl_f_fy")
        self.lb_tbl_f_fy.setGeometry(QRect(174, 4, 47, 16))
        self.lb_tbl_f_fy.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lb_tbl_fw_wi = QLabel(self.frame_6)
        self.lb_tbl_fw_wi.setObjectName(u"lb_tbl_fw_wi")
        self.lb_tbl_fw_wi.setGeometry(QRect(502, 4, 47, 16))
        self.lb_tbl_fw_wi.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lb_tbl_f_fx = QLabel(self.frame_6)
        self.lb_tbl_f_fx.setObjectName(u"lb_tbl_f_fx")
        self.lb_tbl_f_fx.setGeometry(QRect(94, 4, 47, 16))
        self.lb_tbl_f_fx.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lb_tbl_f_m = QLabel(self.frame_6)
        self.lb_tbl_f_m.setObjectName(u"lb_tbl_f_m")
        self.lb_tbl_f_m.setGeometry(QRect(256, 4, 47, 16))
        self.lb_tbl_f_m.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lb_tbl_fw_wf = QLabel(self.frame_6)
        self.lb_tbl_fw_wf.setObjectName(u"lb_tbl_fw_wf")
        self.lb_tbl_fw_wf.setGeometry(QRect(614, 4, 47, 16))
        self.lb_tbl_fw_wf.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_18 = QLabel(self.frame_6)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(390, 4, 47, 16))
        self.label_18.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.widget = QWidget(self.groupBox_1)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(8, 35, 261, 23))
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_20 = QLabel(self.widget)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMinimumSize(QSize(56, 0))
        self.label_20.setStyleSheet(u"QLabel{\n"
"background-color: None;\n"
"	color: rgb(255, 255, 255);\n"
"font-size:10px;\n"
"\n"
"}")

        self.horizontalLayout_2.addWidget(self.label_20)

        self.sp_nElem = QSpinBox(self.widget)
        self.sp_nElem.setObjectName(u"sp_nElem")
        self.sp_nElem.setMinimumSize(QSize(56, 0))
        self.sp_nElem.setMaximumSize(QSize(56, 16777215))
        self.sp_nElem.setCursor(QCursor(Qt.PointingHandCursor))
        self.sp_nElem.setStyleSheet(u"\n"
"QSpinBox{\n"
"\n"
"/* Color de fondo*/\n"
"background-color: rgb(255, 255, 255); \n"
"\n"
"/* borde*/\n"
"border-radius : 5px;\n"
"border : 2px solid  rgb(240, 240, 240);\n"
"\n"
"/* Color de letras*/\n"
"	color: rgb(1, 1, 1);\n"
"\n"
"	font: 10pt \"Times New Roman\";\n"
"}\n"
"\n"
"\n"
"QComboBox:hover{\n"
"\n"
"\n"
"border : 2px solid rgb(254, 251, 216);\n"
"\n"
"}\n"
"\n"
"")
        self.sp_nElem.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.sp_nElem)

        self.widget1 = QWidget(self.groupBox_1)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(501, 35, 241, 23))
        self.horizontalLayout_3 = QHBoxLayout(self.widget1)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_21 = QLabel(self.widget1)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setStyleSheet(u"QLabel{\n"
"background-color: None;\n"
"	color: rgb(255, 255, 255);\n"
"font-size:10px;\n"
"\n"
"}")

        self.horizontalLayout_3.addWidget(self.label_21)

        self.sp_nNo = QSpinBox(self.widget1)
        self.sp_nNo.setObjectName(u"sp_nNo")
        self.sp_nNo.setMinimumSize(QSize(56, 0))
        self.sp_nNo.setMaximumSize(QSize(56, 16777215))
        self.sp_nNo.setCursor(QCursor(Qt.PointingHandCursor))
        self.sp_nNo.setStyleSheet(u"\n"
"QSpinBox{\n"
"\n"
"/* Color de fondo*/\n"
"background-color: rgb(255, 255, 255); \n"
"\n"
"/* borde*/\n"
"border-radius : 5px;\n"
"border : 2px solid  rgb(240, 240, 240);\n"
"\n"
"/* Color de letras*/\n"
"	color: rgb(1, 1, 1);\n"
"\n"
"	font: 10pt \"Times New Roman\";\n"
"}\n"
"\n"
"\n"
"QComboBox:hover{\n"
"\n"
"\n"
"border : 2px solid rgb(254, 251, 216);\n"
"\n"
"}\n"
"\n"
"")
        self.sp_nNo.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.sp_nNo)

        self.widget2 = QWidget(self.groupBox_1)
        self.widget2.setObjectName(u"widget2")
        self.widget2.setGeometry(QRect(10, 353, 231, 23))
        self.horizontalLayout_4 = QHBoxLayout(self.widget2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_22 = QLabel(self.widget2)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setStyleSheet(u"QLabel{\n"
"background-color: None;\n"
"	color: rgb(255, 255, 255);\n"
"font-size:10px;\n"
"\n"
"}")

        self.horizontalLayout_4.addWidget(self.label_22)

        self.sp_nFuer = QSpinBox(self.widget2)
        self.sp_nFuer.setObjectName(u"sp_nFuer")
        self.sp_nFuer.setMinimumSize(QSize(56, 0))
        self.sp_nFuer.setMaximumSize(QSize(56, 16777215))
        self.sp_nFuer.setCursor(QCursor(Qt.PointingHandCursor))
        self.sp_nFuer.setStyleSheet(u"\n"
"QSpinBox{\n"
"\n"
"/* Color de fondo*/\n"
"background-color: rgb(255, 255, 255); \n"
"\n"
"/* borde*/\n"
"border-radius : 5px;\n"
"border : 2px solid  rgb(240, 240, 240);\n"
"\n"
"/* Color de letras*/\n"
"	color: rgb(1, 1, 1);\n"
"\n"
"	font: 10pt \"Times New Roman\";\n"
"}\n"
"\n"
"\n"
"QComboBox:hover{\n"
"\n"
"\n"
"border : 2px solid rgb(254, 251, 216);\n"
"\n"
"}\n"
"\n"
"")
        self.sp_nFuer.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.sp_nFuer)

        self.widget3 = QWidget(self.groupBox_1)
        self.widget3.setObjectName(u"widget3")
        self.widget3.setGeometry(QRect(370, 353, 251, 23))
        self.horizontalLayout_5 = QHBoxLayout(self.widget3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_23 = QLabel(self.widget3)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setStyleSheet(u"QLabel{\n"
"background-color: None;\n"
"	color: rgb(255, 255, 255);\n"
"font-size:10px;\n"
"\n"
"}")

        self.horizontalLayout_5.addWidget(self.label_23)

        self.sp_nFuer_W = QSpinBox(self.widget3)
        self.sp_nFuer_W.setObjectName(u"sp_nFuer_W")
        self.sp_nFuer_W.setMinimumSize(QSize(56, 0))
        self.sp_nFuer_W.setMaximumSize(QSize(56, 16777215))
        self.sp_nFuer_W.setCursor(QCursor(Qt.PointingHandCursor))
        self.sp_nFuer_W.setStyleSheet(u"\n"
"QSpinBox{\n"
"\n"
"/* Color de fondo*/\n"
"background-color: rgb(255, 255, 255); \n"
"\n"
"/* borde*/\n"
"border-radius : 5px;\n"
"border : 2px solid  rgb(240, 240, 240);\n"
"\n"
"/* Color de letras*/\n"
"	color: rgb(1, 1, 1);\n"
"\n"
"	font: 10pt \"Times New Roman\";\n"
"}\n"
"\n"
"\n"
"QComboBox:hover{\n"
"\n"
"\n"
"border : 2px solid rgb(254, 251, 216);\n"
"\n"
"}\n"
"\n"
"")
        self.sp_nFuer_W.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.sp_nFuer_W)

        self.bar_cb_pg_2 = QFrame(self.pagina_1)
        self.bar_cb_pg_2.setObjectName(u"bar_cb_pg_2")
        self.bar_cb_pg_2.setEnabled(True)
        self.bar_cb_pg_2.setGeometry(QRect(0, 860, 861, 36))
        self.bar_cb_pg_2.setMaximumSize(QSize(16777215, 36))
        self.bar_cb_pg_2.setStyleSheet(u"/**background-color: rgb(213, 244, 230);**/background-color: rgb(4, 107, 153);\n"
"")
        self.bar_cb_pg_2.setFrameShape(QFrame.NoFrame)
        self.bar_cb_pg_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.bar_cb_pg_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_archivo = QLabel(self.bar_cb_pg_2)
        self.label_archivo.setObjectName(u"label_archivo")
        self.label_archivo.setStyleSheet(u"QLabel{\n"
"background-color: None;\n"
"	\n"
"/*Letra*/\n"
"	font: 10pt \"Arial\";\n"
"	\n"
"	\n"
"	color: rgb(222, 222, 222);\n"
"}")

        self.horizontalLayout.addWidget(self.label_archivo)

        self.cb_convertir_de = QComboBox(self.bar_cb_pg_2)
        self.cb_convertir_de.addItem("")
        self.cb_convertir_de.addItem("")
        self.cb_convertir_de.setObjectName(u"cb_convertir_de")
        self.cb_convertir_de.setMinimumSize(QSize(0, 20))
        self.cb_convertir_de.setMaximumSize(QSize(111, 16777215))
        font1 = QFont()
        font1.setFamilies([u"Times New Roman"])
        self.cb_convertir_de.setFont(font1)
        self.cb_convertir_de.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-radius :5px;\n"
"font-size:15px;")

        self.horizontalLayout.addWidget(self.cb_convertir_de)

        self.stackedWidget.addWidget(self.pagina_1)
        self.pagina_2 = QWidget()
        self.pagina_2.setObjectName(u"pagina_2")
        self.groupBox_2 = QGroupBox(self.pagina_2)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(0, 10, 1341, 261))
        self.groupBox_2.setStyleSheet(u"QGroupBox{\n"
"/*Borde*/\n"
"border: 2px solid rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"\n"
"	/*Letra*/\n"
"	font: 15pt \"Impact\";\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.label_24 = QLabel(self.groupBox_2)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(530, 138, 159, 31))
        self.label_24.setStyleSheet(u"QLabel{\n"
"background-color: None;\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.cb_elemento = QComboBox(self.groupBox_2)
        self.cb_elemento.setObjectName(u"cb_elemento")
        self.cb_elemento.setGeometry(QRect(690, 147, 51, 21))
        self.cb_elemento.setMinimumSize(QSize(0, 0))
        self.cb_elemento.setMaximumSize(QSize(377, 1000))
        font2 = QFont()
        font2.setFamilies([u"Times New Roman"])
        font2.setPointSize(14)
        font2.setBold(False)
        font2.setItalic(False)
        self.cb_elemento.setFont(font2)
        self.cb_elemento.setLayoutDirection(Qt.LeftToRight)
        self.cb_elemento.setStyleSheet(u"\n"
"QComboBox{\n"
"\n"
"/* Color de fondo*/\n"
"background-color: rgb(97, 134, 133); \n"
"\n"
"/* borde*/\n"
"border-radius : 5px;\n"
"border : 2px solid  rgb(240, 240, 240);\n"
"\n"
"/* Color de letras*/\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"	font: 14pt \"Times New Roman\";\n"
"}\n"
"\n"
"\n"
"QComboBox:hover{\n"
"\n"
"\n"
"border : 2px solid rgb(0, 255, 255);\n"
"\n"
"}\n"
"\n"
"")
        self.cb_elemento.setEditable(False)
        self.label_25 = QLabel(self.groupBox_2)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(10, 30, 391, 21))
        self.label_25.setStyleSheet(u"QLabel{\n"
"background-color: None;\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.tbl_MKGE = QTableWidget(self.groupBox_2)
        if (self.tbl_MKGE.columnCount() < 6):
            self.tbl_MKGE.setColumnCount(6)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tbl_MKGE.setHorizontalHeaderItem(0, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tbl_MKGE.setHorizontalHeaderItem(1, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tbl_MKGE.setHorizontalHeaderItem(2, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tbl_MKGE.setHorizontalHeaderItem(3, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tbl_MKGE.setHorizontalHeaderItem(4, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tbl_MKGE.setHorizontalHeaderItem(5, __qtablewidgetitem24)
        self.tbl_MKGE.setObjectName(u"tbl_MKGE")
        self.tbl_MKGE.setGeometry(QRect(820, 70, 481, 181))
        self.tbl_MKGE.viewport().setProperty("cursor", QCursor(Qt.ArrowCursor))
        self.tbl_MKGE.setStyleSheet(u"QTableWidget{\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius : 5px;\n"
"color: rgb(0, 0, 0);\n"
"font: 75 10pt \"Times New Roman\";\n"
"\n"
"}\n"
"QHeaderView::section{\n"
"border-radius : 1px;\n"
"	background-color: rgb(0, 159, 195);\n"
"\n"
"color: rgb(0, 0, 0);\n"
"font: 75 11pt \"Times New Roman\";\n"
"\n"
"}\n"
"")
        self.tbl_MKGE.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tbl_MKGE.setShowGrid(True)
        self.tbl_MKGE.setGridStyle(Qt.SolidLine)
        self.tbl_MKGE.setSortingEnabled(False)
        self.tbl_MKGE.setRowCount(0)
        self.tbl_MKGE.horizontalHeader().setCascadingSectionResizes(False)
        self.tbl_MKGE.horizontalHeader().setMinimumSectionSize(42)
        self.tbl_MKGE.horizontalHeader().setDefaultSectionSize(80)
        self.tbl_MKGE.horizontalHeader().setProperty("showSortIndicator", False)
        self.tbl_MKGE.verticalHeader().setVisible(False)
        self.tbl_MKGE.verticalHeader().setCascadingSectionResizes(False)
        self.tbl_MKGE.verticalHeader().setMinimumSectionSize(20)
        self.tbl_MKGE.verticalHeader().setDefaultSectionSize(30)
        self.tbl_MKGE.verticalHeader().setProperty("showSortIndicator", False)
        self.tbl_MKGE.verticalHeader().setStretchLastSection(False)
        self.label_26 = QLabel(self.groupBox_2)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(870, 40, 361, 21))
        self.label_26.setStyleSheet(u"QLabel{\n"
"background-color: None;\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.tbl_propiedades = QTableWidget(self.groupBox_2)
        if (self.tbl_propiedades.columnCount() < 5):
            self.tbl_propiedades.setColumnCount(5)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tbl_propiedades.setHorizontalHeaderItem(0, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tbl_propiedades.setHorizontalHeaderItem(1, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tbl_propiedades.setHorizontalHeaderItem(2, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tbl_propiedades.setHorizontalHeaderItem(3, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.tbl_propiedades.setHorizontalHeaderItem(4, __qtablewidgetitem29)
        self.tbl_propiedades.setObjectName(u"tbl_propiedades")
        self.tbl_propiedades.setGeometry(QRect(450, 10, 411, 51))
        self.tbl_propiedades.viewport().setProperty("cursor", QCursor(Qt.ArrowCursor))
        self.tbl_propiedades.setStyleSheet(u"QTableWidget{\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius : 5px;\n"
"color: rgb(0, 0, 0);\n"
"font: 75 10pt \"Calibri\";\n"
"}\n"
"\n"
"QTableWidget:hover{\n"
"\n"
"border : 2px solid  rgb(0, 255, 255);\n"
"\n"
"}\n"
"\n"
"QHeaderView::section{\n"
"border-radius : 1px;\n"
"	background-color: rgb(0, 159, 195);\n"
"\n"
"color: rgb(0, 0, 0);\n"
"font: 75 11pt \"Times New Roman\";\n"
"\n"
"}\n"
"\n"
"QTableWidget:hover{\n"
"\n"
"border : 2px solid  rgb(0, 255, 255);\n"
"\n"
"}\n"
"")
        self.tbl_propiedades.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tbl_propiedades.setShowGrid(True)
        self.tbl_propiedades.setGridStyle(Qt.SolidLine)
        self.tbl_propiedades.setSortingEnabled(False)
        self.tbl_propiedades.setRowCount(0)
        self.tbl_propiedades.horizontalHeader().setCascadingSectionResizes(False)
        self.tbl_propiedades.horizontalHeader().setMinimumSectionSize(42)
        self.tbl_propiedades.horizontalHeader().setDefaultSectionSize(82)
        self.tbl_propiedades.horizontalHeader().setHighlightSections(True)
        self.tbl_propiedades.horizontalHeader().setProperty("showSortIndicator", False)
        self.tbl_propiedades.verticalHeader().setVisible(False)
        self.tbl_propiedades.verticalHeader().setCascadingSectionResizes(False)
        self.tbl_propiedades.verticalHeader().setDefaultSectionSize(29)
        self.tbl_propiedades.verticalHeader().setProperty("showSortIndicator", False)
        self.tbl_propiedades.verticalHeader().setStretchLastSection(False)
        self.tbl_MKL = QTableWidget(self.groupBox_2)
        if (self.tbl_MKL.columnCount() < 6):
            self.tbl_MKL.setColumnCount(6)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.tbl_MKL.setHorizontalHeaderItem(0, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.tbl_MKL.setHorizontalHeaderItem(1, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.tbl_MKL.setHorizontalHeaderItem(2, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.tbl_MKL.setHorizontalHeaderItem(3, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.tbl_MKL.setHorizontalHeaderItem(4, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.tbl_MKL.setHorizontalHeaderItem(5, __qtablewidgetitem35)
        self.tbl_MKL.setObjectName(u"tbl_MKL")
        self.tbl_MKL.setGeometry(QRect(10, 70, 481, 181))
        self.tbl_MKL.viewport().setProperty("cursor", QCursor(Qt.ArrowCursor))
        self.tbl_MKL.setStyleSheet(u"QTableWidget{\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius : 5px;\n"
"color: rgb(0, 0, 0);\n"
"font: 75 10pt \"Calibri\";\n"
"}\n"
"\n"
"QTableWidget:hover{\n"
"\n"
"border : 2px solid  rgb(0, 255, 255);\n"
"\n"
"}\n"
"\n"
"QHeaderView::section{\n"
"border-radius : 1px;\n"
"	background-color: rgb(0, 159, 195);\n"
"\n"
"color: rgb(0, 0, 0);\n"
"font: 75 11pt \"Times New Roman\";\n"
"\n"
"}\n"
"\n"
"QTableWidget:hover{\n"
"\n"
"border : 2px solid  rgb(0, 255, 255);\n"
"\n"
"}\n"
"")
        self.tbl_MKL.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tbl_MKL.setShowGrid(True)
        self.tbl_MKL.setGridStyle(Qt.SolidLine)
        self.tbl_MKL.setSortingEnabled(False)
        self.tbl_MKL.setRowCount(0)
        self.tbl_MKL.horizontalHeader().setCascadingSectionResizes(False)
        self.tbl_MKL.horizontalHeader().setMinimumSectionSize(42)
        self.tbl_MKL.horizontalHeader().setDefaultSectionSize(80)
        self.tbl_MKL.horizontalHeader().setProperty("showSortIndicator", False)
        self.tbl_MKL.verticalHeader().setVisible(False)
        self.tbl_MKL.verticalHeader().setCascadingSectionResizes(False)
        self.tbl_MKL.verticalHeader().setMinimumSectionSize(20)
        self.tbl_MKL.verticalHeader().setDefaultSectionSize(25)
        self.tbl_MKL.verticalHeader().setProperty("showSortIndicator", False)
        self.tbl_MKL.verticalHeader().setStretchLastSection(False)
        self.groupBox = QGroupBox(self.pagina_2)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(0, 282, 1359, 647))
        self.groupBox.setStyleSheet(u"QGroupBox{\n"
"/*Borde*/\n"
"border: 2px solid rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"\n"
"	/*Letra*/\n"
"	font: 15pt \"Impact\";\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.tbl_MKG = QTableWidget(self.groupBox)
        self.tbl_MKG.setObjectName(u"tbl_MKG")
        self.tbl_MKG.setGeometry(QRect(10, 58, 580, 551))
        self.tbl_MKG.viewport().setProperty("cursor", QCursor(Qt.ArrowCursor))
        self.tbl_MKG.setStyleSheet(u"QTableWidget{\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius : 5px;\n"
"color: rgb(0, 0, 0);\n"
"font: 75 10pt \"Calibri\";\n"
"}\n"
"\n"
"QTableWidget:hover{\n"
"\n"
"border : 2px solid  rgb(0, 255, 255);\n"
"\n"
"}\n"
"\n"
"QHeaderView::section{\n"
"border-radius : 1px;\n"
"	background-color: rgb(0, 159, 195);\n"
"\n"
"color: rgb(0, 0, 0);\n"
"font: 75 11pt \"Times New Roman\";\n"
"\n"
"}\n"
"\n"
"QTableWidget:hover{\n"
"\n"
"border : 2px solid  rgb(0, 255, 255);\n"
"\n"
"}\n"
"")
        self.tbl_MKG.setShowGrid(True)
        self.tbl_MKG.setGridStyle(Qt.SolidLine)
        self.tbl_MKG.setSortingEnabled(False)
        self.tbl_MKG.setRowCount(0)
        self.tbl_MKG.horizontalHeader().setCascadingSectionResizes(False)
        self.tbl_MKG.horizontalHeader().setMinimumSectionSize(42)
        self.tbl_MKG.horizontalHeader().setDefaultSectionSize(80)
        self.tbl_MKG.horizontalHeader().setProperty("showSortIndicator", False)
        self.tbl_MKG.verticalHeader().setVisible(False)
        self.tbl_MKG.verticalHeader().setCascadingSectionResizes(False)
        self.tbl_MKG.verticalHeader().setMinimumSectionSize(20)
        self.tbl_MKG.verticalHeader().setDefaultSectionSize(25)
        self.tbl_MKG.verticalHeader().setProperty("showSortIndicator", False)
        self.tbl_MKG.verticalHeader().setStretchLastSection(False)
        self.label_27 = QLabel(self.groupBox)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(10, 34, 281, 21))
        self.label_27.setStyleSheet(u"QLabel{\n"
"background-color: None;\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.wgt_GDL = MatplotlibWidgetaLienzo(self.groupBox)
        self.wgt_GDL.setObjectName(u"wgt_GDL")
        self.wgt_GDL.setGeometry(QRect(752, 110, 591, 465))
        self.wgt_GDL.setStyleSheet(u"/* color de fondo*/\n"
"\n"
"background-color: rgb(179, 239, 255);\n"
"/*borde redondo*/\n"
"border-radius : 10px;\n"
"/* linea de borde*/\n"
"border : 2px solid rgb(205, 205, 205);\n"
"")
        self.tbl_vec_F = QTableWidget(self.groupBox)
        if (self.tbl_vec_F.columnCount() < 1):
            self.tbl_vec_F.setColumnCount(1)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.tbl_vec_F.setHorizontalHeaderItem(0, __qtablewidgetitem36)
        self.tbl_vec_F.setObjectName(u"tbl_vec_F")
        self.tbl_vec_F.setGeometry(QRect(650, 58, 80, 549))
        self.tbl_vec_F.setStyleSheet(u"QTableWidget{\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius : 5px;\n"
"color: rgb(0, 0, 0);\n"
"font: 75 10pt \"Calibri\";\n"
"}\n"
"\n"
"QTableWidget:hover{\n"
"\n"
"border : 2px solid  rgb(0, 255, 255);\n"
"\n"
"}\n"
"\n"
"QHeaderView::section{\n"
"border-radius : 1px;\n"
"	background-color: rgb(0, 159, 195);\n"
"\n"
"color: rgb(0, 0, 0);\n"
"font: 75 11pt \"Times New Roman\";\n"
"\n"
"}\n"
"\n"
"QTableWidget:hover{\n"
"\n"
"border : 2px solid  rgb(0, 255, 255);\n"
"\n"
"}\n"
"")
        self.tbl_vec_F.horizontalHeader().setDefaultSectionSize(80)
        self.tbl_vec_F.verticalHeader().setMinimumSectionSize(20)
        self.tbl_vec_F.verticalHeader().setDefaultSectionSize(25)
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(600, 324, 41, 31))
        self.label_28 = QLabel(self.groupBox)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(612, 30, 151, 21))
        self.label_28.setStyleSheet(u"QLabel{\n"
"background-color: None;\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.label_29 = QLabel(self.groupBox)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(972, 80, 211, 21))
        self.label_29.setStyleSheet(u"QLabel{\n"
"background-color: None;\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.stackedWidget.addWidget(self.pagina_2)
        self.pagina_3 = QWidget()
        self.pagina_3.setObjectName(u"pagina_3")
        self.groupBox_4 = QGroupBox(self.pagina_3)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(0, 10, 1341, 919))
        self.groupBox_4.setStyleSheet(u"QGroupBox{\n"
"/*Borde*/\n"
"border: 2px solid rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"\n"
"	/*Letra*/\n"
"	font: 15pt \"Impact\";\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.frame_4 = QFrame(self.groupBox_4)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(10, 30, 541, 869))
        self.frame_4.setStyleSheet(u"/*border: 2px solid rgb(97, 134, 133);*/\n"
"background-color: rgb(4, 120, 170);\n"
"border-radius: 5px;")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.tbl_g_delta = QTableWidget(self.frame_4)
        if (self.tbl_g_delta.columnCount() < 2):
            self.tbl_g_delta.setColumnCount(2)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.tbl_g_delta.setHorizontalHeaderItem(0, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.tbl_g_delta.setHorizontalHeaderItem(1, __qtablewidgetitem38)
        self.tbl_g_delta.setObjectName(u"tbl_g_delta")
        self.tbl_g_delta.setGeometry(QRect(10, 10, 501, 835))
        self.tbl_g_delta.setStyleSheet(u"QTableWidget{\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius : 5px;\n"
"color: rgb(0, 0, 0);\n"
"font: 75 10pt \"Calibri\";\n"
"}\n"
"\n"
"QTableWidget:hover{\n"
"\n"
"border : 2px solid  rgb(0, 255, 255);\n"
"\n"
"}\n"
"\n"
"QHeaderView::section{\n"
"border-radius : 1px;\n"
"	background-color: rgb(0, 159, 195);\n"
"\n"
"color: rgb(0, 0, 0);\n"
"font: 75 11pt \"Times New Roman\";\n"
"\n"
"}\n"
"\n"
"QTableWidget:hover{\n"
"\n"
"border : 2px solid  rgb(0, 255, 255);\n"
"\n"
"}\n"
"")
        self.tbl_g_delta.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tbl_g_delta.horizontalHeader().setDefaultSectionSize(250)
        self.tbl_g_delta.verticalHeader().setMinimumSectionSize(20)
        self.tbl_g_delta.verticalHeader().setDefaultSectionSize(25)
        self.frame_3 = QFrame(self.groupBox_4)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(580, 30, 731, 867))
        self.frame_3.setStyleSheet(u"/*border: 2px solid rgb(97, 134, 133);*/\n"
"background-color: rgb(4, 120, 170);\n"
"border-radius: 10px;")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.tbl_g_delta_elem = QTableWidget(self.frame_3)
        if (self.tbl_g_delta_elem.columnCount() < 2):
            self.tbl_g_delta_elem.setColumnCount(2)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.tbl_g_delta_elem.setHorizontalHeaderItem(0, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.tbl_g_delta_elem.setHorizontalHeaderItem(1, __qtablewidgetitem40)
        self.tbl_g_delta_elem.setObjectName(u"tbl_g_delta_elem")
        self.tbl_g_delta_elem.setGeometry(QRect(50, 170, 310, 303))
        self.tbl_g_delta_elem.setStyleSheet(u"QTableWidget{\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius : 5px;\n"
"color: rgb(0, 0, 0);\n"
"font: 75 10pt \"Calibri\";\n"
"}\n"
"\n"
"QTableWidget:hover{\n"
"\n"
"border : 2px solid  rgb(0, 255, 255);\n"
"\n"
"}\n"
"\n"
"QHeaderView::section{\n"
"border-radius : 1px;\n"
"	background-color: rgb(0, 159, 195);\n"
"\n"
"color: rgb(0, 0, 0);\n"
"font: 75 11pt \"Times New Roman\";\n"
"\n"
"}\n"
"\n"
"QTableWidget:hover{\n"
"\n"
"border : 2px solid  rgb(0, 255, 255);\n"
"\n"
"}\n"
"")
        self.tbl_g_delta_elem.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tbl_g_delta_elem.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tbl_g_delta_elem.setAutoScroll(True)
        self.tbl_g_delta_elem.horizontalHeader().setDefaultSectionSize(155)
        self.tbl_g_delta_elem.verticalHeader().setMinimumSectionSize(20)
        self.tbl_g_delta_elem.verticalHeader().setDefaultSectionSize(45)
        self.layoutWidget_3 = QWidget(self.frame_3)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(266, 500, 241, 151))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_30 = QLabel(self.layoutWidget_3)
        self.label_30.setObjectName(u"label_30")

        self.verticalLayout_2.addWidget(self.label_30)

        self.slider_Elem = QSlider(self.layoutWidget_3)
        self.slider_Elem.setObjectName(u"slider_Elem")
        self.slider_Elem.setAutoFillBackground(False)
        self.slider_Elem.setStyleSheet(u"background-color: rgb(213, 244, 230);\n"
"border: 2px solid rgb(97, 134, 133);\n"
"border-radius: 5px;")
        self.slider_Elem.setOrientation(Qt.Horizontal)
        self.slider_Elem.setInvertedControls(False)

        self.verticalLayout_2.addWidget(self.slider_Elem)

        self.n_Elem = QLabel(self.layoutWidget_3)
        self.n_Elem.setObjectName(u"n_Elem")
        self.n_Elem.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.n_Elem)

        self.tbl_fuerzas_internas = QTableWidget(self.frame_3)
        if (self.tbl_fuerzas_internas.columnCount() < 1):
            self.tbl_fuerzas_internas.setColumnCount(1)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.tbl_fuerzas_internas.setHorizontalHeaderItem(0, __qtablewidgetitem41)
        self.tbl_fuerzas_internas.setObjectName(u"tbl_fuerzas_internas")
        self.tbl_fuerzas_internas.setGeometry(QRect(492, 168, 218, 311))
        self.tbl_fuerzas_internas.setStyleSheet(u"QTableWidget{\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius : 10px;\n"
"color: rgb(0, 0, 0);\n"
"font: 75 10pt \"Calibri\";\n"
"}\n"
"\n"
"QTableWidget:hover{\n"
"\n"
"border : 2px solid  rgb(0, 255, 255);\n"
"\n"
"}\n"
"\n"
"QHeaderView::section{\n"
"border-radius : 1px;\n"
"	background-color: rgb(0, 159, 195);\n"
"\n"
"color: rgb(0, 0, 0);\n"
"font: 75 11pt \"Times New Roman\";\n"
"\n"
"}\n"
"\n"
"QTableWidget:hover{\n"
"\n"
"border : 2px solid  rgb(0, 255, 255);\n"
"\n"
"}\n"
"")
        self.tbl_fuerzas_internas.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tbl_fuerzas_internas.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tbl_fuerzas_internas.setAutoScroll(False)
        self.tbl_fuerzas_internas.horizontalHeader().setMinimumSectionSize(37)
        self.tbl_fuerzas_internas.horizontalHeader().setDefaultSectionSize(220)
        self.tbl_fuerzas_internas.verticalHeader().setMinimumSectionSize(20)
        self.tbl_fuerzas_internas.verticalHeader().setDefaultSectionSize(45)
        self.widget4 = QWidget(self.frame_3)
        self.widget4.setObjectName(u"widget4")
        self.widget4.setGeometry(QRect(428, 200, 61, 271))
        self.label_9 = QLabel(self.widget4)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(22, 226, 28, 22))
        self.label_9.setFont(font1)
        self.label_12 = QLabel(self.widget4)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(21, 186, 28, 22))
        self.label_12.setFont(font1)
        self.label_10 = QLabel(self.widget4)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(22, 142, 28, 22))
        self.label_10.setFont(font1)
        self.label_5 = QLabel(self.widget4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 12, 28, 22))
        self.label_5.setFont(font1)
        self.label_7 = QLabel(self.widget4)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(20, 100, 28, 22))
        self.label_7.setFont(font1)
        self.label_6 = QLabel(self.widget4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(19, 56, 28, 22))
        self.label_6.setFont(font1)
        self.stackedWidget.addWidget(self.pagina_3)
        self.pagina_5 = QWidget()
        self.pagina_5.setObjectName(u"pagina_5")
        self.groupBox_5 = QGroupBox(self.pagina_5)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setGeometry(QRect(20, 14, 1327, 917))
        self.groupBox_5.setStyleSheet(u"QGroupBox{\n"
"/*Borde*/\n"
"border: 2px solid rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"\n"
"	/*Letra*/\n"
"	font: 15pt \"Impact\";\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.wgt_FIE = MatplotlibWidgetaLienzo(self.groupBox_5)
        self.wgt_FIE.setObjectName(u"wgt_FIE")
        self.wgt_FIE.setGeometry(QRect(32, 36, 1257, 850))
        self.wgt_FIE.setStyleSheet(u"background-color: rgb(179, 239, 255);\n"
"border-radius: 5px;")
        self.stackedWidget.addWidget(self.pagina_5)
        self.pagina_4 = QWidget()
        self.pagina_4.setObjectName(u"pagina_4")
        self.groupBox_6 = QGroupBox(self.pagina_4)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setGeometry(QRect(112, 9, 1231, 919))
        self.groupBox_6.setStyleSheet(u"QGroupBox{\n"
"/*Borde*/\n"
"border: 2px solid rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"\n"
"	/*Letra*/\n"
"	font: 15pt \"Impact\";\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.frame_5 = QFrame(self.groupBox_6)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(290, 30, 917, 865))
        self.frame_5.setStyleSheet(u"background-color: rgb(4, 120, 170);\n"
"border-radius: 5px;")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.wgt_deformada = MatplotlibWidgetaLienzo(self.frame_5)
        self.wgt_deformada.setObjectName(u"wgt_deformada")
        self.wgt_deformada.setGeometry(QRect(20, 46, 878, 781))
        self.wgt_deformada.setStyleSheet(u"background-color: rgb(179, 239, 255);\n"
"border-radius: 5px;")
        self.frame_2 = QFrame(self.groupBox_6)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(20, 36, 261, 629))
        self.frame_2.setStyleSheet(u"/*border: 2px solid rgb(97, 134, 133);*/\n"
"\n"
"QSlider{\n"
"background-color: rgb(4, 120, 170);\n"
"border-radius: 5px;\n"
"}\n"
"QLineEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QLabel{\n"
"color: rgb(255, 255, 255);\n"
"	font: 87 20pt \"Segoe UI Black\";\n"
"	background-color: none;\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.slider_zoom_defor = QSlider(self.frame_2)
        self.slider_zoom_defor.setObjectName(u"slider_zoom_defor")
        self.slider_zoom_defor.setGeometry(QRect(70, 216, 130, 20))
        self.slider_zoom_defor.setStyleSheet(u"background-color: rgb(213, 244, 230);\n"
"border: 2px solid rgb(97, 134, 133);\n"
"border-radius: 5px;")
        self.slider_zoom_defor.setOrientation(Qt.Horizontal)
        self.inline_amplificacion = QLineEdit(self.frame_2)
        self.inline_amplificacion.setObjectName(u"inline_amplificacion")
        self.inline_amplificacion.setGeometry(QRect(90, 316, 95, 20))
        self.label_31 = QLabel(self.frame_2)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(0, 266, 271, 51))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI Black"])
        font3.setPointSize(20)
        font3.setBold(False)
        font3.setItalic(False)
        self.label_31.setFont(font3)
        self.label_31.setStyleSheet(u"")
        self.label_32 = QLabel(self.frame_2)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setGeometry(QRect(0, 186, 261, 31))
        self.label_32.setStyleSheet(u"")
        self.btn_amp_deformada = QPushButton(self.frame_2)
        self.btn_amp_deformada.setObjectName(u"btn_amp_deformada")
        self.btn_amp_deformada.setGeometry(QRect(100, 366, 65, 41))
        font4 = QFont()
        font4.setFamilies([u"Bell MT"])
        font4.setPointSize(12)
        font4.setBold(False)
        font4.setItalic(False)
        self.btn_amp_deformada.setFont(font4)
        self.btn_amp_deformada.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_amp_deformada.setStyleSheet(u"QPushButton{\n"
"/* Color de fondo*/\n"
"/**background-color: rgb(213, 244, 230);**/\n"
"	background-color: rgb(2, 85, 120);\n"
"color: rgb(255,255,255);\n"
"font: 75 12pt \"Bell MT\";\n"
"border-radius : 4px;\n"
"/**border : 2px solid  rgb(240, 240, 240);**/\n"
"\n"
"}\n"
"\n"
"/* Cambia color al estar sobre*/\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(0, 207, 255);\n"
"}\n"
"/* Cambia color al dar click*/\n"
"QPushButton:pressed{\n"
"\n"
"background-color:rgb(173, 238, 236);\n"
"\n"
"}\n"
"\n"
"\n"
"")
        self.btn_amp_deformada.setIconSize(QSize(20, 20))
        self.btn_screen_deformada = QPushButton(self.frame_2)
        self.btn_screen_deformada.setObjectName(u"btn_screen_deformada")
        self.btn_screen_deformada.setGeometry(QRect(60, 486, 151, 111))
        self.btn_screen_deformada.setFont(font4)
        self.btn_screen_deformada.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_screen_deformada.setStyleSheet(u"QPushButton{\n"
"/* Color de fondo*/\n"
"/**background-color: rgb(213, 244, 230);**/\n"
"	background-color: none;\n"
"color: rgb(255,255,255);\n"
"font: 75 12pt \"Bell MT\";\n"
"\n"
"border-radius :20px;\n"
"/**border : 2px solid  rgb(240, 240, 240);**/\n"
"\n"
"}\n"
"\n"
"/* Cambia color al estar sobre*/\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	background-color: rgb(24, 135, 204);\n"
"}\n"
"/* Cambia color al dar click*/\n"
"QPushButton:pressed{\n"
"\n"
"	background-color: rgb(26, 146, 220);\n"
"\n"
"}\n"
"\n"
"\n"
"")
        #icon1 = QIcon()
        #icon1.addFile(u"resource/captura2.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.icon1 = QIcon(os.path.join(basedir, 'resource/captura2.ico'))
        self.btn_screen_deformada.setIcon(self.icon1)
        self.btn_screen_deformada.setIconSize(QSize(150, 150))
        self.stackedWidget.addWidget(self.pagina_4)
        self.label_14 = QLabel(self.cb_paginas)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(12, 900, 561, 29))
        self.bar_cb_pg = QFrame(self.frame_10)
        self.bar_cb_pg.setObjectName(u"bar_cb_pg")
        self.bar_cb_pg.setEnabled(True)
        self.bar_cb_pg.setGeometry(QRect(0, 0, 16777215, 36))
        self.bar_cb_pg.setMaximumSize(QSize(16777215, 36))
        self.bar_cb_pg.setStyleSheet(u"/**background-color: rgb(213, 244, 230);**/background-color: rgb(4, 107, 153);\n"
"")
        self.bar_cb_pg.setFrameShape(QFrame.StyledPanel)
        self.bar_cb_pg.setFrameShadow(QFrame.Raised)
        self.btn_abrir = QPushButton(self.bar_cb_pg)
        self.btn_abrir.setObjectName(u"btn_abrir")
        self.btn_abrir.setGeometry(QRect(50, 0, 32, 34))
        self.btn_abrir.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_abrir.setStyleSheet(u"QPushButton{\n"
"/* Color de fondo*/\n"
"/**background-color: rgb(213, 244, 230);**/\n"
"	background-color: rgb(2, 85, 120);\n"
"\n"
"font: 75 12pt \"Bell MT\";\n"
"border-radius : 4px;\n"
"/**border : 2px solid  rgb(240, 240, 240);**/\n"
"\n"
"}\n"
"\n"
"/* Cambia color al estar sobre*/\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(0, 207, 255);\n"
"}\n"
"/* Cambia color al dar click*/\n"
"QPushButton:pressed{\n"
"\n"
"background-color:rgb(173, 238, 236);\n"
"\n"
"}\n"
"\n"
"\n"
"")
        # icon2 = QIcon()
        # icon2.addFile(u"resource/Abrir.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.icon2 = QIcon(os.path.join(basedir, 'resource/Abrir.ico'))
        self.btn_abrir.setIcon(self.icon2)
        self.btn_abrir.setIconSize(QSize(20, 20))
        self.btn_guardar = QPushButton(self.bar_cb_pg)
        self.btn_guardar.setObjectName(u"btn_guardar")
        self.btn_guardar.setGeometry(QRect(90, 0, 32, 34))
        self.btn_guardar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_guardar.setStyleSheet(u"QPushButton{\n"
"/* Color de fondo*/\n"
"/**background-color: rgb(213, 244, 230);**/\n"
"	background-color: rgb(2, 85, 120);\n"
"\n"
"font: 75 12pt \"Bell MT\";\n"
"border-radius : 4px;\n"
"/**border : 2px solid  rgb(240, 240, 240);**/\n"
"\n"
"}\n"
"\n"
"/* Cambia color al estar sobre*/\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(0, 207, 255);\n"
"}\n"
"/* Cambia color al dar click*/\n"
"QPushButton:pressed{\n"
"\n"
"background-color:rgb(173, 238, 236);\n"
"\n"
"}\n"
"\n"
"\n"
"")
        # icon3 = QIcon()
        # icon3.addFile(u"resource/Guardar.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.icon3 = QIcon(os.path.join(basedir, 'resource/Guardar.ico'))
        self.btn_guardar.setIcon(self.icon3)
        self.btn_guardar.setIconSize(QSize(20, 20))
        self.btn_inicio = QPushButton(self.bar_cb_pg)
        self.btn_inicio.setObjectName(u"btn_inicio")
        self.btn_inicio.setGeometry(QRect(130, 0, 32, 34))
        self.btn_inicio.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_inicio.setStyleSheet(u"QPushButton{\n"
"/* Color de fondo*/\n"
"/**background-color: rgb(213, 244, 230);**/\n"
"	background-color: rgb(2, 85, 120);\n"
"\n"
"font: 75 12pt \"Bell MT\";\n"
"border-radius : 4px;\n"
"/**border : 2px solid  rgb(240, 240, 240);**/\n"
"\n"
"}\n"
"\n"
"/* Cambia color al estar sobre*/\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(0, 207, 255);\n"
"}\n"
"/* Cambia color al dar click*/\n"
"QPushButton:pressed{\n"
"\n"
"background-color:rgb(173, 238, 236);\n"
"\n"
"}\n"
"\n"
"\n"
"")
        # icon4 = QIcon()
        # icon4.addFile(u"resource/I.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.icon4 = QIcon(os.path.join(basedir, 'resource/I.ico'))
        self.btn_inicio.setIcon(self.icon4)
        self.btn_inicio.setIconSize(QSize(20, 20))
        self.btn_matrices = QPushButton(self.bar_cb_pg)
        self.btn_matrices.setObjectName(u"btn_matrices")
        self.btn_matrices.setGeometry(QRect(170, 0, 32, 34))
        self.btn_matrices.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_matrices.setStyleSheet(u"QPushButton{\n"
"/* Color de fondo*/\n"
"/**background-color: rgb(213, 244, 230);**/\n"
"	background-color: rgb(2, 85, 120);\n"
"\n"
"font: 75 12pt \"Bell MT\";\n"
"border-radius : 4px;\n"
"/**border : 2px solid  rgb(240, 240, 240);**/\n"
"\n"
"}\n"
"\n"
"/* Cambia color al estar sobre*/\n"
"QPushButton:hover{\n"
"	background-color: rgb(0, 207, 255);\n"
"}\n"
"/* Cambia color al dar click*/\n"
"QPushButton:pressed{\n"
"\n"
"background-color:rgb(173, 238, 236);\n"
"\n"
"}\n"
"\n"
"\n"
"")
        # icon5 = QIcon()
        # icon5.addFile(u"resource/K.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.icon5 = QIcon(os.path.join(basedir, 'resource/K.ico'))
        self.btn_matrices.setIcon(self.icon5)
        self.btn_matrices.setIconSize(QSize(20, 20))
        self.btn_delta_fuerza = QPushButton(self.bar_cb_pg)
        self.btn_delta_fuerza.setObjectName(u"btn_delta_fuerza")
        self.btn_delta_fuerza.setGeometry(QRect(210, 0, 32, 34))
        self.btn_delta_fuerza.setFont(font4)
        self.btn_delta_fuerza.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_delta_fuerza.setMouseTracking(True)
        self.btn_delta_fuerza.setStyleSheet(u"QPushButton{\n"
"/* Color de fondo*/\n"
"/**background-color: rgb(213, 244, 230);**/\n"
"	background-color: rgb(2, 85, 120);\n"
"\n"
"font: 75 12pt \"Bell MT\";\n"
"border-radius : 4px;\n"
"/**border : 2px solid  rgb(240, 240, 240);**/\n"
"\n"
"}\n"
"\n"
"/* Cambia color al estar sobre*/\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(0, 207, 255);\n"
"}\n"
"/* Cambia color al dar click*/\n"
"QPushButton:pressed{\n"
"\n"
"background-color:rgb(173, 238, 236);\n"
"\n"
"}\n"
"\n"
"\n"
"")
        # icon6 = QIcon()
        # icon6.addFile(u"resource/Delta-F.png", QSize(), QIcon.Normal, QIcon.Off)
        self.icon6 = QIcon(os.path.join(basedir, 'resource/Delta-F.png'))
        self.btn_delta_fuerza.setIcon(self.icon6)
        self.btn_delta_fuerza.setIconSize(QSize(23, 23))
        self.btn_delta_fuerza.setCheckable(False)
        self.btn_delta_fuerza.setChecked(False)
        self.btn_fuerzas = QPushButton(self.bar_cb_pg)
        self.btn_fuerzas.setObjectName(u"btn_fuerzas")
        self.btn_fuerzas.setGeometry(QRect(250, 0, 32, 34))
        self.btn_fuerzas.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_fuerzas.setStyleSheet(u"QPushButton{\n"
"/* Color de fondo*/\n"
"/**background-color: rgb(213, 244, 230);**/\n"
"	background-color: rgb(2, 85, 120);\n"
"\n"
"font: 75 12pt \"Bell MT\";\n"
"border-radius : 4px;\n"
"/**border : 2px solid  rgb(240, 240, 240);**/\n"
"\n"
"}\n"
"\n"
"/* Cambia color al estar sobre*/\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(0, 207, 255);\n"
"}\n"
"/* Cambia color al dar click*/\n"
"QPushButton:pressed{\n"
"\n"
"background-color:rgb(173, 238, 236);\n"
"\n"
"}\n"
"\n"
"\n"
"")
        # icon7 = QIcon()
        # icon7.addFile(u"resource/F.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.icon7 = QIcon(os.path.join(basedir, 'resource/F.ico'))
        self.btn_fuerzas.setIcon(self.icon7)
        self.btn_fuerzas.setIconSize(QSize(20, 20))
        self.btn_deformada = QPushButton(self.bar_cb_pg)
        self.btn_deformada.setObjectName(u"btn_deformada")
        self.btn_deformada.setGeometry(QRect(290, 0, 32, 34))
        self.btn_deformada.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_deformada.setMouseTracking(True)
        self.btn_deformada.setStyleSheet(u"QPushButton{\n"
"/* Color de fondo*/\n"
"/**background-color: rgb(213, 244, 230);**/\n"
"	background-color: rgb(2, 85, 120);\n"
"\n"
"font: 75 12pt \"Bell MT\";\n"
"border-radius : 4px;\n"
"/**border : 2px solid  rgb(240, 240, 240);**/\n"
"\n"
"}\n"
"\n"
"/* Cambia color al estar sobre*/\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(0, 207, 255);\n"
"}\n"
"/* Cambia color al dar click*/\n"
"QPushButton:pressed{\n"
"\n"
"background-color:rgb(173, 238, 236);\n"
"\n"
"}\n"
"\n"
"\n"
"")
        # icon8 = QIcon()
        # icon8.addFile(u"resource/D.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.icon8 = QIcon(os.path.join(basedir, 'resource/D.ico'))
        self.btn_deformada.setIcon(self.icon8)
        self.btn_deformada.setIconSize(QSize(30, 20))
        self.btn_deformada.setCheckable(False)
        self.btn_deformada.setChecked(False)
        self.btn_deformada.setAutoDefault(False)
        self.btn_nuevo = QPushButton(self.bar_cb_pg)
        self.btn_nuevo.setObjectName(u"btn_nuevo")
        self.btn_nuevo.setGeometry(QRect(10, 0, 32, 34))
        self.btn_nuevo.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_nuevo.setStyleSheet(u"QPushButton{\n"
"/* Color de fondo*/\n"
"/**background-color: rgb(213, 244, 230);**/\n"
"	background-color: rgb(2, 85, 120);\n"
"\n"
"font: 75 12pt \"Bell MT\";\n"
"border-radius : 4px;\n"
"/**border : 2px solid  rgb(240, 240, 240);**/\n"
"\n"
"}\n"
"\n"
"/* Cambia color al estar sobre*/\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(0, 207, 255);\n"
"}\n"
"/* Cambia color al dar click*/\n"
"QPushButton:pressed{\n"
"\n"
"background-color:rgb(173, 238, 236);\n"
"\n"
"}\n"
"\n"
"\n"
"")
        # icon9 = QIcon()
        # icon9.addFile(u"resource/Nuevo.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.icon9 = QIcon(os.path.join(basedir, 'resource/Nuevo.ico'))
        self.btn_nuevo.setIcon(self.icon9)
        self.btn_nuevo.setIconSize(QSize(20, 20))

        self.verticalLayout_3.addWidget(self.frame_10)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        Porticos_1920x1080.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Porticos_1920x1080)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1464, 22))
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        self.menuVista = QMenu(self.menubar)
        self.menuVista.setObjectName(u"menuVista")
        self.menuHerramientas = QMenu(self.menubar)
        self.menuHerramientas.setObjectName(u"menuHerramientas")
        self.menuAcerca_de = QMenu(self.menubar)
        self.menuAcerca_de.setObjectName(u"menuAcerca_de")
        Porticos_1920x1080.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menuVista.menuAction())
        self.menubar.addAction(self.menuHerramientas.menuAction())
        self.menubar.addAction(self.menuAcerca_de.menuAction())
        self.menuArchivo.addAction(self.actionNuevo)
        self.menuArchivo.addAction(self.actionAbrir)
        self.menuArchivo.addAction(self.actionGuardar)
        self.menuArchivo.addSeparator()
        self.menuArchivo.addAction(self.actionSalir)
        self.menuVista.addAction(self.actionTema_claro)
        self.menuVista.addAction(self.actionTema_oscuro)
        self.menuHerramientas.addAction(self.actionConversor_de_unidades)
        self.menuAcerca_de.addAction(self.actionManual_de_uso)
        self.menuAcerca_de.addAction(self.actionInformacion)
        self.menuAcerca_de.addSeparator()

        self.retranslateUi(Porticos_1920x1080)

        QMetaObject.connectSlotsByName(Porticos_1920x1080)
    # setupUi

    def retranslateUi(self, Porticos_1920x1080):
        Porticos_1920x1080.setWindowTitle(QCoreApplication.translate("Porticos_1920x1080", u"ANEPY", None))
        self.actionNuevo.setText(QCoreApplication.translate("Porticos_1920x1080", u"Nuevo", None))
        self.actionAbrir.setText(QCoreApplication.translate("Porticos_1920x1080", u"Abrir", None))
        self.actionGuardar.setText(QCoreApplication.translate("Porticos_1920x1080", u"Guardar", None))
        self.actionSalir.setText(QCoreApplication.translate("Porticos_1920x1080", u"Salir", None))
        self.actionTema_claro.setText(QCoreApplication.translate("Porticos_1920x1080", u"Tema claro", None))
        self.actionTema_oscuro.setText(QCoreApplication.translate("Porticos_1920x1080", u"Tema oscuro", None))
        self.actionConversor_de_unidades.setText(QCoreApplication.translate("Porticos_1920x1080", u"Convertidor de unidades", None))
        self.actionInformacion.setText(QCoreApplication.translate("Porticos_1920x1080", u"Acerca de", None))
        self.actionManual_de_uso.setText(QCoreApplication.translate("Porticos_1920x1080", u"Manual de uso", None))
        self.groupBox_1.setTitle(QCoreApplication.translate("Porticos_1920x1080", u"INGRESE DATOS", None))
        ___qtablewidgetitem = self.tbl_Nod.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Porticos_1920x1080", u"Nodo", None));
        ___qtablewidgetitem1 = self.tbl_Nod.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Porticos_1920x1080", u"Coord. x", None));
        ___qtablewidgetitem2 = self.tbl_Nod.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Porticos_1920x1080", u"Coorrd. y", None));
        ___qtablewidgetitem3 = self.tbl_Fuer.horizontalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Porticos_1920x1080", u"Nodo", None));
        ___qtablewidgetitem4 = self.tbl_Fuer.horizontalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Porticos_1920x1080", u"Fx", None));
        ___qtablewidgetitem5 = self.tbl_Fuer.horizontalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Porticos_1920x1080", u"Fy", None));
        ___qtablewidgetitem6 = self.tbl_Fuer.horizontalHeaderItem(3)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Porticos_1920x1080", u"Mz", None));
        self.label_13.setText(QCoreApplication.translate("Porticos_1920x1080", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Cantidad de Restricciones:</span></p></body></html>", None))
        ___qtablewidgetitem7 = self.tbl_Rest.horizontalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Porticos_1920x1080", u"Tipo", None));
        ___qtablewidgetitem8 = self.tbl_Rest.horizontalHeaderItem(1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Porticos_1920x1080", u"Nodo", None));
        ___qtablewidgetitem9 = self.tbl_Rest.horizontalHeaderItem(2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Porticos_1920x1080", u"#  Restriciones", None));
        self.label_19.setText(QCoreApplication.translate("Porticos_1920x1080", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Tipos de apoyos</span></p></body></html>", None))
        self.btn_analizar.setText(QCoreApplication.translate("Porticos_1920x1080", u"Analizar", None))
#if QT_CONFIG(shortcut)
        self.btn_analizar.setShortcut(QCoreApplication.translate("Porticos_1920x1080", u"Ctrl+Return", None))
#endif // QT_CONFIG(shortcut)
        ___qtablewidgetitem10 = self.tbl_Fuer_W.horizontalHeaderItem(0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Porticos_1920x1080", u"Elemento", None));
        ___qtablewidgetitem11 = self.tbl_Fuer_W.horizontalHeaderItem(1)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("Porticos_1920x1080", u"W i", None));
        ___qtablewidgetitem12 = self.tbl_Fuer_W.horizontalHeaderItem(2)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("Porticos_1920x1080", u"W f", None));
        ___qtablewidgetitem13 = self.tbl_Elem.horizontalHeaderItem(0)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("Porticos_1920x1080", u"Elemento", None));
        ___qtablewidgetitem14 = self.tbl_Elem.horizontalHeaderItem(1)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("Porticos_1920x1080", u"Nodo inicial", None));
        ___qtablewidgetitem15 = self.tbl_Elem.horizontalHeaderItem(2)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("Porticos_1920x1080", u"Nodo final", None));
        ___qtablewidgetitem16 = self.tbl_Elem.horizontalHeaderItem(3)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("Porticos_1920x1080", u"Base", None));
        ___qtablewidgetitem17 = self.tbl_Elem.horizontalHeaderItem(4)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("Porticos_1920x1080", u"Altura", None));
        ___qtablewidgetitem18 = self.tbl_Elem.horizontalHeaderItem(5)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("Porticos_1920x1080", u"Mod. E", None));
        self.label_33.setText(QCoreApplication.translate("Porticos_1920x1080", u"[unidad]", None))
        self.label_34.setText(QCoreApplication.translate("Porticos_1920x1080", u"[unidad]", None))
        self.label_2.setText(QCoreApplication.translate("Porticos_1920x1080", u"[unidad]", None))
        self.lb_tbl_elem_B.setText(QCoreApplication.translate("Porticos_1920x1080", u"<html><head/><body><p align=\"center\">[m]</p></body></html>", None))
        self.label.setText(QCoreApplication.translate("Porticos_1920x1080", u"[unidad]", None))
        self.label_4.setText(QCoreApplication.translate("Porticos_1920x1080", u"[unidad]", None))
        self.lb_tbl_elem_h.setText(QCoreApplication.translate("Porticos_1920x1080", u"<html><head/><body><p align=\"center\">[m]</p></body></html>", None))
        self.lb_tbl_elem_E.setText(QCoreApplication.translate("Porticos_1920x1080", u"<html><head/><body><p align=\"center\">[MPa]</p></body></html>", None))
        self.lb_tbl_nod_cy.setText(QCoreApplication.translate("Porticos_1920x1080", u"<html><head/><body><p align=\"center\">[m]</p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("Porticos_1920x1080", u"[unidad]", None))
        self.lb_tbl_nod_cx.setText(QCoreApplication.translate("Porticos_1920x1080", u"<html><head/><body><p align=\"center\">[m]</p></body></html>", None))
        self.label_11.setText(QCoreApplication.translate("Porticos_1920x1080", u"[unidad]", None))
        self.lb_tbl_f_fy.setText(QCoreApplication.translate("Porticos_1920x1080", u"<html><head/><body><p align=\"center\">[KN]</p></body></html>", None))
        self.lb_tbl_fw_wi.setText(QCoreApplication.translate("Porticos_1920x1080", u"<html><head/><body><p align=\"center\">[KN/m]</p></body></html>", None))
        self.lb_tbl_f_fx.setText(QCoreApplication.translate("Porticos_1920x1080", u"<html><head/><body><p align=\"center\">[KN]</p></body></html>", None))
        self.lb_tbl_f_m.setText(QCoreApplication.translate("Porticos_1920x1080", u"<html><head/><body><p align=\"center\">[KN-m]</p></body></html>", None))
        self.lb_tbl_fw_wf.setText(QCoreApplication.translate("Porticos_1920x1080", u"<html><head/><body><p align=\"center\">[KN/m]</p></body></html>", None))
        self.label_18.setText(QCoreApplication.translate("Porticos_1920x1080", u"[unidad]", None))
        self.label_20.setText(QCoreApplication.translate("Porticos_1920x1080", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Cantidad de elementos:</span></p></body></html>", None))
        self.label_21.setText(QCoreApplication.translate("Porticos_1920x1080", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Cantidad de  nodos:</span></p></body></html>", None))
        self.label_22.setText(QCoreApplication.translate("Porticos_1920x1080", u"<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">Cantidad de fuerzas:</span></p></body></html>", None))
        self.label_23.setText(QCoreApplication.translate("Porticos_1920x1080", u"<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">Cantidad de fuerzas W:</span></p></body></html>", None))
        self.label_archivo.setText(QCoreApplication.translate("Porticos_1920x1080", u"<html><head/><body><p><span style=\" font-weight:600; font-style:italic;\">Archivo: </span></p></body></html>", None))
        self.cb_convertir_de.setItemText(0, QCoreApplication.translate("Porticos_1920x1080", u"m, KN, MPa", None))
        self.cb_convertir_de.setItemText(1, QCoreApplication.translate("Porticos_1920x1080", u"pulg, Lb, Psi", None))

#if QT_CONFIG(tooltip)
        self.cb_convertir_de.setToolTip(QCoreApplication.translate("Porticos_1920x1080", u"Sistema de Unidades", None))
#endif // QT_CONFIG(tooltip)
        self.groupBox_2.setTitle(QCoreApplication.translate("Porticos_1920x1080", u"Datos por Elemento", None))
        self.label_24.setText(QCoreApplication.translate("Porticos_1920x1080", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">Elemento:</span></p></body></html>", None))
        self.cb_elemento.setCurrentText("")
        self.label_25.setText(QCoreApplication.translate("Porticos_1920x1080", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Matriz de Rigidez Local de elemento:</span></p></body></html>", None))
        ___qtablewidgetitem19 = self.tbl_MKGE.horizontalHeaderItem(0)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("Porticos_1920x1080", u"1", None));
        ___qtablewidgetitem20 = self.tbl_MKGE.horizontalHeaderItem(1)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("Porticos_1920x1080", u"2", None));
        ___qtablewidgetitem21 = self.tbl_MKGE.horizontalHeaderItem(2)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("Porticos_1920x1080", u"3", None));
        ___qtablewidgetitem22 = self.tbl_MKGE.horizontalHeaderItem(3)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("Porticos_1920x1080", u"4", None));
        ___qtablewidgetitem23 = self.tbl_MKGE.horizontalHeaderItem(4)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("Porticos_1920x1080", u"5", None));
        ___qtablewidgetitem24 = self.tbl_MKGE.horizontalHeaderItem(5)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("Porticos_1920x1080", u"6", None));
        self.label_26.setText(QCoreApplication.translate("Porticos_1920x1080", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Matriz de Rigidez Global de elemento:</span></p></body></html>", None))
        ___qtablewidgetitem25 = self.tbl_propiedades.horizontalHeaderItem(0)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("Porticos_1920x1080", u"L", None));
        ___qtablewidgetitem26 = self.tbl_propiedades.horizontalHeaderItem(1)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("Porticos_1920x1080", u"A", None));
        ___qtablewidgetitem27 = self.tbl_propiedades.horizontalHeaderItem(2)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("Porticos_1920x1080", u"Mod E", None));
        ___qtablewidgetitem28 = self.tbl_propiedades.horizontalHeaderItem(3)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("Porticos_1920x1080", u"Iz", None));
        ___qtablewidgetitem29 = self.tbl_propiedades.horizontalHeaderItem(4)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("Porticos_1920x1080", u"Angulo", None));
        ___qtablewidgetitem30 = self.tbl_MKL.horizontalHeaderItem(0)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("Porticos_1920x1080", u"1", None));
        ___qtablewidgetitem31 = self.tbl_MKL.horizontalHeaderItem(1)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("Porticos_1920x1080", u"2", None));
        ___qtablewidgetitem32 = self.tbl_MKL.horizontalHeaderItem(2)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("Porticos_1920x1080", u"3", None));
        ___qtablewidgetitem33 = self.tbl_MKL.horizontalHeaderItem(3)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("Porticos_1920x1080", u"4", None));
        ___qtablewidgetitem34 = self.tbl_MKL.horizontalHeaderItem(4)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("Porticos_1920x1080", u"5", None));
        ___qtablewidgetitem35 = self.tbl_MKL.horizontalHeaderItem(5)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("Porticos_1920x1080", u"6", None));
        self.groupBox.setTitle(QCoreApplication.translate("Porticos_1920x1080", u"Matriz de Rigidez - Vector Fuerza - GDL", None))
        self.label_27.setText(QCoreApplication.translate("Porticos_1920x1080", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Matriz de Rigidez Global:</span></p></body></html>", None))
        ___qtablewidgetitem36 = self.tbl_vec_F.horizontalHeaderItem(0)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("Porticos_1920x1080", u"F", None));
        self.label_3.setText(QCoreApplication.translate("Porticos_1920x1080", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">{F}=</span></p></body></html>", None))
        self.label_28.setText(QCoreApplication.translate("Porticos_1920x1080", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Vector Fuerza:</span></p></body></html>", None))
        self.label_29.setText(QCoreApplication.translate("Porticos_1920x1080", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Grados De Libertad</span></p></body></html>", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Porticos_1920x1080", u"Grados De Libertad-Desplazamiento-Fuerzas internas", None))
        ___qtablewidgetitem37 = self.tbl_g_delta.horizontalHeaderItem(0)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("Porticos_1920x1080", u"        Grados          ", None));
        ___qtablewidgetitem38 = self.tbl_g_delta.horizontalHeaderItem(1)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("Porticos_1920x1080", u"          \u0394 o  \u03b8      ", None));
        ___qtablewidgetitem39 = self.tbl_g_delta_elem.horizontalHeaderItem(0)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("Porticos_1920x1080", u"             Grados Elem        ", None));
        ___qtablewidgetitem40 = self.tbl_g_delta_elem.horizontalHeaderItem(1)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("Porticos_1920x1080", u"          \u0394 o  \u03b8      ", None));
        self.label_30.setText(QCoreApplication.translate("Porticos_1920x1080", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Elementos</span></p></body></html>", None))
        self.n_Elem.setText(QCoreApplication.translate("Porticos_1920x1080", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">0</span></p></body></html>", None))
        ___qtablewidgetitem41 = self.tbl_fuerzas_internas.horizontalHeaderItem(0)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("Porticos_1920x1080", u"Fuerza", None));
        self.label_9.setText(QCoreApplication.translate("Porticos_1920x1080", u"<html><head/><body><p><span style=\" font-size:11pt;\">Mf</span></p></body></html>", None))
        self.label_12.setText(QCoreApplication.translate("Porticos_1920x1080", u"<html><head/><body><p><span style=\" font-size:11pt;\">Fvf</span></p></body></html>", None))
        self.label_10.setText(QCoreApplication.translate("Porticos_1920x1080", u"<html><head/><body><p><span style=\" font-size:11pt;\">FNf</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("Porticos_1920x1080", u"<html><head/><body><p><span style=\" font-size:11pt;\">FNi</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("Porticos_1920x1080", u"<html><head/><body><p><span style=\" font-size:11pt;\">Mi</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("Porticos_1920x1080", u"<html><head/><body><p><span style=\" font-size:11pt;\">Fvi</span></p></body></html>", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("Porticos_1920x1080", u"Fuerzas Internas en Nodos", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("Porticos_1920x1080", u"Deformada de la estructura", None))
        self.label_31.setText(QCoreApplication.translate("Porticos_1920x1080", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Ingrese valor de amplificación</span></p><p><span style=\" font-weight:600;\"><br/></span></p></body></html>", None))
        self.label_32.setText(QCoreApplication.translate("Porticos_1920x1080", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Deformar<br/></span></p><p align=\"center\"><span style=\" font-size:12pt;\"><br/></span></p></body></html>", None))
        self.btn_amp_deformada.setText(QCoreApplication.translate("Porticos_1920x1080", u"Aplicar", None))
        self.btn_screen_deformada.setText("")
        self.label_14.setText(QCoreApplication.translate("Porticos_1920x1080", u"<html><head/><body><p><span style=\" font-size:7pt; font-weight:600;\">Desarrollado por: </span><span style=\" font-size:7pt;\">JULIANA ANDREA GONZALEZ ROMA\u00d1A Y YHOAN SMITH MOSQUERA PE\u00d1ALOZA</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.btn_abrir.setToolTip(QCoreApplication.translate("Porticos_1920x1080", u"Abrir", None))
#endif // QT_CONFIG(tooltip)
        self.btn_abrir.setText("")
#if QT_CONFIG(tooltip)
        self.btn_guardar.setToolTip(QCoreApplication.translate("Porticos_1920x1080", u"Guardar", None))
#endif // QT_CONFIG(tooltip)
        self.btn_guardar.setText("")
#if QT_CONFIG(tooltip)
        self.btn_inicio.setToolTip(QCoreApplication.translate("Porticos_1920x1080", u"Inicio", None))
#endif // QT_CONFIG(tooltip)
        self.btn_inicio.setText("")
#if QT_CONFIG(tooltip)
        self.btn_matrices.setToolTip(QCoreApplication.translate("Porticos_1920x1080", u"Matrices de rigidez", None))
#endif // QT_CONFIG(tooltip)
        self.btn_matrices.setText("")
#if QT_CONFIG(tooltip)
        self.btn_delta_fuerza.setToolTip(QCoreApplication.translate("Porticos_1920x1080", u"Exportar a Excel", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        self.btn_delta_fuerza.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        self.btn_delta_fuerza.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.btn_delta_fuerza.setText("")
#if QT_CONFIG(tooltip)
        self.btn_fuerzas.setToolTip(QCoreApplication.translate("Porticos_1920x1080", u"Fuerzas Internas", None))
#endif // QT_CONFIG(tooltip)
        self.btn_fuerzas.setText("")
#if QT_CONFIG(tooltip)
        self.btn_deformada.setToolTip(QCoreApplication.translate("Porticos_1920x1080", u"Deformada", None))
#endif // QT_CONFIG(tooltip)
        self.btn_deformada.setText("")
#if QT_CONFIG(tooltip)
        self.btn_nuevo.setToolTip(QCoreApplication.translate("Porticos_1920x1080", u"Nuevo", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.btn_nuevo.setWhatsThis(QCoreApplication.translate("Porticos_1920x1080", u"Nuevo", None))
#endif // QT_CONFIG(whatsthis)
        self.btn_nuevo.setText("")
        self.menuArchivo.setTitle(QCoreApplication.translate("Porticos_1920x1080", u"Archivo", None))
        self.menuVista.setTitle(QCoreApplication.translate("Porticos_1920x1080", u"Vista", None))
        self.menuHerramientas.setTitle(QCoreApplication.translate("Porticos_1920x1080", u"Herramientas", None))
        self.menuAcerca_de.setTitle(QCoreApplication.translate("Porticos_1920x1080", u"Ayuda", None))
    # retranslateUi

