
print("Lista de Tareas")
print("1.Agregar una tarea al final")
print("2.Insertar una tarea en una posicion")
print("3.Eliminar una tarea")
print("4.Ver la lista de tareas")
print("5.Salir del programa")

tareas =[]

num = 0

while num != 5:
    num =int(input("Escoge una de las opciones:"))
    if num == 1:
        tarea=input("Escribe la tarea:")
        tareas.append(tarea)
        print("Se agrego la tarea exitosamente")
    elif num == 2:
       for i in range(len(tareas)) :
           pos=int(input("Digita una posicion entre 0 y "+str(len(tareas)-1)))
           tarea= input("Escribe la tarea:")
           tareas.insert(pos,tarea)
           if 0 <= pos < len(tareas[-1]):
               print("Se agrego la tarea exitosamente")
               print("\nLista actualizada:")
               for i in range(len(tareas)):
                   print(f"{i},{tareas[i]}")
    elif num == 3 :
        for i in range (len(tareas)):
            pos= 0
            if 0 <= pos < len(tareas):
               pos=int(input("Digita una posicion entre 0 y :"+str(len(tareas)-1)))
               del tareas [pos]
               print("Se agrego la tarea exitosamente")
               print("\nLista actualizada:")
               for i in range(len(tareas)):
                   print(f"{i},{tareas[i]}")
    elif num == 4 :
        print (tareas)
    else:
        print("Saiendo del programa")
        
  
   
             
