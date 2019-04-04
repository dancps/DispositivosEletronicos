#!/usr/local/bin/python3.7
import os
import sys

if(len(sys.argv)==1):
	"You must pass a name for the experiment.\nExitting..."
	exit()
elif((len(sys.argv)>2)):
	"You can create only one directory."
	exit()

exp = sys.argv[1]

subfolders = ["codes","Multisim","images","raw_files"]

path = os.getcwd()  
print ("The current working directory is %s" % path)  

print("Creating the experiment: "+exp)
if(os.path.exists(exp)):
	print("The folder ./"+exp+" already exists. Trying to create subfolders.")
else:
	os.mkdir("./"+exp)

print("  Folders:")
for i in subfolders:
	if(os.path.exists("./"+exp+"/"+i)):
		print("    The folder ./"+("./"+exp+"/"+i)+" already exists.")
	else:
		print("    ./"+exp+"/"+i)
		os.mkdir("./"+exp+"/"+i)
