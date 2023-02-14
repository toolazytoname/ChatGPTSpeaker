
class SpeechAgent:
    @classmethod
    def recognize_from_microphone_manual(cls):
        from SpeechToText import SpeetchToText
        file_name = "record.mp3"
        SpeetchToText.recording(file_name)
        # SpeetchToText.recording(file_name, 5)
        text = SpeetchToText.file_to_text_google(file_name)
        import os
        os.system(f"rm {file_name}")
        return text

    @classmethod
    def text_to_speech(cls, text):
        from TextToSpeech import TextToSpeech
        # TextToSpeech.text_to_speech(text)
        TextToSpeech.tts_gtts(text)