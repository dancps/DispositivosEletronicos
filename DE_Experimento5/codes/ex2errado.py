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
'''
plt.figure(0)
plt.subplot(211)
plt.plot(time_1,vCh1_1,label="Canal 1")
plt.plot(time_1,vCh2_1,label="Canal 2")
plt.grid()
plt.legend()
plt.xlabel('tempo [s]')   
plt.ylabel('Voltage[V]')
plt.subplot(212)
gain = []
for i in range(0,len(vCh2_1)):
	if((vCh2_1[i]>=-1 and vCh2_1[i]<=1) and (time_1[i]>-0.0001 and time_1[i]<0.000275)):
		gain.append(vCh1_1[i]/vCh2_1[i])
	else:
		gain.append(0)
plt.plot(time_1,gain,label="Ganho")
plt.grid()
plt.legend()
plt.xlabel('tempo [s]')   
plt.ylabel('Ganho')
'''

gain = []
ch2_cut=[]
ch1_cut=[]
t_cut=[]
for i in range(0,len(vCh2_1)):
	if(vCh2_1[i]>0 and (time_1[i]>-0.00016 and time_1[i]<0.000275)):
		t_cut.append(time_1[i])
		ch1_cut.append(vCh1_1[i])
		ch2_cut.append(vCh2_1[i])

plt.figure(0)
plt.subplot(211)
plt.plot(t_cut,ch1_cut,label="Canal 1(corte)",zorder=4)
plt.plot(time_1,vCh1_1,label="Canal 1",zorder=2)
plt.grid()
plt.legend()
plt.xlabel('tempo [s]')   
plt.ylabel('Voltage[V]')

plt.subplot(212)
plt.plot(t_cut,ch2_cut,label="Canal 2(corte)",zorder=3)
plt.plot(time_1,vCh2_1,label="Canal 2",zorder=1)
plt.grid()
plt.legend()
plt.xlabel('tempo [s]')   
plt.ylabel('Voltage[V]')


plt.figure(1)
plt.subplot(211)
plt.plot(t_cut,ch1_cut,label="Canal 1")
plt.plot(t_cut,ch2_cut,label="Canal 2")
plt.grid()
plt.legend()
plt.xlabel('tempo [s]')   
plt.ylabel('Voltage[V]')
plt.subplot(212)

for i in range(0,len(ch2_cut)):
	gain.append(ch1_cut[i]/ch2_cut[i])
plt.plot(t_cut,gain,label="Ganho")
plt.grid()
plt.legend()
plt.xlabel('tempo [s]')   
plt.ylabel('Ganho')
#plt.savefig(imgFolder+"E1_vt_357.png")

plt.show()