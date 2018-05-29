#!/usr/bin/python3
import speech_recognition as sr
r = sr.Recognizer()
mic = sr.Microphone(device_index = 4)
with mic as source:
	r.adjust_for_ambient_noise(source)
	print("say somthing !!!")
	audio=r.listen(source,timeout = 15)
text = r.recognize_google(audio)
print(text)


