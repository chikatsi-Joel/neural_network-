# Form implementation generated from reading ui file '/home/chikatsi/Bureau/INFOL3/2nd_semester/DataSCience S2/interface.py/barre.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(608, 502)
        self.frame = QtWidgets.QFrame(parent=Form)
        self.frame.setGeometry(QtCore.QRect(0, 0, 611, 41))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.toolButton = QtWidgets.QToolButton(parent=self.frame)
        self.toolButton.setGeometry(QtCore.QRect(570, 0, 41, 41))
        self.toolButton.setStyleSheet("QToolButton{\n"
"    border: none;\n"
"    background: transparent;\n"
"}\n"
"\n"
"QToolButton:hover{\n"
"    background-color: rgba(218, 0, 0, 0.8);\n"
"}\n"
"\n"
"QToolButton:pressed{\n"
"    background-color: ;\n"
"    background-color: rgba(167, 0, 0, 0.8);\n"
"}")
        self.toolButton.setObjectName("toolButton")
        self.toolButton_2 = QtWidgets.QToolButton(parent=self.frame)
        self.toolButton_2.setGeometry(QtCore.QRect(530, 0, 41, 41))
        self.toolButton_2.setStyleSheet("QToolButton{\n"
"    border: none;\n"
"    background: transparent;\n"
"}\n"
"\n"
"QToolButton:hover{\n"
"    background-color: rgba(10, 10, 10, 0.6);\n"
"}")
        self.toolButton_2.setObjectName("toolButton_2")
        self.toolButton_3 = QtWidgets.QToolButton(parent=self.frame)
        self.toolButton_3.setGeometry(QtCore.QRect(490, 0, 41, 41))
        self.toolButton_3.setStyleSheet("QToolButton{\n"
"    border: none;\n"
"    background: transparent;\n"
"}\n"
"\n"
"QToolButton:hover{\n"
"    background-color: rgba(10, 10, 10, 0.6);\n"
"}")
        self.toolButton_3.setObjectName("toolButton_3")
        self.toolButton_4 = QtWidgets.QToolButton(parent=self.frame)
        self.toolButton_4.setGeometry(QtCore.QRect(380, 0, 41, 41))
        self.toolButton_4.setStyleSheet("QToolButton{\n"
"    background: transparent;\n"
"    border-radius: 20px;\n"
"}\n"
"")
        self.toolButton_4.setObjectName("toolButton_4")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.toolButton.setText(_translate("Form", "..."))
        self.toolButton_2.setText(_translate("Form", "..."))
        self.toolButton_3.setText(_translate("Form", "..."))
        self.toolButton_4.setText(_translate("Form", "..."))