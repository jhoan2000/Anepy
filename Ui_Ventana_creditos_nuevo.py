# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CreditosBgdUHO.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt, QTimer)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5.QtWidgets import *

import Logo_rc
import Logo_credits_rc

class Ui_Creditos(object):
    def setupUi(self, Ui_Ventana_creditos):
        if Ui_Ventana_creditos.objectName():
            Ui_Ventana_creditos.setObjectName(u"Ui_Ventana_creditos")
        Ui_Ventana_creditos.resize(418, 622)
        Ui_Ventana_creditos.setMinimumSize(QSize(418, 620))
        Ui_Ventana_creditos.setMaximumSize(QSize(418, 622))
        icon = QIcon()
        icon.addFile(u":/logo/Logo.ico", QSize(), QIcon.Normal, QIcon.Off)
        Ui_Ventana_creditos.setWindowIcon(icon)
        self.actionsalir = QAction(Ui_Ventana_creditos)
        self.actionsalir.setObjectName(u"actionsalir")
        self.actionsalir.setIcon(icon)
        self.centralwidget = QWidget(Ui_Ventana_creditos)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(9)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(9, 9, 9, 2)
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setEnabled(True)
        self.frame_2.setMinimumSize(QSize(400, 400))
        self.frame_2.setStyleSheet(u"QFrame{border-radius: 16px;\n"
"	background-color: rgb(10, 17, 27);\n"
"}\n"
"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label_header = QLabel(self.frame_2)
        self.label_header.setObjectName(u"label_header")
        self.label_header.setGeometry(QRect(0, -1, 400, 145))
        self.label_header.setMinimumSize(QSize(350, 0))
        self.label_header.setStyleSheet(u"QLabel{background-color:#1D88AA;\n"
"border-top-right-radius: 16px;\n"
"border-top-left-radius: 16px;\n"
"border-bottom-right-radius: 0px;\n"
"border-bottom-left-radius: 0px;\n"
"border: none;}\n"
"\n"
"")
        self.label_12 = QLabel(self.frame_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(0, 224, 400, 54))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(10)
        self.label_12.setFont(font)
        self.label_13 = QLabel(self.frame_2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(1, 483, 400, 32))
        self.label_13.setMinimumSize(QSize(400, 0))
        self.label_13.setAlignment(Qt.AlignCenter)
        self.label_14 = QLabel(self.frame_2)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(2, 288, 400, 32))
        self.label_14.setMinimumSize(QSize(400, 0))
        self.label_14.setAlignment(Qt.AlignCenter)
        self.label_15 = QLabel(self.frame_2)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(-1, 344, 400, 32))
        self.label_15.setMinimumSize(QSize(400, 0))
        self.label_16 = QLabel(self.frame_2)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(-1, 372, 400, 32))
        self.label_16.setMinimumSize(QSize(400, 0))
        self.label_17 = QLabel(self.frame_2)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(-3, 263, 400, 32))
        self.label_17.setMinimumSize(QSize(400, 0))
        self.label_17.setAlignment(Qt.AlignCenter)
        self.label_18 = QLabel(self.frame_2)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(2, 314, 400, 33))
        self.label_18.setMinimumSize(QSize(400, 0))
        self.label_18.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.label_19 = QLabel(self.frame_2)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(-1, 406, 400, 44))
        self.label_19.setMinimumSize(QSize(400, 0))
        self.label_20 = QLabel(self.frame_2)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(1, 453, 400, 32))
        self.label_20.setMinimumSize(QSize(400, 0))
        self.label_21 = QLabel(self.frame_2)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(0, 505, 400, 101))
        self.label_21.setMinimumSize(QSize(400, 0))
        self.label_21.setStyleSheet(u"background-color: none;")
        self.btn_salir = QPushButton(self.frame_2)
        self.btn_salir.setObjectName(u"btn_salir")
        self.btn_salir.setGeometry(QRect(101, 11, 209, 211))
        self.btn_salir.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_salir.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(176, 253, 250);\n"
"	border-radius: 100px;\n"
"	border: 5px solid;\n"
"	border-color: rgb(27, 143, 220);\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.523, x2:1, y2:0.528, stop:0.0113636 rgba(27, 150, 226, 255), stop:1 rgba(52, 208, 104, 255));\n"
"	\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.523, x2:1, y2:0.528, stop:0.0113636 rgba(52, 208, 104, 255) , stop:1  rgba(27, 150, 226, 255) );\n"
"	\n"
"\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/Logo_credits/Logo_credits.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_salir.setIcon(icon1)
        self.btn_salir.setIconSize(QSize(200, 200))
        self.btn_salir.setAutoDefault(False)

        self.verticalLayout.addWidget(self.frame_2)

        Ui_Ventana_creditos.setCentralWidget(self.centralwidget)

        self.retranslateUi(Ui_Ventana_creditos)

        QMetaObject.connectSlotsByName(Ui_Ventana_creditos)
    # setupUi

    def retranslateUi(self, Ui_Ventana_creditos):
        Ui_Ventana_creditos.setWindowTitle(QCoreApplication.translate("Ui_Ventana_creditos", u"MainWindow", None))
        self.actionsalir.setText(QCoreApplication.translate("Ui_Ventana_creditos", u"salir", None))
#if QT_CONFIG(shortcut)
        self.actionsalir.setShortcut(QCoreApplication.translate("Ui_Ventana_creditos", u"Ctrl+Q", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.frame_2.setToolTip(QCoreApplication.translate("Ui_Ventana_creditos", u"Cerrar", None))
#endif // QT_CONFIG(tooltip)
        self.label_header.setText("")
        self.label_12.setText(QCoreApplication.translate("Ui_Ventana_creditos", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600;\">ANEPY- Sofware de An\u00e1lisis Estructural Porticos 2D</span></p></body></html>", None))
        self.label_13.setText(QCoreApplication.translate("Ui_Ventana_creditos", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">A\u00f1o 2022</span></p></body></html>", None))
        self.label_14.setText(QCoreApplication.translate("Ui_Ventana_creditos", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Versi\u00f3n 1.0</span></p></body></html>", None))
        self.label_15.setText(QCoreApplication.translate("Ui_Ventana_creditos", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; \">Programa: Ingenieria Civ\u00edl</span></p></body></html>", None))
        self.label_16.setText(QCoreApplication.translate("Ui_Ventana_creditos", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Facultad de Ingenier\u00eda</span></p></body></html>", None))
        self.label_17.setText(QCoreApplication.translate("Ui_Ventana_creditos", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Softwarwe de Educaci\u00f3n</span></p></body></html>", None))
        self.label_18.setText(QCoreApplication.translate("Ui_Ventana_creditos", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">Universidad Tecnol\u00f3gica del Choc\u00f3 Diego Luis C\u00f3rdoba</span></p></body></html>", None))
        self.label_19.setText(QCoreApplication.translate("Ui_Ventana_creditos", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Creado como opci\u00f3n de grado por: </span></p><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Yhoan Smith Mosquera Pe\u00f1aloza</span></p></body></html>", None))
        self.label_20.setText(QCoreApplication.translate("Ui_Ventana_creditos", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Juliana Andrea Gonzalez Roma\u00f1a</span></p></body></html>", None))
        self.label_21.setText(QCoreApplication.translate("Ui_Ventana_creditos", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">ANEPY es un software de uso estudiantil o acad\u00e9mico, los creadores no se hacen</p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> responsables de su uso a nivel profesional, y tampoco a la</p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> interpretaci\u00f3n que el usuario le d\u00e9 a los resultados </p>\n"
"<p align=\"center\" style=\" ma"
                        "rgin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">arrojados por el software.</p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.btn_salir.setToolTip(QCoreApplication.translate("Ui_Ventana_creditos", u"Cerrar(Ctrl+Q)", None))
#endif // QT_CONFIG(tooltip)
        self.btn_salir.setText("")
    # retranslateUi

