#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import db
import solver
from PyQt5.QtWidgets import (QWidget, QToolTip, QPushButton, QApplication, QMainWindow, QDialog, QMessageBox, QLineEdit)
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
		self.cancelButton.clicked.connect(lambda:self.cancelPressed())
		self.runButton.clicked.connect(lambda:self.runPressed())
		
		intRegex = QRegExp("[1-9]+[0-9]*")
		priceRegex = QRegExp("([1-9]+[0-9]*|[1-9]{1}[0-9]*[\.]{1}[0-9]{1,2}|[0]{1}[\.]{1}[0-9]{1,2})")
		self.inputSupplyPopMin.setValidator(QRegExpValidator(intRegex, self))
		self.inputSupplyPopMin.textChanged.connect(lambda: self.inputChanged(self.inputSupplyPopMin))
		self.inputSupplyPopMax.setValidator(QRegExpValidator(intRegex, self))
		self.inputSupplyPopMax.textChanged.connect(lambda: self.inputChanged(self.inputSupplyPopMax))
		self.inputFacilityPopMin.setValidator(QRegExpValidator(intRegex, self))
		self.inputFacilityPopMin.textChanged.connect(lambda: self.inputChanged(self.inputFacilityPopMin))
		self.inputFacilityPopMax.setValidator(QRegExpValidator(intRegex, self))
		self.inputFacilityPopMax.textChanged.connect(lambda: self.inputChanged(self.inputFacilityPopMax))
		self.inputDemandPopMin.setValidator(QRegExpValidator(intRegex, self))
		self.inputDemandPopMin.textChanged.connect(lambda: self.inputChanged(self.inputDemandPopMin))
		self.inputDemandPopMax.setValidator(QRegExpValidator(intRegex, self))
		self.inputDemandPopMax.textChanged.connect(lambda: self.inputChanged(self.inputDemandPopMax))
		self.input_a_min.setValidator(QRegExpValidator(intRegex, self))
		self.input_a_min.textChanged.connect(lambda: self.inputChanged(self.input_a_min))
		self.input_a_max.setValidator(QRegExpValidator(intRegex, self))
		self.input_a_max.textChanged.connect(lambda: self.inputChanged(self.input_a_max))
		self.input_b_min.setValidator(QRegExpValidator(intRegex, self))
		self.input_b_min.textChanged.connect(lambda: self.inputChanged(self.input_b_min))
		self.input_b_max.setValidator(QRegExpValidator(intRegex, self))
		self.input_b_max.textChanged.connect(lambda: self.inputChanged(self.input_b_max))
		self.input_m_min.setValidator(QRegExpValidator(intRegex, self))
		self.input_m_min.textChanged.connect(lambda: self.inputChanged(self.input_m_min))
		self.input_m_max.setValidator(QRegExpValidator(intRegex, self))
		self.input_m_max.textChanged.connect(lambda: self.inputChanged(self.input_m_max))
		self.input_f_min.setValidator(QRegExpValidator(priceRegex, self))
		self.input_f_min.textChanged.connect(lambda: self.inputChanged(self.input_f_min))
		self.input_f_max.setValidator(QRegExpValidator(priceRegex, self))
		self.input_f_max.textChanged.connect(lambda: self.inputChanged(self.input_f_max))
		self.input_fm_min.setValidator(QRegExpValidator(priceRegex, self))
		self.input_fm_min.textChanged.connect(lambda: self.inputChanged(self.input_fm_min))
		self.input_fm_max.setValidator(QRegExpValidator(priceRegex, self))
		self.input_fm_max.textChanged.connect(lambda: self.inputChanged(self.input_fm_max))
		self.input_c0_min.setValidator(QRegExpValidator(priceRegex, self))
		self.input_c0_min.textChanged.connect(lambda: self.inputChanged(self.input_c0_min))
		self.input_c0_max.setValidator(QRegExpValidator(priceRegex, self))
		self.input_c0_max.textChanged.connect(lambda: self.inputChanged(self.input_c0_max))
		self.input_cr_min.setValidator(QRegExpValidator(priceRegex, self))
		self.input_cr_min.textChanged.connect(lambda: self.inputChanged(self.input_cr_min))
		self.input_cr_max.setValidator(QRegExpValidator(priceRegex, self))
		self.input_cr_max.textChanged.connect(lambda: self.inputChanged(self.input_cr_max))
		
		self.inputList = parent.findChildren(QtWidgets.QLineEdit)
		self.show()

		stateList = self.db.get_states()
		self.stateInput.addItem("")
		for state in stateList:
			self.stateInput.addItem("{:2d}-{:s}".format(state[0],state[1]))
		self.stateInput.currentIndexChanged.connect(self.stateComboBoxChange)
		self.stateId = -1

	def stateComboBoxChange(self):
		item = self.stateInput.currentText()
		if (item == ""):
			self.labelCities.setText("")
			self.labelMinPop.setText("")
			self.labelMaxPop.setText("")
			self.stateId = -1
		else:
			stateId = item.split("-")[0]
			state = self.db.get_state_by_id(stateId)
			self.labelCities.setText(str(state["nCities"]))
			self.labelMinPop.setText(str(state["minPop"]))
			self.labelMaxPop.setText(str(state["maxPop"]))
			self.stateId = stateId
		
	def inputChanged(self,currentInput):
		if (currentInput.hasAcceptableInput()):
			currentInput.setStyleSheet("QLineEdit {background-color:white}")
		else:
			currentInput.setStyleSheet("QLineEdit {border: 1px solid red}")

	def cancelPressed(self):
		self.close()

	def runPressed(self):
		if(self.stateId == -1):
			errorFlag = True
		else:
			errorFlag = False
			for lineEdit in self.inputList:
				if(not lineEdit.hasAcceptableInput()):
					errorFlag = True
		if(errorFlag):
			msg = QMessageBox()
			msg.setText("Erro ao tentar solucionar o problema:")
			msg.setInformativeText("Todos os campos devem ser preenchidos corretamente, em que campos de custo devem utilizar (.) como separador decimal e os outos campos preenchidos com inteiros positivos não-nulos. O estado também deve ser selecionado")
			msg.setWindowTitle("Erro")
			msg.exec()
		else:
			inputData = {
				"stateId":        int(self.stateId),
				"supplyPopMin":   int(self.inputSupplyPopMin.text()),
				"supplyPopMax":   int(self.inputSupplyPopMax.text()),
				"facilityPopMin": int(self.inputFacilityPopMin.text()),
				"facilityPopMax": int(self.inputFacilityPopMax.text()),
				"demandPopMin":   int(self.inputDemandPopMin.text()),
				"demandPopMax":   int(self.inputDemandPopMax.text()),
				"fMin":           float(self.input_f_min.text()),
				"fMax":           float(self.input_f_max.text()),
				"fmMin":          float(self.input_f_min.text()),
				"fmMax":          float(self.input_f_max.text()),
				"c0Min":          float(self.input_c0_min.text()),
				"c0Max":          float(self.input_c0_max.text()),
				"crMin":          float(self.input_cr_min.text()),
				"crMax":          float(self.input_cr_max.text()),
				"aMin":           int(self.input_a_min.text()),
				"aMax":           int(self.input_a_max.text()),
				"bMin":           int(self.input_b_min.text()),
				"bMax":           int(self.input_b_max.text()),
				"mMin":           int(self.input_m_min.text()),
				"mMax":           int(self.input_m_max.text())
			}
			
			self.solver = solver.Solver(inputData)
			self.solver.exec_cplex()
			self.solver.plot_sol() 

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

