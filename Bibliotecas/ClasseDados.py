import matplotlib.pyplot as plt

class OsciloscopioCSV(object): #Classe criada para ler csv files
    """Dados obtidos a partir de um arquivo csv.
        
        Fonte pra aprender docstring:
            https://www.datacamp.com/community/tutorials/docstrings-python
            https://www.pythonforbeginners.com/basics/python-docstrings
            https://www.geeksforgeeks.org/python-docstrings/
    """
    def __init__(self, filePath):
    #   super(OsciloscopioCSV, self).__init__()
        #https://pt.stackoverflow.com/questions/22452/como-se-usa-e-para-que-serve-o-super-em-classes-python
        self.__filePath = filePath
        self.__inputCSV = open(filePath)
        self.__lines=[]

        # Le a primeira linha
        #  Como a primeira linha é o cabeçalho do arquivo csv
        #  ele apresenta quantos canais foram usados no osciloscópio
        #  (em numero de colunas) 
        self.__nChannels = len((self.__inputCSV.readline()).split(","))

        # # # Implementar algo que leia a segunda linha. Responsável por 
        # # # dar a unidade.

        # Le cada linha do arquivo csv, separa os espaços entre virgulas
        # e armazena em uma variavel
        for line in self.__inputCSV:
            lineComplete=True
            for i in range(0,len(line.split(","))):
                if(len(line.split(",")[i])==0):
                    lineComplete=False
            if(lineComplete): 
                self.__lines.append(line)

        self.__data=[] # Inicializa variavel que guarda o set de dados

        # Inicializa arrays dentro da array principal
        #   Feito pra que seja 
        for i in range(0,self.__nChannels):
            self.__data.append([])

        for num_line in range(2,len(self.__lines)): # inicia em 2 pois as duas primeiras linhas são apenas cabecalhos
            for i in range(0,self.__nChannels):
                self.__data[i].append(float(self.__lines[num_line].split(",")[i]))

    def GetNChannels(self):
        """Returns the number of channels of the csv files"""
        print("GetNChannels = " + str(self.__nChannels))
        return self.__nChannels

    def GetVoltage(self,source,time):
        """Returns the voltage  in a certain time of a specified channel """
        # pra implementar é necessario ter algum algoritmo que aproxima o valor de tempo
        # ex: GetVoltage(1,1)
        #     aqui ele pegaria o tempo em 1 segundo mas dependendo dos intervalos colocados na leitura talvez haja 0.99s e 1.01s
        #     Como ele decidiria qual amostra usar?
        i = self.__data[0].index(time)
        return self.__data[source][i]

    def GetTime(self,source,voltage):
        """Returns the voltage  in a certain time of a specified channel """
        # pra implementar é necessario ter algum algoritmo que aproxima o valor de tempo
        # ex: GetVoltage(1,1)
        #     aqui ele pegaria o tempo em 1 segundo mas dependendo dos intervalos colocados na leitura talvez haja 0.99s e 1.01s
        #     Como ele decidiria qual amostra usar?
        i = self.__data[source].index(voltage)
        return self.__data[0][i]

    def GetVoltageArray(self,source):
        """Returns an array of all voltages to a channel"""
        return self.__data[source]

    def GetMaxVoltage(self,source):
        """Returns the maximum voltage of a channel"""
        maxVoltage=self.__data[source][0]
        time = None
        for i in range(0,len(self.__data[source])):
            if(self.__data[source][i]>maxVoltage):
                maxVoltage=self.__data[source][i]
                time=self.__data[0][i]
        print("The maximum value of channel {:d} ocurrs in {:.2e} seconds and is {:.2e}V.".format(source,time,maxVoltage))
        return (time,maxVoltage)

    def GetMinVoltage(self,source,tIni=None,tFin=None):
        """Returns the minimum voltage of a channel"""
        if(tIni==None and tFin==None):
            minVoltage=self.__data[source][0] # Gets an sample(initial one)
            time = None
            for i in range(0,len(self.__data[source])):
                if(self.__data[source][i]<minVoltage):
                    minVoltage=self.__data[source][i]
                    time=self.__data[0][i]
            print("The minimum value of channel {:d} ocurrs in {:.2e} seconds and is {:.2e}V.".format(source,time,minVoltage))
        elif(tIni>tFin or tIni==tFin):
            print("(E)  GetMinVoltage: The vaule of interval [{:.2f}:{:.2f}] is invalid.".format(tIni,tFin))
            exit()
        else:
            # Assim como em GetTime
            # pra implementar é necessario ter algum algoritmo que aproxima o valor de tempo
            # ex: GetVoltage(1,1)
            #     aqui ele pegaria o tempo em 1 segundo mas dependendo dos intervalos colocados na leitura talvez haja 0.99s e 1.01s
            #     Como ele decidiria qual amostra usar?
            '''
            minIndex = float(self.__data[0].index(tIni))
            maxIndex = float(self.__data[0].index(tFin))
            minVoltage=self.__data[source][minIndex]
            time = None
            for i in range(minIndex,maxIndex+1):
                if(self.__data[source][i]<minVoltage):
                    minVoltage=self.__data[source][i]
                    time=self.__data[0][i]
            print("The minimum value of channel {:d} ocurrs in {:.2e} seconds and is {:.2e}V.".format(source,time,minVoltage))
            '''
            
            print("(E)  GetMinVoltage: Function not implemented yet.")
            exit()

        return (time,minVoltage)

    def GetPeaks(self,source):
        """Implement the peak finder algorithm."""
        '''
        Alguns possiveis links:
          https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.find_peaks.html
          https://www.geeksforgeeks.org/find-a-peak-in-a-given-array/
          https://medium.com/@rabin_gaire/algorithmic-thinking-peak-finding-ad6f7415d154
          https://courses.csail.mit.edu/6.006/spring11/lectures/lec02.pdf
        '''
        pass  

    def GetAverage(self,source,tmin=None,tmax=None):
        if(tmin==None and tmax==None):
            y=0.
            for x in range(0,len(self.__data[source])):
                y=y+float(self.__data[source][x])
            ymed=y/float(len(self.__data[source]))
        else:
            y=0.
            count=0
            for x in range(0,len(self.__data[source])):
                if(self.__data[0][x]>=float(tmin) and self.__data[0][x]<=tmax):
                    y=y+float(self.__data[source][x])
                    count=count+1
            ymed=y/float(count)
        return ymed

    def ShowData(self):
        plt.plot(self.__data[0], self.__data[1], label='Canal 1')
        plt.plot(self.__data[0], self.__data[2], label='Canal 2')
        plt.xlabel('tempo [s]')
        plt.ylabel('tensão [V]')   
        plt.grid()
        plt.legend()
        plt.show() 

    def GetSourcePath(self):
        print("The path of this experiment is: "+self.__filePath)
        return(self.__filePath)     

class ResistanceDiode(object):
    """Modelo com resistencia e diodo em série."""
    def __init__(self, resistance,vFont,vDiode):
        super(ResistanceDiode, self).__init__()
        self.__resistance = float(resistance)
        self.__vFont = vFont
        self.__vDiode = vDiode
        self.__iDiode = []
        for i in range(0,len(self.__vDiode)):
            self.__iDiode.append((self.__vFont[i]-self.__vDiode[i])/self.__resistance)
    def GetCurrent(self):
        return self.__iDiode
    def GetCaracteristicCurve(self):
        return(self.__vDiode,self.__iDiode)

        