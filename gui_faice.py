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


def get_jobs():
    global K
    global T
    string = K.get()
    T.insert(0, string)


# root window
root = Tk()
root.title('Upwork job searcher')

# frames
navbarFrame = Frame(root, height=60, width=800, bg='gray')
resultsFrame = Frame(root, height=200, width=400, bg='yellow')
keywordsFrame = Frame(root, height=200, width=400, bg='blue')

navbarFrame.pack(side='top', fill='x')
resultsFrame.place(x=50, y=50, width=200, height=200)
keywordsFrame.pack(side='right', fill='x')

# results placement
T = Listbox(resultsFrame, height=30, width=40)
S = Scrollbar(resultsFrame, orient="vertical")
L = Label(resultsFrame, text="SEARCH RESULTS:")
L.pack(side='top')
S.pack(side=RIGHT, fill=Y)
T.pack(side=LEFT, fill=Y)
S.config(command=T.yview)
T.config(yscrollcommand=S.set)
T.insert(END, "http://hello.com")

# keywords placement

L = Label(keywordsFrame, text="input keywords to search")
L.pack(side='top')

K = Entry(keywordsFrame)
K.pack(side=TOP)
K.focus_set()

# navbar buttons
preferencesBtn = Button(navbarFrame, text='Preferences')
quitBtn = Button(navbarFrame, text='Quit')
# navbar button process
preferencesBtn.bind("<Button-1>", Preferences)
quitBtn.bind("<Button-1>", Quit)
# navbar buttons placement
preferencesBtn.place(x=10, y=10, width=400, height=40)
quitBtn.place(x=450, y=10, width=120, height=40)
# keywordsFrame button
searchBtn = Button(keywordsFrame, text='SEARCH', command=get_jobs)
searchBtn.pack(side=RIGHT)


root.mainloop()