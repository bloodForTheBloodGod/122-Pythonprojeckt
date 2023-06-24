
from tkinter import ttk
import ctypes
from wh40k import  *
root = tk.Tk()

# Create five buttons
abilitiesButton = tk.Button(root, text="abilities", command=lambda: open_data_window("select * from abilities"))
factionButton = tk.Button(root, text="faction", command=lambda: open_data_window("select * from faction"))
keywordButton = tk.Button(root, text="keywords", command=lambda: open_data_window("select * from keywords"))
statsheetsButton = tk.Button(root, text="statsheet", command=lambda: open_data_window("SELECT * FROM statsheet join units on statsheet.id = units.id"))
unitButton = tk.Button(root, text="units", command=lambda: open_data_window("select * from units"))
weaponButton = tk.Button(root, text="weapons", command=lambda: open_data_window("select * from weapons"))


# Pack the buttons
abilitiesButton.pack()
factionButton.pack()
keywordButton.pack()
statsheetsButton.pack()
unitButton.pack()
weaponButton.pack()

# Start the main tkinter event loop
root.mainloop()