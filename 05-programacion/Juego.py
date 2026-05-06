class Juego:
    def __init__(self, p):
        self.palabra = p.lower()
        self.palabraOculta = ["*" for _ in self.palabra]
        self.palabraCadena = ""

    def crearPalabra(self):
        self.palabraCadena = "".join(self.palabraOculta)

    def jugar(self):
        self.crearPalabra()
        contador_intentos = 1
        sigue = True
        print("La palabra tiene", len(self.palabra), "letras")
        print("La palabra oculta es: " + self.palabraCadena)
        intentos = len(set(self.palabra)) + 3
        print("Tienes", intentos, "intentos")

        while sigue:
            letra = input("Ingresa una letra: ").lower()
            if not letra:  
                print("No ingresaste ninguna letra. Intenta de nuevo.")
                continue
            letra = letra[0]

            
            if letra in self.palabraOculta:
                print("Ya esa letra la usaste")
                contador_intentos += 1
            elif letra in self.palabra:
                
                posiciones = [i for i in range(len(self.palabra)) if self.palabra[i] == letra]
                for pos in posiciones:
                    self.palabraOculta[pos] = letra

                self.crearPalabra()
                print("¡Encontraste una letra!")
                print("La palabra oculta es: " + self.palabraCadena + "\n")
                contador_intentos += 1

               
                if self.palabraCadena == self.palabra:
                    print("¡Ganaste! Encontraste la palabra:", self.palabra)
                    print("Usaste", contador_intentos, "intentos")
                    sigue = False
            else:
                print("Esa letra no está en la palabra\n")
                contador_intentos += 1

            
            if contador_intentos > intentos:
                print("Se te acabaron los intentos, juega de nuevo")
                print("La palabra era:", self.palabra)
                sigue = False

                
                
