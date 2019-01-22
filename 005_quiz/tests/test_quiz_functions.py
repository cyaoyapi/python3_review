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
		"""Unit test.

		Given : a selected question with correct format
		When : excute the function instruction
		Then : return the correct display string 
		"""

		returned_string = display_question(self.selected_question)
		correct_display = "Who write the unit test in software project ?\n" + \
		  "  1- The system admin\n" + "  2- The tester\n" + "  3- The developer\n"
		self.assertEqual(returned_string, correct_display)


