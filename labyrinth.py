#Laberinto v3

import random
import time

def juego_laberinto_magico():
    print("¡Bienvenido al Laberinto Mágico!")
    print("Te encuentras en un laberinto lleno de sorpresas y desafíos. Tu misión es llegar a la salida.")

    laberinto = [
        ["S", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", "W", " ", "W", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", "W", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", "W", " ", "W", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", "W", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", "W", " ", "W", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", "E"]
    ]

    posicion_jugador = [0, 0]
    tesoros_recogidos = 0

    while True:
        print("\nLaberinto Actual:")
        mostrar_laberinto(laberinto, posicion_jugador)
        print("Tesoro Recogido:", tesoros_recogidos)

        decision = input("\n¿Hacia dónde quieres moverte? (arriba/a, abajo/b, izquierda/i, derecha/d, salir/s): ").lower()

        if decision == "salir" or decision == "s":
            print("¡Gracias por jugar! Hasta luego.")
            break

        nueva_posicion = mover_jugador(posicion_jugador, decision)

        if es_movimiento_valido(nueva_posicion):
            if laberinto[nueva_posicion[0]][nueva_posicion[1]] == "W":
                print("¡Te has encontrado con un muro! Elige otro camino.")
            elif laberinto[nueva_posicion[0]][nueva_posicion[1]] == "E":
                print("¡Felicidades! Has llegado a la salida. ¡Has escapado del Laberinto Mágico!")
                break
            elif laberinto[nueva_posicion[0]][nueva_posicion[1]] == " ":
                print("¡Has avanzado sin problemas!")
            elif laberinto[nueva_posicion[0]][nueva_posicion[1]] == "T":
                print("¡Encontraste un tesoro mágico!")
                tesoros_recogidos += 1
                laberinto[nueva_posicion[0]][nueva_posicion[1]] = " " 
        else:
            print("¡Cuidado! Te estás saliendo del laberinto. Elige otro movimiento.")

        posicion_jugador = nueva_posicion

def mostrar_laberinto(laberinto, posicion_jugador):
    for i in range(len(laberinto)):
        for j in range(len(laberinto[i])):
            if [i, j] == posicion_jugador:
                print("J", end=" ")  #Jugador
            elif laberinto[i][j] == "W":
                print("█", end=" ")  #Muro
            elif laberinto[i][j] == "E":
                print("S", end=" ")  #Salida
            elif laberinto[i][j] == "T":
                print("$", end=" ")  #Tesoro
            else:
                print(" ", end=" ")  #Espacio vacío
        print()

def mover_jugador(posicion_jugador, decision):
    nueva_posicion = posicion_jugador.copy()
    if decision == "arriba" or decision == "a":
        nueva_posicion[0] -= 1
    elif decision == "abajo" or decision == "b":
        nueva_posicion[0] += 1
    elif decision == "izquierda" or decision == "i":
        nueva_posicion[1] -= 1
    elif decision == "derecha" or decision == "d":
        nueva_posicion[1] += 1
    return nueva_posicion

def es_movimiento_valido(nueva_posicion):
    return 0 <= nueva_posicion[0] < 9 and 0 <= nueva_posicion[1] < 9

if __name__ == "__main__":
    juego_laberinto_magico()
