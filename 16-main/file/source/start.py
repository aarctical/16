import pygame as game
import time

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

from tkinter import *
import os
import time

def counter(func):
    def wrapper():
        t1 = time.time()
        func()
        t2 = time.time()-t1
        print(f'{func.__name__} ran in '\
              f' {t2} seconds')
    return wrapper

@counter
def gameHome():
    screen3.destroy()
    lobby()

@counter
def game():
    screen.destroy()
    global screen3
    screen3 = Tk()
    screen3.geometry("1920x1080")
    screen3.title("Game")
    #screen3.iconbitmap('E:/Pictures/live.ico') // broken
    Button(text = "Back to home", width = "50", height = "2", bg = "white", fg = "black", command = gameHome).pack()

@counter
def settingsHome():
    screen2.destroy()
    lobby()

@counter
def settings():
    screen.destroy()
    global screen2
    screen2 = Tk()
    screen2.geometry("1920x1080")
    screen2.title("Settings")
    #screen2.iconbitmap('E:/Pictures/live.ico') // broken
    Button(text = "Back to home", width = "50", height = "2", bg = "white", fg = "black", command = settingsHome).pack()

@counter
def lobby():
    global screen
    screen = Tk()
    screen.geometry("1920x1080")
    screen.title("Home Screen")
    #screen.iconbitmap('E:/Pictures/live.ico') // broken
    Label(text = "Game Home screen", bg = "grey", fg = "white", width = "1920", height = "5", font = ("Calibri", 15)).pack()
    Label(text = "").pack()
    Button(text = "Start New Game", width = "50", height = "2", bg = "white", fg = "black", command = game).pack(padx=900, pady=0, side=TOP)
    Label(text = "").pack()
    Button(text = "Settings", width = "50", height = "2", bg = "white", fg = "black", command = settings).pack(padx=900, pady=0, side=TOP)
    screen.mainloop
lobby()

