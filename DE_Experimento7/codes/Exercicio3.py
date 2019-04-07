#!/usr/bin/env python3.7
# Esse script corresponde ao primeiro exercício do quarto 
# experimento de Dispositivos eletrônicos.
import sys
sys.path.append("../../Bibliotecas/") 
import ClasseDados as cla
from matplotlib import pyplot as plt


imgFolder = "../Imagens/Exercicio3/"


#######################################################################
##     Item A                                                        ##
#######################################################################
read1 =cla.OsciloscopioCSV("../raw_files/dados.csv")
'''
Ex do csv
X--Trace 1::[V(vc2)],Y--Trace 1::[V(vc2)],,X--Trace 2::[V(vb2)],Y--Trace 2::[V(vb2)],,X--Trace 3::[V(ve)],Y--Trace 3::[V(ve)]
0,5.00011,,0,0.620702,,0,0
4e-007,4.99942,,4e-007,0.62071,,4e-007,1.6e-005

xc2,yc2,NADA,xb2,yb2,NADA,xve,yve

'''
read1.GetNChannels()

# Le os dados salvos no csv
ie_1   = read1.GetVoltageArray(0)
iref_1 = read1.GetVoltageArray(1)
ic4_1 = read1.GetVoltageArray(2)

iPow=[]
for i in range(0,len(ie_1)):
    iPow.append((ie_1[i]**2)/(iref_1[i]*1e-3))


plt.figure(0)
#plt.subplot(121)
plt.plot(ie_1,ic4_1,label="$I_{C4}$ (Experimental)",marker="*")
plt.plot(ie_1,iPow,label="$I_{C4}$ (Ideal)",marker="*")
plt.grid()
plt.legend()
plt.ylabel('$I_C$ [mA]')
plt.xlabel('$I_e$ [mA]')
plt.savefig(imgFolder+"DE7_ex4_compare.png")

erro=[]
for i in range(0,len(ie_1)):
    erro.append((abs(ic4_1[i]-iPow[i])/float(ic4_1[i]))*100)  #a diferenca é a corrente de base


#plt.subplot(122)
plt.figure(1)
plt.plot(ie_1,erro,label="Erro percentual",marker="*", color="green")
plt.grid()
plt.legend()
plt.ylabel('Erro percentual[%]')
plt.xlabel('$I_e$ [mA]')
plt.savefig(imgFolder+"DE7_ex4_compare_erro.png")

plt.show()