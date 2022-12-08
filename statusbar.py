from PySimpleGUI import *
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
def statusvalue1(bt):
    BT=bt
    if event=="change":
        val=math.ceil(((100/BT)*BT))
        for i in range(BT,val+1):
            time.sleep(0.05)
            win["progressBar1"].update(i)
            win["value1"].update(i)
#process 2
def statusvalue2(bt):
    BT=bt
    if event=="change":
        val=math.ceil(((100/BT)*BT))
        for i in range(BT,val+1):
            time.sleep(0.05)
            win["progressBar2"].update(i)
            win["value2"].update(i)

#process 3
def statusvalue3(bt):
    BT=bt
    if event=="change":
        val=math.ceil(((100/BT)*BT))
        for i in range(BT,val+1):
            time.sleep(0.05)
            win["progressBar3"].update(i)
            win["value3"].update(i)
def statusvalue4(bt):
    BT=bt
    if event=="change":
        val=math.ceil(((100/BT)*BT))
        for i in range(BT,val+1):
            time.sleep(0.05)
            win["progressBar4"].update(i)
            win["value4"].update(i)
def statusvalue5(bt):
    BT=bt
    if event=="change":
        val=math.ceil(((100/BT)*BT))
        for i in range(BT,val+1):
            time.sleep(0.05)
            win["progressBar5"].update(i)
            win["value5"].update(i)

while True:
    event,value=win.read()
    if event=="Exit" or event==WIN_CLOSED:
        break

    result=fcfs.algorithm()
    for i in result:
        if (i[0])=='1':
            statusvalue1(i[1])
        if (i[0])=='2':
            statusvalue2(i[1])
        if (i[0])=='3':
            statusvalue3(i[1])
        if (i[0])=='4':
            statusvalue4(i[1])
        if (i[0])=='5':
            statusvalue5(i[1])



    

