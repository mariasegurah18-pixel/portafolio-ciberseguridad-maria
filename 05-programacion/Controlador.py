class Controlador:
    def leerPalabras(self):
        try:
            lector = open("palabras.txt","r")
            lista = lector.readlines()
            palabras =[]
            for palabra in lista:
                palabras.append(palabra.strip())
            lector.close()
            return palabras
        except:
            print("Error de lectura")
     
    def escribirPalabras(self,p):
        try:
            palabra = p.lower().strip()
            palabras = self.leerPalabras()
            if palabra not in palabras:
                escritor = open("palabras.txt","a")
                escritor.write(palabra+"\n")
                escritor.close()
                print ("Se almaceno correctamente la palabra")
            else:
                print("La palabra no fue almacenada")
                print("porque ya existe")
            
        except:
            print("Error de escritura")
