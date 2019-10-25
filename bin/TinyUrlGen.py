from tkinter import simpledialog
from pyshorteners import Shortener
from bin import Message
import pyperclip


def tiny_url_gen():
    try:
        d = simpledialog.askstring(title="URL", prompt="Enter URL : ")
        shortener = Shortener('Tinyurl')
        pyperclip.copy(format(shortener.short(d)))
        Message.complete()
    except Exception as e:
        Message.on_error(str(e))
