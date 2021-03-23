from tkinter import *
import mysql.connector
from tkinter import messagebox
import mariadb
from pymysql import *
import xlwt
import pandas.io.sql as sql
import re

raiz = Tk()
raiz.title("Ejercicio Desafío")
raiz.geometry("617x190")
raiz.resizable(0, 0)
miframe = Frame(raiz)
miframe.pack(expand=True, fill="both")
miframe.config(bg="#2a8d90", bd=5, relief="groove")
# raiz.iconbitmap(r"icon_utn.ico")
# crea base si no existe


def create_db():
    try:
        mydb = mysql.connector.connect(
            host="localhost", user="root", password="")
        mycursor = mydb.cursor()
        mycursor.execute("CREATE DATABASE mb_pottery")
        mydb = mysql.connector.connect(
            host="localhost", user="root", password="", database="mb_pottery"
        )
        mycursor = mydb.cursor()
        mycursor.execute(
            "CREATE TABLE alumnos( id int(11) NOT NULL PRIMARY KEY AUTO_INCREMENT, apellido VARCHAR(128) COLLATE utf8_spanish2_ci NOT NULL, nombre varchar(128) COLLATE utf8_spanish2_ci NOT NULL, edad int COLLATE utf8_spanish2_ci NOT NULL )"
        )
        print("Base de datos con tabla creada")
    except:
        print("Ya existe la base de datos")


def myconnection():
    mydb = mysql.connector.connect(
        host="localhost", user="root", password="", database="mb_pottery"
    )
    return mydb


def limpiar():
    cuadrotexto.delete(0, END)
    cuadrotexto1.delete(0, END)
    cuadrotexto2.delete(0, END)
    cuadrotexto3.delete(0, END)


def salir():
    raiz.destroy()


def alta():
    try:
        create_db()
        print("Nueva alta de datos")
        mydb = myconnection()
        print(mydb)
        mycursor = mydb.cursor()
        sql = "INSERT INTO alumnos (apellido, nombre, edad ) VALUES (%s, %s, %s)"
        x = cuadrotexto.get()
        y = cuadrotexto1.get()
        z = int(cuadrotexto2.get())
        print("acabas de presionar ALTA")
        print(x, y, z)
        datos = (x, y, z)
        mycursor.execute(sql, datos)
        mydb.commit()
        messagebox.showinfo("AVISO", "Hi! sos un genio.")
        print(x, y, z)
        cuadrotexto.delete(0, END)
        cuadrotexto1.delete(0, END)
        cuadrotexto2.delete(0, END)
    except Exception:
        print("ocurrio un error... VER INGRESO DE TIPO DE DATO")


def lista():
    mydb = myconnection()
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM alumnos")
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)
    # exportar a un excel
    con = connect(user="root", password="admin",
                  host="localhost", database="mb_pottery")
    # read the data
    df = sql.read_sql("select * from alumnos", con)
    # print the data
    print(df)
    # export the data into the excel sheet
    df.to_excel("lista_alumnos.xls")


c0 = StringVar()
c1 = StringVar()
c2 = StringVar()
c3 = StringVar()
listar = []


def mostrar():
    # messagebox.showinfo('AVISO', 'ingresa un apellido')
    mydb = myconnection()
    mycursor = mydb.cursor()
    print("el campo ID es ", cuadrotexto3.get())
    # Gracias por la info!!!!
    mycursor.execute("SELECT * FROM alumnos WHERE id = '" +
                     cuadrotexto3.get() + "'")
    myresult = mycursor.fetchall()
    print("myresult que es ? ", myresult)
    for x in myresult:
        c0.set(x[0])
        listar.append(x[0])
        c1.set(x[1])
        listar.append(x[1])
        c2.set(x[2])
        listar.append(x[2])
        c3.set(int(x[3]))
        listar.append(x[3])
        print("imprimo la tupla:", x)
        print(type(x))

    # return c1, c2, c3
usuario = mostrar
print("el alumno es:", usuario)

# modificar registro
# c1=StringVar()


def actualiza():
    mydb = myconnection()
    mycursor = mydb.cursor()
    sql = (
        "UPDATE alumnos SET apellido='"
        + cuadrotexto.get()
        + "', nombre='"
        + cuadrotexto1.get()
        + "', edad='"
        + cuadrotexto2.get()
        + "' WHERE id = '"
        + cuadrotexto3.get()
        + "'"
    )
    mycursor.execute(sql)
    mydb.commit()
    messagebox.showinfo("AVISO", "actualizaste un registro")
    print(mycursor.rowcount, "record(s) affected")


def eliminar():
    mydb = myconnection()
    mycursor = mydb.cursor()
    sql = "DELETE FROM alumnos WHERE apellido = '" + cuadrotexto.get() + "'"
    try:
        mycursor.execute(sql)
        mydb.commit()
        messagebox.showinfo("AVISO", "Eliminaste un registro")
        limpiar()
    except:
        mydb.rollback()
        messagebox.showinfo("AVISO", "NO Borraste...la pifiaste en algo")
        mydb.close()

label = Label(
    miframe,
    text="      Ingrese sus datos      ",
    bg="black",
    font=("Helvetica", 14, "bold"),
    fg="#39ff14",
)
label.grid(row=0, columnspan=6, padx=5, pady=5, ipadx=30)

# campo1
nombrelabel = Label(miframe, text="Apellido")
nombrelabel.grid(row=1, column=0, sticky="w", padx=6, pady=6)
cuadrotexto = Entry(miframe, textvariable=c1)
cuadrotexto.focus()
cuadrotexto.grid(row=1, column=1, padx=6, pady=6, ipady=2)


# campo2
text = "      Ingrese sus datos      ",
bg = "black",
nombrelabel1 = Label(miframe, text="Nombre")
nombrelabel1.grid(row=2, column=0, padx=6, pady=6, sticky="w")
cuadrotexto1 = Entry(miframe, textvariable=c2)
cuadrotexto1.grid(row=2, column=1, padx=6, pady=6, ipady=2)


# campo3
nombrelabel2 = Label(miframe, text="Edad")
nombrelabel2.grid(row=3, column=0, padx=6, pady=6, sticky="w")
cuadrotexto2 = Entry(miframe, textvariable=c3)
cuadrotexto2.grid(row=3, column=1, padx=6, pady=6, ipady=2)

# campo4
nombrelabel3 = Label(miframe, text="Id")
nombrelabel3.grid(row=1, column=2, padx=6, pady=6, ipadx=10)
cuadrotexto3 = Entry(miframe)
cuadrotexto3.grid(row=1, column=3, padx=6, pady=6, ipady=2, ipadx=0)

# boton alta
botonalta = Button(miframe, borderwidth=5,
                   text="Alta Registro", command=lambda: alta())
botonalta.grid(row=4, column=0, padx=6, pady=6)

# boton listar
botonlistar = Button(miframe, borderwidth=5,
                     text="Listar", command=lambda: lista())
botonlistar.grid(row=4, column=1, padx=6, pady=6, sticky="ew")

# boton mostrar registro
botonmostrar = Button(miframe, borderwidth=5,
                      text="Mostrar", command=lambda: mostrar())
botonmostrar.grid(row=4, column=2, padx=6, pady=6, ipadx=10, sticky="ew")

# boton selecionar un registro y hacer un update
botonactualizar = Button(
    miframe, borderwidth=5, text="Actualizar", command=lambda: actualiza()
)
botonactualizar.grid(row=4, column=3, padx=6, pady=6, ipadx=8, sticky="w")

# boton selecionar un registro y eliminarte
botonborrar = Button(
    miframe, text="Eliminar", borderwidth=5, command=lambda: eliminar()
)
botonborrar.grid(row=4, column=4, padx=3, pady=6, sticky="w", ipadx=10)
mydb.rollback()
            messagebox.showinfo("AVISO", "NO Borraste...la pifiaste en algo")
            
# boton selecionar un registro y eliminarte
botonsalir = Button(miframe, borderwidth=5, text="Salir",
                    command=lambda: salir())
botonsalir.grid(row=4, column=5, padx=0, pady=6, sticky="w", ipadx=10)

raiz.mainloop()
