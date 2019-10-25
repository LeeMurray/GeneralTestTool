from tkinter import simpledialog
from tkinter import messagebox
from bin import Message
import pyperclip
import lorem


def ipsum_string():
    d = simpledialog.askinteger(title="number", prompt="Enter Number : ")
    c = str(lorem.paragraph()) * 10

    if d > len(c):
        messagebox.showinfo("Error", "Request Too Long. Paragraph is only " + str(len(c)) + " characters long. Please try again.")
    elif d == 0:
        messagebox.showinfo("Error", "Can not preform a request for a 0 string length.")
    else:
        count = c[0:d]
        pyperclip.copy(count)
        Message.complete()
