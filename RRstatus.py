from PySimpleGUI import *
import sjf as sjf
import fcfs as fcfs
import time
import math
theme('pythonPlus')
theme_input_background_color("black")
theme_input_text_color("white")

layout=[
    [ProgressBar(100,orientation='h',size=(50,3),border_width=4,key="progressBar1", bar_color=("Black","white")),Input(key='value1',size=(5,1))],
    [ProgressBar(100,orientation='h',size=(50,3),border_width=4,key="progressBar2", bar_color=("Black","white")),Input(key='value2',size=(5,1))],
    [ProgressBar(100,orientation='h',size=(50,3),border_width=4,key="progressBar3", bar_color=("Black","white")),Input(key='value3',size=(5,1))],
    [ProgressBar(100,orientation='h',size=(50,3),border_width=4,key="progressBar4", bar_color=("Black","white")),Input(key='value4',size=(5,1))],
    [ProgressBar(100,orientation='h',size=(50,3),border_width=4,key="progressBar5", bar_color=("Black","white")),Input(key='value5',size=(5,1))],
    [Button("Display Progress",key="change")],
]

win=Window("progress Bar",layout)

#For process 1
def statusvalue1(initial,OBT,duration):
    initialP=math.ceil(((initial/OBT)*100))
    if event=="change":
        val=math.ceil(((duration/OBT)*100))
        for i in range(initialP,val+1):
            time.sleep(0.05)
            win["progressBar1"].update(i)
            win["value1"].update(i)

def statusvalue2(initial,OBT,duration):
    initialP=math.ceil(((initial/OBT)*100))
    if event=="change":
        val=math.ceil(((duration/OBT)*100))
        for i in range(initialP,val+1):
            time.sleep(0.05)
            win["progressBar2"].update(i)
            win["value2"].update(i)
def statusvalue3(initial,OBT,duration):
    initialP=math.ceil(((initial/OBT)*100))
    if event=="change":
        val=math.ceil(((duration/OBT)*100))
        for i in range(initialP,val+1):
            time.sleep(0.05)
            win["progressBar3"].update(i)
            win["value3"].update(i)

def statusvalue4(initial,OBT,duration):
    initialP=math.ceil(((initial/OBT)*100))
    if event=="change":
        val=math.ceil(((duration/OBT)*100))
        for i in range(initialP,val+1):
            time.sleep(0.05)
            win["progressBar4"].update(i)
            win["value4"].update(i)
def statusvalue5(initial,OBT,duration):
    initialP=math.ceil(((initial/OBT)*100))
    if event=="change":
        val=math.ceil(((duration/OBT)*100))
        for i in range(initialP,val+1):
            time.sleep(0.05)
            win["progressBar5"].update(i)
            win["value5"].update(i)

while True:
    event,value=win.read()
    if event=="Exit" or event==WIN_CLOSED:
        break
    bt=[3,5,2,6,6]
    result= [('p2', 2), ('p4', 2), ('p5', 2), ('p1', 2), ('p2', 2), ('p4', 2), ('p5', 2), ('p1', 1), ('p2', 1), ('p4', 2), ('p5', 2)]
    initial1=0
    initial2=0
    initial3=0
    initial4=0
    initial5=0
    for i in result:
        if i[0]=='p1':
            print(i)
            start=initial1
            duration=initial1+i[1]
            statusvalue1(start,bt[0],duration)
            initial1=duration
        elif i[0]=='p2':
            print(i)
            start=initial2
            duration=initial2+i[1]
            statusvalue2(start,bt[1],duration)
            initial2=duration
        elif i[0]=='p3':
            print(i)
            start=initial3
            duration=initial3+i[1]
            statusvalue3(start,bt[2],duration)
            initial3=duration
        elif i[0]=='p4':
            print(i)
            start=initial4
            duration=initial4+i[1]
            statusvalue4(start,bt[3],duration)
            initial4=duration
        elif i[0]=='p5':
            print(i)
            start=initial5
            duration=initial5+i[1]
            statusvalue5(start,bt[4],duration)
            initial5=duration