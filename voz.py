import pyttsx3


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
