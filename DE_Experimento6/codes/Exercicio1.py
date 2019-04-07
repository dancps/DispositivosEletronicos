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
v_be, i_c = read1.GetChannel(0)

for i in range(0,10):
	print(v_be[i],i_c[i])
rIncr=[]
rIncrMed=[]
for i in range(1,len(i_c)):
	rIncr.append((v_be[i]-v_be[i-1])/float(i_c[i]-i_c[i-1]))
	if(v_be[i]>0 and v_be[i]<0.04):
		rIncrMed.append((v_be[i]-v_be[i-1])/float(i_c[i]-i_c[i-1]))

avgRINCR = sum(rIncrMed) / float(len(rIncrMed))

plt.figure(0)
plt.plot(v_be,i_c,label="$V_e$")
plt.grid()
plt.legend()
plt.ylabel('corrente de coletor [A]')
plt.xlabel('tensão [V]')

plt.figure(1)
plt.plot(v_be[1:],rIncr,label="Resistencia Incremental")
plt.plot([0,0.04],[avgRINCR,avgRINCR],label="Resistencia média ($R_m$={:.2f})".format(avgRINCR))
plt.xlim([0,0.042])
plt.ylim([0,300])
plt.grid()
plt.legend()
plt.title("Resistência incremental")
plt.ylabel('resistência [$\Omega$]')
plt.xlabel('tensão [V]')
plt.savefig(imgFolder+"rIncr.png")


read2 =cla.MultisimCSV("../raw_files/DE6_ex1_3_tri.csv")
read2.GetNChannels()

# Le os dados salvos no csv
t_vc2,vc2   = read2.GetChannel(0)
t_vb2,vb2   = read2.GetChannel(1)
t_ve,ve   = read2.GetChannel(2)

print(t_vc2)
gain=[]
for i in range(0,len(t_vc2)):
	gain.append((vc2[i])/float(vb2[i]))


plt.figure(2)
#plt.plot(t_vc2,gain,label="Ganho")
plt.plot(t_vc2,vc2,label="Ganho")
plt.grid()
plt.legend()
plt.ylabel('ganho')
plt.xlabel('tempo [s]')
plt.savefig(imgFolder+"gain.png")



#plt.show()

