
class SpeechAgent:
    @classmethod
    def recognize_from_microphone_manual(cls):
        from SpeechToText import SpeetchToText
        file_name = "record.mp3"
        # 自动判断静音，停止录音
        # SpeetchToText.recording(file_name)
        # 按照固定时间 5s 录音
        SpeetchToText.recording(file_name, 5)
        # text = SpeetchToText.file_to_text(file_name)
        # 大陆用不了google
        text = SpeetchToText.file_to_text_google(file_name)
        import os
        os.system(f"rm {file_name}")
        return text

    @classmethod
    def text_to_speech(cls, text):
        from TextToSpeech import TextToSpeech
        TextToSpeech.tts_pyttsx3(text)
        # tts_gtts 效果更好，但是大陆用不了
        # TextToSpeech.tts_gtts(text)