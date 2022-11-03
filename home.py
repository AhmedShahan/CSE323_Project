from PySimpleGUI import *

theme("DarkGreen4")
theme_button_color("black")
theme_input_background_color("white")
theme_input_text_color("#001D3C")

algorithm=["FCFS","SJF","Priority","Round Robin"]

process=[]
layout=[
[Text("Welcome to Schedule Management",font=("Jokerman",40,"underline"),size=(1200,1),justification="c")],
[Text("Select Algorithm: ",font=("Tomes & New Roma",15,"bold")),Combo(values=algorithm)],
[Text("Enter Process ",font=("Tomes & New Roma",15,"bold")),InputText(key="proc")],
[Button("+ADD+",key="addP")],




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