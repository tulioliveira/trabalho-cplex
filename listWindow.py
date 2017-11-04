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
        listWindow.resize(828, 335)
        self.buttonBox = QtWidgets.QDialogButtonBox(listWindow)
        self.buttonBox.setGeometry(QtCore.QRect(430, 280, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.layoutWidget = QtWidgets.QWidget(listWindow)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 10, 776, 242))
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
        self.layoutWidget_2 = QtWidgets.QWidget(self.splitter)
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.listWidget = QtWidgets.QListWidget(self.layoutWidget_2)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.layoutWidget_3 = QtWidgets.QWidget(self.splitter)
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.listWidget_2 = QtWidgets.QListWidget(self.layoutWidget_3)
        self.listWidget_2.setObjectName("listWidget_2")
        self.verticalLayout_2.addWidget(self.listWidget_2)
        self.layoutWidget_4 = QtWidgets.QWidget(self.splitter)
        self.layoutWidget_4.setObjectName("layoutWidget_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget_4)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget_4)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.listWidget_3 = QtWidgets.QListWidget(self.layoutWidget_4)
        self.listWidget_3.setObjectName("listWidget_3")
        self.verticalLayout_3.addWidget(self.listWidget_3)
        self.verticalLayout_4.addWidget(self.splitter)

        self.retranslateUi(listWindow)
        self.buttonBox.accepted.connect(listWindow.accept)
        self.buttonBox.rejected.connect(listWindow.reject)
        QtCore.QMetaObject.connectSlotsByName(listWindow)

    def retranslateUi(self, listWindow):
        _translate = QtCore.QCoreApplication.translate
        listWindow.setWindowTitle(_translate("listWindow", "Dialog"))
        self.label.setText(_translate("listWindow", "Lista de Soluções"))
        self.label_2.setText(_translate("listWindow", "Data"))
        self.label_4.setText(_translate("listWindow", "Custo"))
        self.label_3.setText(_translate("listWindow", "Estado"))

