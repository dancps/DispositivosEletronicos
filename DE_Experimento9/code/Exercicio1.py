#!/usr/bin/env python3.7
# Esse script corresponde ao primeiro exercício do quarto 
# experimento de Dispositivos eletrônicos.
import sys
sys.path.append("../../Bibliotecas/") 
import ClasseDados as cla
from matplotlib import pyplot as plt


imgFolder = "../images/Exercicio1/"



#######################################################################
##     Item A                                                        ##
#######################################################################
read1 =cla.MultisimCSV("../Multisim/DE9_Ex13_withVe.csv")
read1.GetNChannels()


time_10C_1, vc_10C_1  = read1.GetChannel(0)
time_ve_10C_1, ve_10C_1  = read1.GetChannel(1)
time_27C_1, vc_27C_1  = read1.GetChannel(2)
time_ve_27C_1, ve_27C_1  = read1.GetChannel(3)
time_60C_1, vc_60C_1  = read1.GetChannel(4)
time_ve_60C_1, ve_60C_1  = read1.GetChannel(5)

time_10C_2=[]
vc_10C_2=[]
time_ve_10C_2=[]
ve_10C_2=[]
time_27C_2=[]
vc_27C_2=[]
time_ve_27C_2=[]
ve_27C_2=[]
time_60C_2=[]
vc_60C_2=[]
time_ve_60C_2=[]
ve_60C_2=[]

for i in range(0,len(time_10C_1)):
	if(time_10C_1[i]<=(1./1e3)):
		time_10C_2.append(time_10C_1[i])
		vc_10C_2.append(vc_10C_1[i])
		time_ve_10C_2.append(time_ve_10C_1[i])
		ve_10C_2.append(ve_10C_1[i])
		time_27C_2.append(time_27C_1[i])
		vc_27C_2.append(vc_27C_1[i])
		time_ve_27C_2.append(time_ve_27C_1[i])
		ve_27C_2.append(ve_27C_1[i])
		time_60C_2.append(time_60C_1[i])
		vc_60C_2.append(vc_60C_1[i])
		time_ve_60C_2.append(time_ve_60C_1[i])
		ve_60C_2.append(ve_60C_1[i])


plt.figure(0)
plt.plot(time_10C_1,vc_10C_1,label="10$^o$C")
plt.plot(time_27C_1,vc_27C_1,label="27$^o$C")
plt.plot(time_60C_1,vc_60C_1,label="60$^o$C")
plt.plot(time_ve_10C_1,ve_10C_1,label="Sine wave")
plt.legend()
plt.grid()
plt.savefig(imgFolder+"ex13_waves.png")

plt.figure(5)
sizeOfMarker=3
plt.plot(time_10C_2,vc_10C_2,label="10$^o$C",marker="o",linestyle="",markersize=sizeOfMarker)
plt.plot(time_27C_2,vc_27C_2,label="27$^o$C",marker="o",linestyle="",markersize=sizeOfMarker)
plt.plot(time_60C_2,vc_60C_2,label="60$^o$C",marker="o",linestyle="",markersize=sizeOfMarker)
plt.plot(time_ve_10C_2,ve_10C_2,label="Sine wave",marker="o",linestyle="",markersize=sizeOfMarker)
plt.legend()
plt.grid()

incrGain_10C_1 = []
incrGain_t_10C_1= []
incrGain_27C_1 = []
incrGain_t_27C_1= []
incrGain_60C_1 = []
incrGain_t_60C_1= []
'''
for i in range(0,len(time_10C_1)):
	if((time_10C_1[i]>=((1e-3)*0.475)) and (time_10C_1[i]<=((1e-3)*0.77))):
		incrGain_10C_1.append(float(vc_10C_1[i])/float(abs(ve_10C_1[i])))
		incrGain_t_10C_1.append(time_10C_1[i])
	if((time_27C_1[i]>=((1e-3)*0.75)) and (time_27C_1[i]<=((1e-3)*0.85))):
		incrGain_27C_1.append(float(vc_27C_1[i])/float(abs(ve_27C_1[i])))
		incrGain_t_27C_1.append(time_27C_1[i])
	if((time_60C_1[i]>=((1e-3)*0.75)) and (time_60C_1[i]<=((1e-3)*0.85))):
		incrGain_60C_1.append(float(vc_60C_1[i])/float(abs(ve_60C_1[i])))
		incrGain_t_60C_1.append(time_60C_1[i])
'''
for i in range(1,len(time_10C_1)):
	incrGain_10C_1.append(float(vc_10C_1[i]-vc_10C_1[i-1])/float(-(ve_10C_1[i]-ve_10C_1[i-1])))
	incrGain_t_10C_1.append(time_10C_1[i]-((time_10C_1[i]-time_10C_1[i-1])/2.))
	incrGain_27C_1.append(float(vc_27C_1[i]-vc_27C_1[i-1])/float(-(ve_27C_1[i]-ve_27C_1[i-1])))
	incrGain_t_27C_1.append(time_27C_1[i]-((time_27C_1[i]-time_27C_1[i-1])/2.))
	incrGain_60C_1.append(float(vc_60C_1[i]-vc_60C_1[i-1])/float(-(ve_60C_1[i]-ve_60C_1[i-1])))
	incrGain_t_60C_1.append(time_60C_1[i]-((time_60C_1[i]-time_60C_1[i-1])/2.))
	# incrGain_27C_1.append(float(vc_27C_1[i])/float(abs(ve_27C_1[i])))
	# incrGain_t_27C_1.append(time_27C_1[i])
	# incrGain_60C_1.append(float(vc_60C_1[i])/float(abs(ve_60C_1[i])))
	# incrGain_t_60C_1.append(time_60C_1[i])



plt.figure(1)
plt.title("Ganho incremental")
plt.plot(incrGain_t_10C_1,incrGain_10C_1,label="10$^o$C")
plt.plot(incrGain_t_27C_1,incrGain_27C_1,label="27$^o$C")
plt.plot(incrGain_t_60C_1,incrGain_60C_1,label="60$^o$C")
plt.legend()
plt.grid()
# plt.savefig(imgFolder+"ex13_incrGain.png")



plt.show()