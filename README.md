# ChatGPTSpeaker
A smart speaker that combines ChatGPT, Speech-to-Text, and Text-to-Speech.
# How to use
## create a config file config.ini

~~~
[porcupine]
access_key=XXXXXXinput_your_key_here

[openai]
api_key=XXXXXXinput_your_key_here
~~~
* visit https://picovoice.ai/ for  porcupine key
* visit https://beta.openai.com/account/api-keys for openai key


##  install  requirements
### Mac
~~~
brew install portaudio
brew install mpg321
pip install -r requirements.txt
~~~
### Linux
The custom wake-up word model for this platform needs to be retrained, and the code also needs to load different wake-up word resources according to the platform selection. (It is probably unnecessary to use the default wake-up word). 

### Windows
Same as the Linux above.

## run main.py

## have fun
* the wake up word is "hello marry",so you should say "Hello Marry"
* ask a question
* you will get a response

enjoy it.

# Some shortcomings to be improved
- [ ] TTS services require scientific networking for access which leads to instability.
- [ ] The overall time consumption needs to be optimized.
- [ ] The mute detection logic is not intelligent enough.
  - [ ] At the beginning: if speech is not given promptly when recording starts, recording may end directly.
  - [ ] At the end: if speech is given slowly during recording, it may be misjudged as ending.  
- [ ] The code is not robust enough.
  - [ ] It does not support scenarios where the TTS network access is abnormal.
  - [ ] No try-catch is used in the overall code.
  - [ ] It feels a bit low to use a while true outside.

# 补充说明
这个工具能否在大陆使用呢？
浏览器访问ChatGPT是不能在中国使用的，连香港也不行。
但是我们在科学上网后可以注册openAI的key，目前为止通过这个key是可以在国内访问的ChatGPT服务的。
但尴尬的事，我的stt 服务都是用的谷歌的服务，这个不行。在想办法代替。之前试过微软的 azure 未果。这个也算是todo 之一。

|  服务   | 是否离线  | 大陆能否访问  |备注
|  ----  | ----  |----  |----  |
| 唤醒词  | 离线 | | |
| 静音监测  | 离线 | | |
| 浏览器访问ChatGPT  | 网络 | 不能| |
| 通过key访问beta模型  | 网络 | 可以| |
| 语音转文字  | 网络 | 不能|目前用的谷歌，打算替换一个质量好且大陆可以访问的|
| 文字转语音  | 网络 | 可以|目前用一个机器音，效果没有谷歌的好，效果有点类似mac 自带的say|




