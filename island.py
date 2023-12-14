#Isla misteriosa

import time
import random

def juego_aventura_isla_misteriosa():
    print("¡Bienvenido a la Aventura en la Isla Misteriosa!")
    print("Te encuentras en una isla misteriosa llena de tesoros. Tu misión es encontrar el tesoro oculto.")

    tesoros = ["Gemas", "Monedas de oro", "Artefactos antiguos", "Mapa del tesoro", "Estatuilla mágica"]
    tesoro_oculto = random.choice(tesoros)
    opciones = ["Explorar la selva", "Investigar la playa", "Subir a la montaña", "Buscar en las cuevas"]

    print("¡Comienza tu aventura!")

    for i in range(3, 0, -1):
        print(f"\n¡Tienes {i} minutos antes de que caiga la noche!")

        print("\nOpciones:")
        for j, opcion in enumerate(opciones, 1):
            print(f"{j}. {opcion}")

        eleccion = input("Elige una opción (1-4): ")

        if eleccion.isdigit() and 1 <= int(eleccion) <= 4:
            eleccion = int(eleccion)
            print(f"\nExplorando...")

            time.sleep(2)  

            if eleccion == 1:
                print("Te aventuras en la selva y encuentras pistas intrigantes.")
            elif eleccion == 2:
                print("Investigas la playa y descubres conchas y mensajes en botellas.")
            elif eleccion == 3:
                print("Subes a la montaña y disfrutas de una vista impresionante.")
            elif eleccion == 4:
                print("Exploras las cuevas y encuentras inscripciones en las paredes.")

            print("¡Es hora de descansar y planificar tu próximo movimiento!")
            time.sleep(2)

        else:
            print("¡Opción inválida! Debes elegir un número del 1 al 4.")

    print("\nLa noche cae sobre la isla. Es momento de decidir tu última acción.")

    for j, opcion in enumerate(opciones, 1):
        print(f"{j}. {opcion}")

    eleccion_final = input("Elige tu última acción (1-4): ")

    if eleccion_final.isdigit() and 1 <= int(eleccion_final) <= 4:
        eleccion_final = int(eleccion_final)
        print("\nRealizando la última acción...")

        time.sleep(2)

        if eleccion_final == 1:
            print("Exploras la selva una vez más y encuentras un antiguo altar.")
        elif eleccion_final == 2:
            print("Regresas a la playa y descubres un cofre enterrado en la arena.")
        elif eleccion_final == 3:
            print("Subes de nuevo a la montaña y hallas una entrada secreta a una caverna.")
        elif eleccion_final == 4:
            print("Regresas a las cuevas y encuentras una puerta oculta.")

        print("¡Descubres el tesoro oculto!")

        if random.random() < 0.5:
            print(f"Felicidades, has encontrado {tesoro_oculto} en la isla misteriosa.")
        else:
            print("¡Desafortunadamente, el tesoro parece estar protegido por antiguas trampas!")

    else:
        print("¡Opción inválida! No tomaste una decisión final.")

    print("\n¡Fin del juego!")

if __name__ == "__main__":
    juego_aventura_isla_misteriosa()
