from tkinter import *

window=Tk()

def km_to_miles():
    #print(e1_value.get())
    miles=float(e1_value.get())*1.68
    t1.config(state=NORMAL)
    t1.delete(1.0,END)
    t1.insert(END,str(miles)+" "+v.get())
    t1.config(state=DISABLED)

def create_list():
    lista1 = [('joel','24','monclova','tec','inglaterra'),
            ('jose','22','monclova','tec','alemania'),
            ('paloma','22','monterrey','tec','guatemala'),
            ('binny','23','chihuahua','tec','canada')]
    #lista = lista1.get()
    t1.config(state=NORMAL)
    t1.delete(1.0,END)
    t1.insert(END,lista1)
    #t1.insert(END,','.join(lista1[0]))
    t1.config(state=DISABLED)

b1 = Button(window,text="Execute",command=km_to_miles)
b1.grid(row=0,column=0)

lista = StringVar()
b2 = Button(window,text="Execute",command=create_list)
b2.grid(row=2,column=2)

e1_value=StringVar()
e1 =Entry(window,textvariable=e1_value)
e1.grid(row=0,column=1) #,rowspan=2)

t1 = Text(window,height=1,width=20)
t1.grid(row=0,column=2)
t1.config(state=DISABLED)

Label(window,text="Textoo").grid(row=3,column=1)

V = IntVar()
r1 = Radiobutton(window,text="Pinchar aqui",variable=V, value=1)
r1.grid(row=1,column=1)

r2 = Radiobutton(window,text="O pinchar aqui",variable=V, value=2)
r2.grid(row=2,column=1)

listbox = Listbox(window)
listbox.grid(row=1,column=0)

listbox.insert(END, "a list entry")

for item in ["one", "two", "three", "four"]:
    listbox.insert(END, item)


v = StringVar(window)
v.set("one Binny")

o1 = OptionMenu(window, v, "one Binny","two Binny's","three Binny's")
o1.grid(row=1,column=2)

window.mainloop()
