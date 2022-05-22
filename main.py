import time
import random
import string
import colorama
from colorama import Fore
import os

num = 1

inputtedlength = int(input(Fore.BLUE + "How many characters should the password be? " + Fore.WHITE))
special = input(Fore.BLUE + "Do you want special characters? [y/n]: " + Fore.WHITE)
numbers = input(Fore.BLUE + "Do you want numbers? [y/n]: " + Fore.WHITE)


ascii_symbols = "!\"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~"

if special == 'y' and numbers == 'y':
	
	for i in range(num):
	    code = "".join(random.choices(
	        string.ascii_uppercase + string.digits + string.ascii_lowercase + ascii_symbols,
	        k = inputtedlength
	    ))
	
	print(f"Password: {code}")

elif special == 'n' and numbers == 'y':
	for i in range(num):
			code = "".join(random.choices(
					string.ascii_uppercase + string.digits + string.ascii_lowercase,
					k = inputtedlength
		))

	print(f"Password: {code}")

elif special == 'y' and numbers == 'n':
	for i in range(num):
			code = "".join(random.choices(
					string.ascii_uppercase + string.ascii_lowercase + ascii_symbols,
					k = inputtedlength
	))

	print(f"Password: {code}")

else:
	for i in range(num):
			code = "".join(random.choices(
					string.ascii_uppercase + string.ascii_lowercase,
					k = inputtedlength
	))

	print(f"Password: {code}")
