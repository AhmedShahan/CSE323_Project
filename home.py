from PySimpleGUI import *

theme("Pythonplus")
theme_button_color("black")
theme_input_background_color("white")
theme_input_text_color("#001D3C")

algorithm=["FCFS","SJF","Priority","Round Robin"]
processname=['P1','P2','P3','P4','P5']
col=[
[Text("Select Algorithm: ",font=("Monotype Corsiva",15,"bold"),size=(12,1)),Combo(values=algorithm)],
[Text("Enter Process Details ",font=("Monotype Corsiva",15,"bold","underline"),size=(10,1))],
[Text("Process Name: ",font=("Monotype Corsiva",15,"bold"),size=(10,1)),Combo(values=processname,key="proc")],

[Text("Arrivel Time",font=("Monotype Corsiva",15,"bold"),size=(10,1)),InputText(key="at",size=(5,1)),Checkbox("Default: 0",key="default")],
[Text("Burst Time: ",font=("Monotype Corsiva",15,"bold"),size=(10,1)),InputText(key="bt",size=(5,1))],
[Text('\t'),Button("+ADD+",key="addP")],
]


layout=[
[Text("Welcome to Schedule Management",font=("Jokerman",30,"underline"),size=(1200,1),justification="c")],

[Column(col)],


[Text("Entered Process:  ",font=("Monotype Corsiva",15,"bold")),Input(key="output")],
[Button("Submit",key='submit')]


]
doc = Window('Schedule Algorith Checker', size=(750,500),location=(100,10),return_keyboard_events=True).Layout(layout)

process=[]
while True:
    event,value=doc.read()
    if event == WIN_CLOSED:
            break
    
    if event=="addP":
        pvalue=value["proc"]
        if len(pvalue)==0:
            popup("Please Enter Process Name")
        else:
            process.append(pvalue)
            doc['output'].update(process)
    if event=="submit":
        print(value)