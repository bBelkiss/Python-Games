#Aventura en la selva

import time

def juego_aventura_selva():
    print("¡Bienvenido a la Aventura en la Selva!")
    print("Te encuentras en medio de una densa selva. Tu misión es llegar a la antigua ciudad escondida.")

    decisiones = [
        {"pregunta": "Encuentras un río. ¿Quieres beber agua directamente del río? (s/n): ", "opcion_correcta": "n",
         "respuesta_correcta": "Decides no beber agua directamente del río y evitas posibles enfermedades del agua."},
        {"pregunta": "Ves una cueva. ¿Quieres explorarla? (s/n): ", "opcion_correcta": "s",
         "respuesta_correcta": "Te adentras en la cueva y descubres un atajo que te ahorra tiempo."},
        {"pregunta": "Oyes rugidos a lo lejos. ¿Quieres acercarte para investigar? (s/n): ", "opcion_correcta": "n",
         "respuesta_correcta": "Decides no acercarte a los rugidos y evitas un encuentro con animales peligrosos."},
        {"pregunta": "Encuentras una bifurcación en el camino. ¿Quieres tomar la ruta izquierda o derecha? (i/d): ",
         "opcion_correcta": "i", "respuesta_correcta": "Tomaste la ruta izquierda y evitaste un pantano peligroso."},
        {"pregunta": "Ves un puente colgante. ¿Quieres cruzarlo? (s/n): ", "opcion_correcta": "s",
         "respuesta_correcta": "Cruzas el puente con éxito y evitas caer al río."},
        {"pregunta": "Encuentras una tirolina. ¿Quieres usarla para cruzar un barranco? (s/n): ", "opcion_correcta": "s",
         "respuesta_correcta": "Usas la tirolina y llegas al otro lado del barranco de manera emocionante."},
        {"pregunta": "Te encuentras con una tribu amigable. ¿Quieres unirte a su celebración? (s/n): ", "opcion_correcta": "s",
         "respuesta_correcta": "Te unes a la celebración y ganas aliados amigables."},
        {"pregunta": "Encuentras una antigua puerta. ¿Quieres intentar abrirla? (s/n): ", "opcion_correcta": "s",
         "respuesta_correcta": "Abres la puerta y descubres la entrada a la antigua ciudad escondida. ¡Felicidades, has ganado el juego!"}
    ]

    puntaje = 0

    for decision in decisiones:
        print("\n" + decision["pregunta"])
        time.sleep(1)
        respuesta_usuario = input().lower()

        if respuesta_usuario == decision["opcion_correcta"]:
            print(f"¡Correcto! {decision['respuesta_correcta']}")
            puntaje += 1
        else:
            print("Incorrecto. Tu aventura en la selva termina aquí.")
            break

    print(f"\nFin del juego. Tu puntaje final es: {puntaje}")

if __name__ == "__main__":
    juego_aventura_selva()
