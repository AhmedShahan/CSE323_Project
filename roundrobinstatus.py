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
    print("Initial",initial)
    print("Duration",duration)
    initialP=math.ceil(((initial/OBT)*100))
    if event=="change":
        val=math.ceil(((duration/OBT)*100))
        for i in range(initialP,val+1):
            time.sleep(0.05)
            win["progressBar1"].update(i)
            win["value1"].update(i)

# [('p1',0,2),('p2',0,2),('p1',2,2),('p2',2,1)]
# statusvalue1(i[1],bt[0],i[2])
#process 2
def statusvalue2(initial,OBT,duration):
    initialP=math.ceil(((initial/OBT)*100))
    if event=="change":
        val=math.ceil(((duration/OBT)*100))
        for i in range(initialP,val+1):
            time.sleep(0.05)
            win["progressBar2"].update(i)
            win["value2"].update(i)
            
            

# #process 3
# def statusvalue3(initial,OBT,duration):
#     if event=="change":

#         count=int((initial/OBT)*100)
#         val=math.ceil(((duration/OBT)*100))
#         for i in range(count,val+1):
#             time.sleep(0.05)
#             win["progressBar3"].update(i)
#             win["value3"].update(i)
        

# def statusvalue4(initial,OBT,duration):
#     if event=="change":
#         count=int((initial/OBT)*100)
#         val=math.ceil(((duration/OBT)*100))
#         for i in range(count,val+1):
#             time.sleep(0.05)
#             win["progressBar4"].update(i)
#             win["value4"].update(i)
            

# def statusvalue5(initial,OBT,duration):
#     if event=="change":
#         count=int((initial/OBT)*100)
#         val=math.ceil(((duration/OBT)*100))
#         for i in range(count,val+1):
#             time.sleep(0.05)
#             win["progressBar5"].update(i)
#             win["value5"].update(i)

while True:
    event,value=win.read()
    if event=="Exit" or event==WIN_CLOSED:
        break
    bt=[8,5]
    result= [('p1',0,2),('p2',0,2),('p1',2,2),('p2',2,2),('p2',4,1),('p1',4,2),('p1',6,2)]
    for i in result:
        # print(i)
        start=i[1]
        start=int(start)
        if i[0]=='p1':
            duration=i[1]+i[2]
            #print(duration)
            statusvalue1(start,bt[0],duration)
            print(start)
            start=start+duration
            print(start)
        if i[0]=='p2':
            duration=i[1]+i[2]
            #print(duration)
            statusvalue2(start,bt[1],duration)
            print(start)
            start=start+duration
            print(start)
        # if i[0]=='p3':
        #     statusvalue3(i[1],bt[0],i[2])
        # if i[0]=='p4':
        #     statusvalue4(i[1],bt[0],i[2])
        # if i[0]=='p5':
        #     statusvalue5(i[1],bt[0],i[2])