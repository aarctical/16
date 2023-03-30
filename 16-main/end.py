from tkinter import * # GUI Directory for python
from tkinter import ttk
import time # Time function for calculating clock speeds
from PIL import Image, ImageTk # Image handling (Icons)
import pygame # Game function for the snake game
import random # Function to detemine where food is located (snake game)

gName = "Schlange" # Game Name
vCount = 0 # This is the version count (For MOD show/hide Function)
vVersion = "Version: 4.0.3" # Version number, manually updated
currentUser = None # Default fallback for functions later on
verifiedUser = None # Default fallback for functions later on

def enterHome(): # This is the home screen
    t1 = time.time() # Takes current time to calculate initialisation times
    global window # Allows the window to be called/modified outside of this function
    global gName # Allows reference of the gName variable
    global verifiedUser # Allows reference of the user variable
    
    # The following 'window' objects start a new window utlising Tkinter

    window = Tk() # Initalises window
    if verifiedUser == None: # Checks if a user is signed in
        window.title(f'{gName} | Home Screen') # If no user: no username shows
    elif verifiedUser != None:
        window.title(f'{gName} | Home Screen | {verifiedUser}') # If user: show username on title
    window.geometry("500x250") # Size of the window

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
        text=f'Welcome to {gName}').grid(row=0,column=2) # This creates a label for the Homescreen welcoming the User to the game
    lbl2 = Label(
        relief=RIDGE,
        text="""How to play:
        Select a button
        Start a new game by pressing \'Play\'
        Exit the game by pressing exit""").grid(row=1,column=2) # This provides a box with instructions on how to play
    lbl3 = Label(
        image=icon5).grid(row=2,column=2) # Welcoming image (hmm)

    t2 = time.time()-t1 # Takes current time and minuses from initialising time -> This is used to see how long windows are taking to load (locally)
    print('>> Window home loaded in', t2) # Prints the above information to the console

    window.mainloop() # Allows the window to run forever unless the breakpoint is reached


def leave(): # This is the exit breakpoint, accessed by the home screen
    t1 = time.time() # Takes current time to calculate initialisation times
    window.destroy() # Shuts the home screen
    print("You seem to have left. Did I upset you? What did I do wrong? I thought you loved me...") # Exit message (See bottom)
    t2 = time.time()-t1 # Takes current time and minuses from initialising time -> This is used to see how long windows are taking to load (locally)
    print('>> Exit executed in', t2) # Prints the above information to the console
    exit() # Break point in the program to stop it running completely (final step in shutdown)
    
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

    pygame.init()
     
    white = (255, 255, 255)
    yellow = (255, 255, 102)
    black = (0, 0, 0)
    red = (213, 50, 80)
    green = (0, 255, 0)
    blue = (50, 153, 213)
     
    dis_width = 600
    dis_height = 400
     
    dis = pygame.display.set_mode((dis_width, dis_height))
    if verifiedUser != None:
        pygame.display.set_caption(f'{gName} | {verifiedUser}')
    else:
        pygame.display.set_caption(f'{gName}')
        
    clock = pygame.time.Clock()
     
    snake_block = 10
    snake_speed = 15
     
    font_style = pygame.font.SysFont("bahnschrift", 25)
    score_font = pygame.font.SysFont("comicsansms", 35)
     
     
    def Your_score(score):
        if verifiedUser != None:
            value = score_font.render(f'{verifiedUser}\'s Score: ' + str(score), True, white)
        else:
            value = score_font.render(f'User\'s Score: ' + str(score), True, white)
        dis.blit(value, [1000, 1000])
     
     
     
    def our_snake(snake_block, snake_list):
        for x in snake_list:
            pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])
     
     
    def message(msg, color):
        mesg = font_style.render(msg, True, color)
        dis.blit(mesg, [dis_width / 6, dis_height / 3])
     
    def gameLoop():
        global verifiedUser
        game_over = False
        game_close = False
        backloop = False
     
        x1 = dis_width / 2
        y1 = dis_height / 2
     
        x1_change = 0
        y1_change = 0
     
        snake_List = []
        Length_of_snake = 1
     
        foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
        foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
     
        while not game_over:
     
            while game_close == True:
                dis.fill(white)

                text = "You lost!\nSPACE to play again\nX to quit"
                font = pygame.font.SysFont("arialblack",30)
   
                def display_text(surface, text, pos, font, color):
                    collection = [word.split(' ') for word in text.splitlines()]
                    space = font.size(' ')[0]
                    x,y = pos
                    for lines in collection:
                        for words in lines:
                            word_surface = font.render(words, True, color)
                            word_width, word_height = word_surface.get_size()
                            if x + word_width >= 600:
                                x = pos[0]
                                y += word_height
                            surface.blit(word_surface, (x,y))
                            x += word_width + space
                        x = pos[0]
                        y += word_height
                
                display_text(dis, text, (150,150), font, (255,0,0))
                Your_score(Length_of_snake - 1)
                pygame.display.update()
     
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_x:
                            game_over = True
                            finalscore = str(Length_of_snake-1)
                            if verifiedUser == None:
                                pygame.quit()
                                enterHome()
                            elif verifiedUser != None:
                                file = open('scores.txt','w')
                                file.write(verifiedUser+' | '+finalscore)
                                file.close()
                                pygame.quit()
                                enterHome()
                        if event.key == pygame.K_SPACE:
                            gameLoop()
                        else:
                            backloop = True
            if backloop == True:
                game_over = True
                print("Again? Really, you\'re busting my balls here man, let me fix this for you.")
                exit()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                        x1_change = -snake_block
                        y1_change = 0
                    elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                        x1_change = snake_block
                        y1_change = 0
                    elif event.key == pygame.K_w or event.key == pygame.K_UP:
                        y1_change = -snake_block
                        x1_change = 0
                    elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                        y1_change = snake_block
                        x1_change = 0
     
            if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
                game_close = True
            x1 += x1_change
            y1 += y1_change
            dis.fill(white)
            pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
            snake_Head = []
            snake_Head.append(x1)
            snake_Head.append(y1)
            snake_List.append(snake_Head)
            if len(snake_List) > Length_of_snake:
                del snake_List[0]
     
            for x in snake_List[:-1]:
                if x == snake_Head:
                    game_close = True
     
            our_snake(snake_block, snake_List)
            Your_score(Length_of_snake - 1)
     
            pygame.display.update()
     
            if x1 == foodx and y1 == foody:
                foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                Length_of_snake += 1
                if verifiedUser != None:
                        pygame.display.set_caption(f'{gName} | {verifiedUser} | Score: '+str(Length_of_snake-1))
                else:
                    pygame.display.set_caption(f'{gName} | Score: '+str(Length_of_snake-1))
     
            clock.tick(snake_speed)
        quit()
     
    gameLoop()


enterHome()


# Leave messages
"""

    Hmm.. We seem to have an error, I've shut the program down to stop further issues.
    >> This result is when a logic  or math operation fails to work, so it shuts the program to stop other errors

    You seem to have left. Did I upset you? What did I do wrong? I thought you loved me...
    >> This result is when you choose to close the game, either in the Home Screen, or during the game

    Oh no. You've broken me again? That's it... We're over!
    >> This result is when an undefined variable is unexpected during editing the settings

    Again? Really, you're busting my balls here man, let me fix this for you.
    >> This result is when a user ends the game, and gives a variable outside the required scope

"""
