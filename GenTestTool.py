import tkinter as tk
from tkinter import simpledialog
import uuid
import names
import pyperclip
import random
import string

root = tk.Tk()
root.title("GenTestTool")
root.grid()
frame = tk.Frame(root)
frame.configure(background='#355c7d', width=400)
frame.pack()


def guid_generator():
    guid = uuid.uuid4()
    response = str(guid)
    pyperclip.copy(response)


def male_first_name():
    m_f_name = names.get_first_name(gender='male')
    pyperclip.copy(m_f_name)


def female_first_name():
    f_f_name = names.get_first_name(gender='female')
    pyperclip.copy(f_f_name)


def last_name():
    l_name = names.get_last_name()
    pyperclip.copy(l_name)


def male_full_name():
    m_full_name = names.get_full_name(gender='male')
    pyperclip.copy(m_full_name)


def female_full_name():
    f_full_name = names.get_full_name(gender='female')
    pyperclip.copy(f_full_name)


def string_generator():
    i = simpledialog.askinteger(title="Number", prompt="Enter the number of characters you need : ")
    t = ''.join(random.choice(string.ascii_lowercase) for x in range(i))
    pyperclip.copy(t)


GUIDGen = tk.Button(frame, bg="#f8b195", text="GUIDGenerator", command=guid_generator, padx=10, pady=10, width=50)
GUIDGen.grid(row=0, column=0, columnspan=2, rowspan=2)

MaleFirstName = tk.Button(frame, bg="#f67280", text="Male First Name Generator", command=male_first_name, padx=10,
                          pady=10, width=47)
MaleFirstName.grid(row=2, column=0, columnspan=2, rowspan=2, ipadx=10, ipady=6)

FemaleFirstName = tk.Button(frame, bg="#f67280", text="Female First Name Generator", command=female_first_name, padx=10,
                            pady=10, width=50)
FemaleFirstName.grid(row=4, column=0, columnspan=2, rowspan=2)

LastName = tk.Button(frame, bg="#c06c84", text="Last Name Generator", command=last_name, padx=10, pady=10, width=50)
LastName.grid(row=6, column=0, columnspan=2, rowspan=2)

MaleFullName = tk.Button(frame, bg="#6c5b7b", text="Male Full Name Generator", command=male_full_name, padx=10,
                         pady=10, width=23)
MaleFullName.grid(row=8, column=0, columnspan=1, rowspan=2)

FemaleFullName = tk.Button(frame, bg="#6c5b7b", text="Female Full Name Generator", command=female_full_name, padx=10,
                           pady=10, width=23)
FemaleFullName.grid(row=8, column=1, columnspan=1, rowspan=2)

String = tk.Button(frame, bg="#355c7d", text="String Generator", command=string_generator, padx=10, pady=10, width=50)
String.grid(row=10, column=0, columnspan=2, rowspan=2)


root.mainloop()