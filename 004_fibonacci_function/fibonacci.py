"""
	Some tests using fibonacci series.
"""


def fibo(n):
	"""Display fibonacci serie number until the given number."""
	series = []
	a, b = 0, 1
	while a <= n:
		series.append(a)
		a, b = b, a+b
	return series

# The progam begins here
try:
	given_number = int(input("Give an integer greater than 1 : "))
	if given_number < 0:
		raise ValueError("Error : the given value must be greater than 0!")
	for nb in fibo(given_number):
		print(f"{nb}", end=" ")
	print(" ")
except ValueError:
	print("Error : the given value must be an positive integer!")
	exit("===Try again!===")
else:
	exit("===End, Good Bye!===")

