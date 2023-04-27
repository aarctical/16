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
    PlayBtn = Button(text="Play",relief=RIDGE,width=20,height=3, fg="green", command=play).grid(row=0,column=1) 
 
    # This will make the 'Settings' Label and its Icon   
    SettingsLbl = Label(image=icon1,relief=RIDGE,bg="white").grid(row=1,column=0)
    SettingsBtn = Button(text="Settings",relief=RIDGE,width=20,height=3, fg="gray", command=settings).grid(row=1,column=1)

    # This will make the 'Version' Label and its Icon
    VersionLbl = Label(image=icon3,relief=RIDGE,bg="white").grid(row=2,column=0)
    VersionBtn = Button(text="Show/Hide Version",relief=RIDGE,width=20,height=3, fg="blue", command=version).grid(row=2,column=1)

    # This will make the 'Exit' Label and its Icon
    ExitLbl = Label(image=icon2,relief=RIDGE,bg="white").grid(row=3,column=0)
    ExitBtn = Button(text="Exit",relief=RIDGE,width=20,height=3, fg="red", command=leave).grid(row=3,column=1)
        
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
    
def version(): # This is the version command that will show the game version
    t1 = time.time() # Calculates the current time and stores it
    global vCount # Allows referencing of the vCount variable
    global vVersion # Allows referencing of the vVersion variable
    if vCount % 2 != 0: # If the click count modulus (check for remainder) 2 (even number) does not equal 0 then
        vlbl = Label( # Create new label for blanking the version
            window,
            text="                             ").grid(row=3,column=2)
    elif vCount % 2 == 0: # Else if the click count modulus 2 equals 0 then
        vlbl = Label( # Create new label for the version
            window,text=vVersion).grid(row=3,column=2) # Using the vVersion variable already defined
    else: # If there is an error, or the count has surpassed python's limit then
        window.destroy() # This will destroy the current screen
        print("Hmm.. We seem to have an error, I've shut the program down to stop further issues.") # This will print out the error message
        exit() # This will exit the game
    vCount = vCount+1 # This incriments the current count of vCount to allow it to be passed again
    t2 = time.time()-t1 # This takes the current time and calculates an execute time
    print('>> Window version loaded in', t2) # This prints the execute time
    
def play():
    return

def saveUserEntry(): # This defines the save username entry that is referenced in settings
    backloop = False # Sets the default error catcher to false
    global uEtr # Globalises the uEtr variable so it can be referenced within this function
    currentUser = uEtr.get() # Sets a variable to the contents of the uEtr (User Entry)
    print(currentUser) # This is just a developer tool to see if the username is being caught properly
    global flbl 
    flbl = Label(
        window,
        text="").pack() # This label creates a spacer between the top of the window and the first label
    if len(currentUser) < 2 or len(currentUser) > 9: # If the entry they have provided does not meet criteria
        flbl = Label(
            window,
            text="This username is not accepted!",
            fg="red").pack() # Return that the username is not accepted
    elif len(currentUser) > 1 and len(currentUser) < 10: # If the entry does meet criteria
        global verifiedUser # Global the variable so it can be referenced
        verifiedUser = currentUser.strip() # Set the verifiedUser to the entry box content (With no whitespace)
        print(verifiedUser) # Developer tool to see if it has been caught properly
        flbl = Label(
            window,
            text="This username is accepted!",
            fg="green").pack() # Return the username is accepted and they can use that username
    else:
        backloop = True # If none of those conditions meet, the error catcher sets to true
    if backloop == True: # If the error catcher is true
        window.destroy() # Stops the window
        print("Oh no. You've broken me again? That's it... We're over!") # Sends a unique error code to the console
        exit() # Exits the game to stop further errors
        

def settings(): # Defines the settings function
    t1 = time.time() # Takes the current time
    global window # Globalises window so it can be referenced
    backloop = False # Sets the error catcher to false
    window.destroy() # Closes the home screen

    window = Tk() # Defines new screen for settings
    window.title(f'{gName} | Settings') # Sets the title of the window
    window.geometry("500x250") # Sets the geometry of the window

    lbl = Label(
        window,
        text="Welcome to Schlange Settings",
    ).pack() # Generates a label for the screen

    btn = Button( # This button allows the user to go back to the home screen
        window,
        text="Back to home",
        fg="blue",
        command=exitSettings).pack() # Generates a button for the screen with the command exitSettings
    if backloop == True: # Error catching
        print("Hmm.. We seem to have an error, I've shut the program down to stop further issues.")
        exit()

    ulbl = Label( # Generates a label for the username
        window,
        text="Player username").pack()
    global uEtr # Allows other functions to call this data set
    uEtr = Entry(
        window,
        )
    uEtr.pack() # Creates an entry box to allow the user to input a username
    
    tsLbl = Label(
        window,
        text="Snake difficulty"
    ).pack()
    tsBtn1 = Button(
        window,
        text="Easy",
        fg="Blue"
    ).pack()
    tsBtn2 = Button(
        window,
        text="Hard",
        fg="red"
    ).pack()

    sEtr = Button( # Creates a button to allow the user to save their username
    window,
    text="Save Settings",
    command=saveUserEntry).pack() # Calls function saveUserEntry --> Saves the username locally

    t2 = time.time()-t1 # Saves current time and takes away from the start time
    print('>> Window settings loaded in', t2) # Returns the load time to the console

def exitSettings(): # Creates function to leave settings
    backloop = True # Enables the error catcher
    window.destroy() # Stops the settings window
    enterHome() # Re-calls the home screen

def play(): # Creates function for the play button
    global window # Allows referencing of variable --> Window
    global verifiedUser # Allows referencing of variable --> verifiedUser (Current User)
    global gName # Allows referencing of variable --> gName (Game Name)
    global vVersion # Allows referencing of variable --> vVersion (Game version)

    window.destroy() # Closes the homescreen

    pygame.init() # Initialises the pygame window
     
    # These variables define colours used in Schlange by an RGB assignment

    white = (255, 255, 255) 
    black = (0, 0, 0)
    green = (0, 255, 0)

    w = 600
    h = 400
     
    window = pygame.display.set_mode((w, h))
    if verifiedUser != None:
        pygame.display.set_caption(f'{gName} | {verifiedUser}')
    else:
        pygame.display.set_caption(f'{gName}')
        
    clock = pygame.time.Clock()
     
    block = 10
    speed = 15
     
    font = pygame.font.SysFont("bahnschrift", 25)
    
    def our_snake(block, list):
        for x in list:
            pygame.draw.rect(window, black, [x[0], x[1], block, block])
     
     
    def message(msg, color):
        mesg = font.render(msg, True, color)
        window.blit(mesg, [w / 6, h / 3])
     
    def gameLoop():
        global verifiedUser
        game_over = False
        game_close = False
        backloop = False
     
        x1 = w / 2
        y1 = h / 2
     
        x1_change = 0
        y1_change = 0
     
        list = []
        length = 1
     
        foodx = round(random.randrange(0, w - block) / 10.0) * 10.0
        foody = round(random.randrange(0, h - block) / 10.0) * 10.0
     
        while not game_over:
     
            while game_close == True:
                window.fill(white)

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
                
                display_text(window, text, (150,150), font, (255,0,0))
                pygame.display.update()
     
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_x:
                            game_over = True
                            finalscore = str(length-1)
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
                        x1_change = -block
                        y1_change = 0
                    elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                        x1_change = block
                        y1_change = 0
                    elif event.key == pygame.K_w or event.key == pygame.K_UP:
                        y1_change = -block
                        x1_change = 0
                    elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                        y1_change = block
                        x1_change = 0
     
            if x1 >= w or x1 < 0 or y1 >= h or y1 < 0:
                game_close = True
            x1 += x1_change
            y1 += y1_change
            window.fill(white)
            pygame.draw.rect(window, green, [foodx, foody, block, block])
            snake_Head = []
            snake_Head.append(x1)
            snake_Head.append(y1)
            list.append(snake_Head)
            if len(list) > length:
                del list[0]
     
            for x in list[:-1]:
                if x == snake_Head:
                    game_close = True
     
            our_snake(block, list)
     
            pygame.display.update()
     
            if x1 == foodx and y1 == foody:
                foodx = round(random.randrange(0, w - block) / 10.0) * 10.0
                foody = round(random.randrange(0, h - block) / 10.0) * 10.0
                length += 1
                if verifiedUser != None:
                        pygame.display.set_caption(f'{gName} | {verifiedUser} | Score: '+str(length-1))
                else:
                    pygame.display.set_caption(f'{gName} | Score: '+str(length-1))
     
            clock.tick(speed)
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
