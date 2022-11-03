from PySimpleGUI import *

theme("DarkGreen4")
theme_button_color("black")
theme_input_background_color("white")
theme_input_text_color("#001D3C")

algorithm=["FCFS","SJF","Priority","Round Robin"]

process=[]
layout=[
[Text("Welcome to Schedule Management",font=("Jokerman",40,"underline"),size=(1200,1),justification="c")],
[Text("Select Algorithm: ",font=("Monotype Corsiva",15,"bold"),size=(17,1)),Combo(values=algorithm)],
[Text("Enter Process Details ",font=("Monotype Corsiva",15,"bold","underline"),size=(10,1))],
[Text("Process Name: ",font=("Monotype Corsiva",15,"bold"),size=(10,1)),InputText(key="proc",size=(5,1))],
[Text("Arrivel Time",font=("Monotype Corsiva",15,"bold"),size=(10,1)),InputText(key="at",size=(5,1)),Checkbox("Default: 0",key="default")],
[Text("Burst Time: ",font=("Monotype Corsiva",15,"bold"),size=(10,1)),InputText(key="bt",size=(5,1))],
[Text('\t\t\t'*2),Button("+ADD+",key="addP")],

# [Text("Enter Process ",font=("Monotype Corsiva",15,"bold"),size=(10,1)),Input(key="output",size=(5,1))],





]
doc = Window('Schedule Algorith Checker', size=(1200,750),location=(100,10),return_keyboard_events=True).Layout(layout)

while True:
    event,value=doc.read()
    if event == WIN_CLOSED:
            break
    
    if event=="addP":
        pvalue=value["proc"]
        if len(pvalue)==0:
            popup("Please Enter Process Name")
        else:
            popup("Process Added")
            process.append(pvalue)
            doc['output'].update(process)