import os
import sys
import subprocess

scenes = [fl for fl in os.listdir("scenes") if ".blend" in fl]
annotations = [fl for fl in os.listdir("annotations") if ".data" in fl]

total = 0
for name in annotations:
    file = open("annotations/" + name, 'r')
    data = file.readlines()
    print (len(data))
    total += len(data)

print ("\n\n", total)