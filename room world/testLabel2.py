import bpy
import sys
import os

filepath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, filepath)

datapath = sys.argv[-1]
fname = datapath.split(os.sep)[-1]

objlist = [obj.name.lower() for obj in bpy.context.scene.objects if obj.get('main') is not None and obj.get('enabled') is None]

rel_to_label = {'on': 14, 'supported by': 14, 'to the left of': 1, 'left of': 1, 'to the right of': 2, 'right of': 2, 'above': 3,
			'below': 4, 'in front of': 5, 'behind': 6, 'over': 7, 'under': 8, 'underneath': 8, 'in': 9, 'inside': 9,
			'touching': 10, 'touch': 10, 'at': 11, 'next to': 11, 'between': 12, 'in between': 12, 'near': 13, 'on top of': 14, 'beside': 15,
			'besides': 15, 'facing': 16, 'to the left of d': 1,'to the left of i': 1, 'to the right of d': 2,'to the right of i': 2,
            'in front of d': 5, 'in front of i': 5}

def test():
    with open(datapath, "r") as f:
        flag = 0
        objtypo = 0
        lines = f.readlines()
        annotations = [line.split(":") for line in lines if line.strip() != ""]
        for i, ele in enumerate(annotations):
            for j in range(len(ele)):
                ele[j] = ele[j].strip().lower()
                ele[1] = ele[1].replace('not ', '')
            if ele[1] not in rel_to_label.keys():
                print('Relation Matching Error: ' + ele[1])
                print('Found in line ' + str(i+1))
                print(fname + '\n')
        for i, ele in enumerate(annotations):
            if len(ele) != 3:
                if len(ele) != 4 or rel_to_label[ele[1]] != 12:
                    print("Colon separation error found in line " + str(i+1))
                    print(ele)
                    print(fname + '\n')
                    flag = 1
        if flag == 1:
            return
        print('colon number correct \n')

        for i, ele in enumerate(annotations):
            for idx in range(len(ele)):
                if idx != 1:
                    if ele[idx].strip().lower() not in objlist:
                        objtypo = 1
                        print('Following obj does not exist: ' + ele[idx].lower())
                        print('Found in line ' + str(i+1))
                        print(fname + '\n')

    if objtypo == 1:
        print(objlist)
    print('annotations check finished')

test()