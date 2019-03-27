from tkinter import *
import random
raiz=Tk()

raiz.title("PREVISION JUBILACION")
raiz.resizable(1,1)
#raiz.iconbitmap("afp.icon")
raiz.geometry("900x720")
raiz.config(bg="red")

sexom=BooleanVar()
sexof=BooleanVar()
a1=BooleanVar()
b1=BooleanVar()
c1=BooleanVar()
d1=BooleanVar()
e1=BooleanVar()
def datos():
	por=float(cuadrocotvol.get())
	nombre=cuadronombre.get()
	a2=a1.get()
	b2=b1.get()
	c2=c1.get()
	d2=d1.get()
	e2=e1.get()
	z=0
	aa=int(cuadroahorro.get())
	##################################### FONDO A ##################################
	if a2 is True:
		
		edad=int(cuadroedad.get())
		sex=sexom.get()
		sex1=sexof.get()
		Sueldo=int(cuadrosueldo.get())
		if sex is True:
			x=Sueldo*0.1
			t=(Sueldo/100)*por
			for i in range(0,(65-edad)*12):
				z=z+x
				z=z+z*random.uniform(0.004,0.0043)
				z=z+t
			z=int(z)+aa
			result.config(text=nombre+" Su ahorro total sera de  $"+str(int(z))+ "pesos"+ "." +" Su pension mensual sera de  $" +str(int((z/20)/12))+" pesos.")
		if sex1 is True:
			x=Sueldo*0.1
			t=(Sueldo/100)*por
			for i in range(0,(60-edad)*12):
				z=z+x
				z=z+z*random.uniform(0.004,0.0043)
				z=z+t
			z=int(z)+aa
			result.config(text=nombre+" Su ahorro total sera de  $"+str(int(z))+ "pesos"+ "." +" Su pension mensual sera de  $" +str(int((z/30)/12))+" pesos.")
			##################FONDO B #############################################################33
	if b2 is True:
		
		edad=int(cuadroedad.get())
		sex=sexom.get()
		sex1=sexof.get()
		Sueldo=int(cuadrosueldo.get())
		if sex is True:
			x=Sueldo*0.1
			t=(Sueldo/100)*por
			for i in range(0,(65-edad)*12):
				z=z+x
				z=z+z*random.uniform(0.004,0.0043)
				z=z+t
			z=int(z)+aa
			result.config(text=nombre+" Su ahorro total sera de  $"+str(int(z))+ " pesos"+ "." +" Su pension mensual sera de  $" +str(int((z/20)/12))+" pesos.")
		if sex1 is True:
			x=Sueldo*0.1
			t=(Sueldo/100)*por
			for i in range(0,(60-edad)*12):
				z=z+x
				z=z+z*random.uniform(0.004,0.0043)
				z=z+t
			z=int(z)+aa
			result.config(text=nombre+" Su ahorro total sera de  $"+str(int(z))+ " pesos"+ "." +" Su pension mensual sera de  $" +str(int((z/30)/12))+" pesos.")
			######################################### FONDO C ##############################################
	if c2 is True:
		
		edad=int(cuadroedad.get())
		sex=sexom.get()
		sex1=sexof.get()
		Sueldo=int(cuadrosueldo.get())
		if sex is True:
			x=Sueldo*0.1
			t=(Sueldo/100)*por
			for i in range(0,(65-edad)*12):
				z=z+x
				z=z+z*random.uniform(0.004,0.0043)
				z=z+t
			z=int(z)+aa
			result.config(text=nombre+" Su ahorro total sera de  $"+str(int(z))+ " pesos"+ "." +" Su pension mensual sera de  $" +str(int((z/20)/12))+" pesos.")
		if sex1 is True:
			x=Sueldo*0.1
			t=(Sueldo/100)*por
			for i in range(0,(60-edad)*12):
				z=z+x
				z=z+z*random.uniform(0.004,0.0043)
				z=z+t
			z=int(z)+aa
			result.config(text=nombre+" Su ahorro total sera de  $"+str(int(z))+ " pesos"+ "." +" Su pension mensual sera de  $" +str(int((z/30)/12))+" pesos.")
				############################################## FONDO D#######################################
	if d2 is True:
		
		edad=int(cuadroedad.get())
		sex=sexom.get()
		sex1=sexof.get()
		Sueldo=int(cuadrosueldo.get())
		if sex is True:
			x=Sueldo*0.1
			t=(Sueldo/100)*por
			for i in range(0,(65-edad)*12):
				z=z+x
				z=z+z*random.uniform(0.004,0.0043)
				z=z+t
			z=int(z)+aa
			result.config(text=nombre+" Su ahorro total sera de  $"+str(int(z))+ " pesos"+ "." +" Su pension mensual sera de  $" +str(int((z/20)/12))+" pesos.")
		if sex1 is True:
			x=Sueldo*0.1
			t=(Sueldo/100)*por
			for i in range(0,(60-edad)*12):
				z=z+x
				z=z+z*random.uniform(0.004,0.0043)
				z=z+t
			z=int(z)+aa
			result.config(text=nombre+" Su ahorro total sera de  $"+str(int(z))+ " pesos"+ "." +" Su pension mensual sera de  $" +str(int((z/30)/12))+" pesos.")
			#################################### FONDO E ###########################################
	if e2 is True:
		
		edad=int(cuadroedad.get())
		sex=sexom.get()
		sex1=sexof.get()
		Sueldo=int(cuadrosueldo.get())
		if sex is True:
			x=Sueldo*0.1
			t=(Sueldo/100)*por
			for i in range(0,(65-edad)*12):
				z=z+x
				z=z+z*random.uniform(0.004,0.0043)
				z=z+t
			z=int(z)+aa
			result.config(text=nombre+" Su ahorro total sera de  $"+str(int(z))+ " pesos"+ "." +" Su pension mensual sera de  $" +str(int((z/20)/12))+" pesos.")
		if sex1 is True:
			x=Sueldo*0.1
			t=(Sueldo/100)*por
			for i in range(0,(60-edad)*12):
				z=z+x
				z=z+z*random.uniform(0.004,0.0043)
				z=z+t
			z=int(z)+aa
			result.config(text=nombre+" Su ahorro total sera de  $"+str(int(z))+ " pesos"+ "." +" Su pension mensual sera de  $" +str(int((z/30)/12))+" pesos.")
raiz.config(bg="white")
miframe=Frame(raiz, width=500, height=400)
miframe.pack()
miframe.pack(fill="both",expand="True")
miframe.config(bg="#2da2ab")

##########CUADROS DE TEXTO#############################


cuadronombre=Entry(miframe)
cuadronombre.grid(row=1,column=1,padx=20 , pady=10,columnspan=2)
cuadronombre.config(justify="center")

cuadroedad=Entry(miframe)
cuadroedad.grid(row=2,column=1,padx=20,pady=10,columnspan=2)
cuadroedad.config(justify="center")

###########SEXOS##################################

mujer=Checkbutton(miframe, text="Femenino", bg="#2da2ab", onvalue=1, offvalue=0,var=sexof)
mujer.grid(row=3,column=1,sticky="w")
mujer.config(justify="center")

hombre=Checkbutton(miframe, text="Masculino", bg="#2da2ab", onvalue=1, offvalue=0,var=sexom)
hombre.grid(row=3,column=2,sticky="w")
hombre.config(justify="center")

##################################################

cuadroahorro=Entry(miframe)
cuadroahorro.grid(row=5,column=1,padx=20,pady=10,columnspan=2)
cuadroahorro.config(justify="center")

cuadrosueldo=Entry(miframe)
cuadrosueldo.grid(row=6,column=1,padx=20,pady=10,columnspan=2)
cuadrosueldo.config(justify="center")

cuadrocotvol=Entry(miframe)
cuadrocotvol.grid(row=7,column=1,padx=20,pady=10,columnspan=2)
cuadrocotvol.config(justify="center")



##########FONDOS####################################

A=Checkbutton(miframe, text="Fondo A", bg="#2da2ab", onvalue=1, offvalue=0,var=a1)
A.grid(row=8,column=1,sticky="w")
A.config(justify="center")

B=Checkbutton(miframe, text="Fondo B", bg="#2da2ab", onvalue=1, offvalue=0,var=b1)
B.grid(row=9,column=1,sticky="w")
B.config(justify="center")

C=Checkbutton(miframe, text="Fondo C", bg="#2da2ab", onvalue=1, offvalue=0,var=c1)
C.grid(row=10,column=1,sticky="w")
C.config(justify="center")

D=Checkbutton(miframe, text="Fondo D", bg="#2da2ab", onvalue=1, offvalue=0,var=d1)
D.grid(row=8,column=2,sticky="w")
D.config(justify="center")

E=Checkbutton(miframe, text="Fondo E", bg="#2da2ab", onvalue=1, offvalue=0,var=e1)
E.grid(row=9,column=2,sticky="w")
E.config(justify="center")

##########LABEL##############################

Titulotexto=Label(miframe, text="CALCULADORA FONDOS DE JUBILACION",fg="white",font=("Comic Sans MS", 18), bg="#2da2ab", padx=20, pady=20)
Titulotexto.grid(row=0, columnspan=3,sticky="e")


txtnombre=Label(miframe, text="Nombre:",bg="#2da2ab", padx=10,pady=10)
txtnombre.grid(row=1,column=0,sticky="w")

txtedad=Label(miframe, text="Edad:",bg="#2da2ab", padx=10,pady=10)
txtedad.grid(row=2,column=0,sticky="w")

txtsexo=Label(miframe, text="Seleccione su sexo", bg="#2da2ab", padx=10, pady=10)
txtsexo.grid(row=3,column=0,sticky="w")

txtahorro=Label(miframe, text="Ahorro acumulado en cuenta obligatoria:" , bg="#2da2ab", padx=10, pady=10)
txtahorro.grid(row=5,column=0,sticky="w")

Sueldo=Label(miframe, text="Sueldo promedio($):",bg="#2da2ab", padx=10,pady=10)
Sueldo.grid(row=6,column=0,sticky="w")

txtcotvol=Label(miframe, text="Ingrese su cotizacion voluntaria(%):", bg="#2da2ab", padx=10, pady=10)
txtcotvol.grid(row=7,column=0,sticky="w")

txtfondo=Label(miframe, text="Seleccione su fondo:",bg="#2da2ab", padx=10,pady=10)
txtfondo.grid(row=9,column=0,sticky="w")







calculo=Button(miframe, text="Calcular", padx=20, pady=10,command=datos)
calculo.grid(row=12, columnspan=2)
result=Label(miframe,bg="#2da2ab", padx=10,pady=10)
result.grid(row=13,columnspan=2)
#txtfondo=Label(miframe, text="hola").place(x=50, y=80)

raiz.mainloop()