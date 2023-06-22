from tkinter import *
from tkinter import ttk
import ctypes
from wh40k import  *
win = Tk()
win.title("Mein Fenster")
from functools import partial
# Bildschirmgröße abrufen
user32 = ctypes.windll.user32
screen_width = user32.GetSystemMetrics(0)
screen_height = user32.GetSystemMetrics(1)

# Fenstergröße einstellen
window_width = int(screen_width * 0.8)  # 80% der Bildschirmbreite
window_height = int(screen_height * 0.8)  # 80% der Bildschirmhöhe
x_position = int((screen_width - window_width) / 2)  # Zentriert auf dem Bildschirm
y_position = int((screen_height - window_height) / 2)

win.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

button1 = Button(win, text="weapons", command=partial(openNewWindow,win))
button1.place(x=100, y=100)

button2 = Button(win, text="abilities", command=partial(openNewWindow,win))
button2.place(x=200, y=100)

button3 = Button(win, text="factions", command=partial(openNewWindow,win))
button3.place(x=300, y=100)

button4 = Button(win, text="keywords", command=partial(openNewWindow,win))
button4.place(x=400, y=100)

button5 = Button(win, text="statsheet", command=partial(openNewWindow,win))
button5.place(x=500, y=100)

win.mainloop()
