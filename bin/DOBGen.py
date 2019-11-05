import random
import pyperclip
import datetime
from bin import Message
from dateutil.relativedelta import relativedelta
import datetime


def generate_date():
    x = (datetime.datetime.now())
    end_year = x.year - 18
    start_year = x.year - 80

    d = str(random.randrange(1, 28)).zfill(2)
    m = str(random.randrange(1, 12)).zfill(2)
    y = str(random.randrange(start_year, end_year))
    string = str(d + "/" + m + "/" + y)

    pyperclip.copy(string)
    Message.complete()

