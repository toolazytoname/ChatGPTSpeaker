class SpeetchToText:
    # 录音
    # 录音必须安装portaudio模块，否则会报错
    # http://portaudio.com/docs/v19-doxydocs/compile_linux.html
    def recording(filename, time=0, threshold=7000):
        """
        :param filename: 文件名
        :param time: 录音时间,如果指定时间，按时间来录音，默认为自动识别是否结束录音
        :param threshold: 判断录音结束的阈值
        :return:
        """
        import pyaudio
        import numpy as np
        from scipy import fftpack
        import wave
        CHUNK = 1024  # 块大小
        FORMAT = pyaudio.paInt16  # 每次采集的位数
        CHANNELS = 1  # 声道数
        RATE = 16000  # 采样率：每秒采集数据的次数
        RECORD_SECONDS = time  # 录音时间
        WAVE_OUTPUT_FILENAME = filename  # 文件存放位置
        p = pyaudio.PyAudio()
        stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
        print("* 录音中...")
        frames = []
        if time > 0:
            for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
                data = stream.read(CHUNK)
                frames.append(data)
        else:
            stopflag = 0
            stopflag2 = 0
            while True:
                data = stream.read(CHUNK)
                rt_data = np.frombuffer(data, np.dtype('<i2'))
                # print(rt_data*10)
                # 傅里叶变换
                fft_temp_data = fftpack.fft(rt_data, rt_data.size, overwrite_x=True)
                fft_data = np.abs(fft_temp_data)[0:fft_temp_data.size // 2 + 1]

                # 测试阈值，输出值用来判断阈值
                print(sum(fft_data) // len(fft_data))

                # 判断麦克风是否停止，判断说话是否结束，# 麦克风阈值，默认7000
                if sum(fft_data) // len(fft_data) > threshold:
                    stopflag += 1
                else:
                    stopflag2 += 1
                oneSecond = int(RATE / CHUNK)
                if stopflag2 + stopflag > oneSecond:
                    if stopflag2 > oneSecond // 3 * 2:
                        break
                    else:
                        stopflag2 = 0
                        stopflag = 0
                frames.append(data)
        print("* 录音结束")
        stream.stop_stream()
        stream.close()
        p.terminate()
        with wave.open(WAVE_OUTPUT_FILENAME, 'wb') as wf:
            wf.setnchannels(CHANNELS)
            wf.setsampwidth(p.get_sample_size(FORMAT))
            wf.setframerate(RATE)
            wf.writeframes(b''.join(frames))

    @classmethod
    def file_to_text_google(cls, file_path):
        try:
            import speech_recognition as sr
            # create a speech recognition object
            r = sr.Recognizer()
            text = None
            # open the file
            with sr.AudioFile(file_path) as source:
                # listen for the data (load audio to memory)
                audio_data = r.record(source)
                # recognize (convert from speech to text)
                text = r.recognize_google(audio_data, language="zh-CN")
                print(text)
        finally:
            return text

    @classmethod
    def microphone_to_text(cls):
        # https://www.lsbin.com/7333.html
        import speech_recognition as sr
        # create a speech recognition object
        r = sr.Recognizer()
        with sr.Microphone() as source:
            # read the audio data from the default microphone
            audio_data = r.record(source, duration=10)
            print("Recognizing...")
            # convert speech to text
            # text = r.recognize_google(audio_data)
            text = r.recognize_google(audio_data, language="zh-CN")
            print(text)
            return text
        return None