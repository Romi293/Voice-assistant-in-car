# from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox

import main

# True if REA is running, False if not
running = False

'''
def changeBtnState():
    if button.configure(image=startIcon):
        print("OK")
        button['image'] = pauseIcon
        main.run_REA()
    else:
        button['image'] = startIcon
'''


def run():
    print("Button clicked!")
    main.run_REA()


def exit():
    print("Exit button clicked")
    main.exit_REA()


def openWindow():
    window = tk.Tk()
    window.configure(background='black')
    window.geometry('600x400')
    window.title('REA')

    startIcon = tk.PhotoImage(file=r"pics/start_icon.png")  # with tk
    pauseIcon = tk.PhotoImage(file=r"pics/pause_icon.png")  # with tk
    logoIcon = ImageTk.PhotoImage(file=r"pics/logo.png")  # with PIL.ImageTk

    ReaImg = tk.Label(window, image=logoIcon, height=90, width=90)  # set image size
    ReaImg.place(x=10, y=10)  # set image position

    button = tk.Button(window, image=startIcon, command=run, height=25, width=25)  # set button size
    button.place(x=250, y=350)  # set button position
    # startBtn.pack()

    buttonExit = tk.Button(window, image=pauseIcon, command=exit, height=25, width=25)  # set button size
    buttonExit.place(x=300, y=350)  # set button position
    # startBtn.pack()

    window.mainloop()
