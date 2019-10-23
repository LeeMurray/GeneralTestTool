import names
import pyperclip


Fname = names.get_first_name(gender='male')

pyperclip.copy(Fname)