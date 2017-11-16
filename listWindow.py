# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'listWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_listWindow(object):
    def setupUi(self, listWindow):
        listWindow.setObjectName("listWindow")
        listWindow.resize(532, 335)
        self.layoutWidget = QtWidgets.QWidget(listWindow)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 511, 242))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.splitter = QtWidgets.QSplitter(self.layoutWidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.layoutWidget_4 = QtWidgets.QWidget(self.splitter)
        self.layoutWidget_4.setObjectName("layoutWidget_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget_4)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.listSolutions = QtWidgets.QListWidget(self.layoutWidget_4)
        self.listSolutions.setObjectName("listSolutions")
        self.verticalLayout_3.addWidget(self.listSolutions)
        self.verticalLayout_4.addWidget(self.splitter)
        self.horizontalLayoutWidget = QtWidgets.QWidget(listWindow)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(350, 250, 171, 91))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.buttonExit = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.buttonExit.setObjectName("buttonExit")
        self.horizontalLayout.addWidget(self.buttonExit)
        self.buttonOpenSolution = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.buttonOpenSolution.setObjectName("buttonOpenSolution")
        self.horizontalLayout.addWidget(self.buttonOpenSolution)

        self.retranslateUi(listWindow)
        QtCore.QMetaObject.connectSlotsByName(listWindow)

    def retranslateUi(self, listWindow):
        _translate = QtCore.QCoreApplication.translate
        listWindow.setWindowTitle(_translate("listWindow", "Lista de Soluções"))
        self.label.setText(_translate("listWindow", "Lista de Soluções"))
        self.buttonExit.setText(_translate("listWindow", "Cancelar"))
        self.buttonOpenSolution.setText(_translate("listWindow", "Visualizar"))

