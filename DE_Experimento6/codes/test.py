#!/usr/bin/env python3.7
# Esse script corresponde ao primeiro exercício do quarto 
# experimento de Dispositivos eletrônicos.
import sys
sys.path.append("../../Bibliotecas/") 
import ClasseDados as cla
from matplotlib import pyplot as plt


imgFolder = "../Imagens/pyImg/Exercicio1/"


#######################################################################
##     Item A                                                        ##
#######################################################################
read1 =cla.MultisimCSV("../raw_files/DE6_ex1_resIncr_interv0.0001.csv")
read1.GetNChannels()

# Le os dados salvos no csv
v_be,i_c   = read1.GetChannel(0)

for i in range(0,10):
	print(v_be[i],i_c[i])
