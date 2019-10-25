import uuid
import pyperclip
from bin import Message


def guid_generator():
    guid = uuid.uuid4()
    response = str(guid)
    pyperclip.copy(response)
    Message.complete()