#Calculadora     
print("Bienvenidos al Menu de opciones ")
print("1.Suma")
print("2.Resta")
print("3.Multiplicacion")
print("4.Division")
print("5.Salir")

opcion = 0

while opcion!= 5:
    num1= int(input("Ingresa el primer numero:"))
    num2= int(input("Ingresa el segundo numero:"))
    opcion = int(input("Ingrese la opcion Seleccionada"))
    if opcion == 1:
        print("El resultado de la suma es :",num1 + num2)
    elif opcion == 2:
        print("El resultado de la resta es :",num1 - num2)
    elif opcion == 3:
        print("El resultado de la multiplicacion es :",num1 *num2)
    elif opcion == 4 :
        print("El resultado de la division es :",num1 // num2)
    else:
        print("Fin del juego")




