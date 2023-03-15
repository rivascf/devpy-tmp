"""
    Convertir texto a voz (TTS) con
    Python usando gTTS
    Ejemplo 3: Escribir múltiples idiomas en un archivo
    @author parzibyte
"""
# from gtts import gTTS
# tts = gTTS('Hola mundo. Estamos convirtiendo texto a voz con Python.', lang='es-us')
# tts_ingles = gTTS('Hello world! testing tts in Python', lang='en')
# tts_frances = gTTS('Salut monde. Nous convertissons le texte en parole avec Python.', lang='fr-fr')

# with open("3_hola_es_en_fr.mp3", "wb") as archivo:
#     tts.write_to_fp(archivo)
#     tts_ingles.write_to_fp(archivo)
#     tts_frances.write_to_fp(archivo)

"""
    Convertir texto a voz (TTS) con
    Python usando gTTS

    Ejemplo 4: Escribir hola mundo en un archivo, en idioma español
    y después reproducirlo

    @author parzibyte
"""
# from gtts import gTTS
# from playsound import playsound

# NOMBRE_ARCHIVO = "sonido_generado.mp3"
# tts = gTTS('Hola mundo. Estamos convirtiendo texto a voz con Python.', lang='es-us')
# Nota: podríamos llamar directamente a save
# with open(NOMBRE_ARCHIVO, "wb") as archivo:
#     tts.write_to_fp(archivo)

# playsound(NOMBRE_ARCHIVO)

"""
    Convertir texto a voz (TTS) con
    Python usando gTTS
    Ejemplo 5: TTS con velocidad lenta
    @author parzibyte
"""
# from gtts import gTTS
# tts = gTTS('Hola mundo. Estamos convirtiendo texto a voz con Python.', lang='es-us', slow=True)
# tts.save("5_hola_mundo.mp3")

####################################################

#from gtts import gTTS
import gtts
from playsound import playsound

NOMBRE_ARCHIVO = "multi_lang_demo.mp3"
print(f"gtts max. chars: {gtts.gTTS.GOOGLE_TTS_MAX_CHARS}")
tts_es_us = gtts.gTTS('Hola mundo. Estamos convirtiendo texto a voz con Python.', lang='es', tld='us')
tts_es_mx = gtts.gTTS('Hola mundo. Estamos convirtiendo texto a voz con Python.', lang='es', tld='com.mx')
tts_es_es = gtts.gTTS('Hola mundo. Estamos convirtiendo texto a voz con Python.', lang='es', tld='es')
tts_ingles = gtts.gTTS('Hello world! testing tts in Python', lang='en')
tts_frances = gtts.gTTS('Salut monde. Nous convertissons le texte en parole avec Python.', lang='fr-fr')
tts_en = gtts.gTTS('hello', lang='en')
tts_mx = gtts.gTTS('Felipe', lang='es', tld='com.mx')
tts_fr = gtts.gTTS('bonjour', lang='fr')

with open(NOMBRE_ARCHIVO, "wb") as archivo:
    tts_es_us.write_to_fp(archivo)
    tts_es_mx.write_to_fp(archivo)
    tts_es_es.write_to_fp(archivo)
    tts_ingles.write_to_fp(archivo)
    tts_frances.write_to_fp(archivo)
    tts_en.write_to_fp(archivo)
    tts_mx.write_to_fp(archivo)
    tts_fr.write_to_fp(archivo)

playsound(NOMBRE_ARCHIVO)
    



# if __name__ == "__main__":
#     voiceChanger()