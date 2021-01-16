# name_function.py
# def get_formatted_name(first, last):
#     """Generate a neatly formatted full name."""
#     full_name = f"{first} {last}"
#     return full_name.title()

# test_name_function.py
import unittest
from name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py'."""
    def test_first_last_name(self):
        """Do names like 'Janis Joplin' work?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')


if __name__ == '__main__':
    unittest.main()

# Method                     Use
# assertEqual(a, b)          Verify that a == b
# assertNotEqual(a, b)       Verify that a != b
# assertTrue(x)              Verify that x is True
# assertFalse(x)             Verify that x is False
# assertIn(item, list)       Verify that item is in list
# assertNotIn(item, list)    Verify that item is not in list

# The unittest.TestCase class has a setUp() method that allows you to create these objects once and then use them in
# each of your test methods. When you include a setUp() method in a TestCase class, Python runs the setUp() method
# before running each method starting with test_.
#
# class TestAnonymousSurvey(unittest.TestCase):
#     """Tests for the class AnonymousSurvey."""
#
#     def setUp(self):
#         """
#         Create a survey and a set of responses for use in all test methods.
#         """
#         question = "What language did you first learn to speak?"
#         self.my_survey = AnonymousSurvey(question)
#         self.responses = ['English', 'Spanish', 'Mandarin']
#
#
#     def test_store_single_response(self):
#         """Test that a single response is stored properly."""
#         self.my_survey.store_response(self.responses[0])
#         self.assertIn(self.responses[0], self.my_survey.responses)

# Note:
# When a test case is running, Python prints one character for each unit test as it is completed. A passing test
# prints a dot, a test that results in an error prints an E, and a test that results in a failed assertion prints an
# F. This is why you’ll see a different number of dots and characters on the first line of output when you run your
# test cases.
