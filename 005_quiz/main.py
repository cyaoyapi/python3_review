"""This program proposes an assessment quiz.
"""

import random

from quiz_functions import display_question

# List of questions/answers
questions_list = [
	['Who is the creator of Python language ?', ['Steve Job', 'Tim Bernes Lee', 
	'Guido Van Rossum', 'Bill Gates'], 3],
	['Which one of these is an agile framework ?', ['Pomodero', 'Scrum', 
	'Test Driven Development'], 2],
	['Who is the first president of Ivory Coast?', ['Boigny Houphouet', 'Robert Guei', 
	'Jean Gaston'], 1],
]

total_questions = len(questions_list) # Store the total of the questions
score = 0 # Init user score
selected_question = random.choice(questions_list) # Select randomly a question

print(len(selected_question[1]))
# Ask the question and display response's choices
print(display_question(selected_question))
# Control the user input
while True:
	try:
		user_response = int(input())
		if user_response not in list(range(1, len(selected_question[1])+1)):
			raise ValueError("The choice must be in the displayed options")
	except ValueError:
		print("Error : The choice must be an integer in the displayed options!")
		print("Try Again!")
		continue
	else:
		break

# Check the response : upgrade score if true
print("OK")
# remove the question

# chef if liste always contains element : if yes reloop else display score and quit.