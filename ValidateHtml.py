import random
import string

# t = lorem.text(i)
i = int(input("Enter the string length you require : "))

t = ''.join(random.choice(string.ascii_lowercase) for x in range(i))

print(t)