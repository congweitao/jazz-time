import speech_recognition as sr

r = sr.Recognizer()
mic = sr.Microphone()
print('录音中...')
with mic as source:
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)

print('录音结束，识别中...')
test = r.recognize_google(audio, language='zh-CN')
print(test)
