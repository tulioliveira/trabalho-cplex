#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import db
import solver
import gmplot
import webbrowser

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
        self.setWindowTitle("Janela Principal")
        self.setupUi(self)
        self.cplexbutton.clicked.connect(self.cplexPressed)
        self.exitbutton.clicked.connect(self.exitPressed)
        self.listbutton.clicked.connect(self.listPressed)
    def exitPressed(self):
        self.close()
    def cplexPressed(self):
        newCplexWindow = cplexWindow(self)
    def listPressed(self):
        newListWindow = listWindow(self)

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
                "fmMin":          float(self.input_fm_min.text()),
                "fmMax":          float(self.input_fm_max.text()),
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
            solutionId = self.solver.exec_cplex()
            if (solutionId == -1):
                msg = QMessageBox()
                msg.setText("Erro ao tentar solucionar o problema:")
                msg.setInformativeText("Não foi possível encontrar uma solução com os parâmetros escolhidos!")
                msg.setWindowTitle("Erro")
                msg.exec()
            else:
                newSolutionWindow = solutionWindow(solutionId, self)


class listWindow(QDialog, Ui_listWindow):
    def __init__(self,parent=None):
        super(listWindow,self).__init__(parent)
        self.setWindowTitle("Listar")
        self.setupUi(self)
        self.db = db.DB('database.sqlite')
        solutions = self.db.get_solutions()
        items = [str(sol['id']) + ': ' + sol['stateName'] + ' (' + sol['created_on'] + ')' for sol in solutions]
        self.listSolutions.addItems(items)
        self.buttonExit.clicked.connect(self.exitButtonPressed)
        self.buttonOpenSolution.clicked.connect(self.openSolution)
        self.listSolutions.itemDoubleClicked.connect(self.openSolution)
        self.show()

    def exitButtonPressed(self):
        self.close()

    def openSolution(self):
        for item in self.listSolutions.selectedItems():
            solutionId = item.text().split(":")[0]
            newSolutionWindow = solutionWindow(solutionId, self)

class solutionWindow(QMainWindow, Ui_solutionWindow):
    def __init__(self,solutionId, parent=None):
        super(solutionWindow,self).__init__(parent)
        self.setWindowTitle("Solução")
        self.setupUi(self)
        self.db = db.DB('database.sqlite')
        self.solutionId = solutionId
        self.solData = self.db.get_solution_by_id(solutionId)
        self.state = self.db.get_state_by_id(self.solData['varParameters']['stateId'])
        self.labelSupplyPoints.setStyleSheet("QLabel { color : red; }")
        self.labelSupplyPointsCount.setStyleSheet("QLabel { color : red; }")
        self.labelSupplyPointsCount.setText(str(len(self.solData["supplyPoints"])))
        self.labelFacilities.setStyleSheet("QLabel { color : blue; }")
        self.labelFacilitiesCount.setStyleSheet("QLabel { color : blue; }")
        self.labelFacilitiesCount.setText(str(len(self.solData["w"])))
        self.labelDemandPoints.setStyleSheet("QLabel { color : green; }")
        self.labelDemandPointsCount.setStyleSheet("QLabel { color : green; }")
        self.labelDemandPointsCount.setText(str(len(self.solData["demandPoints"])))
        self.labelStateName.setText(self.state["name"])
        self.labelTotalCost.setText("R$ {:.2f}".format(self.solData["totalCost"]))
        self.labelTotalFacilitiesCost.setText("R$ {:.2f}".format(self.solData["totalFacilitiesCost"]))
        self.labelTotalProductsCost.setText("R$ {:.2f}".format(self.solData["totalProductsCost"]))
        self.labelTotalUnitsOverflow.setText(str(int(self.solData["totalUnitsOverflow"])) + ' Unidades')
        self.labelTotalOverflowCost.setText("R$ {:.2f}".format(self.solData["totalOverflowCost"]))
        self.google_maps_widget()
        self.exitButton.clicked.connect(self.exitButtonPressed)
        self.show()

    def google_maps_widget(self):
        self.webkit = QWebEngineView(self)
        self.layoutMap.addWidget(self.webkit)
        self.plot_cities()
        self.webkit.show()
    
    def plot_cities(self):
        # Get Latitude and Longitude of Supply Points, Facilities and Demand Points
        spLat = []
        spLon = []
        fLat = []
        fLon = []
        dpLat = []
        dpLon = []
        for supplyPoint in self.solData["supplyPoints"]:
            spLat.append(supplyPoint['lat'])
            spLon.append(supplyPoint['lon'])
        for index in self.solData["w"]:
            fLat.append(self.solData["facilities"][index]["lat"])
            fLon.append(self.solData["facilities"][index]["lon"])
        for demandPoint in self.solData["demandPoints"]:
            dpLat.append(demandPoint['lat'])
            dpLon.append(demandPoint['lon'])
        avglat = (sum(spLat) + sum(fLat) + sum(dpLat))/(len(spLat) + len(fLat) + len(dpLat))
        avglon = (sum(spLon) + sum(fLon) + sum(dpLon))/(len(spLon) + len(fLon) + len(dpLon))

        gm = gmplot.GoogleMapPlotter(avglat,avglon,6)
        spDpLat = (set(spLat) & set(dpLat))
        spDpLon = (set(spLon) & set(dpLon))
        spFLat = (set(spLat) & set(fLat))
        spFLon = (set(spLon) & set(fLon))
        fDpLat = (set(fLat) & set(dpLat))
        fDpLon = (set(fLon) & set(dpLon))
        gm.scatter((set(spDpLat) - set(spFLat)),(set(spDpLon) - set(spFLon)),'y',size=40)
        gm.scatter((set(spFLat) - set(spDpLat)),(set(spFLon) - set(spDpLon)),'m',size=40)
        gm.scatter((set(fDpLat) - set(spFLat)),(set(fDpLon) - set(spFLon)),'c',size=40)
        gm.scatter((set(spDpLat) & set(spFLat) & set(fDpLat)), (set(spDpLon) & set(spFLon) & set(fDpLon)), 'w', size=40)
        gm.scatter((set(fLat) - set(spFLat) - set(fDpLat)),(set(fLon) - set(spFLon) - set(fDpLon)),'b',size=40)
        gm.scatter((set(dpLat) - set(spDpLat) - set(fDpLat)), (set(dpLon) - set(spDpLon) - set(fDpLon)),'g',size=40)
        gm.scatter((set(spLat) - set(spDpLat) - set(spFLat)),(set(spLon) - set(spDpLon) - set(spFLon)),'r',size=40)
        file_name = '/home/tulioliveira/Documentos/trabalho-cplex/map.html'
        gm.draw(file_name)

        url = QUrl("file://" + file_name)
        self.webkit.load(url)

    def exitButtonPressed(self):
        self.close()

