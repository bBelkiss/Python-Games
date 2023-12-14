#Ahorcado

import random

def juego_ahorcado():
    palabras = ["python", "programacion", "codigo", "desarrollo", "diversion", "tecnologia", "computadora"]
    palabra_secreta = random.choice(palabras)
    palabra_adivinada = ['_'] * len(palabra_secreta)
    intentos_maximos = 6
    intentos_realizados = 0

    print("¡Bienvenido al juego del Ahorcado!")
    print("Adivina la palabra secreta.")

    while True:
        print(" ".join(palabra_adivinada))
        letra = input("Ingresa una letra: ").lower()

        if letra.isalpha() and len(letra) == 1:
            if letra in palabra_secreta:
                for i in range(len(palabra_secreta)):
                    if palabra_secreta[i] == letra:
                        palabra_adivinada[i] = letra
            else:
                print("¡Incorrecto! Esa letra no está en la palabra.")
                intentos_realizados += 1

            if intentos_realizados == intentos_maximos:
                print("¡Perdiste! La palabra correcta era:", palabra_secreta)
                break

            if "_" not in palabra_adivinada:
                print("¡Felicidades! ¡Has adivinado la palabra!")
                break
        else:
            print("Por favor, ingresa una letra válida.")

if __name__ == "__main__":
    juego_ahorcado()
