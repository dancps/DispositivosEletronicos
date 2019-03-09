#!/usr/bin/env python3.7
import sys
import matplotlib.pyplot as plt

if(len(sys.argv)==1):
    print("Para executar o programa digite como argumento o arquivo csv a \
        ser lido.\n\tExemplo: ./analise.py files/planilha1.csv")
    exit()

for nArgs in range(1,len(sys.argv)):
    print("Reading file: "+sys.argv[nArgs])
    name = sys.argv[nArgs]
    inputCSV = open(sys.argv[nArgs])
    lines=[]
    for line in inputCSV:
        if(len(line.split(",")[0])>3 and len(line.split(",")[1])>3 and len(line.split(",")[2])>3):
            lines.append(line)
            
    x=[]
    v1=[]
    v2=[]

    print("Number of lines: "+str(len(lines)))
    for num_line in range(2,len(lines)):
        x.append(float(lines[num_line].split(",")[0]))
        v1.append(float(lines[num_line].split(",")[1]))
        v2.append(float(lines[num_line].split(",")[2]))

    plt.plot(x, v1, label='Canal 1')
    plt.plot(x, v2, label='Canal 2')

    plt.xlabel('x label')
    plt.ylabel('y label')   

    plt.title("Simple Plot")

    plt.legend()

    #plt.show()
    print("Saving...")
    plt.savefig('img/'+name.strip(".csv").strip("raw_files"))
    plt.clf()
