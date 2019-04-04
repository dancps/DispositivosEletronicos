#!/usr/bin/env python3.7
# Esse script corresponde ao primeiro exercício do quarto 
# experimento de Dispositivos eletrônicos.
import sys
sys.path.append("../../Bibliotecas/") 
import ClasseDados as cla
from matplotlib import pyplot as plt
import numpy as np


def invert(x):
	for i in range(0,len(x)):
		x[i] = x[i]*(-1)

	return x

imgFolder = "../img/Exercicio2/"

#######################################################################
##                                                                   ##
#######################################################################
print("+++++++++ Item A +++++++++")
#
# 357mV
# 
read_1 = cla.OsciloscopioCSV("../raw_files/scope_17.csv")

read_1.GetNChannels()
# Le os dados salvos no csv
time_1 = read_1.GetVoltageArray(0)
vCh1_1 = read_1.GetVoltageArray(1)
vCh2_1 = read_1.GetVoltageArray(2)
vCh2_1 = invert(vCh2_1)

for i in range(0,len(vCh2_1)):
	time_1[i]=time_1[i]*1000
	vCh2_1[i]=0.57+vCh2_1[i]

plt.figure(0)
plt.subplot(211)
plt.plot(time_1,vCh1_1,label="Canal 1")
plt.plot(time_1,vCh2_1,label="Canal 2",color="orange")
plt.grid()
plt.legend()
plt.xlabel('tempo [ms]')   
plt.ylabel('Voltage[V]')
plt.subplot(212)
gain = []
for i in range(0,len(vCh2_1)):
	gain.append(vCh1_1[i]/vCh2_1[i])
	'''
	if((vCh2_1[i]>=-1 and vCh2_1[i]<=1) and (time_1[i]>-0.0001 and time_1[i]<0.000275)):
		gain.append(vCh1_1[i]/vCh2_1[i])
	else:
		gain.append(0)
	'''
plt.plot(time_1,gain,label="Ganho",color="green")
plt.grid()
plt.legend()
plt.xlabel('tempo [ms]')   
plt.ylabel('Ganho')
plt.savefig(imgFolder+"E2_Gain.png")


plt.figure(1)
plt.subplot(311)
plt.plot(time_1,vCh1_1,label="Canal 1")
plt.grid()
plt.legend()
plt.xlabel('tempo [ms]')   
plt.ylabel('Voltage[V]')

plt.subplot(312)
plt.plot(time_1,vCh2_1,label="Canal 2",color="orange")
plt.grid()
plt.legend()
plt.xlabel('tempo [ms]')   
plt.ylabel('Voltage[V]')
plt.subplot(313)
plt.plot(time_1,gain,label="Ganho",color="green")
plt.grid()
plt.legend()
plt.xlabel('tempo [ms]')   
plt.ylabel('Ganho')
plt.savefig(imgFolder+"E2_GainM.png")

#plt.show()