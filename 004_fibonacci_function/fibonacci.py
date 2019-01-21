"""Some tests using fibonacci series."""

def fibo(n):
	"""Display fibonacci serie number until the given number."""
	series = []
	a, b = 0, 1
	while a <= n:
		series.append(a)
		a, b = b, a+b
	return series


if __name__ == '__main__':
	print("You try to run fibonacci.py directly!")


