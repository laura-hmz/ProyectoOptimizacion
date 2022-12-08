import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

def borrar():
    texto3.delete("1.0","end")
    create_grid(1)
    c.create_rectangle(0,0,500,500, width=1, fill='steelblue')

def Take_input():
    global modificar,pulir,bandera,cont1,cont2,variablefinal
    INPUT = texto.get("1.0", "end-1c")
    modificar = INPUT.replace('\n',' ')
    pulir = modificar.split(' ')
    bandera=1
    vector_aux2= []
    todas_lasx=[]
    todas_lasy=[]
    variable=''
    variable3=''
    variablefinal=''
    z=0
    for i in pulir:
        if i != '': 
            vector_aux2.append(i)
    while(bandera<len(vector_aux2)):
        if bandera%3 == 0 and bandera > 2:
             pintar_pos(int(vector_aux2[bandera]),int(vector_aux2[bandera+1]),500/int(vector_aux2[0]))
             todas_lasx.append(vector_aux2[bandera])
             todas_lasy.append(vector_aux2[bandera+1])
        bandera+=1
    while(z<len(todas_lasx)):
        variable+=(f"abs(x-{todas_lasx[z]})+abs(y-{todas_lasy[z]})+")  
        variable3+=(f"constraint x!={todas_lasx[z]} \/ y!={todas_lasy[z]};\n") 
        z+=1

    variablefinal=variable[:-1]
    create_grid(int(vector_aux2[0]))
    V1='var int: x; \nvar int: y; \nvar float: z;\n'
    V2='\nsolve minimize z;\n'
    V3=(f"constraint x>=0;\nconstraint y>=0;\nconstraint x<{vector_aux2[0]};\nconstraint y<{vector_aux2[0]};")
    V4='output["X=",show(x),"Y=",show(y)];'
    texto3.insert("1.0",f"{V1}\nconstraint z={variablefinal};\n{V2}\n{variable3}\n{V3}\n{V4}")

#funcion que se utiliza para pintar la ciudades
def  pintar_pos(x,y,tamano_matriz):
    tamano_cuadricula=500/tamano_matriz
    moversex=(x)*tamano_matriz
    moversey=(tamano_cuadricula-1-y)*tamano_matriz
    c.create_rectangle(moversex,moversey,moversex+tamano_matriz, moversey+tamano_matriz, width=1, fill='#030504')

#se dibuja el tablero nxn
def create_grid(z):
    c.delete('grid_line') 
    tamano = 500
    tamano_matriz =tamano/z
    i = 0
    n = 0
    # crea lineas veritcales
    while n<tamano:
        n = tamano_matriz*i
        c.create_line([(n,0), (n, tamano)], tag='grid_line')
        i=i+1
    # crea lineas horizontales
    i = 0
    n = 0
    while n<tamano:
        n = tamano_matriz*i
        c.create_line([(0, n), (tamano, n)], tag='grid_line')
        i=i+1
#####################################Interfazzzzzzzz##########################################

root = tk.Tk()
root.geometry("1020x600")
root.title("Arena de dragones Westeros")
bg=ImageTk.PhotoImage(file="dragon.jpg")


frame = Frame(root, width=1020, height=600, bd=1,bg='#ADADFF')
frame.pack()
Label(frame,image=bg).place(x=0,y=0,relwidth=1,relheight=1)

Label(frame,text="REPRESENTACIÓN DE CIUDADES", font=("times new roman",15), bg="khaki3",fg="black",width=45).place(x=500,y=21)

iframe5 = Frame(frame, bd=2,bg='blue') #Donde se pintan las ciudades
iframe5.place(x=500,y=50,width=500, height=500)

c = tk.Canvas(iframe5,bg='#464D43')
c.pack(fill=tk.BOTH, expand=True)
c.create_rectangle(0,0,500,500, width=1, fill='steelblue' )

Label(frame,text="INGRESE LA INFORMACIÓN DE LAS CIUDADES", font=("times new roman",9),bg="khaki3", fg="black",width=57).place(x=20,y= 30)

texto = Text(frame,width=50,height=10,background="white")
texto.place(x=20,y=50)

Label(frame,text="CÓDIGO GENERADO PARA MINIZINC", font=("times new roman",9), bg="khaki3",fg="black",width=57).place(x=20,y=280)

texto3 = Text(frame,width=50,height=15,background="white")
texto3.place(x=20,y=300)

boton1 = Button(frame, height = 1,
                 width = 15,
                 text ="Iniciar",
                 command = lambda:Take_input(),font=("times new roman", 12), bg="green",fg="cornsilk2",bd=0,cursor="hand2").place(x=60,y=230)

boton2 = Button(frame, height = 1,
                 width = 15,
                 text ="Limpiar resultados",
                 command = lambda:borrar(),font=("times new roman", 12), bg="dimgrey",fg="cornsilk2",bd=0,cursor="hand2").place(x=240,y=230)

root.resizable(0,0)
root.mainloop()
