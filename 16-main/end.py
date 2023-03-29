from tkinter import * # GUI Directory for python
import time # Time function for calculating clock speeds
from PIL import Image, ImageTk # Image handling (Icons)

gName = "Schlange" # Game Name
vCount = 0 # This is the version count (For MOD show/hide Function)
vVersion = "Version: 4.0.3"

def saveSettings():
    window2.destroy()
    # More settings add here

def enterHome(): # This is the home screen
    global window # Allows the window to be called/modified outside of this function
    global gName # Allows reference of the gName variable
    window = Tk()
    window.title(f'{gName} ¦ Home Screen')
    window.geometry("500x250")

    icon1 = PhotoImage(file='./img/settings.png')
    icon2 = PhotoImage(file='./img/exit.png')
    icon3 = PhotoImage(file='./img/version.png')
    icon4 = PhotoImage(file='./img/play.png')
    icon5 = PhotoImage(file='./img/hmm.png')

    """Images = [icon1, icon2, icon3, icon4]
    labels = ['Settings', 'Version', 'Play', 'Exit']

    r = 0
    s = 0
    for x in labels:
        Label(image=Images[s], relief=RIDGE, bg='white').grid(row=r,column=0)
        Button(text=x, relief=RIDGE, width=20, height=3).grid(row=r, column=1)
        r = r+1
        s = s+1"""

    PlayLbl = Label(image=icon4,relief=RIDGE,bg="white").grid(row=0,column=0)
    PlayBtn = Button(text="Play",relief=RIDGE,width=20,height=3, command=play).grid(row=0,column=1)
    
    SettingsLbl = Label(image=icon1,relief=RIDGE,bg="white").grid(row=1,column=0)
    SettingsBtn = Button(text="Settings",relief=RIDGE,width=20,height=3, command=settings).grid(row=1,column=1)

    VersionLbl = Label(image=icon3,relief=RIDGE,bg="white").grid(row=2,column=0)
    VersionBtn = Button(text="Show/Hide Version",relief=RIDGE,width=20,height=3, command=version).grid(row=2,column=1)

    ExitLbl = Label(image=icon2,relief=RIDGE,bg="white").grid(row=3,column=0)
    ExitBtn = Button(text="Exit",relief=RIDGE,width=20,height=3, command=leave).grid(row=3,column=1)
        
    lbl1 = Label(
        text=f'Welcome to {gName}').grid(row=0,column=2)
    lbl2 = Label(
        relief=RIDGE,
        text="""How to play:
        Select a button
        Start a new game by pressing \'Play\'
        Exit the game by pressing exit""").grid(row=1,column=2)
    lbl3 = Label(
        image=icon5).grid(row=2,column=2)

    window.mainloop()


def leave():
    window.destroy()
    print("You seem to have left. Did I upset you? What did I do wrong? I thought you loved me...")
    exit()
    
def version():
    global vCount
    global vVersion
    if vCount % 2 != 0:
        vlbl = Label(
            window,
            text="                             ").grid(row=3,column=2)
    elif vCount % 2 == 0:
        vlbl = Label(
            window,text=vVersion).grid(row=3,column=2)
    else:
        window.destroy()
        print("Hmm.. We seem to have an error, I've shut the program down to stop further issues.")
        exit()
    vCount = vCount+1
    
def play():
    return

def settings():
    backloop = False
    window.destroy()

    global window2
    window2 = Tk()
    window2.title("Schlange ¦ Settings")
    window2.geometry("200x150")

    lbl = Label(
        window2,
        text="Welcome to Schlange Settings",
        fg = "black",
        bg="gray"
    ).pack()

    btn = Button(
        window2,
        text="Back to home",
        command=exitSettings).pack()
    if backloop == True:
        print("Hmm.. We seem to have an error, I've shut the program down to stop further issues.")
        exit()

def exitSettings():
    backloop = True
    window2.destroy()
    enterHome()

enterHome()
