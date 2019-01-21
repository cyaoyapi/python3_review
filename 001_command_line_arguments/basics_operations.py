"""This program makes basic mathematic operation operations with 2 given integers.

	  - Addition
	  - Difference
	  - Multiplication
	  - Division
	  - Whole Division
	  - Modulo
"""

import sys

# If there are least or more than 2(without the program himself) given arguments, 
# return a error message corresponding
if len(sys.argv) != 3:
	print("Error : only 2 integers are required as arguments!")
else:
	try:
		print(f"Basics operation with {sys.argv[1]} and {sys.argv[2]}")
		print("=====================================================")
		print(f"Addition : {sys.argv[1]} + {sys.argv[2]} = {int(sys.argv[1]) + int(sys.argv[2])}")
		print(f"Difference : {sys.argv[1]} - {sys.argv[2]} = {int(sys.argv[1]) - int(sys.argv[2])}")
		print(f"Multiplication : {sys.argv[1]} * {sys.argv[2]} = {int(sys.argv[1]) * int(sys.argv[2])}")
		print(f"Division : {sys.argv[1]} / {sys.argv[2]} = {int(sys.argv[1]) / int(sys.argv[2])}")
		print(f"Whole Division : {sys.argv[1]} // {sys.argv[2]} = {int(sys.argv[1]) // int(sys.argv[2])}")
		print(f"Rest of the Euclidean division : {sys.argv[1]} % {sys.argv[2]} = {int(sys.argv[1]) % int(sys.argv[2])}")
	except ZeroDivisionError:
		print("Error : impossible to make division by 0!")
	except:
		print("Error : arguments must be integers!")