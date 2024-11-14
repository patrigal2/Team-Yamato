#Juego final main.py

num_vidas_h = 20
num_vidas_m = 20

regla_juego = """Bienvenid@ a hundir la flota! Tu contrincante va a ser una máquina. Cada uno disparará a una coordenada.
Si logras disparar en una posición de un barco de la maquina, aparecerá una 'X' en el tablero del 
adversario y podrás seguir disparando vayas acertando. Si, por el contrario, disparas al agua, apracerá un '-' en 
eltablero del adversario y el turno será de la maquina. Para ganar, se tienen que "hundir" todos los barcos del adversario."""

import numpy as np
from tablero import Tablero
from funciones import generar_coordenadas_aleatorias, imprimir_tablero
from variables import DIMENSIONES, BARCOS

def empezar_juego():
    pregunta_01 = input("Hola, ¿quieres iniciar una partida?(Contesta si o no)")

    if pregunta_01.lower() == "si":
        pregunta_02 = input("¿Cómo te llamas? ")
        print(regla_juego)
        return pregunta_02
    else:
        print("Hasta la próxima.")
        return None

def main():
    nombre_jugador = empezar_juego()
    if not nombre_jugador:
        return  # Sale si el jugador no quiere iniciar la partida

    print(f"¡Buena suerte, {nombre_jugador}!")

    # Inicializar tableros de jugador y máquina
    tablero_jugador = Tablero(id_jugador="jugador")
    tablero_maquina = Tablero(id_jugador="máquina")

    juego_terminado = False
    turno_jugador = True  

    while not juego_terminado:
        if turno_jugador:
            print("\nTu tablero de disparos:")
            imprimir_tablero(tablero_maquina.tablero_visible)
            try:
                x, y = map(int, input("Introduce las coordenadas de disparo (x y): ").split())
            except ValueError:
                print("Por favor, ingresa dos números separados por un espacio.")
                continue
            
            if tablero_maquina.recibir_disparo(x, y):
                print("¡Impacto! Vuelve a disparar.")
            else:
                print("Agua... le toca a la máquina.")
                turno_jugador = False
        else:
            x, y = generar_coordenadas_aleatorias()
            print(f"La máquina dispara a ({x}, {y})...")
            
            if tablero_jugador.recibir_disparo(x, y):
                print("¡La máquina te ha dado! Vuelve a disparar.")
            else:
                print("La máquina falló... ¡Tu turno!")
                turno_jugador = True
            
        # Comprobación de fin de juego
        if tablero_maquina.barcos_restantes() == 0:
            print("¡Felicidades! Has hundido todos los barcos enemigos. ¡Ganaste!")
            juego_terminado = True
        elif tablero_jugador.barcos_restantes() == 0:
            print("La máquina ha hundido todos tus barcos. Has perdido.")
            juego_terminado = True

if __name__ == "__main__":
    main()
