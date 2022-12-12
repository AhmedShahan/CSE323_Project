from PySimpleGUI import *

theme("PythonPlus")
theme_background_color("#120f2a")
theme_element_background_color("#120f2a")
theme_element_text_color("##120f2a")
theme_button_color("Black")
theme_input_background_color("white")
theme_input_text_color("Black")
process=["p1","p2","p3","p4","p5"]

frame=[
    [Text("Input Process ID ",size=(15,1),font=("Monotype Corsiva",20)),Combo(values=process, key="processid",size=(20,1))],
    [Text("Input Burst Time ",size=(15,1),font=("Monotype Corsiva",20)),Input(size=(10,1),key="bt",font=("Monotype Corsiva",20))],
    [Text("Input Arrival Time ",size=(15,1),font=("Monotype Corsiva",20)),Input(size=(10,1),key="at",font=("Monotype Corsiva",20))],
]

layout=[
    [Image('static/images/pic.png',size=(700,140))],
    [Text("Algorithm: First Come First Serve", size=(30,1), font=("Monotype Corsiva",25))],
    [Frame("Process Details",frame,title_color="white",size=(300,200),font=("monotype Corsiva",20))],
    [Text("\t"),Button("Add Process Details",key="add",font=("Monotype Corsiva",20))],
]


win=Window("Admin Login",layout,size=(800,550),location=(500,100))


while True:
    event,value=win.read()
    
    if event=="Close" or event==WIN_CLOSED:
        break
    elif event=="add":
        pid=value['processid']
        BT=value['bt']
        AT=value['at']

        if len(pid)==0 or len(BT)==0 or len(AT)==0:
            popup_auto_close("Please Enter Process Details")
        else:
            popup_auto_close("Added")