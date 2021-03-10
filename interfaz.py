from tkinter import *
from tkinter import ttk
import mysql.connector
ventana = Tk()

ventana.title("Desafio nivel inicial")

titulo = Label(ventana, text="Formulario de Inscripacion")
docu = Label(ventana, text="Doc. N° ")
mail = Label(ventana, text="Email ")
contra = Label(ventana, text="Contraseña ")
repe_contra = Label(ventana, text="Repetir Contraseña ")
phone = Label(ventana, text="Telefono ")
enviar = Button(ventana, text="Enviar")
salir = Button(ventana, text="Salir")
docu_entry = Entry(ventana, width=15, justify=CENTER)
mail_entry = Entry(ventana, width=15, justify=CENTER)
contra_entry = Entry(ventana, width=15, justify=CENTER)
repe_contra_entry = Entry(ventana, width=15, justify=CENTER)
phone_entry = Entry(ventana, width=15, justify=CENTER)


titulo.grid(row=0, column=0, columnspan=2)
docu.grid(row=1, column=0, padx=5, pady=5)
mail.grid(row=2, column=0, padx=5, pady=5)
contra.grid(row=3, column=0, padx=5, pady=5)
repe_contra.grid(row=4, column=0, padx=5, pady=5)
phone.grid(row=5, column=0, padx=5, pady=5)
enviar.grid(row=6, column=1, padx=5, pady=5)
salir.grid(row=6, column=2, padx=5, pady=5)
docu_entry.grid(row=1, column=1, padx=5, pady=5)
mail_entry.grid(row=2, column=1, padx=5, pady=5)
contra_entry.grid(row=3, column=1, padx=5, pady=5)
repe_contra_entry.grid(row=4, column=1, padx=5, pady=5)
phone_entry.grid(row=5, column=1, padx=5, pady=5)



ventana.mainloop()
