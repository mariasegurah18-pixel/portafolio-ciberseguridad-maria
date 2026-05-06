#Ejercicio 1: Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros),
#calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa corporal es <imc>.

Peso= int(input("Ingrese su peso en kilos:"))
Estatura=float(input("Ingrese su estatura en metro:"))
IMC= Peso/(Estatura*2)

print("Tu indice de masa corporal es:",IMC)

print("")

#Ejercicio 2: Escribir un programa que pida al usuario dos números enteros y muestre por pantallala división <n> entre <m> da un cociente <c>
#y un residuo <r> donde <n> y <m> son los números introducidos por el usuario, y <c> y <r> son el cociente y el residuo de la división entera respectivamente.

n=int(input("Ingrese el primer numero entero:"))
m=int(input("Ingrese el segundo numero entero:"))
c=n//m
r=n%m

print("La division entre",n,"y",m,"\nDa un cociente",c," y un residuo",r)

print("")

#Ejercicio 3: Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo y la empresa de logística les cobra
#por peso de cada paquete así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g.
#Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado.

peso_payaso= 112
peso_muñecas= 75
num_payaso= int(input("Ingrese el numero de payasos vendidos:"))
num_muñecas=int(input("Ingrese el numero de muñecas vendidas:"))
peso_total=(peso_payaso +num_payaso)+(peso_muñecas+num_muñecas)

print("El peso total del paquete es",peso_total,"gramos")

print("")

#Ejercicio 4: Una panadería vende barras de pan a ₡550 cada una. El pan que no es el día tiene un descuento del 60%. Escribir un programa que comience leyendo el número
#de barras vendidas que no son del día. Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca y el costo final total.

precio_barra=550 
descuento=0.60
num_barras=int(input("Ingrese la cantidad de barras de pan vendidas que no estan frescas:"))
costo_total= num_barras*precio_barra*(1-descuento)

print("Precio normal de la barra de pan:",precio_barra,"cls")
print("Descuento por no ser fresca la barra:",(descuento*100),"%")
print("Costo final total:",costo_total)


