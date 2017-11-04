# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'trampo.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1003, 592)
        self.cplex = QtWidgets.QPushButton(Dialog)
        self.cplex.setGeometry(QtCore.QRect(270, 140, 441, 91))
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif")
        font.setPointSize(30)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.cplex.setFont(font)
        self.cplex.setIconSize(QtCore.QSize(20, 20))
        self.cplex.setObjectName("cplex")
        self.listar = QtWidgets.QPushButton(Dialog)
        self.listar.setGeometry(QtCore.QRect(270, 300, 441, 101))
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.listar.setFont(font)
        self.listar.setObjectName("listar")
        self.exit = QtWidgets.QPushButton(Dialog)
        self.exit.setGeometry(QtCore.QRect(772, 520, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.exit.setFont(font)
        self.exit.setObjectName("exit")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.cplex.setText(_translate("Dialog", "CPLEX"))
        self.listar.setText(_translate("Dialog", "Listar"))
        self.exit.setText(_translate("Dialog", "Exit"))

