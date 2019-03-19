#!/usr/bin/env python3.7
# Esse script corresponde ao primeiro exercício do quarto 
# experimento de Dispositivos eletrônicos.
import sys
sys.path.append("../../Bibliotecas/") 
import ClasseDados as cla
from matplotlib import pyplot as plt


imgFolder = "../img/Exercicio1/"


#######################################################################
##     Item A                                                        ##
#######################################################################
print("Item A: 1 kOhms")
read1 =cla.OsciloscopioCSV("../raw_files/scope_27.csv")

read1.GetNChannels()

# Le os dados salvos no csv
time_1   = read1.GetVoltageArray(0)
vFonte_1 = read1.GetVoltageArray(1)
vDiodo_1 = read1.GetVoltageArray(2)

# Define a resistencia
R = 1.001

plt.figure(0)
plt.plot(time_1,vFonte_1,label="Canal 1")
plt.plot(time_1,vDiodo_1,label="Canal 2")
plt.grid()
plt.legend()
plt.ylabel('tensão [V]')
plt.xlabel('tempo [s]')   

# Aqui é gerada uma curva com cerca de 2 pontos para cada tensao
# Isso ocorre pois sao usados 2 periodos nos graficos acima
rd_1 = cla.ResistanceDiode(R,vFonte_1,vDiodo_1)
curve_1 = rd_1.GetCaracteristicCurve()

plt.figure(1)
plt.plot(curve_1[0],curve_1[1], marker='o',label="Curva caracteristica",linestyle="",markersize=1)
plt.grid()
plt.title("Curva característica do diodo Zenner 1N4733A(sem filtro)")
plt.ylabel('corrente [A]')
plt.xlabel('tensão [V]')   
plt.savefig(imgFolder+"E1_1k_cc.png")

# Para consertar este problema, devemos reduzir a quantidade de dados entre 1 e 2 
plt.figure(2)
plt.plot(time_1,vFonte_1,label="Canal 1")
plt.plot(time_1,vDiodo_1,label="Canal 2")
plt.grid()
plt.ylabel('corrente [A]')
plt.xlabel('tensão [V]')  
# Obtem valores para filtragem 
timeMin,mini=read1.GetMinVoltage(1)
timeMax,maxi=read1.GetMaxVoltage(1)
print("Min: "+str(mini)+" s\nMax: "+str(maxi)+" s")
plt.plot(timeMin,mini, marker='o',label="Min",linestyle="")
plt.plot(timeMax,maxi, marker='o',label="Max",linestyle="")
plt.legend()
plt.savefig(imgFolder+"E1_1k_vt.png")

# Filtragem de resultados
time_1_cut   = []
vFonte_1_cut = []
vDiodo_1_cut = []
for i in range(0,len(time_1)):
	if(time_1[i]>=timeMin and time_1[i]<=timeMax):
		time_1_cut.append(time_1[i])   
		vFonte_1_cut.append(vFonte_1[i]) 
		vDiodo_1_cut.append(vDiodo_1[i]) 

plt.figure(3)
plt.subplot(121)
plt.plot(time_1_cut,vFonte_1_cut,label="Canal 1")
plt.plot(time_1_cut,vDiodo_1_cut,label="Canal 2")
plt.grid()
plt.legend()
plt.ylabel('tensão [V]')
plt.xlabel('tempo [s]')    
plt.subplot(122)
rd = cla.ResistanceDiode(R,vFonte_1_cut,vDiodo_1_cut)
i_1,v_1 = rd.GetCaracteristicCurve()
plt.plot(i_1,v_1, marker='o',label="Curva caracteristica",linestyle="",markersize=1)
plt.grid()
plt.ylabel('corrente [A]')
plt.xlabel('tensão [V]')   

#
plt.figure(4)
plt.plot(time_1_cut,vFonte_1_cut,label="Canal 1")
plt.plot(time_1_cut,vDiodo_1_cut,label="Canal 2")
plt.grid()
plt.legend()
plt.ylabel('tensão [V]')
plt.xlabel('tempo [s]')
plt.savefig(imgFolder+"E1_1k_vt_sample.png")
plt.figure(5)
plt.plot(i_1,v_1, marker='o',label="Curva caracteristica",linestyle="",markersize=1)
plt.grid()
plt.ylabel('corrente [A]')
plt.xlabel('tensão [V]')   
plt.title("Curva característica do diodo Zenner 1N4733A")
plt.savefig(imgFolder+"E1_1k_cc_sample.png")


#######################################################################
##     Item B                                                        ##
#######################################################################
print("\nItem B: 330 Ohms")
read2 =cla.OsciloscopioCSV("../raw_files/scope_29.csv")

read2.GetNChannels()

# Le os dados salvos no csv
time_2   = read2.GetVoltageArray(0)
vFonte_2 = read2.GetVoltageArray(1)
vDiodo_2 = read2.GetVoltageArray(2)

# Define a resistencia
R = 1.001

plt.figure(6)
plt.plot(time_2,vFonte_2,label="Canal 1")
plt.plot(time_2,vDiodo_2,label="Canal 2")
plt.grid()
plt.legend()
plt.ylabel('tensão [V]')
plt.xlabel('tempo [s]')   

# Aqui é gerada uma curva com cerca de 2 pontos para cada tensao
# Isso ocorre pois sao usados 2 periodos nos graficos acima
rd_2 = cla.ResistanceDiode(R,vFonte_2,vDiodo_2)
curve_2 = rd_2.GetCaracteristicCurve()

plt.figure(7)
plt.plot(curve_2[0],curve_2[1], marker='o',label="Curva caracteristica",linestyle="",markersize=1)
plt.grid()
plt.title("Curva característica do diodo Zenner 1N4733A(sem filtro)")
plt.ylabel('corrente [A]')
plt.xlabel('tensão [V]')   
plt.savefig(imgFolder+"E1_330_cc.png")

# Para consertar este problema, devemos reduzir a quantidade de dados entre 1 e 2 
plt.figure(8)
plt.plot(time_2,vFonte_2,label="Canal 1")
plt.plot(time_2,vDiodo_2,label="Canal 2")
plt.grid()
plt.ylabel('corrente [A]')
plt.xlabel('tensão [V]')  
# Obtem valores para filtragem 
timeMin,mini=read2.GetMinVoltage(1)
timeMax,maxi=read2.GetMaxVoltage(1)
print("Min: "+str(mini)+" s\nMax: "+str(maxi)+" s")
plt.plot(timeMin,mini, marker='o',label="Min",linestyle="")
plt.plot(timeMax,maxi, marker='o',label="Max",linestyle="")
plt.legend()
plt.savefig(imgFolder+"E1_330_vt.png")

# Filtragem de resultados
time_2_cut   = []
vFonte_2_cut = []
vDiodo_2_cut = []
for i in range(0,len(time_2)):
	if(time_2[i]>=timeMin and time_2[i]<=timeMax):
		time_2_cut.append(time_2[i])   
		vFonte_2_cut.append(vFonte_2[i]) 
		vDiodo_2_cut.append(vDiodo_2[i]) 

plt.figure(9)
plt.subplot(121)
plt.plot(time_2_cut,vFonte_2_cut,label="Canal 1")
plt.plot(time_2_cut,vDiodo_2_cut,label="Canal 2")
plt.grid()
plt.legend()
plt.ylabel('tensão [V]')
plt.xlabel('tempo [s]')    
plt.subplot(122)
rd_2 = cla.ResistanceDiode(R,vFonte_2_cut,vDiodo_2_cut)
i_2,v_2 = rd_2.GetCaracteristicCurve()
plt.plot(i_2,v_2, marker='o',label="Curva caracteristica",linestyle="",markersize=1)
plt.grid()
plt.ylabel('corrente [A]')
plt.xlabel('tensão [V]')   

#
plt.figure(10)
plt.plot(time_2_cut,vFonte_2_cut,label="Canal 1")
plt.plot(time_2_cut,vDiodo_2_cut,label="Canal 2")
plt.grid()
plt.legend()
plt.ylabel('tensão [V]')
plt.xlabel('tempo [s]')
plt.savefig(imgFolder+"E1_330_vt_sample.png")

plt.figure(11)
plt.plot(i_2,v_2, marker='o',label="Curva caracteristica",linestyle="",markersize=1)
plt.grid()
plt.ylabel('corrente [A]')
plt.xlabel('tensão [V]')   
plt.title("Curva característica do diodo Zenner 1N4733A")
plt.savefig(imgFolder+"E1_330_cc_sample.png")

plt.figure(12)
plt.plot(i_1,v_1, marker='o',label="1k$\Omega$",linestyle="",markersize=1)
plt.plot(i_2,v_2, marker='o',label="330$\Omega$",linestyle="",markersize=1)
plt.grid()
plt.legend()
plt.ylabel('corrente [A]')
plt.xlabel('tensão [V]')   
plt.title("Curva característica do diodo Zenner 1N4733A")
plt.savefig(imgFolder+"E1_330_cc_sample_compare.png")

#plt.show()