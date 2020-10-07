import speech_recognition as sr
#import json

filename = "test3.wav"
r = sr.Recognizer()

with sr.AudioFile(filename) as source:
    audio_data = r.listen(source)
    
    try:
        text = r.recognize_google(audio_data)
        print(text)
       
    except:
        print("Error on procesing")