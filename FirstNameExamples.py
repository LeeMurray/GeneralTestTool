import names

name = names.get_first_name()
name1 = names.get_full_name()
name2 = names.get_first_name(gender='male')
name3 = names.get_first_name(gender='female')
name4 = names.get_last_name()


print(name)
print(name1)
print(name2)
print(name3)
print(name4)

Fname = names.get_first_name(gender='male')

pyperclip.copy(Fname)