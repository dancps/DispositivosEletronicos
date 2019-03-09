#!/usr/bin/env python3.7
import sys
import matplotlib.pyplot as plt
import numpy as np

inFile = "raw_files/scope_23.csv"
print("Reading file: "+inFile)
inputCSV = open(inFile)
lines=[]
for line in inputCSV:
    if(len(line.split(",")[0])>3 and len(line.split(",")[1])>3 and len(line.split(",")[2])>3):
        lines.append(line)
        
T=[]
V1=[]
V2=[]

resistence= 9920 #Ohms

I=[]
AVG_V2_ini=0
count_V2_ini=0


v2Max=0
time_v2Max=0
C=[]

print("Number of lines: "+str(len(lines)))
for num_line in range(2,len(lines)):
    t=float(lines[num_line].split(",")[0])
    v1=float(lines[num_line].split(",")[1])
    v2=float(lines[num_line].split(",")[2])
    i = (v1-v2)/resistence
    c = t/(resistence*np.log(1-(v2/0.1)))
    if(v2>v2Max):
        v2Max = v2
        time_v2Max=t

    if(v2>-0.01 and v2<0.01):
        AVG_V2_ini= AVG_V2_ini+v2
        count_V2_ini=count_V2_ini+1

    T.append(t)
    V1.append(v1)
    V2.append(v2)
    I.append(i)
    C.append(c)

plt.figure(0)
plt.plot(T, V1, label='Canal 1')
plt.plot(T, V2, label='Canal 2')
plt.xlabel('tempo [s]')
plt.ylabel('tensão [V]')   
plt.legend()
plt.grid()
plt.plot("Offset: 0V")
plt.savefig('im2/exercicioE_Tensoes')

plt.figure(1)
plt.grid()
plt.plot(T,C,label='Capacitância')
indexC =0
sumC =0
for i in range(0,len(C)):
    sumC = sumC+C[i]
    indexC = indexC+1
print("sumC "+str(sumC))
averageC = sumC/float(indexC)
print("averageC "+str(averageC))
AverageC=[]
for i in range(0,len(C)):
    AverageC.append(averageC)
plt.plot(T,AverageC,label="Média da capacitância(C = {:.2e}F)".format(averageC))
plt.legend()
plt.xlabel('tempo [s]')
plt.ylabel('capcacitância [F]')
plt.savefig('im2/exercicioE_capacitancia')


#plt.show()