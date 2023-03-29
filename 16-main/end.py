from tkinter import *
import time

global gName
gName = "Schlange"

def saveSettings():
    window2.destroy()
    # More settings add here

def settingsMenu():
    window2 = Tk()
    window2.title("Schlange ¦ Settings")
    window2.geometry("200x150")

    lbl = Label(
        window2,
        text="Welcome to Schlange Settings",
        fg = "black",
        bg="gray"
    ).pack()
def endGame():
    quit()
def showVersion():
    lbl = Label(
        window2,
        text="Version 1").pack()

"""etr = Button(
    window2,
    text="Start New Game",
    command=saveUserEntry)
etr.pack(side=TOP)

set = Button(
    window2, 
    text="Settings",
    command=settingsMenu)
set.pack()"""

def enterHome():
    window2 = Tk()
    window2.title(f'{gName} ¦ Home Screen')
    window2.geometry("500x400")

    lbl = Label(
        window2,
        text=f'Welcome to the {gName} homescreen'
    ).pack()

    btn = Button(
        window2,
        text="Settings",
        command=settingsMenu
    ).pack()

    btn2 = Button(
        window2,
        text="Exit",
        command=endGame
    ).pack()

    btn3 = Button(
        window2,
        text="Version",
        command=showVersion
    ).pack()

    global unEntry
    unEntry = Text(window, height=10, width=40).pack(side=TOP)

    btn4 = Button(
        window2,
        text="New Game",
        command=newGame
    ).pack()

    window2.mainloop()

enterHome()
