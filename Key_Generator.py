from random import *
import string

print("leave empty if you dont use password")
#should only be letters
a = input("\nWhat's the pastebin password (only letters): ")

b = int(input("how many passwords do you want: "))

for i in range(b):
    c = randint(1000,99999)
    d = ''.join(choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(8))
    if a is None:
        print(f"{d}{c}")
    else:
        print(f"{d}{c}{a}")
