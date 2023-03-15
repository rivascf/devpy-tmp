import pyttsx3  # import the library



def voiceChanger():
    engine = pyttsx3.init()  # initialize an instance
    voices = engine.getProperty('voices')  # get the available voices
    # eng.setProperty('voice', voice[0].id) #set the voice to index 0 for male voice
    print(f"voices type: {type(voices)}, contains: {len(voices)} voices.")
    # print(*voices, sep="\n")
    for voice in voices:
        if "english" in voice.id:
            print(f"name: {voice.name}, gender: {voice.gender}")
            engine.setProperty('voice', voice.id)
            engine.setProperty("rate", 180)
            engine.say('The quick brown fox jumped over the lazy dog.')
    engine.runAndWait()

    # current_voice = voices[1]
    # engine.runAndWait()
    # engine.setProperty('voice', current_voice.id)  # changing voice to index 1 for female voice
    # engine.setProperty("rate", 180)
    # print(f"Voice: {current_voice.name}")
    # engine.say("This is a demonstration of how to convert index of voice using pyttsx3 library in python.")  # say method for passing text to be spoken
    # engine.runAndWait()  # run and process the voice command

    # current_voice = voices[0]
    # engine.setProperty('voice', current_voice.id)  # changing voice to index 1 for female voice
    # engine.setProperty("rate", 180)
    # print(f"Voice: {current_voice.name}")
    # engine.say("En relación con su proyecto PAPIME, hago de su conocimiento que ya se encuentran disponibles en su entidad académica los recursos financieros correspondientes al presente periodo presupuestal 2023 (etapa 34), por lo que puede comenzar a ejercer su presupuesto a partir de este momento.")  # say method for passing text to be spoken
    # engine.runAndWait()  # run and process the voice command

    # current_voice = voices[2]
    # engine.setProperty('voice', current_voice.id)  # changing voice to index 1 for female voice
    # engine.setProperty("rate", 180)
    # print(f"Voice: {current_voice.name}")
    # engine.say("En relación con su proyecto PAPIME, hago de su conocimiento que ya se encuentran disponibles en su entidad académica los recursos financieros correspondientes al presente periodo presupuestal 2023 (etapa 34), por lo que puede comenzar a ejercer su presupuesto a partir de este momento.")  # say method for passing text to be spoken
    # engine.runAndWait()  # run and process the voice command


if __name__ == "__main__":
    voiceChanger()