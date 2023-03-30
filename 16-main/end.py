from tkinter import * # GUI Directory for python
from tkinter import ttk
import time # Time function for calculating clock speeds
from PIL import Image, ImageTk # Image handling (Icons)
import pygame as game

gName = "Schlange" # Game Name
vCount = 0 # This is the version count (For MOD show/hide Function)
vVersion = "Version: 4.0.3"

""" VARIABLES """
currentUser = None
verifiedUser = None

def closeCurrent():
    window.destroy()

def saveSettings():
    window.destroy()
    # More settings add here

def enterHome(): # This is the home screen
    t1 = time.time()
    global window # Allows the window to be called/modified outside of this function
    global gName # Allows reference of the gName variable
    global verifiedUser
    
    # The following 'window' objects start a new window utlising Tkinter

    window = Tk()
    if verifiedUser == None:
        window.title(f'{gName} | Home Screen')
    elif verifiedUser != None:
        window.title(f'{gName} | Home Screen | {verifiedUser}')
    window.geometry("500x250")

    # The following Icons are pictures used for the Labels on the home screen

    icon1 = PhotoImage(file='./img/settings.png')
    icon2 = PhotoImage(file='./img/exit.png')
    icon3 = PhotoImage(file='./img/version.png')
    icon4 = PhotoImage(file='./img/play.png')
    icon5 = PhotoImage(file='./img/hmm.png')

    # This will make the 'Play' Label and its Icon
    PlayLbl = Label(image=icon4,relief=RIDGE,bg="white").grid(row=0,column=0)
    PlayBtn = Button(text="Play",relief=RIDGE,width=20,height=3, command=play).grid(row=0,column=1) 
 
    # This will make the 'Settings' Label and its Icon   
    SettingsLbl = Label(image=icon1,relief=RIDGE,bg="white").grid(row=1,column=0)
    SettingsBtn = Button(text="Settings",relief=RIDGE,width=20,height=3, command=settings).grid(row=1,column=1)

    # This will make the 'Version' Label and its Icon
    VersionLbl = Label(image=icon3,relief=RIDGE,bg="white").grid(row=2,column=0)
    VersionBtn = Button(text="Show/Hide Version",relief=RIDGE,width=20,height=3, command=version).grid(row=2,column=1)

    # This will make the 'Exit' Label and its Icon
    ExitLbl = Label(image=icon2,relief=RIDGE,bg="white").grid(row=3,column=0)
    ExitBtn = Button(text="Exit",relief=RIDGE,width=20,height=3, command=leave).grid(row=3,column=1)
        
    # ^^ The 'GRID' placement of Tkinter allows me to place objects in a uniformed cell no matter the window size ^^
    
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

    t2 = time.time()-t1
    print('>> Window home loaded in', t2)

    window.mainloop()


def leave():
    t1 = time.time()
    window.destroy()
    print("You seem to have left. Did I upset you? What did I do wrong? I thought you loved me...")
    t2 = time.time()-t1
    print('>> Exit executed in', t2)
    exit()
    
def version():
    t1 = time.time()
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
    t2 = time.time()-t1
    print('>> Window version loaded in', t2)
    
def play():
    return

def saveUserEntry():
    backloop = False
    global uEtr
    currentUser = uEtr.get()
    print(currentUser)
    global flbl
    flbl = Label(
        window,
        text="").pack()
    if len(currentUser) < 2 or len(currentUser) > 9:
        flbl = Label(
            window,
            text="This username is not accepted!",
            fg="red").pack()
    elif len(currentUser) > 1 and len(currentUser) < 10:
        global verifiedUser
        verifiedUser = currentUser.strip()
        print(verifiedUser)
        flbl = Label(
            window,
            text="This username is accepted!",
            fg="green").pack()
    else:
        backloop = True
    if backloop == True:
        window.destroy()
        print("Oh no. You've broken me again? That's it... We're over!")
        exit()
        

def settings():
    t1 = time.time()
    global window
    backloop = False
    window.destroy()

    window = Tk() 
    window.title(f'{gName} | Settings')
    window.geometry("500x250")

    lbl = Label(
        window,
        text="Welcome to Schlange Settings",
    ).pack()

    btn = Button(
        window,
        text="Back to home",
        fg="blue",
        command=exitSettings).pack()
    if backloop == True:
        print("Hmm.. We seem to have an error, I've shut the program down to stop further issues.")
        exit()

    ulbl = Label(
        window,
        text="Player username").pack()
    global uEtr
    uEtr = Entry(
        window,
        )
    uEtr.pack()
    
    sEtr = Button(
        window,
        text="Save username",
        command=saveUserEntry).pack()

    t2 = time.time()-t1
    print('>> Window settings loaded in', t2)

def exitSettings():
    backloop = True
    window.destroy()
    enterHome()

def play():
    global window
    global verifiedUser
    global gName
    global vVersion

    window.destroy()

    t1 = time.time()
    game.init()
    window_width = 800
    window_height = 600
    window = game.display.set_mode((window_width, window_height))
    game.display.update()
    game.display.set_caption(gName)

    white = (255,255,255)
    black = (0,0,0)
    blue = (0,0,255)
    red = (255,0,0)

    x1 = 300
    y1 = 300
    x1_change = 0
    y1_change = 0
    clock = game.time.Clock()
    
    game_over = False
    font_style = game.font.SysFont(None, 50, bold=True, italic=True)
    t2 = time.time()-t1
    t3 = time.time()
    def message(msg, colour):
        mesg = font_style.render(msg, True, colour)
        window.blit(mesg, [window_width/2, window_height/2])

    while not game_over:
        for event in game.event.get():
            if event.type==game.QUIT:
                game_over = True
            if event.type == game.KEYDOWN:
                if event.key == game.K_LEFT:
                    x1_change = -10
                    y1_change = 0
                elif event.key == game.K_RIGHT:
                    x1_change = 10
                    y1_change = 0
                elif event.key == game.K_UP:
                    x1_change = 0
                    y1_change = -10
                elif event.key == game.K_DOWN:
                    x1_change = 0
                    y1_change = 10
        if x1 >= window_width or x1 < 0 or y1 >= window_height or y1 < 0:
            game_over = True
            
        x1 += x1_change
        y1 += y1_change
        window.fill(white)
        game.draw.rect(window, black, [x1, y1, 10, 10])
        game.display.update()
        clock.tick(60)
        
    message('You lost', red)
    game.display.update()
    t4 = time.time()-t3
    time.sleep(3)
    game.quit()
    enterHome()

enterHome()


# Leave messages
"""

    Hmm.. We seem to have an error, I've shut the program down to stop further issues.
    >> This result is when a logic  or math operation fails to work, so it shuts the program to stop other errors

    You seem to have left. Did I upset you? What did I do wrong? I thought you loved me...
    >> This result is when you choose to close the game, either in the Home Screen, or during the game

    Oh no. You've broken me again? That's it... We're over!
    >> This result is when an undefined variable is unexpected during editing the settings

"""
