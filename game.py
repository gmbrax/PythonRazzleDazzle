import setup
from random import *

class game():
    def __init__(self):
        self.__score = 0
        self.__prize = 0
        self.__cost_turn = 0
        self.__money_spent = 0
        self.__turnsList = []

        
    
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

    def obterTurnsList(self):
        return self.__turnsList

    def obterItemTurnsList(self,n):
        return self.__turnsList[n]

    def definirItemTurnsList(self,turno):
        self.__turnsList.append(turno)    

    def turn(self):
        turn = setup.Turn()
        turn.turno()
        
    def run(self):

        self.turn()



 