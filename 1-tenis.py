def solicitar_entrada(mensaje):
    """Función para solicitar entrada al usuario y manejar errores de entrada."""
    while True:
        try:
            entrada = input(mensaje)
            return entrada
        except ValueError:
            print("Entrada inválida. Por favor, intenta de nuevo.")

def actualizar_puntaje(puntajes, jugador):
    """Actualiza el puntaje del jugador según las reglas del tenis."""
    oponente = 1 - jugador
    if puntajes[jugador] == "Adv":  # Si el jugador tiene ventaja y gana el punto
        return True  # Ganador del juego
    elif puntajes[oponente] == "Adv":  # Si el oponente tiene ventaja y el jugador gana el punto
        puntajes[oponente] = 40  # Eliminar la ventaja del oponente, volver a "deuce"
        puntajes[jugador] = 40
        return False
    elif puntajes[jugador] == 40:
        if puntajes[oponente] < 40:
            return True  # Ganador del juego si el oponente no tiene 40
        else:
            puntajes[jugador] = "Adv"  # Otorgar ventaja
            return False
    else:
        puntajes[jugador] = [15, 30, 40][[0, 15, 30].index(puntajes[jugador])]  # Actualizar puntaje normalmente
    return False

def solicitar_ganador_punto(mensaje, jugadores):
    """Solicita al usuario quién gana el punto y maneja errores de entrada."""
    while True:
        entrada = input(mensaje)
        try:
            seleccion = int(entrada) - 1
            if seleccion in [0, 1]:
                return seleccion
            else:
                print(f"Por favor, ingresa un número válido. (1: {jugadores[0]}, 2: {jugadores[1]})")
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número.")

def imprimir_marcador(sets, juegos, puntajes, jugadores):
    """Imprime el estado actual del marcador."""
    print(f"Sets: {jugadores[0]} {sets[0]} - {sets[1]} {jugadores[1]}")
    print(f"Juegos (Set actual): {jugadores[0]} {juegos[0]} - {juegos[1]} {jugadores[1]}")
    print(f"Puntos (Juego actual): {jugadores[0]} {puntajes[0]} - {puntajes[1]} {jugadores[1]}")
def imprimir_estado_del_saque(saque, jugadores):
    """Imprime quién tiene el saque."""
    print(f"Saque: {jugadores[saque]}")
