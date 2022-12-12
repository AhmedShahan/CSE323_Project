from PySimpleGUI import *
import fcfs as fcfs
import math
def fcfsGUI():
    theme("PythonPlus")
    theme_background_color("#120f2a")
    theme_element_background_color("#120f2a")
    theme_element_text_color("##120f2a")
    theme_button_color("Black")
    theme_input_background_color("white")
    theme_input_text_color("Black")

    process=["p1","p2","p3","p4","p5"]
    processDetailes=[]
    added=[]
    frame=[
        [Text("Input Process ID ",size=(15,1),font=("Monotype Corsiva",20)),Combo(values=process, key="processid",size=(20,1))],
        [Text("Input Burst Time ",size=(15,1),font=("Monotype Corsiva",20)),Input(size=(10,1),key="bt",font=("Monotype Corsiva",20))],
        [Text("Input Arrival Time ",size=(15,1),font=("Monotype Corsiva",20)),Input(size=(10,1),key="at",font=("Monotype Corsiva",20))],
    ]
    frame2=[
        [Input(key="pentered")],
    ]
    frame3=[
        [ProgressBar(100,orientation='h',size=(50,3),border_width=4,key="progressBar1", bar_color=("Black","white")),Input(key='value1',size=(5,1))],
        [ProgressBar(100,orientation='h',size=(50,3),border_width=4,key="progressBar2", bar_color=("Black","white")),Input(key='value2',size=(5,1))],
        [ProgressBar(100,orientation='h',size=(50,3),border_width=4,key="progressBar3", bar_color=("Black","white")),Input(key='value3',size=(5,1))],
        [ProgressBar(100,orientation='h',size=(50,3),border_width=4,key="progressBar4", bar_color=("Black","white")),Input(key='value4',size=(5,1))],
        [ProgressBar(100,orientation='h',size=(50,3),border_width=4,key="progressBar5", bar_color=("Black","white")),Input(key='value5',size=(5,1))],
        [Button("Display Progress",key="change")],
    ]
    col1=[
        [Frame("Process Details",frame,title_color="white",size=(300,200),font=("monotype Corsiva",20))],
        [Text("\t"),Button("Add Process Details",key="add",font=("Monotype Corsiva",20))],
        [Frame("Entered Process",frame2,title_color="white",size=(300,200),font=("monotype Corsiva",20))],
    ]
    col2=[
        [Frame("Progress Bar",frame3,title_color="white",size=(700,500),font=("monotype Corsiva",20))],
    ]
    layout=[
        [Image('static/images/pic.png',size=(700,140))],
        [Text("Algorithm: First Come First Serve", size=(30,1), font=("Monotype Corsiva",25))],
        [Column(col1),Column(col2)],
        
    ]
    win=Window("Admin Login",layout,size=(1000,550),location=(300,100))


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
        
        if event=="Close" or event==WIN_CLOSED:
            break
        elif event=="add":
            pid=value['processid']
            BT=value['bt']
            BT=int(BT)
            AT=value['at']
            AT=int(AT)
            def exist():
                for i in added:
                    if i==pid:
                        return True
                    else:
                        return False

            if len(pid)==0 or BT==None or AT==None:
                popup_auto_close("Please Enter Process Details")
            elif exist():
                popup_auto_close("Already exist this process")
            else:
                processDetailes.append((pid,BT,AT))
                added.append(pid)
                popup_auto_close("Added")
                win['pentered'].update(added)
        elif event=="change":
            result=fcfs.algorithm(processDetailes)
            for i in result:
                if (i[0])=='p1':
                    statusvalue1(i[1])
                if (i[0])=='p2':
                    statusvalue2(i[1])
                if (i[0])=='p3':
                    statusvalue3(i[1])
                if (i[0])=='p4':
                    statusvalue4(i[1])
                if (i[0])=='p5':
                    statusvalue5(i[1])
        