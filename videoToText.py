#download ffmpeg: apt-get install ffmpeg. add path of ffmpeg.exe to %PATH
#install pydub
#install SpeechRecognition
#run file in project directory by exeucuting: python videoToText.py


#have a video in mp4 format(named Trial.mp4) in same directory as this file
import os
import speech_recognition as sr
command2mp3 = "ffmpeg -i Trial.mp4 Trial.mp3"
command2wav = "ffmpeg -i Trial.mp3 trial.wav"
os.system(command2mp3)
os.system(command2wav)
r = sr.Recognizer()
audio = sr.AudioFile("trial.wav")
with audio as source:
    r.adjust_for_ambient_noise(source)
    audio = r.record(source)
try:
    print(r.recognize_google(audio))
except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
