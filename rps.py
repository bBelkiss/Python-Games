#Piedra, papel o tijera

import random

def juego_piedra_papel_tijera():
    opciones = ["piedra", "papel", "tijera"]

    while True:
        jugador = input("Elige piedra, papel o tijera (o 'salir' para terminar): ").lower()

        if jugador == 'salir':
            print("¡Gracias por jugar! Hasta luego.")
            break
        computadora = random.choice(opciones)

        if jugador in opciones:
            print(f"Tú elegiste {jugador.capitalize()}. La computadora eligió {computadora.capitalize()}.")

            if jugador == computadora:
                print("¡Es un empate!")
            elif (jugador == "piedra" and computadora == "tijera") or \
                 (jugador == "papel" and computadora == "piedra") or \
                 (jugador == "tijera" and computadora == "papel"):
                print("¡Ganaste!")
            else:
                print("¡La computadora gana!")

        else:
            print("Por favor, elige una opción válida: piedra, papel o tijera.")

if __name__ == "__main__":
    juego_piedra_papel_tijera()
