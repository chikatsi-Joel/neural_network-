# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(600, 493)
        self.container = QtWidgets.QWidget(Form)
        self.container.setGeometry(QtCore.QRect(20, 20, 561, 461))
        self.container.setBaseSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("ori1Uni")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.container.setFont(font)
        self.container.setStyleSheet("QPushButton {\n"
"    background-color: rgb(73, 168, 53);\n"
"    border-radius: 5px;\n"
"    color: rgb(194, 248, 189);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(143, 240, 164);\n"
"    border-radius: 5px;\n"
"}")
        self.container.setObjectName("container")
        self.atom = QtWidgets.QLabel(self.container)
        self.atom.setGeometry(QtCore.QRect(310, 70, 200, 300))
        self.atom.setStyleSheet("background-color: rgb(245, 245, 245);\n"
"border-radius: 10px;")
        self.atom.setText("")
        self.atom.setObjectName("atom")
        self.frame_log = QtWidgets.QWidget(self.container)
        self.frame_log.setGeometry(QtCore.QRect(0, -40, 311, 500))
        self.frame_log.setStyleSheet("background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(182, 255, 156, 130), stop:1 rgb(74, 179, 36, 150));\n"
"border-radius: 10px;")
        self.frame_log.setObjectName("frame_log")
        self.name_title = QtWidgets.QLabel(self.frame_log)
        self.name_title.setGeometry(QtCore.QRect(60, 110, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Sans")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.name_title.setFont(font)
        self.name_title.setStyleSheet("color: rgb(0, 85, 21)")
        self.name_title.setTextFormat(QtCore.Qt.MarkdownText)
        self.name_title.setScaledContents(True)
        self.name_title.setObjectName("name_title")
        self.nom_bas = QtWidgets.QLabel(self.frame_log)
        self.nom_bas.setGeometry(QtCore.QRect(10, 380, 251, 17))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.nom_bas.setFont(font)
        self.nom_bas.setStyleSheet("color: rgb(1, 133, 18);\n"
"background-color: transparent;")
        self.nom_bas.setObjectName("nom_bas")
        self.valider_connexion = QtWidgets.QPushButton(self.container)
        self.valider_connexion.setGeometry(QtCore.QRect(340, 300, 151, 30))
        font = QtGui.QFont()
        font.setFamily("ori1Uni")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.valider_connexion.setFont(font)
        self.valider_connexion.setStyleSheet("")
        self.valider_connexion.setObjectName("valider_connexion")
        self.label_2 = QtWidgets.QLabel(self.container)
        self.label_2.setGeometry(QtCore.QRect(330, 100, 161, 61))
        self.label_2.setBaseSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setFamily("Yrsa")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("QLabel {\n"
"    color: rgb(32, 134, 4);\n"
"    margin-left: 20px;\n"
"    height : 20px;\n"
"}")
        self.label_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_2.setLineWidth(2)
        self.label_2.setObjectName("label_2")
        self.toolButton = QtWidgets.QToolButton(self.container)
        self.toolButton.setGeometry(QtCore.QRect(460, 60, 31, 31))
        self.toolButton.setStyleSheet("border-radius: 15px;\n"
"background: transparent;")
        self.toolButton.setObjectName("toolButton")
        self.gridFrame = QtWidgets.QFrame(self.container)
        self.gridFrame.setGeometry(QtCore.QRect(320, 170, 171, 101))
        self.gridFrame.setStyleSheet("background-color: rgb(247, 255, 247);\n"
"padding: 5px;")
        self.gridFrame.setObjectName("gridFrame")
        self.gridLayout = QtWidgets.QGridLayout(self.gridFrame)
        self.gridLayout.setObjectName("gridLayout")
        self.name_label_2 = QtWidgets.QLabel(self.gridFrame)
        font = QtGui.QFont()
        font.setFamily("Suranna")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.name_label_2.setFont(font)
        self.name_label_2.setStyleSheet("color: green;")
        self.name_label_2.setObjectName("name_label_2")
        self.gridLayout.addWidget(self.name_label_2, 0, 0, 1, 1)
        self.email_edit = QtWidgets.QLineEdit(self.gridFrame)
        self.email_edit.setMaximumSize(QtCore.QSize(16777215, 30))
        self.email_edit.setStyleSheet("border-bottom: 2px solid greenyellow;\n"
"")
        self.email_edit.setObjectName("email_edit")
        self.gridLayout.addWidget(self.email_edit, 1, 1, 1, 1)
        self.name_edit = QtWidgets.QLineEdit(self.gridFrame)
        self.name_edit.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Yrsa")
        self.name_edit.setFont(font)
        self.name_edit.setStyleSheet("border-bottom: 2px solid greenyellow;\n"
"")
        self.name_edit.setObjectName("name_edit")
        self.gridLayout.addWidget(self.name_edit, 0, 1, 1, 1)
        self.email_label = QtWidgets.QLabel(self.gridFrame)
        font = QtGui.QFont()
        font.setFamily("Suranna")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.email_label.setFont(font)
        self.email_label.setStyleSheet("color: green;")
        self.email_label.setObjectName("email_label")
        self.gridLayout.addWidget(self.email_label, 1, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.name_title.setText(_translate("Form", "Processing Movie"))
        self.nom_bas.setText(_translate("Form", "Gradi Joel kappachikatsi@gmail.com"))
        self.valider_connexion.setText(_translate("Form", "se Connecter"))
        self.label_2.setText(_translate("Form", "LOGIN"))
        self.toolButton.setText(_translate("Form", "..."))
        self.name_label_2.setText(_translate("Form", "Name : "))
        self.email_edit.setPlaceholderText(_translate("Form", "email"))
        self.name_edit.setPlaceholderText(_translate("Form", "name"))
        self.email_label.setText(_translate("Form", "Email : "))
