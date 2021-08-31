# Bem vindo ao caos 


from array import *
from random import *
import csv #monark cade os dados?
from datetime import datetime


class table():
    def __init__(self):
        self.ball_table = [
    [4,3,2,4,1,3,2,3,6,4,5,3,4],
    [3,4,5,3,6,4,5,4,1,3,2,4,5],
    [4,3,2,4,1,3,2,3,6,4,5,3,4],
    [3,4,5,3,6,4,5,4,1,3,2,4,2],
    [4,3,2,4,1,3,2,3,6,4,5,3,4],
    [3,4,5,3,6,4,5,4,1,3,2,4,2],
    [4,3,2,4,1,3,2,3,6,4,5,3,4],
    [3,4,5,3,6,4,5,4,1,3,2,4,5],
    [4,3,2,4,1,3,2,3,6,4,5,3,4],
    [3,4,5,3,6,4,5,4,1,3,2,4,5],
    [4,3,2,4,1,3,2,3,6,4,5,3,4]
    ]
    def obter_valor(self,y,x):
        return self.ball_table[y][x]
    
    def obterNumeroLinhasMatriz(self):
        return (len(self.ball_table[0]) - 1) #retorna o tamanho menos -1 pq se nao la na frente estoura o tamanho

    def obterNumeroColunasMatriz(self):
        return (len(self.ball_table) - 1)


class score_card():
    def __init__(self):
        self.flagNull = 0
        self.flag5pts = 1
        self.flag10pts = 2
        self.flag15pts = 4
        self.flag20pts = 8
        self.flag30pts = 16
        self.flag50pts = 32
        self.flag100pts = 64
        self.flagprize = 128
        self.flagdouble = 256

        self.prizeSet = {18,38,19,37,36,21,35,20}
        self.NullSet = {28,26,30,27,32,25,31,24,34,23,33,22}
        self.DoubleMoneySet = {29}
        
        self.pts5Set = {40,17,39}
        self.pts10Set = {16}
        self.pts15Set = {15,41}
        self.pts20Set = {42,14}
        self.pts30Set = {11,45}
        self.pts50Set = {44,13,43,12,46,11,45,10}
        self.pts100Set = {9,48,8,47}
    
    def checarSomaDePontos(self,somatoria):
        
        if somatoria in self.pts5Set:
            
            return self.flag5pts
        
        elif somatoria in self.pts10Set:
            
            return self.flag10pts

        elif somatoria in self.pts15Set:
            
            return self.flag15pts

        elif somatoria in self.pts20Set:
            
            return self.flag20pts

        elif somatoria in self.pts30Set:
            
            return self.flag30pts    

        elif somatoria in self.pts50Set:
            
            return self.flag50pts
        
        elif somatoria in self.pts100Set:
            
            return self.flag100pts 

        elif somatoria in self.prizeSet:
            
            return self.flagprize

        elif somatoria in self.NullSet:
            
            return self.flagNull

        elif somatoria in self.DoubleMoneySet:
            
            return self.flagdouble
        
        else:
            print("Deu pau na matrix SAINDO........")
            exit(1)


class TSVFile():
    
    def __init__(self):
        self.FilePath = str(datetime.now()) + '.tsv'
        self.TSVFile = None
        self.TSVFileWriter = None
        self.AttributeList = ['Turn','Turns_Without_prize','Score','Prize','Money_Spent','Cost_per_turn','Ball_Positions','Ball_Values','Ball_Sum','Score_Flag','Has_Won']
    
    def createfile(self):
        print("Criando Relatorio")
        print(type(self.AttributeList))
        with open(self.FilePath,'w+') as self.TSVFile:
          self.TSVFileWriter = csv.writer(self.TSVFile,delimiter='\t')
          self.TSVFileWriter.writerow(self.AttributeList)

    def writefile(self,InputList):
        if len(InputList) != len(self.AttributeList):
            print("Lista Incompleta")
            exit(2)
        else:
            self.TSVFileWriter.writerow(InputList)

    def closefile(self):
        self.TSVFile.close()              


class Turn():
    
    def __init__(self):

        self.__gameTable = table()
        self.__scoreCard = score_card()
        self.__NumeroTurno = None
        self.__NumeroTurnosSemPremio = 0
        self.__PosiçoesBolasJogadas= []
        self.__ValoresBolasJogadas = []
        self.__SomatoriaValoreBolasJogadas= None
        self.__FlagAutoCheater = None
        self.__PosiçoesBolasJogadasComAutoCheater = []
        self.__FlagResultadoTurnoComAutoCheater = None
        self.__FlagResultadoTurno = None


    def obterPosicoesBolasJogadas(self):
        return self.__PosiçoesBolasJogadas
    
    def definirPosicoesBolasJogadas(self,PosicoesBolas):
        self.__PosiçoesBolasJogadas.append(PosicoesBolas)
    
    def obterValoresBolasJogadas(self):
        return self.__ValoresBolasJogadas
    
    def obterItemValorBolaJogada(self,n):
        return self.__ValoresBolasJogadas[n]

    def definirValoresBolasJogadas(self,Valor):
        self.__ValoresBolasJogadas.append(Valor)

    def obterSomatoriaValoresBolasJogadas(self):
        return self.__SomatoriaValoreBolasJogadas

    def definirSomatoriaValoresBolasJogadas(self,somatoria):
        self.__SomatoriaValoreBolasJogadas = somatoria

    def obterFlagAutocheater(self):
        return self.__FlagAutoCheater

    def definirFlagAutoCheater(self,flag):
        self.__FlagAutoCheater = flag

    def obterPosicoesBolasJogadasComAutoCheater(self):
        return self.__PosiçoesBolasJogadasComAutoCheater

    def definirPosicoesBolasJogadasComAutoCheater(self,PosicoesBolas):
        if self.__FlagAutoCheater is True:
            self.__PosiçoesBolasJogadasComAutoCheater = PosicoesBolas                
        elif self.__FlagAutoCheater is False:
            self.__PosiçoesBolasJogadasComAutoCheater = self.__PosiçoesBolasJogadas
        else:
            exit(3)

    def obterFlagResultadoTurnoComAutoCheater(self):
        return self.__FlagResultadoTurnoComAutoCheater

    def definirFlagResultadoTurnoComAutoCheater(self,flag):
        if self.__FlagAutoCheater is True:
            self.__FlagResultadoTurnoComAutoCheater = flag
        elif self.__FlagAutoCheater is False:
            self.__FlagResultadoTurnoComAutoCheater = self.__FlagResultadoTurno
        else:
            exit(-3)

    def obterFlagResultadoTurno(self):
        return self.__FlagResultadoTurno
    
    def definirFlagResultadoTurno(self,flag):
        self.__FlagResultadoTurno = flag



    def turno(self):

        def jogarBolas(self):
            for x in range(0,8):
                Bola = [randint(0,int(self.__gameTable.obterNumeroColunasMatriz())),randint(0,self.__gameTable.obterNumeroLinhasMatriz())]
                self.definirPosicoesBolasJogadas(Bola)
                

        def obterValoresBolas(self):
            for x in range(0,len(self.__PosiçoesBolasJogadas)):
                posicao = self.__gameTable.obter_valor(self.__PosiçoesBolasJogadas[x][0],self.__PosiçoesBolasJogadas[x][1])
                self.__ValoresBolasJogadas.append(posicao)

        def somarValoresBolas(self):
            somatorio = 0
            for x in range(0,len(self.__ValoresBolasJogadas)):
                somatorio += self.obterItemValorBolaJogada(x)
            self.definirSomatoriaValoresBolasJogadas(somatorio)

        def checarSomaValoresBolas(self):
            FlagResultado = self.__scoreCard.checarSomaDePontos(self.obterSomatoriaValoresBolasJogadas())
            self.definirFlagResultadoTurno(FlagResultado)



        jogarBolas(self)
        obterValoresBolas(self)
        somarValoresBolas(self)
        checarSomaValoresBolas(self)


    

def createfile():
    print("Criando Relatorio")
    tsvFileAddres = datetime.now().strftime("jogo - %d/%m/%Y-%H:%M:%S")+ '.tsv'
    with open(str(datetime.now()) + '.tsv','w+') as tsv_file:
        tsv_writer = csv.writer(tsv_file, delimiter='\t')
        tsv_writer.writerow(['Turn','Turns_Without_prize','Score','Prize','Money_Spent','Cost_per_turn','Ball_Positions','Ball_Values','Ball_Sum','Score_Flag','Has_Won'])
        print(tsv_file)

        return tsv_file
       
def writefile(fileWriter,Stats_List ):
    if len(Stats_List) != 11:
        print("Lista Incompleta")
        exit(2)
    else:
        fileWriter.writerow(Stats_List) 

def closefile(file):
    file.close()
       