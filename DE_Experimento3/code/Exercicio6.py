#!/usr/bin/env python3.7
import sys
sys.path.append("../../Bibliotecas/") 
import ClasseDados as cla
from matplotlib import pyplot as plt

#######################################################################
##     Item A                                                        ##
#######################################################################
print("+++++++++ Item A +++++++++")
read1 = cla.OsciloscopioCSV("../raw_files/scope_52.csv")
read1.GetNChannels()

# Le os dados salvos no csv
time_1 = read1.GetVoltageArray(0)
v1_1 = read1.GetVoltageArray(1)
v2_1= read1.GetVoltageArray(2)

# Plota e printa os graficos
plt.figure(0)
plt.plot(time_1,v1_1,label="Canal 1")
plt.plot(time_1,v2_1,label="Canal 2")
plt.title("1N4007")
plt.grid()
plt.legend()
plt.xlabel('tempo [s]')
plt.ylabel('tensão [V]')   

plt.savefig("../Imagens/Ex6_1N4007.png")

#######################################################################
##     Item B                                                       ##
#######################################################################
print("+++++++++ Item B +++++++++")
read2 = cla.OsciloscopioCSV("../raw_files/scope_54.csv")
read2.GetNChannels()

# Le os dados salvos no csv
time_2 = read2.GetVoltageArray(0)
v1_2 = read2.GetVoltageArray(1)
v2_2= read2.GetVoltageArray(2)

# Plota e printa os graficos
plt.figure(1)
plt.plot(time_2,v1_2,label="Canal 1")
plt.plot(time_2,v2_2,label="Canal 2")
plt.title("1N4148")
plt.grid()
plt.legend()
plt.xlabel('tempo [s]')
plt.ylabel('tensão [V]')
 

plt.savefig("../Imagens/Ex6_1N4148.png")


#######################################################################
##     Item Compare 1N4007                                                        ##
#######################################################################
print("+++++++++ Item 1N4007 +++++++++")

# Plota e printa os graficos
plt.figure(2)
plt.title("1N4007")
plt.plot(time_1,v1_1,label="Canal 1")
plt.plot(time_1,v2_1,label="Canal 2")
ymed_1=read1.GetAverage(2,0.,0.0005)
plt.plot([plt.xlim()[0],plt.xlim()[1]],[ymed_1,ymed_1], label="Tensão média({:.3f}V)".format(ymed_1))
plt.grid()
plt.legend()
plt.xlabel('tempo [s]')
plt.ylabel('tensão [V]')   

plt.savefig("../Imagens/Ex6_1N4007_Comp.png")


plt.figure(3)
plt.title("1N4007")
resistance=9930.
i_1=[]
for i in range(0,len(v2_1)):
	i_1.append((v1_1[i]-v2_1[i])/resistance)
plt.plot(time_1,i_1,label="Corrente")
plt.grid()
plt.legend()
plt.xlabel('tempo [s]')
plt.ylabel('corrente [A]')   
plt.savefig("../Imagens/Ex6_1N4007_Comp2.png")
#######################################################################
##     Item Compare 1N4148                                                       ##
#######################################################################
print("+++++++++ Item 1N4148 +++++++++")

# Plota e printa os graficos
plt.figure(4)
plt.title("1N4148")
plt.plot(time_2,v1_2,label="Canal 1")
plt.plot(time_2,v2_2,label="Canal 2")
ymed_2=read2.GetAverage(2,0.,0.0005)
plt.plot([plt.xlim()[0],plt.xlim()[1]],[ymed_2,ymed_2], label="Tensão média({:.3f}V)".format(ymed_2))
plt.grid()
plt.legend()
plt.xlabel('tempo [s]')
plt.ylabel('tensão [V]')
plt.savefig("../Imagens/Ex6_1N4148_Comp.png")

plt.figure(5)
plt.title("1N4148")
resistance=9930.
i_1=[]
for i in range(0,len(v2_1)):
	i_1.append((v1_1[i]-v2_1[i])/resistance)
plt.plot(time_1,i_1,label="Corrente")
plt.grid()
plt.legend()
plt.xlabel('tempo [s]')
plt.ylabel('corrente [A]')  
plt.savefig("../Imagens/Ex6_1N4148_Comp2.png")



plt.show() 	