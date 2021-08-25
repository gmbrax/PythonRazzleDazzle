from typing import DefaultDict
import setup
from random import *

class game():
    def __init__(self):
        self.__NumeroTurno = 0
        self.__NumeroTurnosSemPremio = 0
        self.__score = 0
        self.__prize = 0
        self.__cost_turn = 1
        self.__money_spent = 0
        self.__turnsList = []
        self.__GanhouJogo = None


    def obterNumeroTurno(self):
        return self.__NumeroTurno
    
    def definirNumeroTurno(self,Numero):
        self.__NumeroTurno += Numero

    def obterNumeroTurnoSemPremio(self):
        return self.__NumeroTurnosSemPremio

    def incrementarTurnoSemPremio(self,valor):
        self.__NumeroTurnosSemPremio += valor

    def definirNumeroTurnoSemPremio(self,turno):
        self.__NumeroTurnosSemPremio = turno

    def JogoGanho(self):
        self.__GanhouJogo = True

    def JogoNaoGanho(self):
        self.__GanhouJogo = False    

    def obterScore(self):
        return self.__score
    
    def definirScore(self,score):
        self.__score += score
    
    def obterPrize(self):
        return self.__prize
    
    def definirPrize(self,prize):
        self.__prize += prize
    
    def obterCostTurn(self):
        return self.__cost_turn 

    def definirCostTurn(self,cost):
        self.__cost_turn += cost

    def obterMoneySpent(self):
        return self.__money_spent
    
    def incrementarValorGasto(self,valor):
        self.__money_spent += valor

    def obterTurnsList(self):
        return self.__turnsList

    def obterItemTurnsList(self,n):
        return self.__turnsList[n]

    def definirItemTurnsList(self,turno):
        self.__turnsList.append(turno)    

    def incrementarTurno(self):
        self.__NumeroTurno += 1
       
        
    
        print("Turno: " + str(self.obterNumeroTurno()))
        print("Turno sem premio: " + str(self.obterNumeroTurnoSemPremio()))
        

    def AutoTurn(self,numeroturnos):
        for x in range(0,numeroturnos):
            turn = setup.Turn()
            turn.turno()
            flagResultadoTurno = turn.obterFlagResultadoTurno()
            print("Flag:" + str(flagResultadoTurno))
            self.incrementarTurno()
            self.incrementarValorGasto(self.obterCostTurn())
        if flagResultadoTurno == 0:
            self.incrementarTurnoSemPremio(1)
        elif flagResultadoTurno == 1:
            self.definirScore(5)
            self.definirNumeroTurnoSemPremio(0)
        elif flagResultadoTurno == 2:
            self.definirScore(10)
            self.definirNumeroTurnoSemPremio(0)
        elif flagResultadoTurno == 4:
            self.definirScore(15)
            self.definirNumeroTurnoSemPremio(0)
        elif flagResultadoTurno == 8:
            self.definirScore(20)
            self.definirNumeroTurnoSemPremio(0)
        elif flagResultadoTurno == 16:
            self.definirScore(30)
            self.definirNumeroTurnoSemPremio(0)
        elif flagResultadoTurno == 32:
            self.definirScore(50)
            self.definirNumeroTurnoSemPremio(0)
        elif flagResultadoTurno == 64:
            self.definirScore(100)
            self.definirNumeroTurnoSemPremio(0)
        elif flagResultadoTurno == 128:
            self.definirPrize(1)
            self.definirNumeroTurnoSemPremio(0)
        elif flagResultadoTurno == 265:
            self.definirCostTurn = (self.obterCostTurn * 2)
            self.incrementarTurnoSemPremio(1)
        else:
            self.definirNumeroTurnoSemPremio(0)

    def turn(self):
       
        self.AutoTurn(2)

    def run(self):

        self.turn()



 