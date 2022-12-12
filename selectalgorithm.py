from PySimpleGUI import *
theme("PythonPlus")
theme_background_color("#120f2a")
theme_element_background_color("#120f2a")
theme_element_text_color("##120f2a")
theme_button_color("Black")
def selectAlgorithm():
    layout=[
        [Image('static/images/pic.png',size=(700,140))],
        [Text("\n")],
        [Text("\t"*4),Button("First Come First Server",button_color='white on black',key="fcfs", size=(20,1),font=("monotype Corsiva",20))],
        [Text("\t"*4),Button("Serve Job First",key="sjf",button_color='white on black', size=(20,1),font=("monotype Corsiva",20))],
        [Text("\t"*4),Button("Priority Algorithm",key="priority", button_color='white on black',size=(20,1),font=("monotype Corsiva",20))],
        [Text("\t"*4),Button("Round Robin Algorithm",key="rr", button_color='white on black',size=(20,1),font=("monotype Corsiva",20))],
    ]
    win=Window("Select Algorithm",layout,size=(800,550),location=(500,100))
    while True:
        event,value=win.read()
        
        if event=="Close" or event==WIN_CLOSED:
            break
        elif event=="next":
            win.close()