import unittest

from fibonacci import fibo

class TestFibonacci(unittest.TestCase):
	"""Test case for fibonacci function."""

	def test_basic(self):
		""" A basic test on fibonacci function."""
		series = fibo(10)
		self.assertEqual(series, [0, 1, 1, 2, 3, 5, 8])

if __name__ == '__main__':
	unittest.main()


