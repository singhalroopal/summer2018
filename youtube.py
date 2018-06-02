#!/usr/bin/python3
#import urllib.parse for encoding data from HTML
import urllib.parse
#import urllib.request for fetching urls
import urllib.request
#import re to match a particular string to the regular expression 
import re
##providing high level interface to allow displaying web based documents to user.
import webbrowser
##taking input in voice
import speech_recognition as sr
r = sr.Recognizer()
mic = sr.Microphone(device_index = 4)
with mic as source:
		r.adjust_for_ambient_noise(source)
		print("say somthing !!!")
		audio=r.listen(source,timeout = 25)
text = r.recognize_google(audio)
print(text)	

query=urllib.parse.urlencode({'search_query':str(text)})
print(query)

html_content=urllib.request.urlopen("http://www.youtube.com/results?"+query)
print(html_content)
url = "https://www.youtube.com/watch?v="
videos = re.findall(r'href=\"\/watch\?v=(.{11})',html_content.read().decode())
webbrowser.open_new(url+videos[0])

