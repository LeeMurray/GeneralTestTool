import random
import pyperclip
from bin import Message


def generate_date():
    d = str(random.randrange(1, 28)).zfill(2)
    m = str(random.randrange(1, 12)).zfill(2)
    y = str(random.randrange(1939, 2001))
    string = str(d + "/" + m + "/" + y)

    pyperclip.copy(string)
    Message.complete()

