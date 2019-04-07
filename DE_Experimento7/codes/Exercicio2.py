#!/usr/bin/env python3.7
# Esse script corresponde ao primeiro exercício do quarto 
# experimento de Dispositivos eletrônicos.
import sys
sys.path.append("../../Bibliotecas/") 
import ClasseDados as cla
from matplotlib import pyplot as plt


imgFolder = "../Imagens/Exercicio2/"


#######################################################################
##     Item A                                                        ##
#######################################################################
read1 =cla.MultisimCSV("../raw_files/ex12.csv")
read1.GetNChannels()

# Le os dados salvos no csv
ie_1,ic4_1  = read1.GetChannel(0)
ie_1=list(map(lambda f: f*1e3,ie_1)) # em mA
ic4_1=list(map(lambda f: f*1e3,ic4_1)) # em mA
iPow=[]
for i in range(0,len(ie_1)):
    iPow.append((ie_1[i]**2)/50e-3)


plt.figure(0)
#plt.subplot(121)
plt.plot(ie_1,ic4_1,label="$I_{C4}$ (Multisim)")
plt.plot(ie_1,iPow,label="$I_{C4}$ (Python)")
plt.grid()
plt.legend()
plt.ylabel('$I_C$ [mA]')
plt.xlabel('$I_e$ [mA]')
#plt.savefig(imgFolder+"DE7_ex13_compare.png")

erro=[]
for i in range(0,len(ie_1)):
    erro.append(((ic4_1[i]-iPow[i])/float(ic4_1[i]))*100)  #a diferenca é a corrente de base


#plt.subplot(122)
plt.figure(1)
plt.plot(ie_1,erro,label="Erro percentual", color="green")
plt.grid()
plt.legend()
plt.ylabel('Erro percentual[%]')
plt.xlabel('$I_e$ [mA]')
#plt.savefig(imgFolder+"DE7_ex13_compare_erro.png")



#######################################################################
##     Comparison                                                    ##
#######################################################################
read2 =cla.OsciloscopioCSV("../raw_files/ex12_comIB_BF3.csv")
read2.GetNChannels()

# Le os dados salvos no csv
ie_2,ic4_2   = read2.GetVoltageArray(0) , read2.GetVoltageArray(1)
tib42,ib4_2 =  read2.GetVoltageArray(2) , read2.GetVoltageArray(3)
iPow_2=[]

print(ie_2)
for i in range(0,len(ie_2)):
    iPow_2.append(((ie_2[i]**2)/50e-6))

        #+ib4_2[i])


plt.figure(2)
plt.subplot(121)
plt.plot(ie_2,ic4_2,label="$I_{C4}$ (Multisim)")
plt.plot(ie_2,iPow_2,label="$I_{C4}$ (Python)")
plt.grid()
plt.legend()
plt.ylabel('$I_C$ [A]')
plt.xlabel('$I_e$ [A]')
#plt.savefig(imgFolder+"DE7_ex13_compare2.png")

erro=[]
for i in range(0,len(ie_2)):
    erro.append(((ic4_2[i]-iPow_2[i])/float(ic4_2[i]))*100.)  #a diferenca é a corrente de base


#plt.figure(3)
plt.subplot(122)
plt.plot(ie_2,erro,label="$I_{C4}$ (Multisim)")
plt.grid()
plt.legend()
plt.ylabel('Erro percentual[%]')
plt.xlabel('$I_e$ [A]')
#plt.savefig(imgFolder+"DE7_ex13_compare2_erro.png")
plt.show()

