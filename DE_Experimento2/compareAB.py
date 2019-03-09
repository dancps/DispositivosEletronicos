#!/usr/bin/env python3.7
import sys
import matplotlib.pyplot as plt

ExA_T=[]
ExA_V1=[]
ExA_V2=[]
ExA_I=[]

ExB_T=[]
ExB_V1=[]
ExB_V2=[]
ExB_I=[]

resistence= 9920 #Ohms


inFile = "raw_files/scope_5.csv"

print("\nReading file: "+inFile)
inputCSV = open(inFile)
lines=[]
for line in inputCSV:
    if(len(line.split(",")[0])>3 and len(line.split(",")[1])>3 and len(line.split(",")[2])>3):
        lines.append(line)
        

print("Number of lines for exercise A: "+str(len(lines)))
iZero=-9999
MaxValY=0
iMaxValY=0
for num_line in range(2,len(lines)):
    t=float(lines[num_line].split(",")[0])
    v1=float(lines[num_line].split(",")[1])
    v2=float(lines[num_line].split(",")[2])
    if(v1>MaxValY):
        MaxValY = v1
        iMaxValY = num_line
    elif((v1>-0.01 and v1<0.01) and iZero==-9999):
        Zero = v1
        iZero=num_line
    

print("   Zero voltage in channel 1: "+str(Zero))
print("   Index of zero voltage in channel 1: "+str(iZero))
print("   Max value of voltage in channel 1: "+str(MaxValY))
print("   Index of max value of voltage in channel 1: "+str(iMaxValY))

for num_line in range(iZero,iMaxValY+1):
    t =0
    v1=0
    v2=0
    i = 0
    t=float(lines[num_line].split(",")[0])
    v1=float(lines[num_line].split(",")[1])
    v2=float(lines[num_line].split(",")[2])
    i = (v1-v2)/resistence

    ExA_T.append(t)
    ExA_V1.append(v1)
    ExA_V2.append(v2)
    ExA_I.append(i)

inFile = "raw_files/scope_9.csv"

print("Reading file: "+inFile)
inputCSV2 = open(inFile)
lines=[]
for line in inputCSV2:
    if(len(line.split(",")[0])>3 and len(line.split(",")[1])>3 and len(line.split(",")[2])>3):
        lines.append(line)
        

print("Number of lines for exercise A: "+str(len(lines)))
iZero=-9999
MaxValY=0
iMaxValY=0
for num_line in range(2,len(lines)):
    t=float(lines[num_line].split(",")[0])
    v1=float(lines[num_line].split(",")[1])
    v2=float(lines[num_line].split(",")[2])
    if(v1>MaxValY):
        MaxValY = v1
        iMaxValY = num_line
    elif((v1>-0.01 and v1<0.01) and iZero==-9999):
        Zero = v1
        iZero=num_line
    

print("   Zero voltage in channel 1: "+str(Zero))
print("   Index of zero voltage in channel 1: "+str(iZero))
print("   Max value of voltage in channel 1: "+str(MaxValY))
print("   Index of max value of voltage in channel 1: "+str(iMaxValY))

for num_line in range(iZero,iMaxValY+1):
    t =0
    v1=0
    v2=0
    i = 0
    t=float(lines[num_line].split(",")[0])
    v1=float(lines[num_line].split(",")[1])
    v2=float(lines[num_line].split(",")[2])
    i = (v1-v2)/resistence

    ExB_T.append(t)
    ExB_V1.append(v1)
    ExB_V2.append(v2)
    ExB_I.append(i)


plt.figure(0)
plt.subplot(1,2,1)
plt.title("Diodo 1N4007")
plt.plot(ExA_T, ExA_V1, label='Canal 1')
plt.plot(ExA_T, ExA_V2, label='Canal 2')
plt.grid()
plt.xlabel('time')
plt.ylabel('voltage')
plt.legend()   
plt.subplot(1,2,2)
plt.title("Diodo 1N5404")
plt.plot(ExB_T, ExB_V1, label='Canal 1')
plt.plot(ExB_T, ExB_V2, label='Canal 2')
plt.xlabel('time')
plt.ylabel('voltage')
plt.grid()
plt.legend()   
plt.savefig('img/compareAB_Tensoes')


plt.figure(1)
plt.title("Curvas características dos diodos")
plt.plot(ExA_V2, ExA_I, label='Curva caracteristicas(1N4007)')
plt.plot(ExB_V2, ExB_I, label='Curva caracteristica(1N5404)')
plt.ylabel('current')
plt.xlabel('voltage')
plt.legend()
plt.grid()
plt.savefig('img/compareAB_curvaCaracteristica')


print("Saving...")
#plt.savefig('img/'+name.strip(".csv").strip("raw_files"))
plt.show()
