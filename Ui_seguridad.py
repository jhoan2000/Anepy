# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'seguridadKDMguE.ui'
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

import Logo_seguridad_rc

class UI_Seguridad(object):
    def setupUi(self, Seguridad):
        if Seguridad.objectName():
            Seguridad.setObjectName(u"Seguridad")
        Seguridad.resize(300, 200)
        Seguridad.setMinimumSize(QSize(265, 178))
        icon = QIcon()
        icon.addFile(u":/Logo pass/logo_seguridad.png", QSize(), QIcon.Normal, QIcon.Off)
        Seguridad.setWindowIcon(icon)
        Seguridad.setIconSize(QSize(100, 100))
        self.centralwidget = QWidget(Seguridad)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setLayoutDirection(Qt.LeftToRight)
        self.frame.setStyleSheet(u"QFrame{\n"
"	/**background-color: rgb(18, 90, 140);**/\n"
"	background-color: rgb(172, 201, 255);\n"
"	border-radius:50px;\n"
"}\n"
"QDial::hover{\n"
"	background-color: qradialgradient(spread:reflect, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(114, 113, 119, 255), stop:0.806818 rgba(172, 201, 255, 255));\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setStyleSheet(u"QLabel{background-color:none;}")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(149, 174, 221);\n"
"border-radius:10px;}\n"
"QLabel{\n"
"	\n"
"	font: 75 16pt \"Segoe UI\";\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lb_d1 = QLabel(self.frame_2)
        self.lb_d1.setObjectName(u"lb_d1")
        self.lb_d1.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.lb_d1)

        self.lb_d2 = QLabel(self.frame_2)
        self.lb_d2.setObjectName(u"lb_d2")
        self.lb_d2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.lb_d2)

        self.lb_d3 = QLabel(self.frame_2)
        self.lb_d3.setObjectName(u"lb_d3")
        self.lb_d3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.lb_d3)

        self.lb_d4 = QLabel(self.frame_2)
        self.lb_d4.setObjectName(u"lb_d4")
        self.lb_d4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.lb_d4)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"background-color: none;\n"
"border:none;")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.dial_d1 = QDial(self.frame_3)
        self.dial_d1.setObjectName(u"dial_d1")
        self.dial_d1.setCursor(QCursor(Qt.PointingHandCursor))
        self.dial_d1.setMaximum(10)

        self.horizontalLayout_2.addWidget(self.dial_d1)

        self.dial_d2 = QDial(self.frame_3)
        self.dial_d2.setObjectName(u"dial_d2")
        self.dial_d2.setCursor(QCursor(Qt.PointingHandCursor))
        self.dial_d2.setMaximum(10)

        self.horizontalLayout_2.addWidget(self.dial_d2)

        self.dial_d3 = QDial(self.frame_3)
        self.dial_d3.setObjectName(u"dial_d3")
        self.dial_d3.setCursor(QCursor(Qt.PointingHandCursor))
        self.dial_d3.setMaximum(10)

        self.horizontalLayout_2.addWidget(self.dial_d3)

        self.dial_d4 = QDial(self.frame_3)
        self.dial_d4.setObjectName(u"dial_d4")
        self.dial_d4.setCursor(QCursor(Qt.PointingHandCursor))
        self.dial_d4.setMaximum(10)

        self.horizontalLayout_2.addWidget(self.dial_d4)


        self.verticalLayout_2.addWidget(self.frame_3)


        self.verticalLayout.addWidget(self.frame)

        Seguridad.setCentralWidget(self.centralwidget)

        self.retranslateUi(Seguridad)

        QMetaObject.connectSlotsByName(Seguridad)
    # setupUi

    def retranslateUi(self, Seguridad):
        Seguridad.setWindowTitle(QCoreApplication.translate("Seguridad", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("Seguridad", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:8px; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">C\u00d3DIGO DE SEGURIDAD</p></body></html>", None))
        self.lb_d1.setText(QCoreApplication.translate("Seguridad", u"0", None))
        self.lb_d2.setText(QCoreApplication.translate("Seguridad", u"0", None))
        self.lb_d3.setText(QCoreApplication.translate("Seguridad", u"0", None))
        self.lb_d4.setText(QCoreApplication.translate("Seguridad", u"0", None))
    # retranslateUi

