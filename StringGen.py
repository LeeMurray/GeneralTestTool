from tkinter import simpledialog
import pyperclip
import random
import string


def string_generator():
    i = simpledialog.askinteger(title="Number", prompt="Enter the number of characters you need : ")
    t = ''.join(random.choice(string.ascii_lowercase) for x in range(i))
    pyperclip.copy(t)