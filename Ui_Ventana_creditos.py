# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'acerca_de.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Creditos(object):
    def setupUi(self, Creditos):
        Creditos.setObjectName("Creditos")
        Creditos.resize(521, 610)
        Creditos.setMinimumSize(QtCore.QSize(521, 610))
        Creditos.setMaximumSize(QtCore.QSize(521, 610))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Logo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Creditos.setWindowIcon(icon)
        Creditos.setWindowOpacity(0.9)
        self.layoutWidget = QtWidgets.QWidget(Creditos)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 30, 491, 351))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.label_9 = QtWidgets.QLabel(self.layoutWidget)
        self.label_9.setObjectName("label_9")
        self.verticalLayout.addWidget(self.label_9)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.label_8)
        self.label_8.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_6.raise_()
        self.label_5.raise_()
        self.label_7.raise_()
        self.label_9.raise_()
        self.label_10 = QtWidgets.QLabel(Creditos)
        self.label_10.setGeometry(QtCore.QRect(10, 410, 541, 91))
        self.label_10.setObjectName("label_10")
        self.pushButton = QtWidgets.QPushButton(Creditos)
        self.pushButton.setGeometry(QtCore.QRect(250, 550, 75, 23))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("QPushButton{\n"
"/* Color de fondo*/\n"
"background-color:  rgb(186, 186, 186);\n"
"\n"
"font: 75 12pt \"Arial\";\n"
"border-radius : 5px;\n"
"border : 2px solid  rgb(240, 240, 240);\n"
"\n"
"}\n"
"\n"
"/* Cambia color al estar sobre*/\n"
"QPushButton:hover{\n"
"\n"
"background-color:rgb(120, 165, 164);\n"
"border : 2px solid  rgb(0, 0, 0);\n"
"\n"
"}\n"
"/* Cambia color al dar click*/\n"
"QPushButton:pressed{\n"
"\n"
"background-color:rgb(173, 238, 236);\n"
"border : 2px solid  rgb(0, 179, 179);\n"
"\n"
"}\n"
"\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.layoutWidget.raise_()
        self.pushButton.raise_()
        self.label_10.raise_()

        self.retranslateUi(Creditos)
        QtCore.QMetaObject.connectSlotsByName(Creditos)

    def retranslateUi(self, Creditos):
        _translate = QtCore.QCoreApplication.translate
        Creditos.setWindowTitle(_translate("Creditos", "Créditos"))
        self.label.setText(_translate("Creditos", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">ANEPY- Sofware de Análisis Estructural Basado en Python</span></p></body></html>"))
        self.label_2.setText(_translate("Creditos", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Softwarwe de Educación</span></p></body></html>"))
        self.label_3.setText(_translate("Creditos", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Versión 1.4</span></p></body></html>"))
        self.label_4.setText(_translate("Creditos", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600; color:#000000;\">Universidad Tecnológica del Chocó Diego Luis Córdoba</span></p></body></html>"))
        self.label_6.setText(_translate("Creditos", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#000000;\">Programa Ingenieria Civíl</span></p></body></html>"))
        self.label_5.setText(_translate("Creditos", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Facultad de Ingeniería</span></p></body></html>"))
        self.label_7.setText(_translate("Creditos", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Creado como opción de grado por: </span></p><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Yhoan Smith Mosquera Peñaloza</span></p></body></html>"))
        self.label_9.setText(_translate("Creditos", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Juliana Andrea Gonzalez Romaña</span></p></body></html>"))
        self.label_8.setText(_translate("Creditos", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Año 2022</span></p></body></html>"))
        self.label_10.setText(_translate("Creditos", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">ANEPY es un software de uso estudiantil o académico, los creadores no se hacen responsables </p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> de su uso a nivel profesional, y tampoco a la interpretación que el usuario le dé a los resultados </p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">arrojados por el software.</p></body></html>"))
        self.pushButton.setText(_translate("Creditos", "Volver"))

