lista_1= [1,2,3,2,4,5,1,6,3,2,7,8]

print("lista_1:",lista_1)

lista_2 = []

for numero in lista_1:
    if not numero in lista_2:
        lista_2.append(numero)
        
print("lista_2:",lista_2)
