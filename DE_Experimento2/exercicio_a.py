#!/usr/bin/env python3.7
import sys
import matplotlib.pyplot as plt

inFile = "raw_files/scope_5.csv"

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

print("Number of lines: "+str(len(lines)))
for num_line in range(2,len(lines)):
    t=float(lines[num_line].split(",")[0])
    v1=float(lines[num_line].split(",")[1])
    v2=float(lines[num_line].split(",")[2])
    i = (v1-v2)/resistence

    T.append(t)
    V1.append(v1)
    V2.append(v2)
    I.append(i)

plt.figure(0)
plt.plot(T, V1, label='Canal 1')
plt.plot(T, V2, label='Canal 2')
plt.xlabel('tempo [s]')
plt.ylabel('tensão [V]')   

plt.legend()
plt.grid()
plt.savefig('img/exercicioA_Tensoes')

plt.figure(1)
plt.plot(V2, I, label='Curva característica')

plt.ylabel('corrente [A]')
plt.xlabel('tensão [V]')   
plt.grid()

plt.title("Diodo 1N4007")

plt.legend()

print("Saving...")
plt.savefig('img/exercicioA_curvaCaracteristica')
plt.show()
