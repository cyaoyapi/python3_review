"""Tests for module 'quiz_functions.py'.
"""

import unittest

from quiz_functions import display_question

class QuizFunctionsTests(unittest.TestCase):
	"""Test case for module 'quiz_functions.py'."""

	def setUp(self):
		self.selected_question = ['Who write the unit test in software project ?',
		['The system admin', 'The tester', 'The developer'], 1]

	def test_display_question_correct(self):
		"""Unit test(1) on function 'test_display_question'.

		Given : a selected question(list) with correct format
		When : excute the function instruction
		Then : return the correct display string 
		"""

		returned_string = display_question(self.selected_question)
		correct_display = "Who write the unit test in software project ?\n" + \
		  "  1- The system admin\n" + "  2- The tester\n" + "  3- The developer\n"
		self.assertEqual(returned_string, correct_display)

	def test_display_question_selected_question_with_bad_size(self):
		"""Unit test(2) on function 'test_display_question'.

		Given : a question(list) with bad size (Different than 3)
		When : excute the function instruction
		Then : raise correct corresponding exception
		"""

		given_question = ['Who write the unit test in software project ?',
		['The system admin', 'The tester', 'The developer'], 1, "More elements"]
		with self.assertRaises(ValueError):
			display_question(given_question)

	def test_display_question_selected_question_with_bad_2nd_element(self):
		"""Unit test(3) on function 'test_display_question'.

		Given : a question(list) with bad 2nd element which must be 
				a list or tuple(of choices)
		When : excute the function instruction
		Then : raise correct corresponding exception
		"""

		given_question = ['Who write the unit test in software project ?',
		'The system admin', 1]
		with self.assertRaises(ValueError):
			display_question(given_question)

	def test_display_question_selected_question_with_bad_3th_element(self):
		"""Unit test(4) on function 'test_display_question'.

		Given : a question(list) with bad 3th element which must be 
				an integer(the index of the correct answer in the choices' list)
		When : excute the function instruction
		Then : raise correct corresponding exception
		"""

		given_question = ['Who write the unit test in software project ?',
		['The system admin', 'The tester', 'The developer'], "1"]
		with self.assertRaises(ValueError):
			display_question(given_question)


