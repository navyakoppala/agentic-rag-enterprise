from gtts import gTTS

def speak(text):

    tts = gTTS(text)

    tts.save(
        "answer.mp3"
    )

    return "answer.mp3"