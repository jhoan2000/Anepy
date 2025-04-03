# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'convertidor_unjbhlXZ.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_Convertidor(object):
    def setupUi(self, Convertidor):
        if not Convertidor.objectName():
            Convertidor.setObjectName(u"Convertidor")
        Convertidor.setEnabled(True)
        Convertidor.resize(400, 300)
        Convertidor.setMaximumSize(QSize(400, 300))
        icon = QIcon()
        icon.addFile(u"Logo.ico", QSize(), QIcon.Normal, QIcon.Off)
        Convertidor.setWindowIcon(icon)
        self.frame = QFrame(Convertidor)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, -1, 391, 101))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(0, 0, 391, 101))
        self.frame_2.setStyleSheet(u"background-color: rgb(0, 50, 23);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.cb_tipo = QComboBox(self.frame_2)
        self.cb_tipo.addItem("")
        self.cb_tipo.addItem("")
        self.cb_tipo.addItem("")
        self.cb_tipo.addItem("")
        self.cb_tipo.addItem("")
        self.cb_tipo.setObjectName(u"cb_tipo")
        self.cb_tipo.setGeometry(QRect(150, 50, 101, 21))
        font = QFont()
        font.setFamily(u"Times New Roman")
        font.setPointSize(14)
        self.cb_tipo.setFont(font)
        self.cb_tipo.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-radius :5px;")
        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(100, 20, 191, 21))
        font1 = QFont()
        font1.setFamily(u"Rockwell Extra Bold")
        font1.setBold(True)
        font1.setWeight(75)
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"font-size:18px;")
        self.frame_3 = QFrame(Convertidor)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(0, 100, 391, 101))
        self.frame_3.setStyleSheet(u"background-color: rgb(0, 72, 33);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.cb_convertir_de = QComboBox(self.frame_3)
        self.cb_convertir_de.setObjectName(u"cb_convertir_de")
        self.cb_convertir_de.setGeometry(QRect(20, 40, 111, 24))
        font2 = QFont()
        font2.setFamily(u"Times New Roman")
        font2.setPointSize(11)
        self.cb_convertir_de.setFont(font2)
        self.cb_convertir_de.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-radius :5px;")
        self.cb_convertir_a = QComboBox(self.frame_3)
        self.cb_convertir_a.setObjectName(u"cb_convertir_a")
        self.cb_convertir_a.setGeometry(QRect(260, 40, 111, 24))
        self.cb_convertir_a.setFont(font2)
        self.cb_convertir_a.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-radius :5px;")
        self.in_valor = QLineEdit(self.frame_3)
        self.in_valor.setObjectName(u"in_valor")
        self.in_valor.setGeometry(QRect(140, 70, 113, 20))
        self.in_valor.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font-size:12px;")
        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 10, 151, 21))
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"font-size:16px;")
        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(290, 10, 47, 13))
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"font-size:14px;")
        self.frame_4 = QFrame(Convertidor)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(0, 200, 391, 101))
        self.frame_4.setStyleSheet(u"background-color: rgb(0, 107, 48);")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.lb_resultado = QLabel(self.frame_4)
        self.lb_resultado.setObjectName(u"lb_resultado")
        self.lb_resultado.setGeometry(QRect(70, 10, 271, 21))
        self.lb_resultado.setFont(font1)
        self.lb_resultado.setCursor(QCursor(Qt.IBeamCursor))
        self.lb_resultado.setStyleSheet(u"font-size:16px;")
        self.bt_convertir = QPushButton(self.frame_4)
        self.bt_convertir.setObjectName(u"bt_convertir")
        self.bt_convertir.setGeometry(QRect(180, 40, 51, 51))
        self.bt_convertir.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_convertir.setStyleSheet(u"QPushButton{\n"
"border-radius :20px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 50, 23);\n"
"font: 75 12px \"MS Shell Dlg 2\";}\n"
"\n"
"/* Cambia color al estar sobre*/\n"
"QPushButton:hover{\n"
"	\n"
"	background-color:rgb(0, 180, 78);\n"
"}\n"
"/* Cambia color al dar click*/\n"
"QPushButton:pressed{\n"
"\n"
"	background-color: rgb(0, 72, 33);\n"
"\n"
"}\n"
"")

        self.retranslateUi(Convertidor)

        QMetaObject.connectSlotsByName(Convertidor)
    # setupUi

    def retranslateUi(self, Convertidor):
        Convertidor.setWindowTitle(QCoreApplication.translate("Convertidor", u"Convertidor de unidades", None))
        self.cb_tipo.setItemText(0, QCoreApplication.translate("Convertidor", u"\u00c1rea", None))
        self.cb_tipo.setItemText(1, QCoreApplication.translate("Convertidor", u"Longitud", None))
        self.cb_tipo.setItemText(2, QCoreApplication.translate("Convertidor", u"Fuerza", None))
        self.cb_tipo.setItemText(3, QCoreApplication.translate("Convertidor", u"Momento", None))
        self.cb_tipo.setItemText(4, QCoreApplication.translate("Convertidor", u"Presi\u00f3n", None))

        self.label_4.setText(QCoreApplication.translate("Convertidor", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; color:#ffffff;\">Conversi\u00f3n</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("Convertidor", u"<html><head/><body><p><span style=\" font-weight:400;\">Convierte de:</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("Convertidor", u"<html><head/><body><p><span style=\" font-weight:400;\">A:</span></p></body></html>", None))
        self.lb_resultado.setText(QCoreApplication.translate("Convertidor", u"<html><head/><body><p align=\"center\">Resultado</p></body></html>", None))
        self.bt_convertir.setText(QCoreApplication.translate("Convertidor", u"Convertir", None))
    # retranslateUi

