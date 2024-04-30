from tkinter import *
from tkinter.ttk import Progressbar
import pyttsx3
from pygame import mixer

voice_sample = pyttsx3.init()
voices=voice_sample.getProperty('voices')
voice_sample.setProperty('voice',voices[1].id)

#load the background music 
mixer.init()
mixer.music.load('kbc.mp3')
mixer.music.play(-1)
