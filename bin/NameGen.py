import names
import pyperclip
from bin import Message


def male_first_name():
    m_f_name = names.get_first_name(gender='male')
    pyperclip.copy(m_f_name)
    Message.complete()


def female_first_name():
    f_f_name = names.get_first_name(gender='female')
    pyperclip.copy(f_f_name)
    Message.complete()


def last_name():
    l_name = names.get_last_name()
    pyperclip.copy(l_name)
    Message.complete()


def mass_last_name():
    lst_name = names.get_last_name()
    return lst_name


def male_full_name():
    m_full_name = names.get_full_name(gender='male')
    pyperclip.copy(m_full_name)
    Message.complete()


def female_full_name():
    f_full_name = names.get_full_name(gender='female')
    pyperclip.copy(f_full_name)
    Message.complete()