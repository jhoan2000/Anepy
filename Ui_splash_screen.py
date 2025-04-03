# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'splash_screenYpviDB.ui'
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

class Ui_SplashScreen(object):
    def setupUi(self, SplashScreen):
        if SplashScreen.objectName():
            SplashScreen.setObjectName(u"SplashScreen")
        SplashScreen.resize(377+55, 532) # (610, 377)
        icon = QIcon()
        icon.addFile(u":/logo/Logo.ico", QSize(), QIcon.Normal, QIcon.Off)
        SplashScreen.setWindowIcon(icon)
        self.centralwidget = QWidget(SplashScreen)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.dropShadowFrame = QFrame(self.centralwidget)
        self.dropShadowFrame.setObjectName(u"dropShadowFrame")
        self.dropShadowFrame.setStyleSheet(u"\n"
"	color: rgb(220, 220, 220);\n"
"	background-color: #046B99;\n"
"	border-radius: 10px;\n"
"	background-repeat: no-repeat;\n"
"")
        self.dropShadowFrame.setFrameShape(QFrame.StyledPanel)
        self.dropShadowFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.dropShadowFrame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_logo = QLabel(self.dropShadowFrame)
        self.label_logo.setObjectName(u"label_logo")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_logo.sizePolicy().hasHeightForWidth())
        self.label_logo.setSizePolicy(sizePolicy)
        self.label_logo.setBaseSize(QSize(0, 0))
        font = QFont()
        font.setPointSize(5)
        self.label_logo.setFont(font)
        self.label_logo.setStyleSheet(u"")
        self.label_logo.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_logo)

        self.frame_3 = QFrame(self.dropShadowFrame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"background-repeat: no-repeat,no-repeat ;")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(self.frame_3)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background: none;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_titulo = QLabel(self.frame)
        self.label_titulo.setObjectName(u"label_titulo")
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(40)
        self.label_titulo.setFont(font1)
        self.label_titulo.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: none;")
        self.label_titulo.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_titulo)

        self.label_descripcion = QLabel(self.frame)
        self.label_descripcion.setObjectName(u"label_descripcion")
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(14)
        self.label_descripcion.setFont(font2)
        self.label_descripcion.setStyleSheet(u"color: rgb(200, 200, 200);\n"
"background-color: none;\n"
"")
        self.label_descripcion.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_descripcion)


        self.verticalLayout_2.addWidget(self.frame)

        self.frame_2 = QFrame(self.frame_3)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-color:none;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.progressBar = QProgressBar(self.frame_2)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setStyleSheet(u"QProgressBar{\n"
"	\n"
"	\n"
"	\n"
"	\n"
"	background-color: rgb(62, 62, 58);\n"
"	color: rgb(200, 200, 200);\n"
"	border-style:none;\n"
"	border-radius:10px;\n"
"	text-align:center;\n"
"}\n"
"QProgressBar::chunk{\n"
"	border-radius:10px;\n"
"	\n"
"	\n"
"	/**background-color: qlineargradient(spread:pad, x1:0, y1:0.523, x2:1, y2:0.528, stop:0.0113636 rgba(27, 150, 226, 255), stop:1 rgba(52, 208, 104, 255));**/\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.523, x2:1, y2:0.528, stop:0.0113636 rgba(27, 150, 226, 255), stop:1 rgba(27, 27, 26, 255));\n"
"}\n"
"")
        self.progressBar.setValue(70)

        self.verticalLayout_4.addWidget(self.progressBar)

        self.label_loading = QLabel(self.frame_2)
        self.label_loading.setObjectName(u"label_loading")
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(12)
        self.label_loading.setFont(font3)
        self.label_loading.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_loading.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_loading)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.label_creditos = QLabel(self.frame_3)
        self.label_creditos.setObjectName(u"label_creditos")
        font4 = QFont()
        font4.setFamily(u"Segoe UI")
        font4.setPointSize(10)
        self.label_creditos.setFont(font4)
        self.label_creditos.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_creditos.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.label_creditos)


        self.verticalLayout_5.addWidget(self.frame_3)


        self.verticalLayout.addWidget(self.dropShadowFrame)

        SplashScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SplashScreen)

        QMetaObject.connectSlotsByName(SplashScreen)
    # setupUi

    def retranslateUi(self, SplashScreen):
        SplashScreen.setWindowTitle(QCoreApplication.translate("SplashScreen", u"MainWindow", None))
        self.label_logo.setText(QCoreApplication.translate("SplashScreen", u"<html><head/><body><p><img src=\":/logo/Logo.ico\"/></p></body></html>", None))
        self.label_titulo.setText(QCoreApplication.translate("SplashScreen", u"<strong>ANEPY</strong> APP", None))
        self.label_descripcion.setText(QCoreApplication.translate("SplashScreen", u"<strong>APP</strong> DESCRIPTION", None))
        self.label_loading.setText(QCoreApplication.translate("SplashScreen", u"<html><head/><body><p>loading...</p></body></html>", None))
        self.label_creditos.setText(QCoreApplication.translate("SplashScreen", u"<html><head/><body><p><span style=\" font-weight:600;\">Creado por:</span> J&amp;Y</p></body></html>", None))
    # retranslateUi

