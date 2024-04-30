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
expected_answer = ['Bangalore','Delhi','Surya Sen','The Hauge','Wellington Stadium','Beauxbatons','Alam Ara','The aperture','Mahesh Bhupati','Genome','Flute','Longbourn','Raj Kapoor','Hubble','1957']

questions = ['Which city is known as the silicon valley of india?','Which city in india has most UNESCO heritage sites?','Who among the following was not involved in the Lahore conspiracy case?','The international Court of justice sits in?','The national stadium in Delhi was earlier known as?','What was the name of the wizarding school in France?','Which is the first talkie feature film of india?','What determines the sharpness of a camera?','Who is the first Indian to win a Grand Slam tennis tournament?','A cell builds its proteins from the Instructions encoded in its _.','Which of the following musical instruments is NOT of foreign origin?','According to the classic novel Pride & Prejudice,where does the Bennet family live?','Who is known as the showman of Indian film industry?','Who first proposed that the galaxy was expanding?','What year was the oldest programming language still in use invented?']
first_option = ['Hyderabad','Delhi','Surya Sen','The Hauge','Irwin Stadium','Hogwarts','Raja Harishchandra','The aperture','Sania Mirza','Cytoplasm','Tabla','Pemberly','Raj Kapoor','Einstein','1957']
second_option = ['Mumbai','Jaipur','Bhagat Singh','Geneva','Mountabatten Stadium','Beauxbatons','Alam Ara','The exposure time','Rohan Bopanna','Amino acid', 'Flute','Longbourn','Nargis','Kepler','1952']
third_option = ['Chennai','Jaisalmer','Rajguru','Vienna','Wellington Stadium','Drumstrang','Duniya na mane','The focal length','Mahesh Bhupati','Lysosome','Sitar','Rosings','Dev Anand','Hubble','1960']
fourth_option = ['Bangalore','Agra','Sukhdev','Rome','Canning Stadium','Castelobruxo','Aadami','Size of the camera','Leander Paes','Genome','Violin','London','Rajendra Kumar','Maxwell','1974']
root = Tk()

root.geometry('1270x652+0+0')  # dimensions of the screen
root.title("who wants to be a millionaire?")  # name of the window

root.config(bg="black")  # changing the color of window

leftframe = Frame(root, bg='black', padx=90)  # creating the left part of the screen
leftframe.grid(row=0, column=0)  # using the grid method to put it on the window

topFrame = Frame(leftframe, bg='black', pady=15)
topFrame.grid()

centerFrame = Frame(leftframe, bg="black", pady=15)
centerFrame.grid(row=1, column=0)

bottomFrame = Frame(leftframe)
bottomFrame.grid(row=2, column=0)

rightframe = Frame(root, pady=25, padx=50, bg="black")  # check the values
rightframe.grid(row=0, column=1)

image50 = PhotoImage(file="50-50.png")
image50X = PhotoImage(file="50-50-X.png")
support_50_50Button = Button(topFrame, image=image50, bg='black', bd=0, activebackground="lavender", width=180, height=80,command=support_50_50)
support_50_50Button.grid(row=0, column=0)

spectator_poll = PhotoImage(file="audiencePole.png")
spectator_pollX=PhotoImage(file="audiencePoleX.png")
spectator_pollButton = Button(topFrame, image=spectator_poll, bg="black", bd=0, activebackground="lavender", width=180,
                            height=80,command=spectator_poll_lifeline)
spectator_pollButton.grid(row=0, column=1)

phoneImage= PhotoImage(file="phoneAFriend.png")
phoneImageX= PhotoImage(file="phoneAFriendX.png")
call_for_assistanceButton = Button(topFrame, image=phoneImage, bg="black", bd=0, activebackground="lavender", width=180,
                                height=80,command=call_for_assistance)
call_for_assistanceButton.grid(row=0, column=2)

callimage=PhotoImage(file='phone.png')
select_call_button=Button(root,image=callimage,bd=0,bg='black',activebackground='black',cursor='hand2',command=phonepress)


centerImage = PhotoImage(file="center.png")
logoLabel = Label(centerFrame, image=centerImage, bg='black', width=300, height=200)
logoLabel.grid(row=0, column=0)

amountdisplay = PhotoImage(file="Picture1.png")
amountdisplay1 = PhotoImage(file="Picture1.png")
amountdisplay2 = PhotoImage(file="Picture2.png")
amountdisplay3 = PhotoImage(file="Picture3.png")
amountdisplay4 = PhotoImage(file="Picture4.png")
amountdisplay5 = PhotoImage(file="Picture5.png")
amountdisplay6 = PhotoImage(file="Picture6.png")
amountdisplay7 = PhotoImage(file="Picture7.png")
amountdisplay8 = PhotoImage(file="Picture8.png")
amountdisplay9 = PhotoImage(file="Picture9.png")
amountdisplay10 = PhotoImage(file="Picture10.png")
amountdisplay11 = PhotoImage(file="Picture11.png")
amountdisplay12 = PhotoImage(file="Picture12.png")
amountdisplay13 = PhotoImage(file="Picture13.png")
amountdisplay14 = PhotoImage(file="Picture14.png")
amountdisplay15 = PhotoImage(file="Picture15.png")

Amountdisplay = [amountdisplay1, amountdisplay2, amountdisplay3,amountdisplay4, amountdisplay5,amountdisplay6, amountdisplay7, amountdisplay8, amountdisplay9, amountdisplay10,
                amountdisplay11, amountdisplay12, amountdisplay13, amountdisplay4, amountdisplay15]
amountLabel = Label(rightframe, image=amountdisplay, bg='Black')
amountLabel.grid(row=0, column=0)

layoutImage = PhotoImage(file="lay.png")
layoutLabel = Label(bottomFrame, image=layoutImage, bg="Black")
layoutLabel.grid()
questionArea = Text(bottomFrame, font=("arial", 18, "bold"), width=34, height=2, wrap='word', bg="black", fg="white",
                    bd=0)
questionArea.place(x=70, y=10)
questionArea.insert(END, questions[0])
# A
labelA = Label(bottomFrame, text='A:', bg="black", fg='white', font=("arial", 16, "bold"))
labelA.place(x=60, y=110)

optionButton1 = Button(bottomFrame, text=first_option[0], font=('arial', 12, "bold"), bg="black", fg="white", bd=0,
                        activebackground="black", activeforeground="white", cursor='hand2')
optionButton1.place(x=100, y=110)
# B
labelB = Label(bottomFrame, text='B:', bg="black", fg='white', font=("arial", 16, "bold"))
labelB.place(x=330, y=110)

optionButton2 = Button(bottomFrame, text=second_option[0], font=('arial', 12, "bold"), bg="black", fg="white", bd=0,
                        activebackground="black", activeforeground="white", cursor='hand2')
optionButton2.place(x=370, y=110)
# c
labelC = Label(bottomFrame, text='C:', bg="black", fg='white', font=("arial", 16, "bold"))
labelC.place(x=60, y=190)

optionButton3 = Button(bottomFrame, text=third_option[0], font=('arial', 12, "bold"), bg="black", fg="white", bd=0,
                        activebackground="black", activeforeground="white", cursor='hand2')
optionButton3.place(x=100, y=190)
# D
labelD = Label(bottomFrame, text='D:', bg="black", fg='white', font=("arial", 16, "bold"))
labelD.place(x=330, y=190)

optionButton4 = Button(bottomFrame, text=fourth_option[0], font=('arial', 12, "bold"), bg="black", fg="white", bd=0,
                        activebackground="black", activeforeground="white", cursor='hand2')
optionButton4.place(x=370, y=190)

statusbarA=Progressbar(root,orient=VERTICAL,length=120)
statusbarB=Progressbar(root,orient=VERTICAL,length=120)
statusbarC=Progressbar(root,orient=VERTICAL,length=120)
statusbarD=Progressbar(root,orient=VERTICAL,length=120)

statusbarLabelA=Label(root,text='A',font=('arial',20,'bold'),bg='black',fg='white')
statusbarLabelB=Label(root,text='B',font=('arial',20,'bold'),bg='black',fg='white')
statusbarLabelC=Label(root,text='C',font=('arial',20,'bold'),bg='black',fg='white')
statusbarLabelD=Label(root,text='D',font=('arial',20,'bold'),bg='black',fg='white')
