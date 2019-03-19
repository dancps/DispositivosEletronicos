#!/usr/bin/env python3.7
# Esse script corresponde ao primeiro exercício do quarto 
# experimento de Dispositivos eletrônicos.
import sys
sys.path.append("../../Bibliotecas/") 
import ClasseDados as cla
from matplotlib import pyplot as plt
import numpy as np


imgFolder = "../img/Exercicio3/"


#######################################################################
##     Item A                                                        ##
#######################################################################
print("+++++++++ Item A +++++++++")
read_1 =cla.OsciloscopioCSV("../raw_files/scope_19.csv")

read_1.GetNChannels()

# Le os dados salvos no csv
time_1   = read_1.GetVoltageArray(0)
vFonte_1 = read_1.GetVoltageArray(1)
vDiodo_1 = read_1.GetVoltageArray(2)

plt.figure(0)
plt.plot(time_1,vFonte_1,label="$V_e$")
plt.plot(time_1,vDiodo_1,label="$V_o$")
plt.grid()
plt.legend()
plt.ylabel('tensão [V]')
plt.xlabel('tempo [s]')   
plt.savefig(imgFolder+"E3_vt.png")

V_total= 1.5
RH1=1.8
RH2=1.0
RH3=1.5
sumRH=RH1+RH2+RH3
V_RH1=(RH1/sumRH)*V_total
V_RH2=(RH2/sumRH)*V_total
V_RH3=(RH3/sumRH)*V_total
V_Node1=V_RH3
V_Node2=V_RH3+V_RH2
print("Voltage in the resistors:")
print("The voltage in the 1st reisistor is {:.2f} V".format(V_RH1))
print("The voltage in the 2nd reisistor is {:.2f} V".format(V_RH2))
print("The voltage in the 3rd reisistor is {:.2f} V".format(V_RH3))
print("Resulting in a sum of :"+str(V_RH1+V_RH3+V_RH2))
print("So the levels are:")
print("Node1:"+str(V_Node1))
print("Node2:"+str(V_Node2))

plt.figure(6)
plt.plot(time_1,vFonte_1,label="$V_e$")
plt.plot(time_1,vDiodo_1,label="$V_o$")
'''
interval = 1e-9
result=[]
while(len(result)<1 and interval<(0.3/5000.)):
	for i in range(0,len(vFonte_1)):
		if(vFonte_1[i]>=V_Node2-interval and vFonte_1[i]<=V_Node2+interval):
			plt.plot(time_1[i],V_Node2,markerstyle="o",markersize=2)
			print("Plotted")
	interval=interval*10
'''
plt.plot([min(time_1),max(time_1)],[V_Node1,V_Node1],label="Break point 1")
plt.plot([min(time_1),max(time_1)],[V_Node2,V_Node2],label="Break point 2")
plt.plot([min(time_1),max(time_1)],[-V_Node1,-V_Node1],label="Negative break point 1")
plt.plot([min(time_1),max(time_1)],[-V_Node2,-V_Node2],label="Negative break point 2")
#plt.plot(read_1.GetTime(2,V_Node2),V_Node2,label="Break point 2")
plt.grid()
plt.legend()
plt.ylabel('tensão [V]')
plt.xlabel('tempo [s]')   
plt.savefig(imgFolder+"E3_vt_brLine.png")

# Esse link ajudou muito: http://www.kennethkuhn.com/students/ee431/piecewise_linear_circuits.pdf


#######################################################################
##     Item B                                                        ##
#######################################################################
print("+++++++++ Item B +++++++++")
read_2 =cla.OsciloscopioCSV("../raw_files/scope_21.csv")
read_2_fft =cla.OsciloscopioCSV("../raw_files/scope_21_fft.csv")

read_2.GetNChannels()
read_2_fft.GetNChannels()

# Le os dados salvos no csv
time_2   = read_2.GetVoltageArray(0)
vFonte_2 = read_2.GetVoltageArray(1)

# Le os dados da FFT
freq_2   = read_2_fft.GetVoltageArray(0)
vdBv_2 = read_2_fft.GetVoltageArray(1)


plt.figure(2)
plt.plot(time_2,vFonte_2,label="$V_e$")
plt.grid()
plt.legend()
plt.ylabel('tensão [V]')
plt.xlabel('tempo [s]')   

plt.figure(3)
#plt.subplot(121)
maxFreq,maxdB=read_2_fft.GetMaxVoltage(1)
plt.plot(freq_2,vdBv_2,label="FFT")
plt.plot(maxFreq,maxdB,marker="o",linestyle="",label="Max({:.1f},{:.1f})".format(maxFreq,maxdB))
plt.grid()
plt.legend()
plt.title("Fast Fourier Transform")
plt.ylabel('intensidade [dBv]')
plt.xlabel('frequência [Hz]') 
plt.savefig(imgFolder+"E3_fft.png")


plt.figure(9)
#plt.subplot(122)
fftSig = abs(np.fft.fft(vFonte_2))#/len(vFonte_2)~
T = time_2[2]-time_2[1]
df=1/T
freqs = np.fft.fftfreq(len(vFonte_2))*len(vFonte_2)*df
maxim= max(fftSig)
for i in range(0,len(fftSig)):
	fftSig[i]=20.*np.log10(fftSig[i]/maxim)
plt.plot(freqs,fftSig)
plt.grid()
plt.legend()
plt.title("Fast Fourier Transform")
plt.ylabel('intensidade [dBv]')
plt.xlabel('frequência [Hz]') 


#######################################################################
##     Item A                                                        ##
#######################################################################
print("+++++++++ Item C +++++++++")
read_3 =cla.OsciloscopioCSV("../raw_files/scope_23.csv")

read_3.GetNChannels()

# Le os dados salvos no csv
time_3   = read_3.GetVoltageArray(0)
vFonte_3 = read_3.GetVoltageArray(1)
vDiodo_3 = read_3.GetVoltageArray(2)

plt.figure(4)
plt.plot(time_3,vFonte_3,label="$V_e$")
plt.plot(time_3,vDiodo_3,label="$V_o$")
plt.grid()
plt.legend()
plt.ylabel('tensão [V]')
plt.xlabel('tempo [s]')   



#######################################################################
##     Item A                                                        ##
#######################################################################
print("+++++++++ Item D +++++++++")
read_4 =cla.OsciloscopioCSV("../raw_files/scope_25.csv")

read_4.GetNChannels()

# Le os dados salvos no csv
time_4   = read_4.GetVoltageArray(0)
vFonte_4 = read_4.GetVoltageArray(1)
vDiodo_4 = read_4.GetVoltageArray(2)

plt.figure(5)
plt.plot(time_4,vFonte_4,label="$V_e$")
plt.plot(time_4,vDiodo_4,label="$V_o$")
plt.grid()
plt.legend()
plt.ylabel('tensão [V]')
plt.xlabel('tempo [s]')   
plt.show()