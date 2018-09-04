from tkinter import *

window=Tk()

def convert():
    grams = 1000 * float(e1_value.get())
    t1.config(state=NORMAL)
    t1.delete(1.0,END)
    t1.insert(END,grams)
    t1.config(state=DISABLED)
    pd = 2.20462 * float(e1_value.get())
    t2.config(state=NORMAL)
    t2.delete(1.0,END)
    t2.insert(END,pd)
    t2.config(state=DISABLED)
    oz = 35.274 * float(e1_value.get())
    t3.config(state=NORMAL)
    t3.delete(1.0,END)
    t3.insert(END,oz)
    t3.config(state=DISABLED)

#Etiqueta
Label(window,text="Kg").grid(row=0,column=0)

#Cuadro de entrada de texto
e1_value = StringVar()
e1 = Entry(window,textvariable=e1_value).grid(row=0,column=1)

#Boton
Button(window,text="Convert",command=convert).grid(row=0,column=2)

t1 = Text(window,height=1,width=20)
t1.grid(row=1,column=0)
t1.config(state=DISABLED)
t2 = Text(window,height=1,width=20)
t2.grid(row=1,column=1)
t2.config(state=DISABLED)
t3 = Text(window,height=1,width=20)
t3.grid(row=1,column=2)
t3.config(state=DISABLED)

window.mainloop()
