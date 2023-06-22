import mysql.connector
from tkinter import *

cnx = mysql.connector.connect(user='root', password='root',
                              host='localhost',
                              database='warhammer40k')
cnx.close()


def openNewWindow(win):
    # Toplevel object which will
    # be treated as a new window
    newWindow = Toplevel(win)

    # sets the title of the
    # Toplevel widget
    newWindow.title("New Window")

    # sets the geometry of toplevel
    newWindow.geometry("200x200")

    # A Label widget to show in toplevel
    Label(newWindow,
          text="This is a new window").pack()
