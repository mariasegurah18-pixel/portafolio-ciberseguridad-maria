import Interfaz
import Controlador
import Juego
import random

interfaz = Interfaz.Interfaz()
controlador = Controlador.Controlador()

listaPalabras = controlador.leerPalabras()
continua = True

while continua:
    respuesta = interfaz.menu()
    match respuesta:
        case "4":
            continua = False
            interfaz.mensaje("Fin del juego !!")
        case "1":
            p = random.choice(listaPalabras)
            juego = Juego.Juego(p)
            juego.jugar()
        case "2":
            interfaz.salidaPalabras(controlador.leerPalabras())
        case "3":
            p = interfaz.agregarPalabra()
            controlador.escribirPalabras(p)
        case _:
            interfaz.mensaje("El valor ingresado es incorrecto")
            


