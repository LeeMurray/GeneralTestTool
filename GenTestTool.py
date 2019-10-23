import tkinter as tk
import uuid
import names
import pyperclip

root = tk.Tk()
root.title("GenTestTool")
root.iconbitmap('Skull Logo.ico')
root.config(background="#355c7d")
frame = tk.Frame(root)
frame.configure(background='#355c7d', width=200)
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


GUIDGen = tk.Button(frame, bg="#f8b195", text="GUIDGenerator", command=guid_generator)
GUIDGen.pack(fill=tk.X, padx=10, pady=10, ipadx=10, ipady=10)

MaleFirstName = tk.Button(frame, bg="#f67280", text="Male First Name Generator", command=male_first_name)
MaleFirstName.pack(fill=tk.X, padx=10, pady=10, ipadx=10, ipady=10)

FemaleFirstName = tk.Button(frame, bg="#f67280", text="Female First Name Generator", command=female_first_name)
FemaleFirstName.pack(fill=tk.X, padx=10, pady=10, ipadx=10, ipady=10)

LastName = tk.Button(frame, bg="#c06c84", text="Last Name Generator", command=last_name)
LastName.pack(fill=tk.X, padx=10, pady=10, ipadx=10, ipady=10)

MaleFullName = tk.Button(frame, bg="#6c5b7b", text="Male Full Name Generator", command=male_full_name)
MaleFullName.pack(side=tk.LEFT, fill=tk.X, padx=10, pady=10, ipadx=10, ipady=10)

FemaleFullName = tk.Button(frame, bg="#6c5b7b", text="Female Full Name Generator", command=female_full_name)
FemaleFullName.pack(side=tk.LEFT, fill=tk.X, padx=10, pady=10, ipadx=10, ipady=10)

root.mainloop()