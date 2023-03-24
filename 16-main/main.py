from tkinter import *
import time
import pygame

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
            home_screen()
            return "This has been accepted.. loading game."

def newGame2(username):
    pygame.init()
    dis=pygame.display.set_mode((400,300))
    pygame.display.update()
    pygame.quit()
    quit()


def newGame(username):
    cScore = 0
    window2 = Tk()
    label = Label(
        text = f'Your score is currently {cScore}',
        foreground = "grey",
        background = "black"
    ).pack(side=TOP)
    """pygame.init()
    dis=pygame.display.set_mode((400,300))
    pygame.display.update()
    pygame.quit()"""

def home_screen():
    window = Tk()
    window.title("Schlange ¦ Entry")
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

    def saveEntry(): # does not work for some reason
        username = unEntry.get(1, "ERROR")
        print(username)
        if len(username) < 2:
            print("This username is not accepted")
        else:
            if len(username) > 9:
                print("This username is not accepted")
            else:
                window.destroy()
                newGame(username)

    unEntry = Text(window, height=10, width=40)
    unEntry.pack(side=TOP)

    etr = Button(
        window,
        text="Submit",
        command=saveEntry)
    etr.pack(side=TOP)

    window.mainloop()

def enterHome(username):
    window2 = Tk()
    window2.title(f'Schlange ¦ Home Screen ¦ {username}')
    window2.geometry("500x400")
    lbl = Label(
        window2,
        text="Test").pack()
    window2.mainloop()

newUsername(input("Enter username "))

    
