
from tkinter import ttk
import ctypes

# Create five buttons
from tkinter import ttk
import tkinter as tk
import ctypes
from wh40k import *

root = tk.Tk()

#Bestimme die Größe des Bildschirms
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

#Berechne die gewünschte Fenstergröße
window_width = screen_width // 2
window_height = screen_height // 2

#Positioniere das Fenster in der Mitte des Bildschirms
x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2

#Setze die Fenstergröße und Position
root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

#Ändere die Hintergrundfarbe des Fensters
root.configure(bg='light blue')

#Erzeuge fünf Buttons
abilitiesButton = tk.Button(root, text="abilities", command=lambda: open_data_window("select * from abilities"), width=20, height=4)
factionButton = tk.Button(root, text="faction", command=lambda: open_data_window("select * from faction"), width=20, height=4)
keywordButton = tk.Button(root, text="keywords", command=lambda: open_data_window("select * from keywords"), width=20, height=4)
statsheetsButton = tk.Button(root, text="statsheet", command=lambda: open_data_window("SELECT * FROM statsheet join units on statsheet.id = units.id"), width=20, height=4)
unitButton = tk.Button(root, text="units", command=lambda: open_data_window("select * from units"), width=20, height=4)
weaponButton = tk.Button(root, text="weapons", command=lambda: open_data_window("select * from weapons"), width=20, height=4)

#Platziere die Buttons im Grid-Layout
abilitiesButton.grid(row=0, column=0, padx=10, pady=10)
factionButton.grid(row=0, column=1, padx=10, pady=10)
keywordButton.grid(row=0, column=2, padx=10, pady=10)
statsheetsButton.grid(row=0, column=3, padx=10, pady=10)
unitButton.grid(row=0, column=4, padx=10, pady=10)
weaponButton.grid(row=0, column=5, padx=10, pady=10)

#Zentriere die Buttons horizontal im Fenster
root.grid_columnconfigure((0, 1, 2, 3, 4, 5), weight=1)

#Zentriere die Buttons vertikal im Fenster
root.grid_rowconfigure(0, weight=1)

#Starte die Haupt-Tkinter-Ereignisschleife
root.mainloop()
