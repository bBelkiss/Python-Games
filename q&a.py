#Preguntas y respuestas

import random

def juego_preguntas():
    preguntas = {
        "¿Cuál es la capital de Argentina?": ["Santiago", "Montevideo", "Asunción", "Buenos Aires"],
        "¿En qué año se declaró la independencia de Argentina?": ["1810", "1820", "1830", "1816"],
        "¿Cuál es el monumento más emblemático de Buenos Aires?": ["Obelisco", "Torre Eiffel", "Estátua da Liberdade", "Coliseo"],
        "¿Qué baile es típico de Argentina?": ["Tango", "Samba", "Flamenco", "Cha-cha-cha"],
        "¿Cuál es el plato nacional de Argentina?": ["Asado", "Sushi", "Pizza", "Paella"]
    }

    preguntas_keys = list(preguntas.keys())
    random.shuffle(preguntas_keys)

    puntaje = 0

    print("¡Bienvenido al juego de Preguntas y Respuestas!")

    for pregunta_key in preguntas_keys:
        pregunta = pregunta_key
        opciones = preguntas[pregunta_key]

        print("\n" + pregunta)

        for i, opcion in enumerate(opciones, 1):
            print(f"{i}. {opcion}")

        try:
            respuesta_usuario = int(input("Ingresa el número de tu respuesta: "))

            if 1 <= respuesta_usuario <= len(opciones):
                if opciones[respuesta_usuario - 1] == opciones[0]:
                    print("¡Correcto! ¡Has ganado 1 punto!")
                    puntaje += 1
                else:
                    print(f"Incorrecto. La respuesta correcta es: {opciones[0]}")
            else:
                print("Por favor, ingresa un número válido.")
        except ValueError:
            print("Por favor, ingresa un número.")

    print(f"\nFin del juego. Tu puntaje final es: {puntaje}")

if __name__ == "__main__":
    juego_preguntas()
