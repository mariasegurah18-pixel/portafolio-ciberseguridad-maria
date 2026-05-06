#Tarea POO

class Pila:
    def __init__ (self):
        self.elementos = []
        self.maximo = 6
        
    def push(self,valor):
        if len(self.elementos) < self.maximo:
            self.elementos.append(valor)
            print("El valor fue agregado a la pila",valor)
        else:
            print("La pila esta llena")
            return valor

    def pop (self):
        if self.elementos:
            valor = self.elementos.pop()
            print("El valor fue eliminado de la pila",valor)
            return valor
        else:
            print("La pila esta vacia")
            return None

        
    def mostrar(self):
        valores =""
        contador = len(self.elementos)-1
        for i in range(len(self.elementos)):
            valores += str(self.elementos[contador])+"\n"
            contador -=1
        return valores 
    

    def ver(self,pos):
        try:
            return self.elementos[pos]
        except IndexError:
            return "Posición fuera de rango"

p = Pila()
for v in [10, 20, 30, 40, 50, 60]:
    p.push(v)
p.push(70)
    
print(p.mostrar())

print(p.ver(1))  
print(p.ver(-1))  
print(p.ver(10))

for _ in range(7):
    p.pop()
