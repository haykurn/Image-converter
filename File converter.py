# Importing libraries and modules
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from PIL import Image

# Function to browse image
def browse():
    global img
    filename = filedialog.askopenfilename(title="Select a file")  # Selecting a file from the system
    img = Image.open(filename)  # Opening the selected file

# Function to change from png to jpg
def png_to_jpg():
    global img
    export_file_path = filedialog.asksaveasfilename(defaultextension='.jpg')  # Choosing the path and changing extension to jpg
    img.save(export_file_path)  # Saving the file on the desired path

# Function to change from jpg to png
def jpg_to_png():
    global img
    export_file_path = filedialog.asksaveasfilename(defaultextension='.png')  # Choosing the path and changing extension to png
    img.save(export_file_path)  # Saving the file on the desired path

# Creating GUI
root = Tk()
root.geometry('600x250')  # Geometry of window
root.title('Convert file jpg to png')  # Fixing the typo here
Label(root, text='Image Format Converter', font='arial 15').place(x=210, y=10)
Button(root, text='Png To Jpg', command=png_to_jpg, fg='red', font='arial 10').place(x=120, y=95)
Button(root, text='Jpg To Png', command=jpg_to_png, fg='red', font='arial 10').place(x=450, y=95)

root.mainloop()