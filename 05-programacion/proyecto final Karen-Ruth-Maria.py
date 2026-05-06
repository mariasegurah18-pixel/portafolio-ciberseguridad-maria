def crear_tablero():
    return ["-" for _ in range(9)]
 
def ver_tablero(tablero):
    print("\n")
    print(tablero[0] + "|" + tablero[1] + "|" + tablero[2] + "   1 | 2 | 3")
    print(tablero[3] + "|" + tablero[4] + "|" + tablero[5] + "   4 | 5 | 6")
    print(tablero[6] + "|" + tablero[7] + "|" + tablero[8] + "   7 | 8 | 9")
    print("\n")
 
def verificar_ganador(tablero):
    for i in [0, 3, 6]:  
        if tablero[i] == tablero[i+1] == tablero[i+2] != "-":
            return tablero[i]
    for i in [0, 1, 2]:  
        if tablero[i] == tablero[i+3] == tablero[i+6] != "-":
            return tablero[i]
    
    if tablero[0] == tablero[4] == tablero[8] != "-":
        return tablero[0]
    if tablero[2] == tablero[4] == tablero[6] != "-":
        return tablero[2]
    return 0  
 
def jugador(valor, tablero): 
    anoto = False
    while not anoto: 
        try:
            posicion = int(input(f"Jugador {valor}, elige una posición del 1 al 9: ")) - 1
            if 0 <= posicion <= 8:
                if tablero[posicion] == "-":
                    tablero[posicion] = valor
                    anoto = True
                else:
                    print("Esa posición ya está ocupada.")
            else:
                print("Elige una posición válida (1 a 9).")
        except ValueError:
            print("Por favor, ingresa un número válido.")
 
def preguntar_reinicio():
    respuesta = input("¿Quieres jugar otra partida? (s/n): ")
    return respuesta == "s"
 
print("¡Bienvenido al juego de tres en linea!")
 
victorias_jugador1 = 0
victorias_jugador2 = 0
empates = 0
 
while True:
    tablero = crear_tablero()
    estado_ganador = 0
    turno1 = True
    turnos_realizados = 0
 
    ver_tablero(tablero)
 
    while True:
        valor = "x" if turno1 else "o"
        print(f"Turno del jugador {'1' if turno1 else '2'} = {valor}")
 
        jugador(valor, tablero)
        ver_tablero(tablero)
 
        estado_ganador = verificar_ganador(tablero)
 
        if estado_ganador != 0:
            if estado_ganador == "x":
                print("¡Felicidades! El jugador 1 ha ganado.")
                victorias_jugador1 += 1
            else:
                print("¡Felicidades! El jugador 2 ha ganado.")
                victorias_jugador2 += 1
            break
 
        turnos_realizados += 1
        if turnos_realizados == 9:
            print("¡Es un empate!")
            empates += 1
            break
 
        turno1 = not turno1  
 

    print("\nMarcador:")
    print(f"Jugador 1 (x): {victorias_jugador1} victorias")
    print(f"Jugador 2 (o): {victorias_jugador2} victorias")
    print(f"Empates: {empates}\n")
 
    
    if not preguntar_reinicio():
        print("¡Gracias por jugar!")
        break
