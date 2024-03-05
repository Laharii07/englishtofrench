import os
from tkinter import *
from googletrans import Translator, LANGUAGES
from PIL import Image, ImageTk
import pyttsx3

def translate_text(event=None):
    input_text = entry.get()
    source_language = 'en'  # English
    dest_language = 'fr'    # french

    translator = Translator()
    translation = translator.translate(input_text, src=source_language, dest=dest_language)

    output_var.set(translation.text)

    # Read out the translated text using pyttsx3 with a different voice
    engine = pyttsx3.init()

    # Get the list of available voices
    voices = engine.getProperty('voices')

    # Use a different voice (You can change the index to select a different voice)
    engine.setProperty('voice', voices[1].id)

    engine.say(translation.text)
    engine.runAndWait()

root = Tk()
root.geometry('502x500')
root.resizable(0, 0)
root.title("Text Translator")

# Set icon file path
script_directory = os.path.dirname(os.path.abspath(__file__))
icon_path = os.path.join(script_directory, 'myicon.ico')

# Check if icon file exists before setting it
if os.path.exists(icon_path):
    root.iconbitmap(icon_path)
else:
    print(f"Warning: Icon file '{icon_path}' not found. Make sure the file exists.")

# Load background image
background_image_path = os.path.join(script_directory, 'background_image.jpg')
if os.path.exists(background_image_path):
    background_image = Image.open(background_image_path)
    background_photo = ImageTk.PhotoImage(background_image)
else:
    print(f"Warning: Background image file '{background_image_path}' not found. Make sure the file exists.")
    background_photo = None

# Change background to image
if background_photo:
    background_label = Label(root, image=background_photo)
    background_label.place(relwidth=1, relheight=1)

# Input
label_input = Label(root, text="Enter Text:", font=('Arial', 11))
label_input.grid(row=0, column=0, padx=10, pady=10, sticky='w')

entry = Entry(root, font=('Arial', 12), width=40)
entry.grid(row=0, column=1, padx=10, pady=10)

# Output
output_var = StringVar()
output_label = Label(root, textvariable=output_var, font=('Arial', 12), wraplength=400)
output_label.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Bind Enter key to translate function
entry.bind('<Return>', translate_text)

root.mainloop()
