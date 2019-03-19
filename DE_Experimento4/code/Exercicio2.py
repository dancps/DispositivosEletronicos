#!/usr/bin/env python3.7
# Esse script corresponde ao primeiro exercício do quarto 
# experimento de Dispositivos eletrônicos.
import sys
sys.path.append("../../Bibliotecas/") 
import ClasseDados as cla
from matplotlib import pyplot as plt


imgFolder = "../img/Exercicio2/"


#######################################################################
##     Item A                                                        ##
#######################################################################
read1 =cla.OsciloscopioCSV("../raw_files/scope_17.csv")

read1.GetNChannels()

# Le os dados salvos no csv
time_1   = read1.GetVoltageArray(0)
vFonte_1 = read1.GetVoltageArray(1)
vDiodo_1 = read1.GetVoltageArray(2)
vFunc=[]
for i in range(0,len(time_1)):
	if(vFonte_1[i]==0):
		vFunc.append(0.00)
	else:
		vFunc.append(vDiodo_1[i]/vFonte_1[i])

plt.figure(0)
plt.plot(time_1,vFonte_1,label="$V_e$")
plt.plot(time_1,vDiodo_1,label="$V_o$")
plt.grid()
plt.legend()
plt.ylabel('tensão [V]')
plt.xlabel('tempo [s]')   
plt.savefig(imgFolder+"E2_vt.png")



plt.figure(1)
plt.plot(time_1,vFunc,label="Transf",marker="o",linestyle="",markersize=1,color="green")
plt.grid()
plt.title("Função de transferência")
plt.ylabel('ganho')
plt.xlabel('tempo [s]')   
plt.savefig(imgFolder+"E2_transf.png")

plt.figure(2)
plt.plot(time_1,vFonte_1,label="$V_e$")
plt.plot(time_1,vDiodo_1,label="$V_o$")
plt.plot(time_1,vFunc,label="Função de transferência",marker="o",linestyle="",markersize=1)
plt.grid()
plt.legend()
plt.ylabel('ganho')
plt.xlabel('tempo [s]')   
plt.savefig(imgFolder+"E2_vt_transf.png")

plt.show()

