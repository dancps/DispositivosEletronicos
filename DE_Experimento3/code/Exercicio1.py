#!/usr/bin/env python3.7
import sys
sys.path.append("../../Bibliotecas/") 
import ClasseDados as cla
from matplotlib import pyplot as plt

#######################################################################
##     Item A                                                        ##
#######################################################################
print("+++++++++ Item A +++++++++")
read1 = cla.OsciloscopioCSV("../raw_files/scope_14.csv")
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

plt.savefig("../Imagens/Ex1itemA.png")


#######################################################################
##     Item B                                                        ##
#######################################################################
print("+++++++++ Item B +++++++++")
read2 = cla.OsciloscopioCSV("../raw_files/scope_16.csv")
read2.GetNChannels()

# Le os dados salvos no csv
time_2 = read2.GetVoltageArray(0)
v1_2 = read2.GetVoltageArray(1)
v2_2= read2.GetVoltageArray(2)

# Plota e printa os graficos
plt.figure(1)
plt.plot(time_2,v1_2,label="Canal 1")
plt.plot(time_2,v2_2,label="Canal 2")
plt.grid()
plt.legend()
plt.xlabel('tempo [s]')
plt.ylabel('tensão [V]')   

plt.savefig("../Imagens/Ex1itemB.png")


#######################################################################
##     Item C                                                        ##
#######################################################################
print("+++++++++ Item C +++++++++")
read3 = cla.OsciloscopioCSV("../raw_files/scope_18.csv")
read3.GetNChannels()

# Le os dados salvos no csv
time_3 = read3.GetVoltageArray(0)
v1_3 = read3.GetVoltageArray(1)
v2_3= read3.GetVoltageArray(2)

# Plota e printa os graficos
plt.figure(2)
plt.plot(time_3,v1_3,label="Canal 1")
plt.plot(time_3,v2_3,label="Canal 2")
plt.grid()
plt.legend()
plt.xlabel('tempo [s]')
plt.ylabel('tensão [V]')   

plt.savefig("../Imagens/Ex1itemC.png")


#######################################################################
##     comparison                                                    ##
#######################################################################
plt.figure(3)

plt.plot(time_1,v1_1,label="Tensão da fonte")
plt.plot(time_1,v2_1,label="Sinal retificado")

plt.plot(time_2,v2_2,label="Sinal retificado, com capacitor")

plt.plot(time_3,v2_3,label="Sinal retificado, com capacitor e resitor")

plt.grid()
plt.legend()
plt.xlabel('tempo [s]')
plt.ylabel('tensão [V]')   
plt.savefig("../Imagens/Ex1COMPARE.png")

plt.show() 	