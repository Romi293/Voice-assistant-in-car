# from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox

import main2

# True if REA is running, False if not
running = False

window = tk.Tk()
window.configure(background='black')
window.geometry('600x400')
window.title('REA')


def showMsg():
    print('You clicked the Submit button!')
    main2.run_REA()


startIcon = tk.PhotoImage(file=r"pics/start_icon.png")  # with tk
logoIcon = ImageTk.PhotoImage(file=r"pics/logo.png")  # with PIL.ImageTk

ReaImg = tk.Label(window, image=logoIcon, height=90, width=90)  # set image size
ReaImg.place(x=10, y=10)  # set image position

startBtn = tk.Button(window, image=startIcon, command=showMsg, height=25, width=25)  # set button size
startBtn.place(x=280, y=350)  # set button position
# startBtn.pack()

window.mainloop()
