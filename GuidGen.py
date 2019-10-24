import uuid
import pyperclip

def guid_generator():
    guid = uuid.uuid4()
    response = str(guid)
    pyperclip.copy(response)