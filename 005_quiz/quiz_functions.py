"""Module of functions used in the program.
"""

def display_question(selected_question: list=None) -> str:
	"""This function displays question and its choices."""
	
	if len(selected_question) != 3:
		raise ValueError("The given argument must be a list of 3 elements")
	elif not isinstance(selected_question[1], (list, tuple)):
		raise ValueError("The second element of given argument must be a list or a tuple")
	returned_string = str(selected_question[0]) + "\n"
	for key, choice in enumerate(selected_question[1]):
	    returned_string += f"  {key + 1}- {choice}\n"
	return returned_string 