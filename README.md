# ChatGPTSpeaker
A smart speaker ，combine ChatGPT  with Speech-to-Text and  Text-to-Speech
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


##  install  requirements in Mac
~~~
brew install portaudio
brew install mpg321
pip install -r requirements.txt
~~~

## run main.py

## have fun
* the wake up word is "hello marry",so you should say "Hello Marry"
* ask a question
* you will get a response

enjoy it.

# 补充说明
这个工具能否在大陆使用呢？
浏览器访问ChatGPT是不能在中国使用的，连香港也不行。
但是我们在科学上网后可以注册openAI的key，目前为止通过这个key是可以在国内访问的ChatGPT服务的。
但尴尬的事，我的stt 服务都是用的谷歌的服务，这个不行。在想办法代替。之前试过微软的 azure 未果。这个也算是todo 之一。

|  服务   | 是否离线  | 大陆能否访问  |
|  ----  | ----  |----  |
| 唤醒词  | 离线 | |
| 浏览器访问ChatGPT  | 网络 | 不能|
| 通过key访问beta模型  | 网络 | 可以|
| 语音转文字  | 网络 | 目前用的谷歌，不可以。todo 替换一个质量好且大陆可以访问的|
| 文字转语音  | 网络 | 目前用一个机器音，效果没有谷歌的好，效果有点类似mac 自带的say|




