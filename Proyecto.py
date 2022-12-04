import tkinter as tk
from tkinter import *

def borrar():
    texto3.delete("1.0","end")
    create_grid(1)
    c.create_rectangle(0,0,500,500, width=1, fill='white')

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
###############################################################################

root = tk.Tk()
root.geometry("1000x610")
root.title("Arena de dragones Westeros")
c = tk.Canvas(root,bg='#ADADFF')
c.pack(fill=tk.BOTH, expand=True)
c.create_rectangle(0,0,500,500, width=1, fill='white')

Label(c,text="CUADRANTE REPRESENTACIÓN DE CIUDADES", font=("times new roman",15), bg="khaki3",fg="black").place(x=20,y=530)
Label(c,text="Información ciudades", font=("times new roman",9), bg="khaki3",fg="black").grid(padx=550,pady=5)
texto = Text(c,width=50,height=10,background="white")
texto.grid(padx=550,pady=5)
Label(c,text="Código minizinc", font=("times new roman",9), bg="khaki3",fg="black").grid(padx=550,pady=5)
texto3 = Text(c,width=50,height=16,background="white")
texto3.grid(padx=550,pady=3)
Display = Button(c, height = 2,
                 width = 20,
                 text ="Solucionar",
                 command = lambda:Take_input(),font=("times new roman", 12), bg="dimgrey",fg="cornsilk2",bd=0,cursor="hand2").place(x=560,y=510)
Display2 = Button(c, height = 2,
                 width = 20,
                 text ="Borrar",
                 command = lambda:borrar(),font=("times new roman", 12), bg="dimgrey",fg="cornsilk2",bd=0,cursor="hand2").place(x=760,y=510)

root.resizable(0,0)
root.mainloop()
