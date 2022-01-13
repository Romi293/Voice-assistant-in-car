import tkinter as tk
from tk import *
# pip install pillow
from PIL import Image, ImageTk

import main2


def sayHello():
    print("button clicked!")


def openWindow():
    window = tk.Tk()
    window.configure(background='black')

    # title = tk.Label(text="REA", foreground="yellow", width=50, height=50)

    startIcon = tk.PhotoImage(file=r"pics/start.png")  # with tk
    logoIcon = ImageTk.PhotoImage(file=r"pics/logo.png")  # with PIL.ImageTk

    startBtn = tk.Button(window, image=startIcon, command=sayHello(), height=25, width=25)  # set button size
    startBtn.place(x=280, y=300)  # set button position

    ReaImg = tk.Label(window, image=logoIcon, height=90, width=90)  # set image size
    ReaImg.place(x=10, y=10)  # set image position

    window.title("REA")
    window.geometry("600x400")
    window.mainloop()


if __name__ == "__main__":
    openWindow()
