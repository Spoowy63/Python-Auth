from requests import *
from re import *

"""
in your pastebin type it like this: Flip 76424553 Flop
------------------------
Flip is the username 
76424553 is the id
Flop is the password
"""

web = get("pastebin_Link_Here")


usrn = str(input("Username: "))
psw = str(input("Password: "))
idi = str(input("ID: "))

full1  = findall(rf"{usrn}.*{psw}", web.text)
full = full1[0]


id = str(full.split()[1])

if ((usrn and psw in web.text) and (idi == id) and (id in full)):
    print("success")
else:
    print("Not registered")
