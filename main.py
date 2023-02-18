import os
import pvporcupine
from pvrecorder import PvRecorder
from datetime import datetime
import logging




def picovoice():
    from configparser import ConfigParser
    cfg = ConfigParser()
    cfg.read('config.ini')
    access_key = cfg.get('porcupine', 'access_key')

    hello_marry_path = os.path.dirname(__file__) + "/Hello-Marry_en_mac_v2_1_0/Hello-Marry_en_mac_v2_1_0.ppn"
    keyword_paths = [hello_marry_path]

    keywords = list()
    for x in keyword_paths:
        keyword_phrase_part = os.path.basename(x).replace('.ppn', '').split('_')
        if len(keyword_phrase_part) > 6:
            keywords.append(' '.join(keyword_phrase_part[0:-6]))
        else:
            keywords.append(keyword_phrase_part[0])
    porcupine = pvporcupine.create(
        access_key=access_key,
        keyword_paths=keyword_paths,
        # keywords=['picovoice', 'bumblebee']
    )
    recorder = PvRecorder(-1, frame_length=porcupine.frame_length)
    recorder.start()
    logging.info('Using device: %s' % recorder.selected_device)
    logging.info('Listening {')
    for keyword in zip(keywords):
        logging.info('  %s ' % (keyword))
    logging.info('}')
    while True:
        pcm = recorder.read()
        result = porcupine.process(pcm)
        if result >= 0:
            recorder.stop()
            logging.info('[%s] Detected %s' % (str(datetime.now()), keywords[result]))
            logging.info("wake up keyword detected，start recording！")
            from SpeechAgent import SpeechAgent
            SpeechAgent.text_to_speech("说吧，宝贝，我听着呢")
            run()
            recorder.start()
            logging.info('Listening ，wake me up please ')


def chatGPT(text):
    from ChatGPTAgent import chatGPT
    if len(text) == 0:
        return
    text = text.replace('\n', ' ').replace('\r', '').strip()
    logging.info(f'chatGPT Q: {text}')
    from SpeechAgent import SpeechAgent
    SpeechAgent.text_to_speech("我开始谨慎地思考了，这可能会花一些时间，显得我很沉稳")
    res = chatGPT.ask(text)
    logging.info(f'chatGPT A: {res}')
    return res


def run():
    from SpeechAgent import SpeechAgent
    logging.info('start recognize_from_microphone')
    question = SpeechAgent.recognize_from_microphone_manual()
    SpeechAgent.text_to_speech("录音结束")
    if question is not None and len(question) != 0:
        SpeechAgent.text_to_speech(f"你的问题是{question}")
        logging.info(f'recognize_from_microphone, text={question}')
        answer = chatGPT(question)
        SpeechAgent.text_to_speech(answer)
    else:
        SpeechAgent.text_to_speech(f"我没有听清")
        logging.info('question is None, some thing wrong happened')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    logging.basicConfig(filename='ChatLog.log', encoding='utf-8', level=logging.INFO)
    picovoice()
