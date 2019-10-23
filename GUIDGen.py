import uuid
import pyperclip

GUID = uuid.uuid4()
Responce = str(GUID)

pyperclip.copy(Responce)