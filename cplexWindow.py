# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cplexWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_cplexWindow(object):
    def setupUi(self, cplexWindow):
        cplexWindow.setObjectName("cplexWindow")
        cplexWindow.resize(678, 399)
        self.centralwidget = QtWidgets.QWidget(cplexWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(480, 360, 168, 27))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.runLabel = QtWidgets.QPushButton(self.layoutWidget)
        self.runLabel.setObjectName("runLabel")
        self.horizontalLayout_10.addWidget(self.runLabel, 0, QtCore.Qt.AlignRight)
        self.cancelLabel = QtWidgets.QPushButton(self.layoutWidget)
        self.cancelLabel.setObjectName("cancelLabel")
        self.horizontalLayout_10.addWidget(self.cancelLabel)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 0, 651, 341))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.statelabel = QtWidgets.QLabel(self.layoutWidget1)
        self.statelabel.setObjectName("statelabel")
        self.horizontalLayout.addWidget(self.statelabel)
        self.stateInput = QtWidgets.QComboBox(self.layoutWidget1)
        self.stateInput.setObjectName("stateInput")
        self.horizontalLayout.addWidget(self.stateInput)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.fixed_cost1 = QtWidgets.QLabel(self.layoutWidget1)
        self.fixed_cost1.setObjectName("fixed_cost1")
        self.horizontalLayout_2.addWidget(self.fixed_cost1)
        self.label_10 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_10.setMaximumSize(QtCore.QSize(50, 30))
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_2.addWidget(self.label_10)
        self.fixed_cost1_lb = QtWidgets.QLineEdit(self.layoutWidget1)
        self.fixed_cost1_lb.setMaximumSize(QtCore.QSize(206, 29))
        self.fixed_cost1_lb.setObjectName("fixed_cost1_lb")
        self.horizontalLayout_2.addWidget(self.fixed_cost1_lb)
        self.label_11 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_11.setMaximumSize(QtCore.QSize(30, 30))
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_2.addWidget(self.label_11)
        self.fixed_cost1_ub = QtWidgets.QLineEdit(self.layoutWidget1)
        self.fixed_cost1_ub.setMaximumSize(QtCore.QSize(206, 29))
        self.fixed_cost1_ub.setObjectName("fixed_cost1_ub")
        self.horizontalLayout_2.addWidget(self.fixed_cost1_ub)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.fixed_cost2 = QtWidgets.QLabel(self.layoutWidget1)
        self.fixed_cost2.setObjectName("fixed_cost2")
        self.horizontalLayout_3.addWidget(self.fixed_cost2)
        self.label_12 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_12.setMaximumSize(QtCore.QSize(50, 30))
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_3.addWidget(self.label_12)
        self.fixed_cost2_lb = QtWidgets.QLineEdit(self.layoutWidget1)
        self.fixed_cost2_lb.setMaximumSize(QtCore.QSize(206, 29))
        self.fixed_cost2_lb.setObjectName("fixed_cost2_lb")
        self.horizontalLayout_3.addWidget(self.fixed_cost2_lb)
        self.label_13 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_13.setMaximumSize(QtCore.QSize(30, 30))
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_3.addWidget(self.label_13)
        self.fixed_cost2_ub = QtWidgets.QLineEdit(self.layoutWidget1)
        self.fixed_cost2_ub.setMaximumSize(QtCore.QSize(206, 29))
        self.fixed_cost2_ub.setObjectName("fixed_cost2_ub")
        self.horizontalLayout_3.addWidget(self.fixed_cost2_ub)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.capacity1 = QtWidgets.QLabel(self.layoutWidget1)
        self.capacity1.setObjectName("capacity1")
        self.horizontalLayout_4.addWidget(self.capacity1)
        self.label_14 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_14.setMaximumSize(QtCore.QSize(50, 30))
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_4.addWidget(self.label_14)
        self.capacity1_lb = QtWidgets.QLineEdit(self.layoutWidget1)
        self.capacity1_lb.setMaximumSize(QtCore.QSize(206, 29))
        self.capacity1_lb.setObjectName("capacity1_lb")
        self.horizontalLayout_4.addWidget(self.capacity1_lb)
        self.label_15 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_15.setMaximumSize(QtCore.QSize(30, 30))
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_4.addWidget(self.label_15)
        self.capacity1_ub = QtWidgets.QLineEdit(self.layoutWidget1)
        self.capacity1_ub.setMaximumSize(QtCore.QSize(206, 29))
        self.capacity1_ub.setObjectName("capacity1_ub")
        self.horizontalLayout_4.addWidget(self.capacity1_ub)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.capacity2 = QtWidgets.QLabel(self.layoutWidget1)
        self.capacity2.setObjectName("capacity2")
        self.horizontalLayout_5.addWidget(self.capacity2)
        self.label_16 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_16.setMaximumSize(QtCore.QSize(50, 30))
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_5.addWidget(self.label_16)
        self.capacity2_lb = QtWidgets.QLineEdit(self.layoutWidget1)
        self.capacity2_lb.setMaximumSize(QtCore.QSize(206, 29))
        self.capacity2_lb.setObjectName("capacity2_lb")
        self.horizontalLayout_5.addWidget(self.capacity2_lb)
        self.label_17 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_17.setMaximumSize(QtCore.QSize(30, 30))
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_5.addWidget(self.label_17)
        self.capacity2_ub = QtWidgets.QLineEdit(self.layoutWidget1)
        self.capacity2_ub.setMaximumSize(QtCore.QSize(206, 29))
        self.capacity2_ub.setObjectName("capacity2_ub")
        self.horizontalLayout_5.addWidget(self.capacity2_ub)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.demand = QtWidgets.QLabel(self.layoutWidget1)
        self.demand.setObjectName("demand")
        self.horizontalLayout_6.addWidget(self.demand)
        self.label_18 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_18.setMaximumSize(QtCore.QSize(50, 30))
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_6.addWidget(self.label_18)
        self.demand_lb = QtWidgets.QLineEdit(self.layoutWidget1)
        self.demand_lb.setMaximumSize(QtCore.QSize(206, 29))
        self.demand_lb.setObjectName("demand_lb")
        self.horizontalLayout_6.addWidget(self.demand_lb)
        self.label_19 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_19.setMaximumSize(QtCore.QSize(30, 30))
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_6.addWidget(self.label_19)
        self.demand_ub = QtWidgets.QLineEdit(self.layoutWidget1)
        self.demand_ub.setMaximumSize(QtCore.QSize(206, 29))
        self.demand_ub.setObjectName("demand_ub")
        self.horizontalLayout_6.addWidget(self.demand_ub)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.numbernode1 = QtWidgets.QLabel(self.layoutWidget1)
        self.numbernode1.setObjectName("numbernode1")
        self.horizontalLayout_8.addWidget(self.numbernode1)
        self.label_22 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_22.setMaximumSize(QtCore.QSize(50, 30))
        self.label_22.setObjectName("label_22")
        self.horizontalLayout_8.addWidget(self.label_22)
        self.numbernode1_lb = QtWidgets.QLineEdit(self.layoutWidget1)
        self.numbernode1_lb.setMaximumSize(QtCore.QSize(206, 29))
        self.numbernode1_lb.setObjectName("numbernode1_lb")
        self.horizontalLayout_8.addWidget(self.numbernode1_lb)
        self.label_23 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_23.setMaximumSize(QtCore.QSize(30, 30))
        self.label_23.setObjectName("label_23")
        self.horizontalLayout_8.addWidget(self.label_23)
        self.numbernode1_ub = QtWidgets.QLineEdit(self.layoutWidget1)
        self.numbernode1_ub.setMaximumSize(QtCore.QSize(206, 29))
        self.numbernode1_ub.setObjectName("numbernode1_ub")
        self.horizontalLayout_8.addWidget(self.numbernode1_ub)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.numbernode2 = QtWidgets.QLabel(self.layoutWidget1)
        self.numbernode2.setObjectName("numbernode2")
        self.horizontalLayout_9.addWidget(self.numbernode2)
        self.label_24 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_24.setMaximumSize(QtCore.QSize(50, 30))
        self.label_24.setObjectName("label_24")
        self.horizontalLayout_9.addWidget(self.label_24)
        self.numbernode2_lb = QtWidgets.QLineEdit(self.layoutWidget1)
        self.numbernode2_lb.setMaximumSize(QtCore.QSize(206, 29))
        self.numbernode2_lb.setObjectName("numbernode2_lb")
        self.horizontalLayout_9.addWidget(self.numbernode2_lb)
        self.label_25 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_25.setMaximumSize(QtCore.QSize(30, 30))
        self.label_25.setObjectName("label_25")
        self.horizontalLayout_9.addWidget(self.label_25)
        self.numbernode2_ub = QtWidgets.QLineEdit(self.layoutWidget1)
        self.numbernode2_ub.setMaximumSize(QtCore.QSize(206, 29))
        self.numbernode2_ub.setObjectName("numbernode2_ub")
        self.horizontalLayout_9.addWidget(self.numbernode2_ub)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.prodcutsclient = QtWidgets.QLabel(self.layoutWidget1)
        self.prodcutsclient.setObjectName("prodcutsclient")
        self.horizontalLayout_7.addWidget(self.prodcutsclient)
        self.productsclient_ub = QtWidgets.QLineEdit(self.layoutWidget1)
        self.productsclient_ub.setMaximumSize(QtCore.QSize(206, 29))
        self.productsclient_ub.setObjectName("productsclient_ub")
        self.horizontalLayout_7.addWidget(self.productsclient_ub)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        cplexWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(cplexWindow)
        QtCore.QMetaObject.connectSlotsByName(cplexWindow)

    def retranslateUi(self, cplexWindow):
        _translate = QtCore.QCoreApplication.translate
        cplexWindow.setWindowTitle(_translate("cplexWindow", "MainWindow"))
        self.runLabel.setText(_translate("cplexWindow", "RUN"))
        self.cancelLabel.setText(_translate("cplexWindow", "CANCEL"))
        self.statelabel.setText(_translate("cplexWindow", "Estado:"))
        self.fixed_cost1.setText(_translate("cplexWindow", "Custo Fixo L1:"))
        self.label_10.setText(_translate("cplexWindow", "de"))
        self.label_11.setText(_translate("cplexWindow", "a:"))
        self.fixed_cost2.setText(_translate("cplexWindow", "Custo Fixo L2:"))
        self.label_12.setText(_translate("cplexWindow", "de"))
        self.label_13.setText(_translate("cplexWindow", "a:"))
        self.capacity1.setText(_translate("cplexWindow", "Capacidade N1:"))
        self.label_14.setText(_translate("cplexWindow", "de"))
        self.label_15.setText(_translate("cplexWindow", "a:"))
        self.capacity2.setText(_translate("cplexWindow", "Capacidade N2:"))
        self.label_16.setText(_translate("cplexWindow", "de"))
        self.label_17.setText(_translate("cplexWindow", "a:"))
        self.demand.setText(_translate("cplexWindow", "Demanda:"))
        self.label_18.setText(_translate("cplexWindow", "de"))
        self.label_19.setText(_translate("cplexWindow", "a:"))
        self.numbernode1.setText(_translate("cplexWindow", "# de nós L1:"))
        self.label_22.setText(_translate("cplexWindow", "de"))
        self.label_23.setText(_translate("cplexWindow", "a:"))
        self.numbernode2.setText(_translate("cplexWindow", "# de nós L2:"))
        self.label_24.setText(_translate("cplexWindow", "de"))
        self.label_25.setText(_translate("cplexWindow", "a:"))
        self.prodcutsclient.setText(_translate("cplexWindow", "# de produtos p/ cliente:"))

