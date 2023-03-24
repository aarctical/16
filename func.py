from readline import insert_text
from tkinter import *
import time
import random

import coreUser.sql as sql
import func

userBase = []
count = 0

def baseScreen(title, size):
    screen = Tk()
    screen.title(title)
    screen.size(size)
    label1 = Tk.label("hi").pack()
    screen.mainloop()

class error():
    def existUser():
        print("This user is already in the database! Try a different username or email!")
    def password():
        print("This is the incorrect password for this account, try again?")
        count = count + 1
    def badPassword():
        print("This password is not strong enough! Your password must be over 5 characters!")
    def badUser():
        print("This user is not found in the userBase, create a user instead?")

class allUser():
    def __init__(un, email, fname, pw, highscore):
        newUsername = un
        newEmail = email
        newFirst = fname
        newPass = pw
        highscore = 0
    def newUser(un, email, fname, pw, highscore):
        un = un
        email = email
        fname = fname
        pw = pw
        if un or email in userBase:
            error.existUser()
        if len(pw) < 5:
            error.badPassword()
        
class mainGame():
    def __init__(user, highscore):
        if user not in userBase:
            error.badUser()
    
        if highscore == 0:
            highscore = 1
    def login(un, pw):
        if un not in userBase:
            error.badUser()
        elif sql.checkUser != True:
            return