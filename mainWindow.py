# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(438, 363)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.cplexbutton = QtWidgets.QPushButton(self.centralwidget)
        self.cplexbutton.setObjectName("cplexbutton")
        self.verticalLayout.addWidget(self.cplexbutton)
        self.listbutton = QtWidgets.QPushButton(self.centralwidget)
        self.listbutton.setObjectName("listbutton")
        self.verticalLayout.addWidget(self.listbutton)
        self.exitbutton = QtWidgets.QPushButton(self.centralwidget)
        self.exitbutton.setObjectName("exitbutton")
        self.verticalLayout.addWidget(self.exitbutton)
        self.listbutton.raise_()
        self.exitbutton.raise_()
        self.cplexbutton.raise_()
        mainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(mainWindow)
        self.exitbutton.clicked.connect(mainWindow.close)
        self.listbutton.clicked.connect(mainWindow.showNormal)
        self.cplexbutton.clicked.connect(mainWindow.showNormal)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "MainWindow"))
        self.cplexbutton.setText(_translate("mainWindow", "CPLEX"))
        self.listbutton.setText(_translate("mainWindow", "LISTAR"))
        self.exitbutton.setText(_translate("mainWindow", "SAIR"))

