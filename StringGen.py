from tkinter import simpledialog
from tkinter import messagebox
import pyperclip
# import random
# import string
import lorem


# def string_generator():
    # i = simpledialog.askinteger(title="Number", prompt="Enter the number of characters you need : ")
    # t = ''.join(random.choice(string.ascii_lowercase) for x in range(i))
    # pyperclip.copy(t)


def ipsum_string():
    d = simpledialog.askinteger(title="number", prompt="Enter Number : ")
    c = str(lorem.paragraph())

    if d > len(c):
        messagebox.showinfo("Error", "Request Too Long. Paragraph is only " + str(len(c)) + " characters long. Please try again.")
        # print("Request Too Long. Paragraph is only" + str(len(c)) + "long. Please try again.")
    elif d == 0:
        messagebox.showinfo("Error", "Can not preform a request for a 0 string length.")
        # print("You want a string of 0 whats the point...")
    else:
        count = c[0:d]
        pyperclip.copy(count)
