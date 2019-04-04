#!/usr/bin/env python3.7
# Esse script corresponde ao primeiro exercício do quarto 
# experimento de Dispositivos eletrônicos.
import sys
sys.path.append("../../Bibliotecas/") 
import ClasseDados as cla
from matplotlib import pyplot as plt
import numpy as np


imgFolder = "../img/Exercicio1/"

def invert(x):
	for i in range(0,len(x)):
		x[i] = x[i]*(-1)

	return x

def current(x):
	for i in range(0,len(x)):
		x[i] = x[i]/(1000.)

	return x


#######################################################################
##                                                                   ##
#######################################################################
print("+++++++++ Item A +++++++++")
#
# 357mV
# 
read_1 = cla.OsciloscopioCSV("../raw_files/scope_1.csv")

read_1.GetNChannels()

# Le os dados salvos no csv
time_1 = read_1.GetVoltageArray(0)
vCh1_1 = read_1.GetVoltageArray(1)
vCh2_1 = read_1.GetVoltageArray(2)
vCh2_1 = invert(vCh2_1)

# 
# 601mV
# 
read_2 = cla.OsciloscopioCSV("../raw_files/scope_9.csv")
read_2.GetNChannels()

# Le os dados salvos no csv
time_2 = read_2.GetVoltageArray(0)
vCh1_2 = read_2.GetVoltageArray(1)
vCh2_2 = read_2.GetVoltageArray(2)
vCh2_2 = invert(vCh2_2)

# 
# 621mV
# 
read_3 = cla.OsciloscopioCSV("../raw_files/scope_3.csv")
read_3.GetNChannels()

# Le os dados salvos no csv
time_3 = read_3.GetVoltageArray(0)
vCh1_3 = read_3.GetVoltageArray(1)
vCh2_3 = read_3.GetVoltageArray(2)
vCh2_3 = invert(vCh2_3)

# 
# 640mV
# 
read_4 = cla.OsciloscopioCSV("../raw_files/scope_5.csv")
read_4.GetNChannels()

# Le os dados salvos no csv
time_4 = read_4.GetVoltageArray(0)
vCh1_4 = read_4.GetVoltageArray(1)
vCh2_4 = read_4.GetVoltageArray(2)
vCh2_4 = invert(vCh2_4)


# 
# 665mV
# 
read_5 = cla.OsciloscopioCSV("../raw_files/scope_7.csv")
read_5.GetNChannels()

# Le os dados salvos no csv
time_5 = read_5.GetVoltageArray(0)
vCh1_5 = read_5.GetVoltageArray(1)
vCh2_5 = read_5.GetVoltageArray(2)
vCh2_5 = invert(vCh2_5)

plt.figure(0)
plt.plot(vCh2_2,vCh1_2,label="601mV",marker="o",linestyle="-",zorder=3)
plt.plot(vCh2_3,vCh1_3,label="621mV",marker="o",linestyle="-",zorder=1)
plt.plot(vCh2_4,vCh1_4,label="640mV",marker="o",linestyle="-",zorder=2)
plt.xlim(-2,3)
plt.grid()
plt.legend()
plt.xlabel('-Ch2 [V]')   
plt.ylabel('Ch1 [V]')
plt.savefig(imgFolder+"E1_Lissajous.png")

iCh1_2=current(vCh1_2)
iCh1_3=current(vCh1_3)
iCh1_4=current(vCh1_4)

plt.figure(7)

plt.plot(vCh2_2,iCh1_2,label="601mV",marker="o",linestyle="-",zorder=3)
plt.plot(vCh2_3,iCh1_3,label="621mV",marker="o",linestyle="-",zorder=1)
plt.plot(vCh2_4,iCh1_4,label="640mV",marker="o",linestyle="-",zorder=2)
plt.grid()
plt.legend()
plt.title("Curva característica IxV")
plt.xlabel('-Ch2 [V]')   
plt.ylabel('corrente [A]')
plt.savefig(imgFolder+"E1_LissajousIV.png")

plt.figure(1)
plt.plot(time_1,vCh1_1,label="Canal 1")
plt.plot(time_1,vCh2_1,label="-Canal 2")
plt.grid()
plt.legend()
plt.title("357mV")
plt.xlabel('tempo [s]')   
plt.ylabel('Voltage[V]')
plt.savefig(imgFolder+"E1_vt_357.png")

plt.figure(2)
plt.plot(time_2,vCh1_2,label="Canal 1")
plt.plot(time_2,vCh2_2,label="-Canal 2")
plt.grid()
plt.legend()
plt.title("601mV")
plt.xlabel('tempo [s]')   
plt.ylabel('Voltage[V]')
plt.savefig(imgFolder+"E1_vt_601.png")

plt.figure(3)
plt.plot(time_3,vCh1_3,label="Canal 1")
plt.plot(time_3,vCh2_3,label="-Canal 2")
plt.grid()
plt.legend()
plt.title("621mV")
plt.xlabel('tempo [s]')   
plt.ylabel('Voltage[V]')
plt.savefig(imgFolder+"E1_vt_621.png")

plt.figure(4)
plt.plot(time_4,vCh1_4,label="Canal 1")
plt.plot(time_4,vCh2_4,label="-Canal 2")
plt.grid()
plt.legend()
plt.title("640mV")
plt.xlabel('tempo [s]')   
plt.ylabel('Voltage[V]')
plt.savefig(imgFolder+"E1_vt_640.png")

plt.figure(5)
plt.plot(time_5,vCh1_5,label="Canal 1")
plt.plot(time_5,vCh2_5,label="-Canal 2")
plt.grid()
plt.legend()
plt.title("665mV")
plt.xlabel('tempo [s]')   
plt.ylabel('Voltage[V]')
plt.savefig(imgFolder+"E1_vt_665.png")



plt.figure(6)
plt.plot(vCh1_1,vCh2_1,label="357mV",marker="o",linestyle="-")
plt.plot(vCh1_5,vCh2_5,label="665mV",marker="o",linestyle="-")
plt.grid()
plt.legend()
plt.xlabel('-Ch2 [V]')   
plt.ylabel('Ch1[V]')
plt.savefig(imgFolder+"E1_LissajousERR.png")




#plt.show()