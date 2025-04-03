# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Porticos_v3.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import os
basedir = os.path.dirname(__file__)

class Ui_Porticos(object):
    def setupUi(self, Porticos):
        Porticos.setObjectName("Porticos")
        Porticos.resize(1365, 769)
        icon = QtGui.QIcon(os.path.join(basedir, "Logo.ico"))
        #icon.addPixmap(QtGui.QPixmap("Logo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Porticos.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(Porticos)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setStyleSheet("")
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1363, 746))
        self.scrollAreaWidgetContents.setMinimumSize(QtCore.QSize(0, 0))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_10 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_10.setMinimumSize(QtCore.QSize(1350, 720))
        self.frame_10.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.cb_paginas = QtWidgets.QFrame(self.frame_10)
        self.cb_paginas.setEnabled(True)
        self.cb_paginas.setGeometry(QtCore.QRect(0, 36, 1363, 719))
        self.cb_paginas.setStyleSheet("/**background-color: rgb(4, 107, 153);**/\n"
"background-color: rgb(23, 123, 189);\n"
"\n"
"")
        self.cb_paginas.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.cb_paginas.setFrameShadow(QtWidgets.QFrame.Raised)
        self.cb_paginas.setObjectName("cb_paginas")
        self.stackedWidget = QtWidgets.QStackedWidget(self.cb_paginas)
        self.stackedWidget.setEnabled(True)
        self.stackedWidget.setGeometry(QtCore.QRect(9, -1, 1501, 652))
        self.stackedWidget.setMouseTracking(False)
        self.stackedWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.stackedWidget.setObjectName("stackedWidget")
        self.pagina_1 = QtWidgets.QWidget()
        self.pagina_1.setObjectName("pagina_1")
        self.groupBox_1 = QtWidgets.QGroupBox(self.pagina_1)
        self.groupBox_1.setEnabled(True)
        self.groupBox_1.setGeometry(QtCore.QRect(0, 10, 1341, 599))
        self.groupBox_1.setStyleSheet("QGroupBox{\n"
"/*Borde*/\n"
"border: 2px solid rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"\n"
"    /*Letra*/\n"
"    font: 15pt \"Impact\";\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.groupBox_1.setObjectName("groupBox_1")
        self.sp_nElem = QtWidgets.QSpinBox(self.groupBox_1)
        self.sp_nElem.setGeometry(QtCore.QRect(180, 39, 56, 16))
        self.sp_nElem.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.sp_nElem.setStyleSheet("\n"
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
"    color: rgb(1, 1, 1);\n"
"\n"
"    font: 10pt \"Times New Roman\";\n"
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
        self.sp_nElem.setAlignment(QtCore.Qt.AlignCenter)
        self.sp_nElem.setObjectName("sp_nElem")
        self.tbl_Nod = QtWidgets.QTableWidget(self.groupBox_1)
        self.tbl_Nod.setGeometry(QtCore.QRect(504, 84, 240, 125))
        self.tbl_Nod.setStyleSheet("QTableWidget{\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius : 5px;\n"
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
"    background-color: rgb(0, 159, 195);\n"
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
        self.tbl_Nod.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tbl_Nod.setRowCount(0)
        self.tbl_Nod.setObjectName("tbl_Nod")
        self.tbl_Nod.setColumnCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_Nod.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_Nod.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_Nod.setHorizontalHeaderItem(2, item)
        self.tbl_Nod.horizontalHeader().setDefaultSectionSize(80)
        self.tbl_Nod.horizontalHeader().setMinimumSectionSize(42)
        self.tbl_Nod.verticalHeader().setVisible(False)
        self.tbl_Nod.verticalHeader().setDefaultSectionSize(25)
        self.sp_nNo = QtWidgets.QSpinBox(self.groupBox_1)
        self.sp_nNo.setGeometry(QtCore.QRect(661, 35, 56, 16))
        self.sp_nNo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.sp_nNo.setStyleSheet("\n"
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
"    color: rgb(1, 1, 1);\n"
"\n"
"    font: 10pt \"Times New Roman\";\n"
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
        self.sp_nNo.setAlignment(QtCore.Qt.AlignCenter)
        self.sp_nNo.setObjectName("sp_nNo")
        self.sp_nFuer = QtWidgets.QSpinBox(self.groupBox_1)
        self.sp_nFuer.setGeometry(QtCore.QRect(174, 226, 56, 16))
        self.sp_nFuer.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.sp_nFuer.setStyleSheet("\n"
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
"    color: rgb(1, 1, 1);\n"
"\n"
"    font: 10pt \"Times New Roman\";\n"
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
        self.sp_nFuer.setAlignment(QtCore.Qt.AlignCenter)
        self.sp_nFuer.setObjectName("sp_nFuer")
        self.tbl_Fuer = QtWidgets.QTableWidget(self.groupBox_1)
        self.tbl_Fuer.setGeometry(QtCore.QRect(9, 265, 320, 125))
        self.tbl_Fuer.setStyleSheet("QTableWidget{\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius : 5px;\n"
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
"    background-color: rgb(0, 159, 195);\n"
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
        self.tbl_Fuer.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tbl_Fuer.setRowCount(0)
        self.tbl_Fuer.setObjectName("tbl_Fuer")
        self.tbl_Fuer.setColumnCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_Fuer.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_Fuer.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_Fuer.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_Fuer.setHorizontalHeaderItem(3, item)
        self.tbl_Fuer.horizontalHeader().setDefaultSectionSize(80)
        self.tbl_Fuer.horizontalHeader().setMinimumSectionSize(42)
        self.tbl_Fuer.verticalHeader().setVisible(False)
        self.tbl_Fuer.verticalHeader().setDefaultSectionSize(20)
        self.tbl_Fuer.verticalHeader().setMinimumSectionSize(20)
        self.wgt_Rest = MatplotlibWidgetaLienzo(self.groupBox_1)
        self.wgt_Rest.setGeometry(QtCore.QRect(369, 442, 331, 144))
        self.wgt_Rest.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius : 5px")
        self.wgt_Rest.setObjectName("wgt_Rest")
        self.wgt_porticos = MatplotlibWidgetaLienzo(self.groupBox_1)
        self.wgt_porticos.setGeometry(QtCore.QRect(758, 48, 574, 481))
        self.wgt_porticos.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.wgt_porticos.setMouseTracking(False)
        self.wgt_porticos.setStyleSheet("/* color de fondo*/\n"
"\n"
"background-color: rgb(179, 239, 255);\n"
"/*borde redondo*/\n"
"border-radius : 10px;\n"
"/* linea de borde*/\n"
"border : 2px solid rgb(205, 205, 205);\n"
"")
        self.wgt_porticos.setObjectName("wgt_porticos")
        self.label_13 = QtWidgets.QLabel(self.groupBox_1)
        self.label_13.setGeometry(QtCore.QRect(10, 407, 221, 21))
        self.label_13.setStyleSheet("QLabel{\n"
"background-color: None;\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.label_13.setObjectName("label_13")
        self.tbl_Rest = QtWidgets.QTableWidget(self.groupBox_1)
        self.tbl_Rest.setGeometry(QtCore.QRect(9, 457, 331, 125))
        self.tbl_Rest.setStyleSheet("QTableWidget{\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius : 5px;\n"
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
"    background-color: rgb(0, 159, 195);\n"
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
        self.tbl_Rest.setRowCount(0)
        self.tbl_Rest.setObjectName("tbl_Rest")
        self.tbl_Rest.setColumnCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_Rest.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_Rest.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_Rest.setHorizontalHeaderItem(2, item)
        self.tbl_Rest.horizontalHeader().setDefaultSectionSize(110)
        self.tbl_Rest.horizontalHeader().setMinimumSectionSize(42)
        self.tbl_Rest.horizontalHeader().setSortIndicatorShown(False)
        self.tbl_Rest.verticalHeader().setVisible(False)
        self.tbl_Rest.verticalHeader().setCascadingSectionResizes(False)
        self.tbl_Rest.verticalHeader().setDefaultSectionSize(25)
        self.tbl_Rest.verticalHeader().setHighlightSections(True)
        self.tbl_Rest.verticalHeader().setMinimumSectionSize(20)
        self.sp_nRest = QtWidgets.QSpinBox(self.groupBox_1)
        self.sp_nRest.setGeometry(QtCore.QRect(236, 412, 56, 16))
        self.sp_nRest.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.sp_nRest.setStyleSheet("\n"
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
"    color: rgb(1, 1, 1);\n"
"\n"
"    font: 10pt \"Times New Roman\";\n"
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
        self.sp_nRest.setAlignment(QtCore.Qt.AlignCenter)
        self.sp_nRest.setObjectName("sp_nRest")
        self.label_19 = QtWidgets.QLabel(self.groupBox_1)
        self.label_19.setGeometry(QtCore.QRect(373, 408, 191, 21))
        self.label_19.setStyleSheet("QLabel{\n"
"background-color: None;\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.label_19.setObjectName("label_19")
        self.btn_analizar = QtWidgets.QPushButton(self.groupBox_1)
        self.btn_analizar.setGeometry(QtCore.QRect(950, 540, 151, 31))
        self.btn_analizar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_analizar.setStyleSheet("QPushButton{\n"
"/* Color de fondo*/\n"
"/**background-color: rgb(213, 244, 230);**/\n"
"    background-color: rgb(11, 65, 116);\n"
"    color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Bell MT\";\n"
"border-radius : 4px;\n"
"/**border : 2px solid  rgb(240, 240, 240);**/\n"
"\n"
"}\n"
"\n"
"/* Cambia color al estar sobre*/\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: rgb(18, 90, 140);\n"
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
        self.btn_analizar.setObjectName("btn_analizar")
        self.label_20 = QtWidgets.QLabel(self.groupBox_1)
        self.label_20.setGeometry(QtCore.QRect(8, 35, 191, 21))
        self.label_20.setStyleSheet("QLabel{\n"
"background-color: None;\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.groupBox_1)
        self.label_21.setGeometry(QtCore.QRect(501, 35, 161, 21))
        self.label_21.setStyleSheet("QLabel{\n"
"background-color: None;\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.groupBox_1)
        self.label_22.setGeometry(QtCore.QRect(10, 221, 171, 21))
        self.label_22.setStyleSheet("QLabel{\n"
"background-color: None;\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.label_22.setObjectName("label_22")
        self.tbl_Fuer_W = QtWidgets.QTableWidget(self.groupBox_1)
        self.tbl_Fuer_W.setGeometry(QtCore.QRect(369, 265, 320, 125))
        self.tbl_Fuer_W.setStyleSheet("QTableWidget{\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius : 5px;\n"
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
"    background-color: rgb(0, 159, 195);\n"
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
        self.tbl_Fuer_W.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tbl_Fuer_W.setObjectName("tbl_Fuer_W")
        self.tbl_Fuer_W.setColumnCount(3)
        self.tbl_Fuer_W.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_Fuer_W.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_Fuer_W.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_Fuer_W.setHorizontalHeaderItem(2, item)
        self.tbl_Fuer_W.horizontalHeader().setDefaultSectionSize(112)
        self.tbl_Fuer_W.verticalHeader().setCascadingSectionResizes(False)
        self.tbl_Fuer_W.verticalHeader().setDefaultSectionSize(25)
        self.tbl_Fuer_W.verticalHeader().setMinimumSectionSize(20)
        self.label_23 = QtWidgets.QLabel(self.groupBox_1)
        self.label_23.setGeometry(QtCore.QRect(370, 221, 177, 21))
        self.label_23.setStyleSheet("QLabel{\n"
"background-color: None;\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.label_23.setObjectName("label_23")
        self.sp_nFuer_W = QtWidgets.QSpinBox(self.groupBox_1)
        self.sp_nFuer_W.setGeometry(QtCore.QRect(547, 224, 56, 16))
        self.sp_nFuer_W.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.sp_nFuer_W.setStyleSheet("\n"
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
"    color: rgb(1, 1, 1);\n"
"\n"
"    font: 10pt \"Times New Roman\";\n"
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
        self.sp_nFuer_W.setAlignment(QtCore.Qt.AlignCenter)
        self.sp_nFuer_W.setObjectName("sp_nFuer_W")
        self.tbl_Elem = QtWidgets.QTableWidget(self.groupBox_1)
        self.tbl_Elem.setGeometry(QtCore.QRect(7, 84, 480, 125))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.tbl_Elem.setFont(font)
        self.tbl_Elem.setStyleSheet("QTableWidget{\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius : 5px;\n"
"color: rgb(0, 0, 0);\n"
"font: 75 10pt \"Calibri\";\n"
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
"    background-color: rgb(0, 159, 195);\n"
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
        self.tbl_Elem.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tbl_Elem.setEditTriggers(QtWidgets.QAbstractItemView.AnyKeyPressed|QtWidgets.QAbstractItemView.DoubleClicked|QtWidgets.QAbstractItemView.EditKeyPressed)
        self.tbl_Elem.setProperty("showDropIndicator", True)
        self.tbl_Elem.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.tbl_Elem.setRowCount(0)
        self.tbl_Elem.setObjectName("tbl_Elem")
        self.tbl_Elem.setColumnCount(6)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_Elem.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_Elem.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_Elem.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_Elem.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_Elem.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_Elem.setHorizontalHeaderItem(5, item)
        self.tbl_Elem.horizontalHeader().setDefaultSectionSize(80)
        self.tbl_Elem.horizontalHeader().setMinimumSectionSize(42)
        self.tbl_Elem.verticalHeader().setVisible(False)
        self.tbl_Elem.verticalHeader().setDefaultSectionSize(20)
        self.tbl_Elem.verticalHeader().setMinimumSectionSize(20)
        self.label = QtWidgets.QLabel(self.groupBox_1)
        self.label.setGeometry(QtCore.QRect(28, 66, 47, 13))
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox_1)
        self.label_2.setGeometry(QtCore.QRect(108, 66, 47, 13))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.groupBox_1)
        self.label_4.setGeometry(QtCore.QRect(188, 66, 47, 13))
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.lb_tbl_elem_B = QtWidgets.QLabel(self.groupBox_1)
        self.lb_tbl_elem_B.setGeometry(QtCore.QRect(273, 66, 29, 16))
        self.lb_tbl_elem_B.setStyleSheet("color: rgb(255, 255, 255);")
        self.lb_tbl_elem_B.setObjectName("lb_tbl_elem_B")
        self.lb_tbl_elem_h = QtWidgets.QLabel(self.groupBox_1)
        self.lb_tbl_elem_h.setGeometry(QtCore.QRect(353, 66, 29, 16))
        self.lb_tbl_elem_h.setStyleSheet("color: rgb(255, 255, 255);")
        self.lb_tbl_elem_h.setObjectName("lb_tbl_elem_h")
        self.lb_tbl_elem_E = QtWidgets.QLabel(self.groupBox_1)
        self.lb_tbl_elem_E.setGeometry(QtCore.QRect(433, 66, 29, 16))
        self.lb_tbl_elem_E.setStyleSheet("color: rgb(255, 255, 255);")
        self.lb_tbl_elem_E.setObjectName("lb_tbl_elem_E")
        self.label_8 = QtWidgets.QLabel(self.groupBox_1)
        self.label_8.setGeometry(QtCore.QRect(528, 66, 47, 13))
        self.label_8.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_8.setObjectName("label_8")
        self.lb_tbl_nod_cy = QtWidgets.QLabel(self.groupBox_1)
        self.lb_tbl_nod_cy.setGeometry(QtCore.QRect(688, 66, 29, 16))
        self.lb_tbl_nod_cy.setStyleSheet("color: rgb(255, 255, 255);")
        self.lb_tbl_nod_cy.setObjectName("lb_tbl_nod_cy")
        self.lb_tbl_nod_cx = QtWidgets.QLabel(self.groupBox_1)
        self.lb_tbl_nod_cx.setGeometry(QtCore.QRect(608, 66, 29, 16))
        self.lb_tbl_nod_cx.setStyleSheet("color: rgb(255, 255, 255);")
        self.lb_tbl_nod_cx.setObjectName("lb_tbl_nod_cx")
        self.label_11 = QtWidgets.QLabel(self.groupBox_1)
        self.label_11.setGeometry(QtCore.QRect(29, 250, 47, 13))
        self.label_11.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_11.setObjectName("label_11")
        self.lb_tbl_f_fx = QtWidgets.QLabel(self.groupBox_1)
        self.lb_tbl_f_fx.setGeometry(QtCore.QRect(109, 250, 47, 13))
        self.lb_tbl_f_fx.setStyleSheet("color: rgb(255, 255, 255);")
        self.lb_tbl_f_fx.setObjectName("lb_tbl_f_fx")
        self.lb_tbl_f_fy = QtWidgets.QLabel(self.groupBox_1)
        self.lb_tbl_f_fy.setGeometry(QtCore.QRect(189, 250, 47, 13))
        self.lb_tbl_f_fy.setStyleSheet("color: rgb(255, 255, 255);")
        self.lb_tbl_f_fy.setObjectName("lb_tbl_f_fy")
        self.lb_tbl_f_m = QtWidgets.QLabel(self.groupBox_1)
        self.lb_tbl_f_m.setGeometry(QtCore.QRect(264, 250, 47, 13))
        self.lb_tbl_f_m.setStyleSheet("color: rgb(255, 255, 255);")
        self.lb_tbl_f_m.setObjectName("lb_tbl_f_m")
        self.lb_tbl_fw_wi = QtWidgets.QLabel(self.groupBox_1)
        self.lb_tbl_fw_wi.setGeometry(QtCore.QRect(514, 250, 47, 13))
        self.lb_tbl_fw_wi.setStyleSheet("color: rgb(255, 255, 255);")
        self.lb_tbl_fw_wi.setObjectName("lb_tbl_fw_wi")
        self.lb_tbl_fw_wf = QtWidgets.QLabel(self.groupBox_1)
        self.lb_tbl_fw_wf.setGeometry(QtCore.QRect(629, 250, 47, 13))
        self.lb_tbl_fw_wf.setStyleSheet("color: rgb(255, 255, 255);")
        self.lb_tbl_fw_wf.setObjectName("lb_tbl_fw_wf")
        self.label_18 = QtWidgets.QLabel(self.groupBox_1)
        self.label_18.setGeometry(QtCore.QRect(404, 250, 47, 13))
        self.label_18.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_18.setObjectName("label_18")
        self.label_33 = QtWidgets.QLabel(self.groupBox_1)
        self.label_33.setGeometry(QtCore.QRect(157, 437, 47, 13))
        self.label_33.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_33.setObjectName("label_33")
        self.label_34 = QtWidgets.QLabel(self.groupBox_1)
        self.label_34.setGeometry(QtCore.QRect(47, 437, 47, 13))
        self.label_34.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_34.setObjectName("label_34")
        self.bar_cb_pg_2 = QtWidgets.QFrame(self.pagina_1)
        self.bar_cb_pg_2.setEnabled(True)
        self.bar_cb_pg_2.setGeometry(QtCore.QRect(0, 613, 1363, 31))
        self.bar_cb_pg_2.setMaximumSize(QtCore.QSize(16777215, 36))
        self.bar_cb_pg_2.setStyleSheet("/**background-color: rgb(213, 244, 230);**/background-color: rgb(4, 107, 153);\n"
"")
        self.bar_cb_pg_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.bar_cb_pg_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bar_cb_pg_2.setObjectName("bar_cb_pg_2")
        self.label_archivo = QtWidgets.QLabel(self.bar_cb_pg_2)
        self.label_archivo.setGeometry(QtCore.QRect(1, 1, 440, 31))
        self.label_archivo.setStyleSheet("QLabel{\n"
"background-color: None;\n"
"    \n"
"/*Letra*/\n"
"    font: 10pt \"Arial\";\n"
"    \n"
"    \n"
"    color: rgb(222, 222, 222);\n"
"}")
        self.label_archivo.setObjectName("label_archivo")
        self.cb_convertir_de = QtWidgets.QComboBox(self.bar_cb_pg_2)
        self.cb_convertir_de.setGeometry(QtCore.QRect(1239, 4, 111, 24))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.cb_convertir_de.setFont(font)
        self.cb_convertir_de.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-radius :5px;")
        self.cb_convertir_de.setObjectName("cb_convertir_de")
        self.cb_convertir_de.addItem("")
        self.cb_convertir_de.addItem("")
        self.stackedWidget.addWidget(self.pagina_1)
        self.pagina_2 = QtWidgets.QWidget()
        self.pagina_2.setObjectName("pagina_2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.pagina_2)
        self.groupBox_2.setGeometry(QtCore.QRect(0, 10, 1341, 261))
        self.groupBox_2.setStyleSheet("QGroupBox{\n"
"/*Borde*/\n"
"border: 2px solid rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"\n"
"    /*Letra*/\n"
"    font: 15pt \"Impact\";\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_24 = QtWidgets.QLabel(self.groupBox_2)
        self.label_24.setGeometry(QtCore.QRect(560, 140, 121, 31))
        self.label_24.setStyleSheet("QLabel{\n"
"background-color: None;\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.label_24.setObjectName("label_24")
        self.cb_elemento = QtWidgets.QComboBox(self.groupBox_2)
        self.cb_elemento.setGeometry(QtCore.QRect(690, 147, 51, 21))
        self.cb_elemento.setMinimumSize(QtCore.QSize(0, 0))
        self.cb_elemento.setMaximumSize(QtCore.QSize(377, 1000))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.cb_elemento.setFont(font)
        self.cb_elemento.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.cb_elemento.setStyleSheet("\n"
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
"    color: rgb(255, 255, 255);\n"
"\n"
"    font: 14pt \"Times New Roman\";\n"
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
        self.cb_elemento.setCurrentText("")
        self.cb_elemento.setObjectName("cb_elemento")
        self.label_25 = QtWidgets.QLabel(self.groupBox_2)
        self.label_25.setGeometry(QtCore.QRect(10, 30, 341, 21))
        self.label_25.setStyleSheet("QLabel{\n"
"background-color: None;\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.label_25.setObjectName("label_25")
        self.tbl_MKGE = QtWidgets.QTableWidget(self.groupBox_2)
        self.tbl_MKGE.setGeometry(QtCore.QRect(820, 70, 481, 181))
        self.tbl_MKGE.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.tbl_MKGE.setStyleSheet("QTableWidget{\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius : 5px;\n"
"color: rgb(0, 0, 0);\n"
"font: 75 10pt \"Times New Roman\";\n"
"\n"
"}\n"
"QHeaderView::section{\n"
"border-radius : 1px;\n"
"    background-color: rgb(0, 159, 195);\n"
"\n"
"color: rgb(0, 0, 0);\n"
"font: 75 11pt \"Times New Roman\";\n"
"\n"
"}\n"
"")
        self.tbl_MKGE.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tbl_MKGE.setShowGrid(True)
        self.tbl_MKGE.setGridStyle(QtCore.Qt.SolidLine)
        self.tbl_MKGE.setRowCount(0)
        self.tbl_MKGE.setObjectName("tbl_MKGE")
        self.tbl_MKGE.setColumnCount(6)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_MKGE.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_MKGE.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_MKGE.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_MKGE.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_MKGE.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_MKGE.setHorizontalHeaderItem(5, item)
        self.tbl_MKGE.horizontalHeader().setCascadingSectionResizes(False)
        self.tbl_MKGE.horizontalHeader().setDefaultSectionSize(80)
        self.tbl_MKGE.horizontalHeader().setMinimumSectionSize(42)
        self.tbl_MKGE.horizontalHeader().setSortIndicatorShown(False)
        self.tbl_MKGE.verticalHeader().setVisible(False)
        self.tbl_MKGE.verticalHeader().setCascadingSectionResizes(False)
        self.tbl_MKGE.verticalHeader().setDefaultSectionSize(30)
        self.tbl_MKGE.verticalHeader().setMinimumSectionSize(20)
        self.tbl_MKGE.verticalHeader().setSortIndicatorShown(False)
        self.tbl_MKGE.verticalHeader().setStretchLastSection(False)
        self.label_26 = QtWidgets.QLabel(self.groupBox_2)
        self.label_26.setGeometry(QtCore.QRect(870, 40, 361, 21))
        self.label_26.setStyleSheet("QLabel{\n"
"background-color: None;\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.label_26.setObjectName("label_26")
        self.tbl_propiedades = QtWidgets.QTableWidget(self.groupBox_2)
        self.tbl_propiedades.setGeometry(QtCore.QRect(450, 10, 411, 51))
        self.tbl_propiedades.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.tbl_propiedades.setStyleSheet("QTableWidget{\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius : 5px;\n"
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
"    background-color: rgb(0, 159, 195);\n"
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
        self.tbl_propiedades.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tbl_propiedades.setShowGrid(True)
        self.tbl_propiedades.setGridStyle(QtCore.Qt.SolidLine)
        self.tbl_propiedades.setRowCount(0)
        self.tbl_propiedades.setObjectName("tbl_propiedades")
        self.tbl_propiedades.setColumnCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_propiedades.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_propiedades.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_propiedades.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_propiedades.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_propiedades.setHorizontalHeaderItem(4, item)
        self.tbl_propiedades.horizontalHeader().setCascadingSectionResizes(False)
        self.tbl_propiedades.horizontalHeader().setDefaultSectionSize(82)
        self.tbl_propiedades.horizontalHeader().setHighlightSections(True)
        self.tbl_propiedades.horizontalHeader().setMinimumSectionSize(42)
        self.tbl_propiedades.horizontalHeader().setSortIndicatorShown(False)
        self.tbl_propiedades.verticalHeader().setVisible(False)
        self.tbl_propiedades.verticalHeader().setCascadingSectionResizes(False)
        self.tbl_propiedades.verticalHeader().setDefaultSectionSize(25)
        self.tbl_propiedades.verticalHeader().setSortIndicatorShown(False)
        self.tbl_propiedades.verticalHeader().setStretchLastSection(False)
        self.tbl_MKL = QtWidgets.QTableWidget(self.groupBox_2)
        self.tbl_MKL.setGeometry(QtCore.QRect(10, 70, 481, 181))
        self.tbl_MKL.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.tbl_MKL.setStyleSheet("QTableWidget{\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius : 5px;\n"
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
"    background-color: rgb(0, 159, 195);\n"
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
        self.tbl_MKL.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tbl_MKL.setShowGrid(True)
        self.tbl_MKL.setGridStyle(QtCore.Qt.SolidLine)
        self.tbl_MKL.setRowCount(0)
        self.tbl_MKL.setObjectName("tbl_MKL")
        self.tbl_MKL.setColumnCount(6)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_MKL.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_MKL.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_MKL.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_MKL.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_MKL.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_MKL.setHorizontalHeaderItem(5, item)
        self.tbl_MKL.horizontalHeader().setCascadingSectionResizes(False)
        self.tbl_MKL.horizontalHeader().setDefaultSectionSize(80)
        self.tbl_MKL.horizontalHeader().setMinimumSectionSize(42)
        self.tbl_MKL.horizontalHeader().setSortIndicatorShown(False)
        self.tbl_MKL.verticalHeader().setVisible(False)
        self.tbl_MKL.verticalHeader().setCascadingSectionResizes(False)
        self.tbl_MKL.verticalHeader().setDefaultSectionSize(25)
        self.tbl_MKL.verticalHeader().setMinimumSectionSize(20)
        self.tbl_MKL.verticalHeader().setSortIndicatorShown(False)
        self.tbl_MKL.verticalHeader().setStretchLastSection(False)
        self.groupBox = QtWidgets.QGroupBox(self.pagina_2)
        self.groupBox.setGeometry(QtCore.QRect(0, 280, 1341, 365))
        self.groupBox.setStyleSheet("QGroupBox{\n"
"/*Borde*/\n"
"border: 2px solid rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"\n"
"    /*Letra*/\n"
"    font: 15pt \"Impact\";\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.groupBox.setObjectName("groupBox")
        self.tbl_MKG = QtWidgets.QTableWidget(self.groupBox)
        self.tbl_MKG.setGeometry(QtCore.QRect(10, 50, 531, 290))
        self.tbl_MKG.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.tbl_MKG.setStyleSheet("QTableWidget{\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius : 5px;\n"
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
"    background-color: rgb(0, 159, 195);\n"
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
        self.tbl_MKG.setGridStyle(QtCore.Qt.SolidLine)
        self.tbl_MKG.setRowCount(0)
        self.tbl_MKG.setObjectName("tbl_MKG")
        self.tbl_MKG.setColumnCount(0)
        self.tbl_MKG.horizontalHeader().setCascadingSectionResizes(False)
        self.tbl_MKG.horizontalHeader().setDefaultSectionSize(80)
        self.tbl_MKG.horizontalHeader().setMinimumSectionSize(42)
        self.tbl_MKG.horizontalHeader().setSortIndicatorShown(False)
        self.tbl_MKG.verticalHeader().setVisible(False)
        self.tbl_MKG.verticalHeader().setCascadingSectionResizes(False)
        self.tbl_MKG.verticalHeader().setDefaultSectionSize(25)
        self.tbl_MKG.verticalHeader().setMinimumSectionSize(20)
        self.tbl_MKG.verticalHeader().setSortIndicatorShown(False)
        self.tbl_MKG.verticalHeader().setStretchLastSection(False)
        self.label_27 = QtWidgets.QLabel(self.groupBox)
        self.label_27.setGeometry(QtCore.QRect(10, 30, 221, 21))
        self.label_27.setStyleSheet("QLabel{\n"
"background-color: None;\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.label_27.setObjectName("label_27")
        self.wgt_GDL = MatplotlibWidgetaLienzo(self.groupBox)
        self.wgt_GDL.setGeometry(QtCore.QRect(730, 50, 591, 290))
        self.wgt_GDL.setStyleSheet("/* color de fondo*/\n"
"\n"
"background-color: rgb(179, 239, 255);\n"
"/*borde redondo*/\n"
"border-radius : 10px;\n"
"/* linea de borde*/\n"
"border : 2px solid rgb(205, 205, 205);\n"
"")
        self.wgt_GDL.setObjectName("wgt_GDL")
        self.tbl_vec_F = QtWidgets.QTableWidget(self.groupBox)
        self.tbl_vec_F.setGeometry(QtCore.QRect(600, 50, 80, 290))
        self.tbl_vec_F.setStyleSheet("QTableWidget{\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius : 5px;\n"
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
"    background-color: rgb(0, 159, 195);\n"
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
        self.tbl_vec_F.setObjectName("tbl_vec_F")
        self.tbl_vec_F.setColumnCount(1)
        self.tbl_vec_F.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_vec_F.setHorizontalHeaderItem(0, item)
        self.tbl_vec_F.horizontalHeader().setDefaultSectionSize(80)
        self.tbl_vec_F.verticalHeader().setDefaultSectionSize(25)
        self.tbl_vec_F.verticalHeader().setMinimumSectionSize(20)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(550, 200, 41, 31))
        self.label_3.setObjectName("label_3")
        self.label_28 = QtWidgets.QLabel(self.groupBox)
        self.label_28.setGeometry(QtCore.QRect(600, 30, 131, 21))
        self.label_28.setStyleSheet("QLabel{\n"
"background-color: None;\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.label_28.setObjectName("label_28")
        self.label_29 = QtWidgets.QLabel(self.groupBox)
        self.label_29.setGeometry(QtCore.QRect(940, 20, 161, 21))
        self.label_29.setStyleSheet("QLabel{\n"
"background-color: None;\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.label_29.setObjectName("label_29")
        self.stackedWidget.addWidget(self.pagina_2)
        self.pagina_3 = QtWidgets.QWidget()
        self.pagina_3.setObjectName("pagina_3")
        self.groupBox_4 = QtWidgets.QGroupBox(self.pagina_3)
        self.groupBox_4.setGeometry(QtCore.QRect(0, 10, 1341, 611))
        self.groupBox_4.setStyleSheet("QGroupBox{\n"
"/*Borde*/\n"
"border: 2px solid rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"\n"
"    /*Letra*/\n"
"    font: 15pt \"Impact\";\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.groupBox_4.setObjectName("groupBox_4")
        self.frame_4 = QtWidgets.QFrame(self.groupBox_4)
        self.frame_4.setGeometry(QtCore.QRect(10, 30, 541, 561))
        self.frame_4.setStyleSheet("/*border: 2px solid rgb(97, 134, 133);*/\n"
"background-color: rgb(4, 120, 170);\n"
"border-radius: 5px;")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.tbl_g_delta = QtWidgets.QTableWidget(self.frame_4)
        self.tbl_g_delta.setGeometry(QtCore.QRect(10, 10, 501, 531))
        self.tbl_g_delta.setStyleSheet("QTableWidget{\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius : 5px;\n"
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
"    background-color: rgb(0, 159, 195);\n"
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
        self.tbl_g_delta.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tbl_g_delta.setObjectName("tbl_g_delta")
        self.tbl_g_delta.setColumnCount(2)
        self.tbl_g_delta.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_g_delta.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_g_delta.setHorizontalHeaderItem(1, item)
        self.tbl_g_delta.horizontalHeader().setDefaultSectionSize(250)
        self.tbl_g_delta.verticalHeader().setDefaultSectionSize(25)
        self.tbl_g_delta.verticalHeader().setMinimumSectionSize(20)
        self.frame_3 = QtWidgets.QFrame(self.groupBox_4)
        self.frame_3.setGeometry(QtCore.QRect(580, 30, 721, 561))
        self.frame_3.setStyleSheet("/*border: 2px solid rgb(97, 134, 133);*/\n"
"background-color: rgb(4, 120, 170);\n"
"border-radius: 10px;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.tbl_g_delta_elem = QtWidgets.QTableWidget(self.frame_3)
        self.tbl_g_delta_elem.setGeometry(QtCore.QRect(50, 30, 310, 280))
        self.tbl_g_delta_elem.setStyleSheet("QTableWidget{\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius : 5px;\n"
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
"    background-color: rgb(0, 159, 195);\n"
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
        self.tbl_g_delta_elem.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tbl_g_delta_elem.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tbl_g_delta_elem.setAutoScroll(True)
        self.tbl_g_delta_elem.setObjectName("tbl_g_delta_elem")
        self.tbl_g_delta_elem.setColumnCount(2)
        self.tbl_g_delta_elem.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_g_delta_elem.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_g_delta_elem.setHorizontalHeaderItem(1, item)
        self.tbl_g_delta_elem.horizontalHeader().setDefaultSectionSize(155)
        self.tbl_g_delta_elem.verticalHeader().setDefaultSectionSize(45)
        self.tbl_g_delta_elem.verticalHeader().setMinimumSectionSize(20)
        self.layoutWidget_3 = QtWidgets.QWidget(self.frame_3)
        self.layoutWidget_3.setGeometry(QtCore.QRect(266, 360, 241, 151))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_30 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_30.setObjectName("label_30")
        self.verticalLayout_2.addWidget(self.label_30)
        self.slider_Elem = QtWidgets.QSlider(self.layoutWidget_3)
        self.slider_Elem.setAutoFillBackground(False)
        self.slider_Elem.setStyleSheet("background-color: rgb(213, 244, 230);\n"
"border: 2px solid rgb(97, 134, 133);\n"
"border-radius: 5px;")
        self.slider_Elem.setOrientation(QtCore.Qt.Horizontal)
        self.slider_Elem.setInvertedControls(False)
        self.slider_Elem.setObjectName("slider_Elem")
        self.verticalLayout_2.addWidget(self.slider_Elem)
        self.n_Elem = QtWidgets.QLabel(self.layoutWidget_3)
        self.n_Elem.setAlignment(QtCore.Qt.AlignCenter)
        self.n_Elem.setObjectName("n_Elem")
        self.verticalLayout_2.addWidget(self.n_Elem)
        self.tbl_fuerzas_internas = QtWidgets.QTableWidget(self.frame_3)
        self.tbl_fuerzas_internas.setGeometry(QtCore.QRect(492, 28, 218, 280))
        self.tbl_fuerzas_internas.setStyleSheet("QTableWidget{\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius : 5px;\n"
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
"    background-color: rgb(0, 159, 195);\n"
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
        self.tbl_fuerzas_internas.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tbl_fuerzas_internas.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tbl_fuerzas_internas.setAutoScroll(False)
        self.tbl_fuerzas_internas.setObjectName("tbl_fuerzas_internas")
        self.tbl_fuerzas_internas.setColumnCount(1)
        self.tbl_fuerzas_internas.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_fuerzas_internas.setHorizontalHeaderItem(0, item)
        self.tbl_fuerzas_internas.horizontalHeader().setDefaultSectionSize(220)
        self.tbl_fuerzas_internas.horizontalHeader().setMinimumSectionSize(37)
        self.tbl_fuerzas_internas.verticalHeader().setDefaultSectionSize(45)
        self.tbl_fuerzas_internas.verticalHeader().setMinimumSectionSize(20)
        self.label_5 = QtWidgets.QLabel(self.frame_3)
        self.label_5.setGeometry(QtCore.QRect(451, 62, 28, 22))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame_3)
        self.label_6.setGeometry(QtCore.QRect(450, 106, 28, 22))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.frame_3)
        self.label_7.setGeometry(QtCore.QRect(451, 146, 28, 22))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_9 = QtWidgets.QLabel(self.frame_3)
        self.label_9.setGeometry(QtCore.QRect(453, 268, 28, 22))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.frame_3)
        self.label_10.setGeometry(QtCore.QRect(453, 185, 28, 22))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_12 = QtWidgets.QLabel(self.frame_3)
        self.label_12.setGeometry(QtCore.QRect(452, 229, 28, 22))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.stackedWidget.addWidget(self.pagina_3)
        self.pagina_5 = QtWidgets.QWidget()
        self.pagina_5.setObjectName("pagina_5")
        self.groupBox_5 = QtWidgets.QGroupBox(self.pagina_5)
        self.groupBox_5.setGeometry(QtCore.QRect(20, 14, 1295, 631))
        self.groupBox_5.setStyleSheet("QGroupBox{\n"
"/*Borde*/\n"
"border: 2px solid rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"\n"
"    /*Letra*/\n"
"    font: 15pt \"Impact\";\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.groupBox_5.setObjectName("groupBox_5")
        self.wgt_FIE = MatplotlibWidgetaLienzo(self.groupBox_5)
        self.wgt_FIE.setGeometry(QtCore.QRect(36, 29, 1211, 591))
        self.wgt_FIE.setStyleSheet("background-color: rgb(179, 239, 255);\n"
"border-radius: 5px;")
        self.wgt_FIE.setObjectName("wgt_FIE")
        self.stackedWidget.addWidget(self.pagina_5)
        self.pagina_4 = QtWidgets.QWidget()
        self.pagina_4.setObjectName("pagina_4")
        self.groupBox_6 = QtWidgets.QGroupBox(self.pagina_4)
        self.groupBox_6.setGeometry(QtCore.QRect(112, 9, 1219, 631))
        self.groupBox_6.setStyleSheet("QGroupBox{\n"
"/*Borde*/\n"
"border: 2px solid rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"\n"
"    /*Letra*/\n"
"    font: 15pt \"Impact\";\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.groupBox_6.setObjectName("groupBox_6")
        self.frame_5 = QtWidgets.QFrame(self.groupBox_6)
        self.frame_5.setGeometry(QtCore.QRect(290, 30, 904, 561))
        self.frame_5.setStyleSheet("background-color: rgb(4, 120, 170);\n"
"border-radius: 5px;")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.wgt_deformada = MatplotlibWidgetaLienzo(self.frame_5)
        self.wgt_deformada.setGeometry(QtCore.QRect(20, 30, 878, 560))
        self.wgt_deformada.setStyleSheet("background-color: rgb(179, 239, 255);\n"
"border-radius: 5px;")
        self.wgt_deformada.setObjectName("wgt_deformada")
        self.frame_2 = QtWidgets.QFrame(self.groupBox_6)
        self.frame_2.setGeometry(QtCore.QRect(20, 30, 261, 561))
        self.frame_2.setStyleSheet("/*border: 2px solid rgb(97, 134, 133);*/\n"
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
"    font: 87 20pt \"Segoe UI Black\";\n"
"    background-color: none;\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.slider_zoom_defor = QtWidgets.QSlider(self.frame_2)
        self.slider_zoom_defor.setGeometry(QtCore.QRect(70, 60, 130, 20))
        self.slider_zoom_defor.setStyleSheet("background-color: rgb(213, 244, 230);\n"
"border: 2px solid rgb(97, 134, 133);\n"
"border-radius: 5px;")
        self.slider_zoom_defor.setOrientation(QtCore.Qt.Horizontal)
        self.slider_zoom_defor.setObjectName("slider_zoom_defor")
        self.inline_amplificacion = QtWidgets.QLineEdit(self.frame_2)
        self.inline_amplificacion.setGeometry(QtCore.QRect(90, 160, 95, 20))
        self.inline_amplificacion.setObjectName("inline_amplificacion")
        self.label_31 = QtWidgets.QLabel(self.frame_2)
        self.label_31.setGeometry(QtCore.QRect(0, 110, 271, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_31.setFont(font)
        self.label_31.setStyleSheet("")
        self.label_31.setObjectName("label_31")
        self.label_32 = QtWidgets.QLabel(self.frame_2)
        self.label_32.setGeometry(QtCore.QRect(0, 30, 261, 31))
        self.label_32.setStyleSheet("")
        self.label_32.setObjectName("label_32")
        self.btn_amp_deformada = QtWidgets.QPushButton(self.frame_2)
        self.btn_amp_deformada.setGeometry(QtCore.QRect(100, 210, 65, 41))
        font = QtGui.QFont()
        font.setFamily("Bell MT")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.btn_amp_deformada.setFont(font)
        self.btn_amp_deformada.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_amp_deformada.setStyleSheet("QPushButton{\n"
"/* Color de fondo*/\n"
"/**background-color: rgb(213, 244, 230);**/\n"
"    background-color: rgb(2, 85, 120);\n"
"color: rgb(255,255,255);\n"
"font: 75 12pt \"Bell MT\";\n"
"border-radius : 4px;\n"
"/**border : 2px solid  rgb(240, 240, 240);**/\n"
"\n"
"}\n"
"\n"
"/* Cambia color al estar sobre*/\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: rgb(0, 207, 255);\n"
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
        self.btn_amp_deformada.setIconSize(QtCore.QSize(20, 20))
        self.btn_amp_deformada.setObjectName("btn_amp_deformada")
        self.btn_screen_deformada = QtWidgets.QPushButton(self.frame_2)
        self.btn_screen_deformada.setGeometry(QtCore.QRect(60, 330, 151, 111))
        font = QtGui.QFont()
        font.setFamily("Bell MT")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.btn_screen_deformada.setFont(font)
        self.btn_screen_deformada.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_screen_deformada.setStyleSheet("QPushButton{\n"
"/* Color de fondo*/\n"
"/**background-color: rgb(213, 244, 230);**/\n"
"    background-color: none;\n"
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
"    \n"
"    \n"
"    background-color: rgb(24, 135, 204);\n"
"}\n"
"/* Cambia color al dar click*/\n"
"QPushButton:pressed{\n"
"\n"
"    background-color: rgb(26, 146, 220);\n"
"\n"
"}\n"
"\n"
"\n"
"")
        self.btn_screen_deformada.setText("")
        icon1 = QtGui.QIcon(os.path.join(basedir,"resource", "captura2.ico"))
        #icon1.addPixmap(QtGui.QPixmap("resource/captura2.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_screen_deformada.setIcon(icon1)
        self.btn_screen_deformada.setIconSize(QtCore.QSize(150, 150))
        self.btn_screen_deformada.setObjectName("btn_screen_deformada")
        self.stackedWidget.addWidget(self.pagina_4)
        self.label_14 = QtWidgets.QLabel(self.cb_paginas)
        self.label_14.setGeometry(QtCore.QRect(12, 652, 519, 29))
        self.label_14.setObjectName("label_14")
        self.bar_cb_pg = QtWidgets.QFrame(self.frame_10)
        self.bar_cb_pg.setEnabled(True)
        self.bar_cb_pg.setGeometry(QtCore.QRect(0, 0, 1363, 36))
        self.bar_cb_pg.setMaximumSize(QtCore.QSize(16777215, 36))
        self.bar_cb_pg.setStyleSheet("/**background-color: rgb(213, 244, 230);**/background-color: rgb(4, 107, 153);\n"
"")
        self.bar_cb_pg.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.bar_cb_pg.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bar_cb_pg.setObjectName("bar_cb_pg")
        self.btn_abrir = QtWidgets.QPushButton(self.bar_cb_pg)
        self.btn_abrir.setGeometry(QtCore.QRect(50, 0, 32, 34))
        self.btn_abrir.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_abrir.setStyleSheet("QPushButton{\n"
"/* Color de fondo*/\n"
"/**background-color: rgb(213, 244, 230);**/\n"
"    background-color: rgb(2, 85, 120);\n"
"\n"
"font: 75 12pt \"Bell MT\";\n"
"border-radius : 4px;\n"
"/**border : 2px solid  rgb(240, 240, 240);**/\n"
"\n"
"}\n"
"\n"
"/* Cambia color al estar sobre*/\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: rgb(0, 207, 255);\n"
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
        self.btn_abrir.setText("")
        icon2 = QtGui.QIcon(os.path.join(basedir,"resource", "Abrir.ico"))
        #icon2.addPixmap(QtGui.QPixmap("resource/Abrir.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_abrir.setIcon(icon2)
        self.btn_abrir.setIconSize(QtCore.QSize(20, 20))
        self.btn_abrir.setObjectName("btn_abrir")
        self.btn_guardar = QtWidgets.QPushButton(self.bar_cb_pg)
        self.btn_guardar.setGeometry(QtCore.QRect(90, 0, 32, 34))
        self.btn_guardar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_guardar.setStyleSheet("QPushButton{\n"
"/* Color de fondo*/\n"
"/**background-color: rgb(213, 244, 230);**/\n"
"    background-color: rgb(2, 85, 120);\n"
"\n"
"font: 75 12pt \"Bell MT\";\n"
"border-radius : 4px;\n"
"/**border : 2px solid  rgb(240, 240, 240);**/\n"
"\n"
"}\n"
"\n"
"/* Cambia color al estar sobre*/\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: rgb(0, 207, 255);\n"
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
        self.btn_guardar.setText("")
        icon3 = QtGui.QIcon(os.path.join(basedir,"resource", "Guardar.ico"))
        #icon3.addPixmap(QtGui.QPixmap("resource/Guardar.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_guardar.setIcon(icon3)
        self.btn_guardar.setIconSize(QtCore.QSize(20, 20))
        self.btn_guardar.setObjectName("btn_guardar")
        self.btn_inicio = QtWidgets.QPushButton(self.bar_cb_pg)
        self.btn_inicio.setGeometry(QtCore.QRect(130, 0, 32, 34))
        self.btn_inicio.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_inicio.setStyleSheet("QPushButton{\n"
"/* Color de fondo*/\n"
"/**background-color: rgb(213, 244, 230);**/\n"
"    background-color: rgb(2, 85, 120);\n"
"\n"
"font: 75 12pt \"Bell MT\";\n"
"border-radius : 4px;\n"
"/**border : 2px solid  rgb(240, 240, 240);**/\n"
"\n"
"}\n"
"\n"
"/* Cambia color al estar sobre*/\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: rgb(0, 207, 255);\n"
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
        self.btn_inicio.setText("")
        icon4 = QtGui.QIcon(os.path.join(basedir,"resource", "I.ico"))
        #icon4.addPixmap(QtGui.QPixmap("resource/I.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_inicio.setIcon(icon4)
        self.btn_inicio.setIconSize(QtCore.QSize(20, 20))
        self.btn_inicio.setObjectName("btn_inicio")
        self.btn_matrices = QtWidgets.QPushButton(self.bar_cb_pg)
        self.btn_matrices.setGeometry(QtCore.QRect(170, 0, 32, 34))
        self.btn_matrices.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_matrices.setStyleSheet("QPushButton{\n"
"/* Color de fondo*/\n"
"/**background-color: rgb(213, 244, 230);**/\n"
"    background-color: rgb(2, 85, 120);\n"
"\n"
"font: 75 12pt \"Bell MT\";\n"
"border-radius : 4px;\n"
"/**border : 2px solid  rgb(240, 240, 240);**/\n"
"\n"
"}\n"
"\n"
"/* Cambia color al estar sobre*/\n"
"QPushButton:hover{\n"
"    background-color: rgb(0, 207, 255);\n"
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
        self.btn_matrices.setText("")
        icon5 = QtGui.QIcon(os.path.join(basedir,"resource", "K.ico"))
        #icon5.addPixmap(QtGui.QPixmap("resource/K.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_matrices.setIcon(icon5)
        self.btn_matrices.setIconSize(QtCore.QSize(20, 20))
        self.btn_matrices.setObjectName("btn_matrices")
        self.btn_delta_fuerza = QtWidgets.QPushButton(self.bar_cb_pg)
        self.btn_delta_fuerza.setGeometry(QtCore.QRect(210, 0, 32, 34))
        font = QtGui.QFont()
        font.setFamily("Bell MT")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.btn_delta_fuerza.setFont(font)
        self.btn_delta_fuerza.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_delta_fuerza.setMouseTracking(True)
        self.btn_delta_fuerza.setAccessibleName("")
        self.btn_delta_fuerza.setAccessibleDescription("")
        self.btn_delta_fuerza.setStyleSheet("QPushButton{\n"
"/* Color de fondo*/\n"
"/**background-color: rgb(213, 244, 230);**/\n"
"    background-color: rgb(2, 85, 120);\n"
"\n"
"font: 75 12pt \"Bell MT\";\n"
"border-radius : 4px;\n"
"/**border : 2px solid  rgb(240, 240, 240);**/\n"
"\n"
"}\n"
"\n"
"/* Cambia color al estar sobre*/\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: rgb(0, 207, 255);\n"
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
        self.btn_delta_fuerza.setText("")
        icon6 = QtGui.QIcon(os.path.join(basedir,"resource", "Delta-F.png"))
        #icon6.addPixmap(QtGui.QPixmap("resource/Delta-F.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_delta_fuerza.setIcon(icon6)
        self.btn_delta_fuerza.setIconSize(QtCore.QSize(23, 23))
        self.btn_delta_fuerza.setCheckable(False)
        self.btn_delta_fuerza.setChecked(False)
        self.btn_delta_fuerza.setObjectName("btn_delta_fuerza")
        self.btn_fuerzas = QtWidgets.QPushButton(self.bar_cb_pg)
        self.btn_fuerzas.setGeometry(QtCore.QRect(250, 0, 32, 34))
        self.btn_fuerzas.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_fuerzas.setStyleSheet("QPushButton{\n"
"/* Color de fondo*/\n"
"/**background-color: rgb(213, 244, 230);**/\n"
"    background-color: rgb(2, 85, 120);\n"
"\n"
"font: 75 12pt \"Bell MT\";\n"
"border-radius : 4px;\n"
"/**border : 2px solid  rgb(240, 240, 240);**/\n"
"\n"
"}\n"
"\n"
"/* Cambia color al estar sobre*/\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: rgb(0, 207, 255);\n"
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
        self.btn_fuerzas.setText("")
        icon7 = QtGui.QIcon(os.path.join(basedir,"resource", "F.ico"))
        #icon7.addPixmap(QtGui.QPixmap("resource/F.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_fuerzas.setIcon(icon7)
        self.btn_fuerzas.setIconSize(QtCore.QSize(20, 20))
        self.btn_fuerzas.setObjectName("btn_fuerzas")
        self.btn_deformada = QtWidgets.QPushButton(self.bar_cb_pg)
        self.btn_deformada.setGeometry(QtCore.QRect(290, 0, 32, 34))
        self.btn_deformada.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_deformada.setMouseTracking(False)
        self.btn_deformada.setStyleSheet("QPushButton{\n"
"/* Color de fondo*/\n"
"/**background-color: rgb(213, 244, 230);**/\n"
"    background-color: rgb(2, 85, 120);\n"
"\n"
"font: 75 12pt \"Bell MT\";\n"
"border-radius : 4px;\n"
"/**border : 2px solid  rgb(240, 240, 240);**/\n"
"\n"
"}\n"
"\n"
"/* Cambia color al estar sobre*/\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: rgb(0, 207, 255);\n"
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
        self.btn_deformada.setText("")
        icon8 = QtGui.QIcon(os.path.join(basedir,"resource", "D.ico"))
        #icon8.addPixmap(QtGui.QPixmap("resource/D.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_deformada.setIcon(icon8)
        self.btn_deformada.setIconSize(QtCore.QSize(30, 20))
        self.btn_deformada.setCheckable(False)
        self.btn_deformada.setChecked(False)
        self.btn_deformada.setAutoDefault(False)
        self.btn_deformada.setObjectName("btn_deformada")
        self.btn_nuevo = QtWidgets.QPushButton(self.bar_cb_pg)
        self.btn_nuevo.setGeometry(QtCore.QRect(10, 0, 32, 34))
        self.btn_nuevo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_nuevo.setStyleSheet("QPushButton{\n"
"/* Color de fondo*/\n"
"/**background-color: rgb(213, 244, 230);**/\n"
"    background-color: rgb(2, 85, 120);\n"
"\n"
"font: 75 12pt \"Bell MT\";\n"
"border-radius : 4px;\n"
"/**border : 2px solid  rgb(240, 240, 240);**/\n"
"\n"
"}\n"
"\n"
"/* Cambia color al estar sobre*/\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: rgb(0, 207, 255);\n"
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
        self.btn_nuevo.setText("")
        icon9 = QtGui.QIcon(os.path.join(basedir,"resource", "Nuevo.ico"))
        icon9.addPixmap(QtGui.QPixmap("resource/Nuevo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_nuevo.setIcon(icon9)
        self.btn_nuevo.setIconSize(QtCore.QSize(20, 20))
        self.btn_nuevo.setObjectName("btn_nuevo")
        self.verticalLayout_3.addWidget(self.frame_10)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        Porticos.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Porticos)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1365, 21))
        self.menubar.setObjectName("menubar")
        self.menuArchivo = QtWidgets.QMenu(self.menubar)
        self.menuArchivo.setObjectName("menuArchivo")
        self.menuVista = QtWidgets.QMenu(self.menubar)
        self.menuVista.setObjectName("menuVista")
        self.menuHerramientas = QtWidgets.QMenu(self.menubar)
        self.menuHerramientas.setObjectName("menuHerramientas")
        self.menuAcerca_de = QtWidgets.QMenu(self.menubar)
        self.menuAcerca_de.setObjectName("menuAcerca_de")
        Porticos.setMenuBar(self.menubar)
        self.actionNuevo = QtWidgets.QAction(Porticos)
        self.actionNuevo.setObjectName("actionNuevo")
        self.actionAbrir = QtWidgets.QAction(Porticos)
        self.actionAbrir.setObjectName("actionAbrir")
        self.actionGuardar = QtWidgets.QAction(Porticos)
        self.actionGuardar.setObjectName("actionGuardar")
        self.actionSalir = QtWidgets.QAction(Porticos)
        self.actionSalir.setObjectName("actionSalir")
        self.actionTema_claro = QtWidgets.QAction(Porticos)
        self.actionTema_claro.setObjectName("actionTema_claro")
        self.actionTema_oscuro = QtWidgets.QAction(Porticos)
        self.actionTema_oscuro.setObjectName("actionTema_oscuro")
        self.actionConversor_de_unidades = QtWidgets.QAction(Porticos)
        self.actionConversor_de_unidades.setObjectName("actionConversor_de_unidades")
        self.actionInformacion = QtWidgets.QAction(Porticos)
        self.actionInformacion.setObjectName("actionInformacion")
        self.actionManual_de_uso = QtWidgets.QAction(Porticos)
        self.actionManual_de_uso.setObjectName("actionManual_de_uso")
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
        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menuVista.menuAction())
        self.menubar.addAction(self.menuHerramientas.menuAction())
        self.menubar.addAction(self.menuAcerca_de.menuAction())

        self.retranslateUi(Porticos)
        QtCore.QMetaObject.connectSlotsByName(Porticos)

    def retranslateUi(self, Porticos):
        _translate = QtCore.QCoreApplication.translate
        Porticos.setWindowTitle(_translate("Porticos", "ANEPY"))
        self.groupBox_1.setTitle(_translate("Porticos", "INGRESE DATOS"))
        item = self.tbl_Nod.horizontalHeaderItem(0)
        item.setText(_translate("Porticos", "Nodo"))
        item = self.tbl_Nod.horizontalHeaderItem(1)
        item.setText(_translate("Porticos", "Coord. x"))
        item = self.tbl_Nod.horizontalHeaderItem(2)
        item.setText(_translate("Porticos", "Coorrd. y"))
        item = self.tbl_Fuer.horizontalHeaderItem(0)
        item.setText(_translate("Porticos", "Nodo"))
        item = self.tbl_Fuer.horizontalHeaderItem(1)
        item.setText(_translate("Porticos", "Fx"))
        item = self.tbl_Fuer.horizontalHeaderItem(2)
        item.setText(_translate("Porticos", "Fy"))
        item = self.tbl_Fuer.horizontalHeaderItem(3)
        item.setText(_translate("Porticos", "Mz"))
        self.label_13.setText(_translate("Porticos", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Cantidad de Restricciones:</span></p></body></html>"))
        item = self.tbl_Rest.horizontalHeaderItem(0)
        item.setText(_translate("Porticos", "Tipo"))
        item = self.tbl_Rest.horizontalHeaderItem(1)
        item.setText(_translate("Porticos", "Nodo"))
        item = self.tbl_Rest.horizontalHeaderItem(2)
        item.setText(_translate("Porticos", "#  Restriciones"))
        self.label_19.setText(_translate("Porticos", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Tipos de apoyos</span></p></body></html>"))
        self.btn_analizar.setText(_translate("Porticos", "Analizar"))
        self.btn_analizar.setShortcut(_translate("Porticos", "Ctrl+Return"))
        self.label_20.setText(_translate("Porticos", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Cantidad de elementos:  </span></p></body></html>"))
        self.label_21.setText(_translate("Porticos", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Cantidad de  nodos:</span></p></body></html>"))
        self.label_22.setText(_translate("Porticos", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Cantidad de fuerzas:</span></p></body></html>"))
        item = self.tbl_Fuer_W.horizontalHeaderItem(0)
        item.setText(_translate("Porticos", "Elemento"))
        item = self.tbl_Fuer_W.horizontalHeaderItem(1)
        item.setText(_translate("Porticos", "W i"))
        item = self.tbl_Fuer_W.horizontalHeaderItem(2)
        item.setText(_translate("Porticos", "W f"))
        self.label_23.setText(_translate("Porticos", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Cantidad de fuerzas W:</span></p></body></html>"))
        item = self.tbl_Elem.horizontalHeaderItem(0)
        item.setText(_translate("Porticos", "Elemento"))
        item = self.tbl_Elem.horizontalHeaderItem(1)
        item.setText(_translate("Porticos", "Nodo inicial"))
        item = self.tbl_Elem.horizontalHeaderItem(2)
        item.setText(_translate("Porticos", "Nodo final"))
        item = self.tbl_Elem.horizontalHeaderItem(3)
        item.setText(_translate("Porticos", "Base"))
        item = self.tbl_Elem.horizontalHeaderItem(4)
        item.setText(_translate("Porticos", "Altura"))
        item = self.tbl_Elem.horizontalHeaderItem(5)
        item.setText(_translate("Porticos", "Mod. E"))
        self.label.setText(_translate("Porticos", "[unidad]"))
        self.label_2.setText(_translate("Porticos", "[unidad]"))
        self.label_4.setText(_translate("Porticos", "[unidad]"))
        self.lb_tbl_elem_B.setText(_translate("Porticos", "<html><head/><body><p align=\"center\">[m]</p></body></html>"))
        self.lb_tbl_elem_h.setText(_translate("Porticos", "<html><head/><body><p align=\"center\">[m]</p></body></html>"))
        self.lb_tbl_elem_E.setText(_translate("Porticos", "<html><head/><body><p align=\"center\">[MPa]</p></body></html>"))
        self.label_8.setText(_translate("Porticos", "[unidad]"))
        self.lb_tbl_nod_cy.setText(_translate("Porticos", "<html><head/><body><p align=\"center\">[m]</p></body></html>"))
        self.lb_tbl_nod_cx.setText(_translate("Porticos", "<html><head/><body><p align=\"center\">[m]</p></body></html>"))
        self.label_11.setText(_translate("Porticos", "[unidad]"))
        self.lb_tbl_f_fx.setText(_translate("Porticos", "<html><head/><body><p align=\"center\">[KN]</p></body></html>"))
        self.lb_tbl_f_fy.setText(_translate("Porticos", "<html><head/><body><p align=\"center\">[KN]</p></body></html>"))
        self.lb_tbl_f_m.setText(_translate("Porticos", "<html><head/><body><p align=\"center\">[KN-m]</p></body></html>"))
        self.lb_tbl_fw_wi.setText(_translate("Porticos", "<html><head/><body><p align=\"center\">[KN/m]</p></body></html>"))
        self.lb_tbl_fw_wf.setText(_translate("Porticos", "<html><head/><body><p align=\"center\">[KN/m]</p></body></html>"))
        self.label_18.setText(_translate("Porticos", "[unidad]"))
        self.label_33.setText(_translate("Porticos", "[unidad]"))
        self.label_34.setText(_translate("Porticos", "[unidad]"))
        self.label_archivo.setText(_translate("Porticos", "<html><head/><body><p><span style=\" font-weight:600; font-style:italic;\">Archivo: </span></p></body></html>"))
        self.cb_convertir_de.setToolTip(_translate("Porticos", "Sistema de Unidades"))
        self.cb_convertir_de.setItemText(0, _translate("Porticos", "m, KN, MPa"))
        self.cb_convertir_de.setItemText(1, _translate("Porticos", "pulg, Lb, Psi"))
        self.groupBox_2.setTitle(_translate("Porticos", "Datos por Elemento"))
        self.label_24.setText(_translate("Porticos", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">Elemento:</span></p></body></html>"))
        self.label_25.setText(_translate("Porticos", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Matriz de Rigidez Local de elemento:</span></p></body></html>"))
        self.tbl_MKGE.setSortingEnabled(False)
        item = self.tbl_MKGE.horizontalHeaderItem(0)
        item.setText(_translate("Porticos", "1"))
        item = self.tbl_MKGE.horizontalHeaderItem(1)
        item.setText(_translate("Porticos", "2"))
        item = self.tbl_MKGE.horizontalHeaderItem(2)
        item.setText(_translate("Porticos", "3"))
        item = self.tbl_MKGE.horizontalHeaderItem(3)
        item.setText(_translate("Porticos", "4"))
        item = self.tbl_MKGE.horizontalHeaderItem(4)
        item.setText(_translate("Porticos", "5"))
        item = self.tbl_MKGE.horizontalHeaderItem(5)
        item.setText(_translate("Porticos", "6"))
        self.label_26.setText(_translate("Porticos", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Matriz de Rigidez Global de elemento:</span></p></body></html>"))
        self.tbl_propiedades.setSortingEnabled(False)
        item = self.tbl_propiedades.horizontalHeaderItem(0)
        item.setText(_translate("Porticos", "L"))
        item = self.tbl_propiedades.horizontalHeaderItem(1)
        item.setText(_translate("Porticos", "A"))
        item = self.tbl_propiedades.horizontalHeaderItem(2)
        item.setText(_translate("Porticos", "Mod E"))
        item = self.tbl_propiedades.horizontalHeaderItem(3)
        item.setText(_translate("Porticos", "Iz"))
        item = self.tbl_propiedades.horizontalHeaderItem(4)
        item.setText(_translate("Porticos", "Angulo"))
        self.tbl_MKL.setSortingEnabled(False)
        item = self.tbl_MKL.horizontalHeaderItem(0)
        item.setText(_translate("Porticos", "1"))
        item = self.tbl_MKL.horizontalHeaderItem(1)
        item.setText(_translate("Porticos", "2"))
        item = self.tbl_MKL.horizontalHeaderItem(2)
        item.setText(_translate("Porticos", "3"))
        item = self.tbl_MKL.horizontalHeaderItem(3)
        item.setText(_translate("Porticos", "4"))
        item = self.tbl_MKL.horizontalHeaderItem(4)
        item.setText(_translate("Porticos", "5"))
        item = self.tbl_MKL.horizontalHeaderItem(5)
        item.setText(_translate("Porticos", "6"))
        self.groupBox.setTitle(_translate("Porticos", "Matriz de Rigidez - Vector Fuerza - GDL"))
        self.tbl_MKG.setSortingEnabled(False)
        self.label_27.setText(_translate("Porticos", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Matriz de Rigidez Global:</span></p></body></html>"))
        item = self.tbl_vec_F.horizontalHeaderItem(0)
        item.setText(_translate("Porticos", "F"))
        self.label_3.setText(_translate("Porticos", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">{F}=</span></p></body></html>"))
        self.label_28.setText(_translate("Porticos", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Vector Fuerza:</span></p></body></html>"))
        self.label_29.setText(_translate("Porticos", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Grados De Libertad</span></p></body></html>"))
        self.groupBox_4.setTitle(_translate("Porticos", "Grados De Libertad-Desplazamiento-Fuerzas internas"))
        item = self.tbl_g_delta.horizontalHeaderItem(0)
        item.setText(_translate("Porticos", "        Grados          "))
        item = self.tbl_g_delta.horizontalHeaderItem(1)
        item.setText(_translate("Porticos", "          Δ o  θ      "))
        item = self.tbl_g_delta_elem.horizontalHeaderItem(0)
        item.setText(_translate("Porticos", "             Grados Elem        "))
        item = self.tbl_g_delta_elem.horizontalHeaderItem(1)
        item.setText(_translate("Porticos", "          Δ o  θ      "))
        self.label_30.setText(_translate("Porticos", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Elementos</span></p></body></html>"))
        self.n_Elem.setText(_translate("Porticos", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">0</span></p></body></html>"))
        item = self.tbl_fuerzas_internas.horizontalHeaderItem(0)
        item.setText(_translate("Porticos", "Fuerza"))
        self.label_5.setText(_translate("Porticos", "<html><head/><body><p><span style=\" font-size:11pt;\">FNi</span></p></body></html>"))
        self.label_6.setText(_translate("Porticos", "<html><head/><body><p><span style=\" font-size:11pt;\">Fvi</span></p></body></html>"))
        self.label_7.setText(_translate("Porticos", "<html><head/><body><p><span style=\" font-size:11pt;\">Mi</span></p></body></html>"))
        self.label_9.setText(_translate("Porticos", "<html><head/><body><p><span style=\" font-size:11pt;\">Mf</span></p></body></html>"))
        self.label_10.setText(_translate("Porticos", "<html><head/><body><p><span style=\" font-size:11pt;\">FNf</span></p></body></html>"))
        self.label_12.setText(_translate("Porticos", "<html><head/><body><p><span style=\" font-size:11pt;\">Fvf</span></p></body></html>"))
        self.groupBox_5.setTitle(_translate("Porticos", "Fuerzas Internas en Nodos"))
        self.groupBox_6.setTitle(_translate("Porticos", "Deformada de la estructura"))
        self.label_31.setText(_translate("Porticos", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600;\">Ingrese valor de amplificacion</span></p><p><span style=\" font-weight:600;\"><br/></span></p></body></html>"))
        self.label_32.setText(_translate("Porticos", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Deformar<br/></span></p><p align=\"center\"><span style=\" font-size:12pt;\"><br/></span></p></body></html>"))
        self.btn_amp_deformada.setText(_translate("Porticos", "Aplicar"))
        self.label_14.setText(_translate("Porticos", "<html><head/><body><p><span style=\" font-size:7pt; font-weight:600;\">Desarrollado por: </span><span style=\" font-size:7pt;\">JULIANA ANDREA GONZALEZ ROMAÑA Y YHOAN SMITH MOSQUERA PEÑALOZA</span></p></body></html>"))
        self.btn_abrir.setToolTip(_translate("Porticos", "Abrir"))
        self.btn_guardar.setToolTip(_translate("Porticos", "Guardar"))
        self.btn_inicio.setToolTip(_translate("Porticos", "Inicio"))
        self.btn_matrices.setToolTip(_translate("Porticos", "Matrices de rigidez"))
        self.btn_delta_fuerza.setToolTip(_translate("Porticos", "Exportar a Excel"))
        self.btn_fuerzas.setToolTip(_translate("Porticos", "Fuerzas Internas"))
        self.btn_deformada.setToolTip(_translate("Porticos", "Deformada"))
        self.btn_nuevo.setToolTip(_translate("Porticos", "Nuevo"))
        self.btn_nuevo.setWhatsThis(_translate("Porticos", "Nuevo"))
        self.menuArchivo.setTitle(_translate("Porticos", "Archivo"))
        self.menuVista.setTitle(_translate("Porticos", "Vista"))
        self.menuHerramientas.setTitle(_translate("Porticos", "Herramientas"))
        self.menuAcerca_de.setTitle(_translate("Porticos", "Ayuda"))
        self.actionNuevo.setText(_translate("Porticos", "Nuevo"))
        self.actionAbrir.setText(_translate("Porticos", "Abrir"))
        self.actionGuardar.setText(_translate("Porticos", "Guardar"))
        self.actionSalir.setText(_translate("Porticos", "Salir"))
        self.actionTema_claro.setText(_translate("Porticos", "Tema claro"))
        self.actionTema_oscuro.setText(_translate("Porticos", "Tema oscuro"))
        self.actionConversor_de_unidades.setText(_translate("Porticos", "Convertidor de unidades"))
        self.actionInformacion.setText(_translate("Porticos", "Acerca de"))
        self.actionManual_de_uso.setText(_translate("Porticos", "Manual de uso"))

from UI_Matplotlib_PyQt5 import MatplotlibWidgetaLienzo
