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

    for i in range(15):
        if data == expected_answer[i]:

            if data == expected_answer[14]:
                def wrap_up():
                    root2.destroy()
                    root.destroy()

                def replay():
                    support_50_50Button.config(state=NORMAL, image=image50)
                    spectator_pollButton.config(state=NORMAL, image=spectator_poll)
                    call_for_assistanceButton.config(state=NORMAL, image=phoneImage)
                    root2.destroy()
                    questionArea.delete(1.0, END)
                    questionArea.insert(END, questions[0])
                    optionButton1.config(text=first_option[0])
                    optionButton2.config(text=second_option[0])
                    optionButton3.config(text=third_option[0])
                    optionButton4.config(text=fourth_option[0])
                    amountLabel.config(image=amountdisplay)
               
                mixer.music.stop()
                mixer.music.load('Kbcwon.mp3')
                mixer.music.play()

                root2 = Toplevel()
                root2.overrideredirect(True)
                root2.config(bg='Green')
                root2.geometry('500x400+140+30')
                root2.title('You won 0 rupees')
                imgLabel = Label(root2, image=centerImage, bd=0)
                imgLabel.pack(pady=30)

                winLabel = Label(root2, text="You won", font=(" arial", 40, 'bold'), bg='Green', fg='white')
                winLabel.pack()

                playagainButton = Button(root2, text="Replay", font=('arial', 20, 'bold'), bg='Green', fg="white",
                                            activebackground='black', activeforeground='white', bd=0, cursor='hand2',
                                            command=replay)
                playagainButton.pack()

                closeButton = Button(root2, text="close", font=('arial', 20, 'bold'), bg='Green', fg="white",
                                        activebackground='black', activeforeground='white', bd=0, cursor='hand2',
                                        command=wrap_up)
                closeButton.pack()

                # smile_image = PhotoImage(file='happy.png')
                # happyLabel = Label(root2, image=smile_image, bg="black")
                # happyLabel.place()
                root1.mainloop()
                break

            questionArea.delete(1.0, END)
            questionArea.insert(END, questions[i + 1])

            optionButton1.config(text=first_option[i + 1])
            optionButton2.config(text=second_option[i + 1])
            optionButton3.config(text=third_option[i + 1])
            optionButton4.config(text=fourth_option[i + 1])
            amountLabel.config(image=Amountdisplay[i + 1])

        if data not in expected_answer:
            def wrap_up():
                root1.destroy()
                root.destroy()

            def have_another_try():
                support_50_50Button.config(state=NORMAL,image=image50)
                spectator_pollButton.config(state=NORMAL,image=spectator_poll)
                call_for_assistanceButton.config(state=NORMAL,image=phoneImage)
                root1.destroy()
                questionArea.delete(1.0, END)
                questionArea.insert(END, questions[0])
                optionButton1.config(text=first_option[0])
                optionButton2.config(text=second_option[0])
                optionButton3.config(text=third_option[0])
                optionButton4.config(text=fourth_option[0])
                amountLabel.config(image=amountdisplay)

            root1 = Toplevel()
            root1.overrideredirect(True)
            root1.config(bg='Red')
            root1.geometry('500x400+140+30')
            root1.title('You won 0 rupees')
            imgLabel = Label(root1, image=centerImage, bd=0)
            imgLabel.pack(pady=30)

            loseLabel = Label(root1, text="You lose", font=("arial", 40, 'bold'), bg='Red', fg='white')
            loseLabel.pack()

            try_againButton = Button(root1, text="Have another try", font=('arial', 20, 'bold'), bg='Red', fg="white",
                                    activebackground='black', activeforeground='white', bd=0, cursor='hand2',
                                    command=have_another_try)
            try_againButton.pack()

            closeButton = Button(root1, text="close", font=('arial', 20, 'bold'), bg='Red', fg="white",
                                    activebackground='black', activeforeground='white', bd=0, cursor='hand2',
                                    command = wrap_up)
            closeButton.pack()

            sad_image = PhotoImage(file='sad.png')
            sadLabel = Label(root1, image=sad_image, bg="black")
            sadLabel.place()
            root1.mainloop()
            break
def support_50_50():
    support_50_50Button.config(image=image50X,state=DISABLED)
    if questionArea.get(1.0,'end-1c')==questions[0]:
        optionButton1.config(text='')
        optionButton2.config(text='')
    if questionArea.get(1.0,'end-1c')==questions[1]:
        optionButton2.config(text='')
        optionButton3.config(text='')
    if questionArea.get(1.0,'end-1c')==questions[2]:
        optionButton3.config(text='')
        optionButton4.config(text='')
    if questionArea.get(1.0,'end-1c')==questions[3]:
        optionButton2.config(text='')
        optionButton4.config(text='')
    if questionArea.get(1.0,'end-1c')==questions[4]:
        optionButton4.config(text='')
        optionButton3.config(text='')
    if questionArea.get(1.0,'end-1c')==questions[5]:
        optionButton1.config(text='')
        optionButton3.config(text='')
    if questionArea.get(1.0,'end-1c')==questions[6]:
        optionButton1.config(text='')
        optionButton4.config(text='')
    if questionArea.get(1.0,'end-1c')==questions[7]:
        optionButton4.config(text='')
        optionButton3.config(text='')
    if questionArea.get(1.0,'end-1c')==questions[8]:
        optionButton2.config(text='')
        optionButton4.config(text='')
    if questionArea.get(1.0,'end-1c')==questions[9]:
        optionButton2.config(text='')
        optionButton1.config(text='')
    if questionArea.get(1.0,'end-1c')==questions[10]:
        optionButton4.config(text='')
        optionButton3.config(text='')
    if questionArea.get(1.0,'end-1c')==questions[11]:
        optionButton1.config(text='')
        optionButton4.config(text='')
    if questionArea.get(1.0,'end-1c')==questions[12]:
        optionButton3.config(text='')
        optionButton2.config(text='')
    if questionArea.get(1.0,'end-1c')==questions[13]:
        optionButton1.config(text='')
        optionButton4.config(text='')
    if questionArea.get(1.0,'end-1c')==questions[14]:
        optionButton2.config(text='')
        optionButton4.config(text='')

def spectator_poll_lifeline():
    spectator_pollButton.config(image=spectator_pollX,state=DISABLED)
    statusbarA.place(x=580,y=190)
    statusbarB.place(x=620,y=190)
    statusbarC.place(x=660,y=190)
    statusbarD.place(x=700,y=190)

    statusbarLabelA.place(x=580,y=320)
    statusbarLabelB.place(x=620,y=320)
    statusbarLabelC.place(x=660,y=320)
    statusbarLabelD.place(x=700,y=320)

    if questionArea.get(1.0,'end-1c')==questions[0]:
        statusbarA.config(value=30)
        statusbarB.config(value=60)
        statusbarC.config(value=50)
        statusbarD.config(value=90)
    if questionArea.get(1.0,'end-1c')==questions[1]:
        statusbarA.config(value=90)
        statusbarB.config(value=80)
        statusbarC.config(value=50)
        statusbarD.config(value=10)
    if questionArea.get(1.0,'end-1c')==questions[2]:
        statusbarA.config(value=90)
        statusbarB.config(value=60)
        statusbarC.config(value=50)
        statusbarD.config(value=45)
    if questionArea.get(1.0,'end-1c')==questions[3]:
        statusbarA.config(value=95)
        statusbarB.config(value=60)
        statusbarC.config(value=50)
        statusbarD.config(value=10)
    if questionArea.get(1.0,'end-1c')==questions[4]:
        statusbarA.config(value=10)
        statusbarB.config(value=80)
        statusbarC.config(value=50)
        statusbarD.config(value=15)
    if questionArea.get(1.0,'end-1c')==questions[5]:
        statusbarA.config(value=30)
        statusbarB.config(value=60)
        statusbarC.config(value=50)
        statusbarD.config(value=10)
    if questionArea.get(1.0,'end-1c')==questions[6]:
        statusbarA.config(value=30)
        statusbarB.config(value=70)
        statusbarC.config(value=10)
        statusbarD.config(value=50)
    if questionArea.get(1.0,'end-1c')==questions[7]:
        statusbarA.config(value=50)
        statusbarB.config(value=20)
        statusbarC.config(value=50)
        statusbarD.config(value=90)
    if questionArea.get(1.0,'end-1c')==questions[8]:
        statusbarA.config(value=10)
        statusbarB.config(value=40)
        statusbarC.config(value=90)
        statusbarD.config(value=70)
    if questionArea.get(1.0,'end-1c')==questions[9]:
        statusbarA.config(value=30)
        statusbarB.config(value=60)
        statusbarC.config(value=50)
        statusbarD.config(value=90)
    if questionArea.get(1.0,'end-1c')==questions[10]:
        statusbarA.config(value=90)
        statusbarB.config(value=60)
        statusbarC.config(value=40)
        statusbarD.config(value=10)
    if questionArea.get(1.0,'end-1c')==questions[11]:
        statusbarA.config(value=30)
        statusbarB.config(value=90)
        statusbarC.config(value=50)
        statusbarD.config(value=40)
    if questionArea.get(1.0,'end-1c')==questions[12]:
        statusbarA.config(value=90)
        statusbarB.config(value=60)
        statusbarC.config(value=50)
        statusbarD.config(value=30)
    if questionArea.get(1.0,'end-1c')==questions[13]:
        statusbarA.config(value=30)
        statusbarB.config(value=90)
        statusbarC.config(value=50)
        statusbarD.config(value=40)
    if questionArea.get(1.0,'end-1c')==questions[14]:
        statusbarA.config(value=90)
        statusbarB.config(value=60)
        statusbarC.config(value=50)
        statusbarD.config(value=10)

def call_for_assistance():
    mixer.music.load('calling.mp3')
    mixer.music.play()
    select_call_button.place(x=70,y=260)
    call_for_assistanceButton.config(image=phoneImageX,state=DISABLED)

def phonepress():
    for i in range(15):
        if questionArea.get(1.0,'end-1c')==questions[i]:
            voice_sample.say(f'The answer is {expected_answer[i]}')
            voice_sample.runAndWait()
