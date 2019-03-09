#!/usr/bin/env python3.7
import sys
sys.path.append("../../Bibliotecas/") 
import ClasseDados as cla
from matplotlib import pyplot as plt

#######################################################################
##     Item A                                                        ##
#######################################################################
print("+++++++++ Item A +++++++++")
read1 = cla.OsciloscopioCSV("../raw_files/scope_22.csv")
read1.GetNChannels()

# Le os dados salvos no csv
time_1 = read1.GetVoltageArray(0)
v1_1 = read1.GetVoltageArray(1)
v2_1= read1.GetVoltageArray(2)

# Plota e printa os graficos
plt.figure(0)
plt.plot(time_1,v1_1,label="Canal 1")
plt.plot(time_1,v2_1,label="Canal 2")
plt.grid()
plt.legend()
plt.xlabel('tempo [s]')
plt.ylabel('tensão [V]')   

plt.savefig("../Imagens/Ex2itemA.png")


plt.show() 	