import PySimpleGUI as pg
from selectalgorithm import selectAlgorithm
close = 'static/images/close.png'
next = 'static/images/next.png'
pg.theme("PythonPlus")
pg.theme_background_color("#120f2a")
pg.theme_element_background_color("#120f2a")
pg.theme_element_text_color("##120f2a")

frame=[    
    [
        pg.Image('static/images/shaan3.png'),
        pg.Text("Shahan Ahmed\nDepartment of Electrical & Computer Engineer.\nMajor Computer Science & Enineering\nEmail:shahan.ahmed@northsouth.edu\n",
                size=(50,4),justification="left",font=("monotype Corsiva",15),background_color="#120f2a"),
    ], 
    [pg.Text("=====================================================================",background_color="black")],
    [
        
        pg.Image('static/images/afsara.png'),
        pg.Text("Afsara Waziha\nDepartment of Electrical & Computer Engineer.\nMajor Computer Science & Enineering\nEmail:afsara.waziha@northsouth.edu",
                size=(50,4),justification="left",font=("monotype Corsiva",15),background_color="#120f2a"),
    ], 
    [pg.Text("=====================================================================",background_color="black")],
    [
        pg.Image('static/images/shaan3.png'),
        pg.Text("Shahan Ahmed\nDepartment of Electrical & Computer Engineer.\nMajor Computer Science & Enineering\nEmail:shahan.ahmed@northsouth.edu\n",
                size=(50,4),justification="left",font=("monotype Corsiva",15),background_color="#120f2a"),
    ],  
]
layout=[
    
    [
        pg.Image('static/images/pic.png',size=(700,140)),
    ],
    # [pg.Text("",background_color="#120f2a")],
    [
    pg.Frame("Developed By",frame,title_color="white",size=(500,400),font=("monotype Corsiva",20)),
    pg.Text("\t",background_color="#120f2a"),
    pg.ReadFormButton('', button_color="#120f2a",image_filename=close, image_size=(45, 45), image_subsample=2, border_width=0,key="Close"),
    pg.ReadFormButton('', button_color="#120f2a",image_filename=next, image_size=(115,45), image_subsample=2, border_width=0,key="next")
    ],
]

win=pg.Window("Admin Login",layout,size=(800,600),location=(400,100))


while True:
    event,value=win.read()
    
    if event=="Close" or event==pg.WIN_CLOSED:
        break
    elif event=="next":
        win.close()
        selectAlgorithm()

