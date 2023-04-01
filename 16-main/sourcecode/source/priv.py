    lbl = Label(
        window2,
        text=f'Welcome to the {gName} homescreen'
    ).pack()

    lbl2 = Label(
        window2,
        image=IconS).pack(side=LEFT)
    lbl3 = Label(
        window2,
        image=IconE).pack(side=LEFT)
    lbl4 = Label(
        window2,
        image=IconV).pack(side=LEFT)
    lbl5 = Label(
        window2,
        image=IconP).pack(side=LEFT)

    btn = Button(
        window2,
        text="Settings",
        command=settingsMenu
    ).pack(side=RIGHT)

    btn2 = Button(
        window2,
        text="Exit",
        command=endGame
    ).pack(side=RIGHT)

    btn3 = Button(
        window2,
        text="Version",
        command=showVersion
    ).pack(side=RIGHT)

    btn4 = Button(
        window2,
        text="New Game",
        command=newGame
    ).pack(side=RIGHT)