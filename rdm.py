#Adivina el número

import random

def adivina_el_numero():
    numero_secreto = random.randint(1, 20)
    intentos_realizados = 0

    print("¡Bienvenido a Adivina el Número!")
    print("Estoy pensando en un número entre 1 y 20.")

    while True:
        try:
            intento = int(input("¿Cuál es tu adivinanza? "))
        except ValueError:
            print("Por favor, ingresa un número válido.")
            continue

        intentos_realizados += 1

        if intento < numero_secreto:
            print("Demasiado bajo. Intenta nuevamente.")
        elif intento > numero_secreto:
            print("Demasiado alto. Intenta nuevamente.")
        else:
            print(f"¡Felicidades! ¡Has adivinado el número en {intentos_realizados} intentos!")
            break

if __name__ == "__main__":
    adivina_el_numero()
