from Tkinter import *


def Quit(ev):
    global root
    root.destroy()


def Preferences(ev):
    global root
    # create child window
    win = Toplevel(root)
    # display message
    message = "This is the preferences window"
    Label(win, text=message).pack(padx=100, pady=100)
    # preferences window placement
    x = root.winfo_rootx()
    y = root.winfo_rooty()
    geom = "+%d+%d" % (x+100, y + 100)
    win.geometry(geom)
    # quit child window and return to root window
    # the button is optional here, simply use the corner x of the child window
    Button(win, text='OK', command=win.destroy).pack()

# root window
root = Tk()
root.title('Upwork job searcher')

# top navbar
panelFrame = Frame(root, height=60, bg='gray')
textFrame = Frame(root, height=340, width=800)

panelFrame.pack(side='top', fill='x')
textFrame.pack(side='bottom', fill='both', expand=1)

# keyword placement

listNodes = Listbox(root, height=50, width=40)
S = Scrollbar(root, orient="vertical")

S.pack(side=LEFT, fill=Y)
T.pack(side=LEFT, fill=Y)
S.config(command=T.yview)
T.config(yscrollcommand=S.set)
T.insert(END, "http://hello.com")


# navbar buttons
preferencesBtn = Button(panelFrame, text='Preferences')
quitBtn = Button(panelFrame, text='Quit')
# navbar button process
preferencesBtn.bind("<Button-1>", Preferences)
quitBtn.bind("<Button-1>", Quit)
# navbar buttons placement
preferencesBtn.place(x=10, y=10, width=400, height=40)
# saveBtn.place(x=60, y=10, width=40, height=40)
quitBtn.place(x=450, y=10, width=120, height=40)
# navbar buttons placement


root.mainloop()