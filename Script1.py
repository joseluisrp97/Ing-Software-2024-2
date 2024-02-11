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

def verificar_cambio_de_cancha(juegos):
    """Determina si se debe realizar un cambio de cancha."""
    return (juegos[0] + juegos[1]) % 2 != 0

def main():
    jugadores = [solicitar_entrada("Nombre del Jugador 1: "), solicitar_entrada("Nombre del Jugador 2: ")]
    sets = [0, 0]
    juegos = [0, 0]
    puntajes = [0, 0]
    saque = 0  # El jugador 1 comienza sacando

    while sets[0] < 2 and sets[1] < 2:
        ganador_juego = False
        puntajes = [0, 0]  # Resetear puntajes para el nuevo juego

        while not ganador_juego:
            imprimir_estado_del_saque(saque, jugadores)
            imprimir_marcador(sets, juegos, puntajes, jugadores)
            
            ganador_punto = solicitar_ganador_punto(f"Quién gana el punto? (1: {jugadores[0]}, 2: {jugadores[1]}): ", jugadores)
            ganador_juego = actualizar_puntaje(puntajes, ganador_punto)
            
            if ganador_juego:
                juegos[ganador_punto] += 1
                puntajes = [0, 0]  # Resetear puntajes para el nuevo juego
                if juegos[ganador_punto] >= 6 and (juegos[ganador_punto] - juegos[1 - ganador_punto] >= 2) or (juegos[ganador_punto] == 7):
                    sets[ganador_punto] += 1
                    juegos = [0, 0]  # Resetear juegos para el nuevo set
                
                saque = 1 - saque  # Alternar el saque para el próximo juego
                
                if (juegos[0] + juegos[1]) % 2 != 0:
                    print("Cambio de cancha.")
                    
                if sets[0] == 2 or sets[1] == 2:  # Verificar si hay ganador del partido
                    print(f"Partido terminado. {jugadores[ganador_punto]} gana el partido {sets[0]} sets a {sets[1]}.")
                    return

if __name__ == "__main__":
    main()