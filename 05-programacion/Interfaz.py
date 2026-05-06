class Interfaz:
    def __init__(self):
        bienvenida = """
        ***********************
        *  JUEGO DE AHORCADO  *
        *  Adivina la palabra *
        ***********************"""
        print (bienvenida)
        
    def menu(self):
        menu = """
        ******************************
        *            Menu            *
        * Digita la opcion deseada:  *
        *                            *
        * 1.Jugar Ahorcado           *
        * 2.Ver las palabras         *
        * 3.Agregar una nueva palabra*
        * 4.Salir                    *
        ******************************
        Tu respuesta es: """
        respuesta = input(menu)
        return respuesta
        
    def mensaje(self,mensaje):
        
        print(mensaje)

    def salidaPalabras(self,palabras):
        salida = "Las palabras almacenadas son :\n"
        for palabra in palabras:
            salida = salida +"-"+ palabra +"\n"
        print(salida)
                
    def agregarPalabra(self):
        mensaje = "Digita la palabra que deseas agregar :"
        respuesta = input(mensaje).strip().lower()
        return respuesta 
            
            
