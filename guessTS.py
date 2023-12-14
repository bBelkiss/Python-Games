#Adivina la canción

import random

def juego_encuentra_la_letra():
    canciones_taylor_swift = {
        "Love Story": "Romeo, take me somewhere we can be alone. I'll be waiting, all there's left to do is run.",
        "Shake It Off": "Cause the players gonna play, play, play, play, play. And the haters gonna hate, hate, hate, hate, hate.",
        "Blank Space": "Got a long list of ex-lovers, they'll tell you I'm insane. But I got a blank space, baby, and I'll write your name.",
        "Bad Blood": "Band-aids don't fix bullet holes, you say sorry just for show. You live like that, you live with ghosts.",
        "Delicate": "Is it cool that I said all that? Is it too soon to do this yet? 'Cause I know that it's delicate.",
        "Cardigan": "Vintage tee, brand new phone. High heels on cobblestones. When you are young, they assume you know nothing."
    }

    cancion_seleccionada = random.choice(list(canciones_taylor_swift.keys()))
    letra_cancion = canciones_taylor_swift[cancion_seleccionada]

    print(f"¡Bienvenido al juego 'Encuentra la Letra' con Taylor Swift!")
    print(f"Adivina la letra de la canción: '{cancion_seleccionada}'")
    print("Las palabras faltantes están representadas por guiones bajos.")

    letra_oculta = ocultar_letra(letra_cancion)
    print("\n" + letra_oculta)

    palabras_adivinadas = set()
    intentos_maximos = 3
    intentos_realizados = 0

    while "_" in letra_oculta and intentos_realizados < intentos_maximos:
        palabra_usuario = input("\nIngresa una palabra para completar la letra: ").lower()

        if palabra_usuario in letra_cancion.lower() and palabra_usuario not in palabras_adivinadas:
            palabras_adivinadas.add(palabra_usuario)
            letra_oculta = revelar_letra(letra_cancion, letra_oculta, palabra_usuario, palabras_adivinadas)
            print("\n¡Correcto! Palabras adivinadas:", ", ".join(palabras_adivinadas))
        else:
            intentos_realizados += 1
            print("\n¡Incorrecto! Inténtalo de nuevo. Intentos restantes:", intentos_maximos - intentos_realizados)

        print("\n" + letra_oculta)

    if "_" not in letra_oculta:
        print(f"\n¡Felicidades! Has completado la letra de '{cancion_seleccionada}'. ¡Eres un verdadero fan de Taylor Swift!")
    else:
        print(f"\n¡Agotaste tus intentos! La letra completa de '{cancion_seleccionada}' es:\n{letra_cancion}")

def ocultar_letra(letra_cancion):
    letra_oculta = ""
    for char in letra_cancion:
        if char.isalpha():
            letra_oculta += "_" if char.islower() else "_"
        else:
            letra_oculta += char
    return letra_oculta

def revelar_letra(letra_cancion, letra_oculta, palabra_usuario, palabras_adivinadas):
    palabra_usuario = palabra_usuario.lower()
    letra_oculta_actualizada = ""

    i = 0
    while i < len(letra_cancion):
        if letra_cancion[i].isalpha():
            palabra_actual = ""
            while i < len(letra_cancion) and letra_cancion[i].isalpha():
                palabra_actual += letra_cancion[i]
                i += 1

            if palabra_actual.lower() in palabras_adivinadas:
                letra_oculta_actualizada += palabra_actual
            else:
                letra_oculta_actualizada += "_" * len(palabra_actual)
        else:
            letra_oculta_actualizada += letra_cancion[i]
            i += 1

    return letra_oculta_actualizada

if __name__ == "__main__":
    juego_encuentra_la_letra()
