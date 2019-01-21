"""
	This program test if a given integer is a primer number.
"""

from sys import argv

class TooManyArgsError(Exception):
	"""An exception class to control inputs.
		Raise exception when the user gives more than one argument.
	"""
	pass


try:
	if len(argv) > 2:
		raise TooManyArgsError()
	elif int(argv[1]) == 2:
		print(f"{argv[1]} is a primer number.")
	else:
		for n in range(2,int(argv[1])):
			if int(argv[1]) % n == 0:
				print(f"{argv[1]} is not a primer number.")
				break
		else: # A related 'else' to the loop 'for'
			print(f"{argv[1]} is a primer number.")
except TooManyArgsError:
	print("Error, the program requires only one integer as argument!")
	exit("==Try again!==")
except ValueError:
	print("Error, the argument must be an integer!")
	exit("==Try again!==")
else:
	print("==End, Good bye!===")
	exit()

