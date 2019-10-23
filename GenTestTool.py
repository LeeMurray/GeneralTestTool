import os
import tkinter as tk

root = tk.Tk()
root.title("GenTestTool")
root.config(background="#355c7d")
frame = tk.Frame(root)
frame.pack()


def guid_generator():
    os.system('GUIDGen.py')


def first_name():
    os.system('FirstName.py')


def last_name():
    os.system('LastName.py')


def full_name():
    os.system('FullName.py')


GUIDGen = tk.Button(frame, bg="#f8b195", text="GUIDGen", command=guid_generator)
GUIDGen.pack(fill=tk.X, padx=10, pady=10, ipadx=10, ipady=10)

FirstName = tk.Button(frame, bg="#f67280", text="First Name Generator", command=first_name)
FirstName.pack(fill=tk.X, padx=10, pady=10, ipadx=10, ipady=10)

LastName = tk.Button(frame, bg="#c06c84", text="Last Name Generator", command=last_name)
LastName.pack(fill=tk.X, padx=10, pady=10, ipadx=10, ipady=10)

FullName = tk.Button(frame, bg="#6c5b7b", text="Full Name Generator", command=full_name)
FullName.pack(fill=tk.X, padx=10, pady=10, ipadx=10, ipady=10)

root.mainloop()