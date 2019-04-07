#!/usr/bin/env python3.7
# Esse script corresponde ao primeiro exercício do quarto 
# experimento de Dispositivos eletrônicos.
import sys
sys.path.append("../../Bibliotecas/") 
import ClasseDados as cla
from matplotlib import pyplot as plt


imgFolder = "../Imagens/pyImg/Exercicio3/"


#######################################################################
##     Item A                                                        ##
#######################################################################
read1 =cla.MultisimCSV("../raw_files/DE6_ex3_3Sweep5754.csv")

read1.GetNChannels()

# Le os dados salvos no csv
vdd_1,ic_1   = read1.GetChannel(0)


plt.figure(0)
plt.subplot(121)
plt.plot(vdd_1,ic_1,label="$I_{C_{Q3}}$",linestyle="",marker="o",markersize="2")
plt.grid()
plt.legend()
plt.ylabel('$I_C$ [A]')
plt.xlabel('$V_{dd}$ [V]')
#plt.savefig(imgFolder+"DE7_ex13_compare.png")

plt.show()

