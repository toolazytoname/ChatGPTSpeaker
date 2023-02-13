
class TextToSpeech:
    @classmethod
    def tts_gtts(cls, text):
        from gtts import gTTS
        import os
        language = "zh"
        file_name = "tts_result"
        audio = gTTS(text=text, lang=language)
        audio.save(file_name)
        os.system(f"mpg321 {file_name}")
        os.system(f"rm {file_name}")
        pass

    @classmethod
    def tts_pyttsx3(cls, text):
        import pyttsx3
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()