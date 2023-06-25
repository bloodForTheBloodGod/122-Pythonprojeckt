import mysql.connector
from tkinter import ttk
import tkinter as tk
import re
try:
    db = mysql.connector.connect(user='', password='',
                              host='localhost',
                              database='warhammer40k')
except mysql.connector.Error as e:
    print("Error connecting to the database: please check username and passwort", e)
    # Handle the error appropriately, such as displaying an error message to the user
    # and taking necessary actions.

# Variable to keep track of the currently open cell window
current_cell_window = None


def fetch_data(button_query):
    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Execute a query to fetch all data from the dynamically constructed table
    cursor.execute(button_query)

    # Fetch all the data
    data = cursor.fetchall()

    # Close the cursor
    cursor.close()

    # Return the fetched data
    return data


def open_data_window(button_value):
    # Create a new window
    data_window = tk.Toplevel()

    # Create a search entry widget
    search_entry = ttk.Entry(data_window)
    search_entry.pack(padx=10, pady=10)

    # Create a Canvas widget
    canvas = tk.Canvas(data_window)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Create a Scrollbar widget for vertical scrolling
    scrollbar_y = ttk.Scrollbar(data_window, orient=tk.VERTICAL, command=canvas.yview)
    scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)

    # Create a Scrollbar widget for horizontal scrolling
    scrollbar_x = ttk.Scrollbar(data_window, orient=tk.HORIZONTAL, command=canvas.xview)
    scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)

    # Create a Frame inside the Canvas for scrollable content
    frame = ttk.Frame(canvas)

    # Add the Frame to the Canvas
    canvas.create_window((0, 0), window=frame, anchor=tk.NW)
    try:
        # Fetch the data
        original_data = fetch_data(button_value)
        data = original_data

        # Create labels for column names
        for j, column_name in enumerate(data[0]):
            label = ttk.Label(frame, text=column_name)
            label.grid(row=0, column=j, padx=5, pady=5, sticky='nsew')

        # Insert data into labels
        label_widgets = []
        for i, row in enumerate(data[0:]):
            label_row = []
            for j, value in enumerate(row):
                label = ttk.Label(frame, text=value)
                label.grid(row=i, column=j, padx=5, pady=5, sticky='nsew')
                label.bind('<Button-1>', lambda event, row=i, column=j: show_cell_content(row, column, data))
                label_row.append(label)
            label_widgets.append(label_row)

        # Configure the Scrollbars to work with the Canvas and Frame
        scrollbar_y.configure(command=canvas.yview)
        scrollbar_x.configure(command=canvas.xview)
        canvas.configure(yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set)
    except IndexError:
        print("No data available for the selected button.")
    except Exception as e:
        print("An error occurred:", e)

    # Function to configure the Canvas scroll region based on the Frame size
    def configure_canvas(event):
        canvas.configure(scrollregion=canvas.bbox('all'))

    # Bind the configure_canvas function to the Frame size change event
    frame.bind('<Configure>', configure_canvas)

    # Function to filter the data based on the search text
    def filter_data():
        search_text = search_entry.get()
        if search_text:
            # Clear previous search highlights
            clear_search()

            # Create regex pattern for search
            pattern = re.compile(search_text, re.IGNORECASE)

            # Filter the data based on search
            filtered_data = [data[0]]  # Include the column names in the filtered data
            for row in original_data[1:]:
                if any(pattern.search(str(value)) for value in row):
                    filtered_data.append(row)
            update_labels(filtered_data)
        else:
            update_labels(original_data)

    # Function to update the labels with filtered data
    def update_labels(filtered_data):
        for i, row in enumerate(filtered_data[1:]):
            for j, value in enumerate(row):
                label_widgets[i][j].config(text=value)

    # Function to clear previous search highlights
    def clear_search():
        for i in range(len(label_widgets)):
            for j in range(len(label_widgets[i])):
                label_widgets[i][j].config(text="")

    # Bind the filter_data function to the search entry key release event
    search_entry.bind('<KeyRelease>', lambda event: filter_data())

    # Start the Tkinter event loop for the data_window
    data_window.mainloop()


def show_cell_content(row, column, data):
    global current_cell_window

    # Check if there is already a cell window open
    if current_cell_window is not None:
        current_cell_window.destroy()

    # Create a new window
    cell_window = tk.Toplevel()

    # Assign the new window to the current_cell_window variable
    current_cell_window = cell_window
    try:
        # Get the content of the clicked cell
        cell_content = data[row][column]

        # Create a Label to display the cell content
        label = tk.Label(cell_window, text=cell_content)
        label.pack(padx=10, pady=10)

        # Start the Tkinter event loop for the cell_window
        cell_window.mainloop()
    except IndexError:
        print("No data available for the selected cell.")
    except Exception as e:
        print("An error occurred:", e)