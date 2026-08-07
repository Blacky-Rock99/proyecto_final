import pyttsx3
import time
from colorama import Fore, Style, init
print("ECO VOICE iniciado")

init()

# Inicializar el motor de voz
engine = pyttsx3.init()



def hablar(texto):
    print(texto)

    voz = pyttsx3.init()

    voz.setProperty("rate", 160)
    voz.setProperty("volume", 1.0)

    voices = voz.getProperty("voices")
    voz.setProperty("voice", voices[15].id)

    voz.say(texto)
    voz.runAndWait()

    voz.stop()


def linea():
    print(Fore.GREEN + "=" * 60 + Style.RESET_ALL)

def titulo():

    linea()

    print("""
🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍

        ECO VOICE

     LA TIERRA TE HABLA

🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍
""")

    linea()

def introduccion():

    hablar ("""Hola.Soy el planeta Tierra. \
    Gracias por dedicar unos minutos para escucharme. \
    ¿Sabías que el planeta produce cada vez más gases de efecto invernadero debido a las actividades humanas? \
    Cada vez que desperdiciamos energía, usamos más combustible del necesario o No reciclamos, aumentamos nuestra huella de carbono. \
    El cambio climático provoca temperaturas más altas, incendios forestales, sequías, inundaciones y pone en riesgo a miles de especies. \
    Pero existe una buena noticia. Cada persona puede ayudar con pequeños cambios en su vida diaria. \
    Responderás diez preguntas. \
    Al finalizar descubrirás qué tanto estás ayudando al planeta.  
    ¡Comencemos!""" )

def hacer_preguntas():

    preguntas = [
        "¿Apagas las luces cuando sales de una habitación?",
        "¿Desconectas los cargadores cuando ya no los utilizas?",
        "¿Reciclas papel, plástico y vidrio?",
        "¿Cierras la llave del agua mientras te cepillas los dientes?",
        "¿Utilizas bolsas reutilizables cuando haces compras?",
        "¿Usas bicicleta, caminas o transporte público cuando es posible?",
        "¿Utilizas focos LED o de bajo consumo?",
        "¿Apagas la computadora o televisión cuando ya no las usas?",
        "¿Evitas desperdiciar comida?",
        "¿Has plantado o cuidado árboles o áreas verdes?"
    ]

    respuestas = []
    puntos = 0

    hablar("""
Ahora analizaré tus hábitos para conocer cómo ayudas al planeta.

Para cada pregunta tendrás tres opciones.

Opción 1 significa Siempre.

Opción 2 significa Algunas veces.

Opción 3 significa Nunca.

Comencemos.
""")

    for numero, pregunta in enumerate(preguntas, start=1):

        print("\n" + "=" * 60)
        print("PREGUNTA", numero, "DE 10")
        print("=" * 60)

        # La Tierra hace UNA pregunta
        hablar(pregunta)

        print("\n1 = Siempre")
        print("2 = Algunas veces")
        print("3 = Nunca")

        while True:

            respuesta = input("\nTu respuesta: ")

            if respuesta == "1":

                puntos += 2
                respuestas.append(1)

                print("Respuesta registrada.")

                break

            elif respuesta == "2":

                puntos += 1
                respuestas.append(2)

                print("Respuesta registrada.")

                break

            elif respuesta == "3":

                puntos += 0
                respuestas.append(3)

                print("Respuesta registrada.")

                break

            else:

                print("Escribe solamente 1, 2 o 3.")

    hablar("""
Has terminado las diez preguntas.

Ahora analizaré tus respuestas.
""")

    return puntos, respuestas

def mostrar_resultado(puntos):

    linea()

    print("🌎 REPORTE ECO VOICE 🌎")

    linea()

    print("Puntaje obtenido:", puntos, "/20")

    if puntos >= 17:

        nivel = "Guardián del Planeta"

        mensaje = """
Excelente trabajo.

Tus hábitos ayudan mucho a reducir el impacto climático.

Continúa con estas buenas acciones y sigue ayudando a proteger nuestro planeta.
"""

    elif puntos >= 10:

        nivel = "Amigo de la Tierra"

        mensaje = """
Vas por buen camino.

Con algunos cambios puedes ayudar todavía más.

Cada pequeño esfuerzo cuenta cuando se trata de proteger nuestro planeta.
"""

    else:

        nivel = "Necesito tu ayuda"

        mensaje = """
La Tierra necesita que mejores algunos hábitos para proteger el medio ambiente.

Pero no te preocupes.

Nunca es demasiado tarde para comenzar a cambiar nuestras acciones.
"""

    print("\nNivel:", nivel)
    print(mensaje)

    hablar(f"""
Tu resultado es:

{nivel}.

{mensaje}
""")

    return nivel

def recomendaciones(respuestas):

    consejos = []

    if respuestas[0] != 1:
        consejos.append(
            "Recuerda apagar las luces que no estés utilizando para ahorrar energía."
        )

    if respuestas[1] != 1:
        consejos.append(
            "Desconectar cargadores ayuda a reducir el consumo innecesario de electricidad."
        )

    if respuestas[2] != 1:
        consejos.append(
            "Separar y reciclar residuos ayuda a disminuir la contaminación."
        )

    if respuestas[3] != 1:
        consejos.append(
            "Cerrar la llave mientras te cepillas los dientes ayuda a conservar agua."
        )

    if respuestas[4] != 1:
        consejos.append(
            "Usar bolsas reutilizables reduce la cantidad de plástico en el planeta."
        )

    if respuestas[5] != 1:
        consejos.append(
            "Caminar, usar bicicleta o transporte público puede disminuir las emisiones de carbono."
        )

    if respuestas[6] != 1:
        consejos.append(
            "Los focos LED consumen menos energía y ayudan al medio ambiente."
        )

    if respuestas[7] != 1:
        consejos.append(
            "Apagar aparatos electrónicos cuando no los uses ahorra electricidad."
        )

    if respuestas[8] != 1:
        consejos.append(
            "Evitar desperdiciar comida reduce las emisiones generadas por la producción de alimentos."
        )

    if respuestas[9] != 1:
        consejos.append(
            "Cuidar árboles y áreas verdes ayuda a capturar dióxido de carbono."
        )

    linea()

    print("🌱 CONSEJOS DE LA TIERRA 🌱")

    linea()

    if len(consejos) == 0:

        mensaje = """
Excelente.

Todos tus hábitos ayudan mucho al planeta.

No tengo recomendaciones para ti.

¡Sigue así!
"""

    else:

        mensaje = """
Tengo algunas recomendaciones para ayudarte a proteger el planeta.

"""

        for consejo in consejos:
            mensaje += "\n" + consejo + "\n"

    print(mensaje)

    hablar(mensaje)

def personalidad_tierra(nivel):

    linea()

    print("🌎 MENSAJE PERSONAL DE LA TIERRA 🌎")

    linea()

    if nivel == "Guardián del Planeta":

        mensaje = """
Me siento feliz de ver que estás tomando buenas decisiones.

Tus acciones demuestran que pequeñas decisiones pueden generar grandes cambios.

Gracias por proteger mis bosques, océanos y animales.

Continúa inspirando a otras personas a cuidar nuestro hogar.
"""

    elif nivel == "Amigo de la Tierra":

        mensaje = """
Estoy orgullosa de que estés intentando mejorar.

Cada cambio positivo que haces ayuda a disminuir el impacto ambiental.

Todavía hay acciones que puedes mejorar.

Recuerda que protegerme comienza con pequeños hábitos diarios.
"""

    else:

        mensaje = """
Necesito que prestes más atención a mis necesidades.

Mis ecosistemas están siendo afectados por las acciones humanas.

La buena noticia es que todavía puedes cambiar tus hábitos.

Cada acción positiva puede ayudar a construir un futuro mejor.
"""

    print(mensaje)

    hablar(mensaje)

def analizar_planeta():

    hablar("Estoy analizando tus respuestas.")

    print("\nAnalizando impacto ambiental...\n")

    for i in range(0, 101, 10):

        barra = "█" * (i // 10)

        espacios = "░" * (10 - (i // 10))

        print(
            Fore.GREEN +
            f"[{barra}{espacios}] {i}%"
            +
            Style.RESET_ALL
        )

        time.sleep(0.5)


    hablar("El análisis ha terminado.")

def guardar_reporte(puntos, nivel):

    archivo = open(
        "reporte_eco_voice.txt",
        "w",
        encoding="utf-8"
    )


    archivo.write(
        "========= ECO VOICE =========\n\n"
    )

    archivo.write(
        "Reporte del usuario\n\n"
    )

    archivo.write(
        f"Puntaje obtenido: {puntos}/20\n"
    )

    archivo.write(
        f"Nivel ambiental: {nivel}\n"
    )


    archivo.write(
        "\nGracias por ayudar al planeta 🌎"
    )


    archivo.close()


    print(
        Fore.CYAN +
        "\nReporte guardado como reporte_eco_voice.txt"
        +
        Style.RESET_ALL
    )

def empezar_nuevamente():

    while True:

        respuesta = input(
            "\n¿Quieres analizar otro usuario? (s/n): "
        )


        if respuesta.lower() == "s":

            return True


        elif respuesta.lower() == "n":

            hablar(
                "Gracias por cuidar el planeta. Hasta pronto."
            )

            return False


        else:

            print(
                "Escribe solamente s o n."
            )

def emocion_tierra(puntos):

    if puntos >= 17:

        return "😊 La Tierra está feliz"


    elif puntos >= 10:

        return "😐 La Tierra tiene esperanza"


    else:

        return "😟 La Tierra necesita ayuda"

def main():

    continuar = True

    while continuar:

        titulo()

        introduccion()

        puntos, respuestas = hacer_preguntas()

        analizar_planeta()

        nivel = mostrar_resultado(puntos)

        personalidad_tierra(nivel)

        recomendaciones(respuestas)

        guardar_reporte(
            puntos,
            nivel
        )

        estado = emocion_tierra(puntos)

        print(estado)

        hablar(estado)

        continuar = empezar_nuevamente()

if __name__ == "__main__":
        main()