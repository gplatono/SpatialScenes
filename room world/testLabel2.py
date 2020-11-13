import bpy
import sys
import os

filepath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, filepath)

datapath = sys.argv[-1]
fname = datapath.split(os.sep)[-1]

objlist = [obj.name.lower() for obj in bpy.context.scene.objects if obj.get('main') is not None and obj.get('enabled') is None]

def test():
    with open(datapath, "r") as f:
        flag = 0
        lines = f.readlines()
        annotations = [line.split(":") for line in lines if line.strip() != ""]
        for i, ele in enumerate(annotations):
            if len(ele) != 3:
                if len(ele) != 4 or ele[1] != 'between':
                    print("Colon separation error found in line " + str(i+1))
                    print(ele)
                    print(fname + '\n')
                    flag = 1
        if flag == 1:
            return
        print('colon number correct \n')

        for i, ele in enumerate(annotations):
            if len(ele) != 3:
                if len(ele) != 4 or ele[1] != 'between':
                    print("error")
            for idx in range(len(ele)):
                if idx != 1:
                    if ele[idx].strip().lower() not in objlist:
                        print('Following obj does not exist: ' + ele[idx].lower())
                        print('Found in line ' + str(i+1))
                        print(fname + '\n')

    print('annotations check finished')

test()