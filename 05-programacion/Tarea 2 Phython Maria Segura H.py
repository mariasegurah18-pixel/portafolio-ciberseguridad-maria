#Tarea 2

#Ejercicio 1: Escriba un programa que simule una alcancía. El programa solicitará primero una cantidad, que será la cantidad de dinero que queremos ahorrar. A continuación, el programa solicitará una y otra vez las cantidades que se irán ahorrando, hasta que el total ahorrado iguale o supere al objetivo. El programa no comprobará que las cantidades sean posit

objetivo = float(input("Ingrese el monto que deseas ahorrar :"))
ahorrado = 0


while ahorrado < objetivo:
    cantidad= int(input("Ingrese la cantidad a ahorrar "))
    ahorrado += cantidad
    if ahorrado >= objetivo :
        print("Felicidades has alcanzado tu meta de ahorro!!!!")
    else:
        print("Te falta" , objetivo-ahorrado,"para alcanzar tu meta") 

print("---------------------------------")

#Ejercicio 2: Escriba un programa que almacene un número entre 1 y 100 en una variable, ustedes eligen el número, luego el usuario debe adivinarlo, se le piden números al usuario hasta que lo adivine. El programa proporciona pistas ("muy alto" o "muy bajo") hasta que el usuario acierte. Además, el programa lleva un conteo de los intentos realizados.

valor =float(input("Adivina el numero que estoy pensando\nIngrese un valor  entre 1 y 100:"))           
numero =(valor//2)
intentos = 5

while intentos > 0 :
      intento = float(input("Ingresa un numero:"))
      intentos +=1
      if intento < numero:
         print("Muy bajo,intenta nuevamente")
      elif intento > numero:
          print("Muy alto ,intenta nuevamente")
      else:
          intento == numero;
          print("Felicidades !!!!!! Has adivinado el numero en",intentos-5,"intentos")
          print("Fin del juego ")
          intentos = -1
