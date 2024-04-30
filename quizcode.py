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
