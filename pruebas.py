from tkinter import *
from tkinter import ttk
 
root = Tk()
Lb1 = Listbox(root, width=50, height=50)
 
def lista(event):
    print ("..............")
    result=["list1","list2"]
    for rx in result:
        Lb1.insert(END,rx)
    Lb1.pack()
    Lb1.grid(row=3,column=0)
 
def combo(root):
 
    value = StringVar()
    root.title('titulo de mi ventana')
    label1=Label(root,text="Seleccione marca de la impresora")
    label1.grid(row=0,column=0)
 
    #Aki esta mi problema, nose como mandarselo a la def lista()
    box = ttk.Combobox(root, textvariable=value, state='readonly')
 
    box["value"] = ["opcion1","opcion2"]
 
    # aqui generamos el evento cada vez que se selecciona un elemento del combobox
    box.bind("<<ComboboxSelected>>",lista)
 
    box.grid(column=0, row=1)
 
combo(root)
root.mainloop()