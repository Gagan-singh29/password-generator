import random
import string

print('Hellooo, Welcome to Password generator!')



length=int(input("Enter the length of password: "))
if length<=12:
    length=int(input("Please Enter Min 12 length to continue:"))
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

all = lower + upper + num + symbols

temp = random.sample(all,length)

password = "".join(temp)

print(password)
