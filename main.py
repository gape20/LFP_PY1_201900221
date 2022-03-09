import tkinter as tk
from tkinter import ttk
import os

class interfaz:
    def __init__(self,ventana):
        self.ventana = ventana
        ventana.title("Menú principal")
        ancho_ventana = 800
        alto_ventana = 800

        x_ventana = ventana.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = ventana.winfo_screenheight() // 2 - alto_ventana // 2

        posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
        ventana.geometry(posicion)
        ventana.resizable(0,0)
        
        label1 = tk.Label(ventanaP,text='Menu Principal', font='Helvetica 40 bold', bg='deep pink')
        label1.place(x=10, y=10)

        button1 = tk.Button(ventanaP, text='Analizar', font='Helvetica 20 bold', bg='deep pink')
        button1.place(x=10, y=740)
        button2 = tk.Button(ventanaP, text='Ir', font='Helvetica 20 bold', command= self.ObtenerItem, bg='deep pink')
        button2.place(x=500, y=20)

        self.entrada = tk.StringVar()
        entry1 = tk.Entry(ventanaP, textvariable= self.entrada)
        #entrada.set("hola")
        entry1.place(x=20, y=100, width=750, height=600)

        self.combo1 = ttk.Combobox(ventanaP, state="readonly", font='Helvetica 15 bold')
        self.combo1.place(x=550, y=20, width=220, height=50)
        self.combo1['values']= ('Reporte de Tokens','Reporte de errores','Manual Tecnico', 'Manual de Usuario')
        self.combo1.bind("<<ComboboxSelected>>", lambda _ : texto.config(text=f"Selección '{self.combo1.get()}'"))
        inidice = self.entrada.get()

        texto = tk.Label(ventanaP, text="Selección :")
        texto.place(x=550, y=75, width=220, height=20)
    
    def ObtenerItem(self):
        entrada = self.combo1.get()
        if entrada == 'Reporte de Tokens':
            print('Mostrando Reporte de Tokens...')
            
        elif entrada == 'Reporte de errores':
            print('Mostrando Reporte de errores...')
        elif entrada == 'Manual Tecnico':
            print('Mostrando Manual Tecnico...')
        elif entrada == 'Manual de Usuario':
            print('Mostrando Manual de Usuario...')
            os.system('ManualUsuario.pdf')
        else: 
            print('No ha seleccionado ninguna opcion')

ventanaP = tk.Tk()
menu = interfaz(ventanaP)
ventanaP.configure(bg='light pink')
ventanaP.mainloop()
