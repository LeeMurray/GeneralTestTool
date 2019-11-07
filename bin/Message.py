from tkinter import messagebox
from bin import MassDataGen
import time


def complete():
    messagebox.showinfo("Info", "Info : Copied to clipboard")


def on_error(e):
    messagebox.showerror("Error", "Error : " + e + ", Please try again.")


def process_complete():
    messagebox.showinfo("Complete", "Complete : Data stored in Files/Data.csv Enjoy.")
