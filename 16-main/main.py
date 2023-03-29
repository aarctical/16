from tkinter import *
import time
# import pygame as game

gName = 'Schlange'

"""def newGame2(username):
    pygame.init()
    dis=pygame.display.set_mode((400,300))
    pygame.display.update()
    pygame.quit()
    quit()"""


def newGame(username):
    cScore = 0
    window2 = Tk()

    label = Label(
        text = f'Your score is currently {cScore}',
        foreground = "grey",
        background = "black"
    )    

class user:
    global window
    global window2
    global window3

    def homescreen():
        window = Tk()
        window.title("Schlange ¦ Homescreen")
        window.geometry('200x150')
        
        lbl = Label(
            window,
            text="Welcome to Schlange, to continue please enter a username",
            fg = "black",
            bg = "gray")
        lbl.pack(side=TOP)
        lbl = Label(
            window,
            text="")
        lbl.pack(side=TOP)

        window.mainloop()

    def saveUserEntry(): # does not work for some reason
        username = unEntry.get(1.0, END)
        print(username)
        if len(username) < 2:
            print("This username is not accepted")
        if len(username) > 9:
            print("This username is not accepted")
        else:
            window.destroy()
            enterHome(username)

    def saveSettings():
        window3.destroy()

    def settingsMenu():
        window3 = Tk()
        window3.title("Schlange ¦ Settings")
        window3.geometry("200x150")

        lbl = Label(
            window3,
            text="Welcome to Schlange Settings",
            fg = "black",
            bg="gray"
        )
        lbl.pack()
    def saveEntry():        
        global unEntry
        unEntry = Text(window, height=10, width=40)
        unEntry.pack(side=TOP)

    etr = Button(
        window3,
        text="Start New Game",
        command=saveUserEntry)
    etr.pack(side=TOP)

    set = Button(
        window3, 
        text="Settings",
        command=settingsMenu)
    set.pack()

def enterHome(username):
    window2 = Tk()
    window2.title(f'Schlange ¦ Home Screen ¦ {username}')
    window2.geometry("500x400")

    lbl = Label(
        window2,
        text=f'Welcome to the schlange homescreen {username}'
    ).pack()

    btn = Button(
        window2,
        text="settings",
        command=settingsMenu
    ).pack()

    btn2 = Button(
        window2,
        text="Exit",
        command=quit()
    ).pack()

    btn3 = Button(
        window2,
        text="Version",
        command=showVersion
    ).pack()

    window2.mainloop()

def newUsername(x):
    noUser = True
    while noUser == True: 
        if len(x) < 3:
            return "This username is not accepted"
        if len(x) > 9:
            return "This username is not accepted"
        if len(x) > 2 and len(x) < 10:
            noUser = False
            global username
            username = x
            user.homescreen()
            return "This has been accepted.. loading game."

class game:
    def __init__(user):
        user.username = username
        user.currentScore = 0
        print(f'Welcome to {gName}, {username}')

    def newGame(user):
        game.init()
        window_width = 800
        window_height = 600
        window = game.display.set_mode((window_width, window_height))
        game.display.update()
        game.display.set_caption('Snake')

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
            clock.tick(30)
        message('You lost', red)
        game.display.update()
        time.sleep(3)
        game.quit()
        quit()

newUsername(input("Enter username "))

    
