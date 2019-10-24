import tkinter as tk
import NameGen
import GuidGen
import StringGen

root = tk.Tk()
root.title("GenTestTool")
root.grid()
frame = tk.Frame(root)
frame.configure(background='#355c7d', width=400)
frame.pack()


GUIDGen = tk.Button(frame, bg="#f8b195", text="GUIDGenerator", command=GuidGen.guid_generator, padx=10, pady=10, width=50)
GUIDGen.grid(row=0, column=0, columnspan=2, rowspan=2)

MaleFirstName = tk.Button(frame, bg="#f67280", text="Male First Name Generator", command=NameGen.male_first_name, padx=10,
                          pady=10, width=47)
MaleFirstName.grid(row=2, column=0, columnspan=2, rowspan=2, ipadx=10, ipady=6)

FemaleFirstName = tk.Button(frame, bg="#f67280", text="Female First Name Generator", command=NameGen.female_first_name, padx=10,
                            pady=10, width=50)
FemaleFirstName.grid(row=4, column=0, columnspan=2, rowspan=2)

LastName = tk.Button(frame, bg="#c06c84", text="Last Name Generator", command=NameGen.last_name, padx=10, pady=10, width=50)
LastName.grid(row=6, column=0, columnspan=2, rowspan=2)

MaleFullName = tk.Button(frame, bg="#6c5b7b", text="Male Full Name Generator", command=NameGen.male_full_name, padx=10,
                         pady=10, width=23)
MaleFullName.grid(row=8, column=0, columnspan=1, rowspan=2)

FemaleFullName = tk.Button(frame, bg="#6c5b7b", text="Female Full Name Generator", command=NameGen.female_full_name, padx=10,
                           pady=10, width=23)
FemaleFullName.grid(row=8, column=1, columnspan=1, rowspan=2)

String = tk.Button(frame, bg="#355c7d", text="String Generator", command=StringGen.ipsum_string, padx=10, pady=10, width=50)
String.grid(row=10, column=0, columnspan=2, rowspan=2)


root.mainloop()