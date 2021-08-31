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

    def definirCostTurn(self):
        self.__cost_turn = (self.__cost_turn *2)

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
       
        
    
        
        
    def atualizarVariaveisJogo(self,flagResultadoTurno):
        if flagResultadoTurno is 0:
            self.incrementarTurnoSemPremio(1)

        elif flagResultadoTurno is 1:
            self.definirScore(5)
        elif flagResultadoTurno is 2:
            self.definirScore(10)
        elif flagResultadoTurno is 4:
            self.definirScore(15)
        elif flagResultadoTurno is 8:
            self.definirScore(20)
        elif flagResultadoTurno is 16:
            self.definirScore(30)
        elif flagResultadoTurno is 32:
            self.definirScore(50)
        elif flagResultadoTurno is 64:
            self.definirScore(100)
        elif flagResultadoTurno is 128:
            self.definirPrize(1)
        elif flagResultadoTurno is 256:
            self.definirPrize(1)
            self.definirCostTurn()
        else:
            exit(-99)

    def TurnPrint(self,turn):
        print("------------------------------------------------------------------------------------------------------")
        print("Turno: " + str(self.obterNumeroTurno()))
        print("Turnos sem premio: " + str(self.obterNumeroTurnoSemPremio()))
        print("Valor Gasto: " +  "US$ " + str(self.obterMoneySpent()))
        print("Valor da Aposta: " + "US$ " + str(self.obterCostTurn()))
        print("Posições das Bolas:" + str(turn.obterPosicoesBolasJogadas()) )
        print("Valor das Bolas Jogadas" + str(turn.obterValoresBolasJogadas()))
        print("Somatoria das Bolas Jogadas: " + str(turn.obterSomatoriaValoresBolasJogadas()))
        print("Flag Resultado: " + str(turn.obterFlagResultadoTurno()))
        print("Score: " + str(self.obterScore()))
        print("Premios Acumulados:" + str(self.obterPrize()))
        

        

    def AutoTurn(self,numeroturnos):
        for x in range(0,numeroturnos):
            turn = setup.Turn()
            turn.turno()
            flagResultadoTurno = turn.obterFlagResultadoTurno()
            self.incrementarTurno()
            self.incrementarValorGasto(self.obterCostTurn())
            self.atualizarVariaveisJogo(flagResultadoTurno)
            self.TurnPrint(turn)

    def turn(self):
       
        self.AutoTurn(300)

    def run(self):

        self.turn()



 