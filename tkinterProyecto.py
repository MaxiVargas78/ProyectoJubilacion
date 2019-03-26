from tkinter import *

raiz=Tk()
raiz.title("Simulador de Pensiones")

	
raiz.config(bg="white")
miframe=Frame()
miframe.pack()
miframe.pack(fill="both",expand="True")
miframe.config(bg="#56d6df")



cuadronombre=Entry(miframe)
cuadronombre.grid(row=1,column=1,padx=20 , pady=10,columnspan=2)
cuadronombre.config(justify="center")

cuadroedad=Entry(miframe)
cuadroedad.grid(row=2,column=1,padx=20,pady=10,columnspan=2)
cuadroedad.config(justify="center")


mujer=Checkbutton(miframe, text="Femenino", bg="#56d6df", onvalue=1, offvalue=0)
mujer.grid(row=3,column=1,sticky="w")
mujer.config(justify="center")

hombre=Checkbutton(miframe, text="Masculino", bg="#56d6df", onvalue=1, offvalue=0)
hombre.grid(row=3,column=2,sticky="w")
hombre.config(justify="center")


##########LABEL##############################

txtsimuladordepensiones=Label(miframe, text="SIMULADOR DE PENSIONES",bg="#56d6df", padx=20, pady=20, font=(20))
txtsimuladordepensiones.grid(row=0, columnspan=3)


txtnombre=Label(miframe, text="Nombre:",bg="#56d6df", padx=10,pady=10)
txtnombre.grid(row=1,column=0)

txtedad=Label(miframe, text="Edad:",bg="#56d6df", padx=10,pady=10)
txtedad.grid(row=2,column=0)

txtsexo=Label(miframe, text="Seleccione su sexo", bg="#56d6df", padx=10, pady=10)
txtsexo.grid(row=3,column=0)

txtahorro=Label(miframe, text="Ahorro acumulado en cuenta obligatoria:" , bg="#56d6df", padx=10, pady=10)
txtahorro.grid(row=5,column=0)

txtsueldo=Label(miframe, text="Sueldo promedio($):",bg="#56d6df", padx=10,pady=10)
txtsueldo.grid(row=6,column=0)

txtcotvol=Label(miframe, text="Ingrese su cotizacion voluntaria(%):", bg="#56d6df", padx=10, pady=10)
txtcotvol.grid(row=7,column=0)

txtfondo=Label(miframe, text="Seleccione su fondo:",bg="#56d6df", padx=10,pady=10)
txtfondo.grid(row=9,column=0)




def datos():
	x=txtedad.get
	result.config(text="Su pension estimada sera de "+str(x)+"$")

calculo=Button(miframe, text="Calcular", padx=20, pady=10,command=datos)
calculo.grid(row=12, columnspan=2)
result=Label(miframe,bg="#56d6df", padx=10,pady=10)
result.grid(row=13,columnspan=2)
#txtfondo=Label(miframe, text="hola").place(x=50, y=80)

raiz.mainloop() 