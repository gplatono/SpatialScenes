import os
import sys
import subprocess

scenes = [fl for fl in os.listdir("scenes") if ".blend" in fl]
annotations = [fl for fl in os.listdir("annotations") if ".data" in fl]

def train(epochs):
    scene_idx = 0
    for epoch in range(epochs):
        scene = scenes[scene_idx]
        name = scene.split(".blend")[0] + '.data'
        if name in annotations and (name in ['RW201.data','RW202.data','RW203.data','RW204.data','RW205.data','RW206.data',
            'RW207.data','RW208.data','RW209.data','RW210.data']):
            command = ['/Applications/Blender.app/Contents/MacOS/Blender', "scenes" + os.sep + scene, '--background', '-P',
                       'testLabel2.py', '--',"annotations" + os.sep + name]
            #command = ['C:\\Program Files\\Blender Foundation\\Blender 2.90\\blender.exe', "scenes" + os.sep + scene, '--background', '-P',
            #           'testLabel2.py', '--', "annotations" + os.sep + name]
            #command = ['../blender/blender', "scenes" + os.sep + scene, '--background', '-P',
            #           'testLabel2.py', '--', "annotations" + os.sep + name]
            subprocess.run(command)

        scene_idx += 1

if __name__ == '__main__':
    train(len(scenes))

