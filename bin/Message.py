from tkinter import messagebox


def complete():
    messagebox.showinfo("Info", "Info : Copied to clipboard")


def on_error(e):
    messagebox.showerror("Error", "Error : " + e + ", Please try again.")