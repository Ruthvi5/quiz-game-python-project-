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

def choice(action):
    select_call_button.place_forget()
    statusbarA.place_forget()
    statusbarB.place_forget()
    statusbarC.place_forget()
    statusbarD.place_forget()

    statusbarLabelA.place_forget()
    statusbarLabelB.place_forget()
    statusbarLabelC.place_forget()
    statusbarLabelD.place_forget()
    b = action.widget
    data = b['text']
