#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import db
from PyQt5.QtWidgets import (QWidget, QToolTip, QPushButton, QApplication, QMainWindow, QDialog, QMessageBox)
from PyQt5.QtGui import *	
from PyQt5.QtWebEngine import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import *
from ex import *
from cplexWindow import *
from listWindow import *	 
from solutionWindow import *	 
from mainWindow import *

if __name__ == '__main__':
	app = QApplication(sys.argv) 
	newWindow = mainWindow()
	newWindow.show()
	sys.exit(app.exec_())

class mainWindow(QMainWindow, Ui_mainWindow):
	def __init__(self,parent=None):
		super(mainWindow,self).__init__(parent)
		self.setWindowTitle("Minha primeira U.I.")
		self.setupUi(self)
		self.cplexbutton.clicked.connect(self.cplexPressed)
		self.exitbutton.clicked.connect(self.exitPressed)
		self.listbutton.clicked.connect(self.listPressed)
	def exitPressed(self):
		self.close()
	def cplexPressed(self):
		newWindow2 = cplexWindow(self)
	def listPressed(self):
		newWindow3 = listWindow(self)

class cplexWindow(QMainWindow, Ui_cplexWindow):
	def __init__(self,parent=None):
		super(cplexWindow,self).__init__(parent)
		self.inputError = 0
		self.db=db.DB('database.sqlite')
		self.setWindowTitle("CPLEX")
		self.setupUi(self)
		self.cancelLabel.clicked.connect(self.cancelPressed)
		self.runLabel.clicked.connect(lambda:self.runPressed())
		self.fixed_cost1_lb.textChanged.connect(lambda:self.inputChanged(self.fixed_cost1_lb))
		self.fixed_cost1_ub.textChanged.connect(lambda:self.inputChanged(self.fixed_cost1_ub))
		self.fixed_cost2_lb.textChanged.connect(lambda:self.inputChanged(self.fixed_cost2_lb))
		self.fixed_cost2_ub.textChanged.connect(lambda:self.inputChanged(self.fixed_cost2_ub))
		self.capacity1_lb.textChanged.connect(lambda:self.inputChanged(self.capacity1_lb))
		self.capacity1_ub.textChanged.connect(lambda:self.inputChanged(self.capacity1_ub))
		self.capacity2_lb.textChanged.connect(lambda:self.inputChanged(self.capacity2_lb))
		self.capacity2_ub.textChanged.connect(lambda:self.inputChanged(self.capacity2_ub))
		self.demand_ub.textChanged.connect(lambda:self.inputChanged(self.demand_ub))
		self.demand_lb.textChanged.connect(lambda:self.inputChanged(self.demand_lb))
		self.numbernode1_lb.textChanged.connect(lambda:self.inputChanged(self.numbernode1_lb))
		self.numbernode1_ub.textChanged.connect(lambda:self.inputChanged(self.numbernode1_ub))
		self.numbernode2_lb.textChanged.connect(lambda:self.inputChanged(self.numbernode2_lb))
		self.numbernode2_ub.textChanged.connect(lambda:self.inputChanged(self.numbernode2_ub))
		self.productsclient_ub.textChanged.connect(lambda:self.inputChanged(self.productsclient_ub))
		self.show()

		stateList = self.db.get_states()
		self.stateInput.addItem("")
		for state in stateList:
			self.stateInput.addItem("{:2d}-{:s}".format(state[0],state[1]))
		self.stateInput.currentIndexChanged.connect(self.stateComboBoxChange)

		self.fixedCost1lb = self.inputChanged(self.fixed_cost1_lb) 
		self.fixedCost1ub = self.inputChanged(self.fixed_cost1_ub)
		self.fixedCost2lb = self.inputChanged(self.fixed_cost2_lb)
		self.fixedCost2ub = self.inputChanged(self.fixed_cost2_ub)
		self.capacity1lb = self.inputChanged(self.capacity1_lb)
		self.capacity1ub = self.inputChanged(self.capacity1_ub)
		self.capacity2lb = self.inputChanged(self.capacity2_lb)
		self.capacity2ub = self.inputChanged(self.capacity2_ub)
		self.demandlb = self.inputChanged(self.demand_lb)
		self.demandub = self.inputChanged(self.demand_ub)
		self.numberNode1lb = self.inputChanged(self.numbernode1_lb)
		self.numberNode1ub = self.inputChanged(self.numbernode1_ub)
		self.numberNode2lb = self.inputChanged(self.numbernode2_lb)
		self.numberNode2ub = self.inputChanged(self.numbernode2_ub)
		self.productsClientub = self.inputChanged(self.productsclient_ub)
		self.stateId = self.stateComboBoxChange()

	def stateComboBoxChange(self):
		item = self.stateInput.currentText()
		if (item == ""):
			return -1
		else:
			return item.split("-")[0]

	def inputChanged(self,currentInput):
		########## PASSAR O VALOR DO ERRO PRA RUNPRESSED ############
		currentText = currentInput.text()
		if (len(currentText) == 0):
			currentInput.setStyleSheet("QLineEdit {background-color:white}")
		else:
			try:
				manipulateValue = float(currentText)
				print (manipulateValue+1)
				currentInput.setStyleSheet("QLineEdit {background-color:white}")
				if self.inputError > 0:
					self.inputError -= 1 
			except ValueError:
				currentInput.setStyleSheet("QLineEdit {border: 1px solid red}")
				self.inputError += 1

	def cancelPressed(self):
		self.close()

	def runPressed(self):
		########## PASSAR O VALOR DE ERRO PARA ESSA FUNCAO ###########
		if(self.inputError > 0):
			msg = QMessageBox()
			msg.setText("As entradas devem ser numéricas")
			msg.setInformativeText("Erro ao tentar solucionar o problema")
			msg.setWindowTitle("Erro em alguma entrada do usuário")
			msg.setDetailedText("Por favor digite apenas números e pontos nas entradas da janela")
			msg.exec()
		else:
			newWindow4 = solutionWindow(self)
			#ALGORITMO DA SOLUCAO#

class listWindow(QDialog, Ui_listWindow):
	def __init__(self,parent=None):
		super(listWindow,self).__init__(parent)
		self.setWindowTitle("Listar")
		self.setupUi(self)
		self.show()

	def accept(self):
		self.done(1) 

	def reject(self):
		self.done(1)

class solutionWindow(QMainWindow, Ui_solutionWindow):
	def __init__(self,parent=None):
		super(solutionWindow,self).__init__(parent)
		self.setWindowTitle("Solution")
		self.setupUi(self)
		self.exitButton.clicked.connect(self.exitButtonPressed)
		self.show()
	def exitButtonPressed(self):
		self.close()

