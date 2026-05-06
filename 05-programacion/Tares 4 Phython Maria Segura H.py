materias= ['Español','Matematicas','Sociales','Ciencias' ,'Civica']

notas =[0,0,0,0,0]

for i in range(5):
    print("Ingrese sus notas en este orden de materias",materias[i],)
    notas[i] = int(input("Ingrese la nota de: "))

for i in range (5):
    if notas[i]>= 70 :
        print("Aprobo ",materias[i]," con", notas[i],)
    else:
        print("Perdio",materias[i],"con",notas[i],)
