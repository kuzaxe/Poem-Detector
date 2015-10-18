import unittest
from poetry_functions import check_syllables

x = {
        'DOG': ['A', 'B1'],
        'FOG': ['G', 'A', 'B1'],
        'SMOLOG': ['B', 'IH0', 'F', 'A', 'B1'],
        'A': ['OP1'],
        'THE': ['AO', 'OP1'],
        'BAYA': ['W', 'IH1', 'OP1'],
        'CRAYO': ['L', 'AY1', 'OP1'],
        'CAT': ['D0', 'F'],
        'BAT': ['DH', 'D0', 'F'], 
        'MATEY': ['H1', 'D0', 'F'], 
        'DART': ['F', 'ER1', 'S', 'T'], 
        'FARTY': ['EH1', 'ER1', 'S', 'T'],
        'MART': ['P', 'ER1', 'S', 'T']}

class Test_check_syllables(unittest.TestCase):

    def test_01_correct_number_of_syllables_multiple_items(self):
        ''' Tests multiple poem lines with correct syllables.
        '''
        poem_line = ['Dog', 'Fog', 'Smolog']
        pattern = ([1, 1, 2], ['A', 'A', 'A'])
        expected = []
        self.assertEqual(check_syllables(poem_line, pattern, x), expected, "Did not pass: poem_line = ['Dog', 'Fog', 'Smolog'] / pattern = ([1, 1, 2], ['A', 'A', 'A'])")


    def test_02_correct_number_of_syllables_one_item(self):
        ''' Tests a poem line with correct syllables.
        '''
        poem_line = ['Dog',]
        pattern = ([1], ['A'])
        expected = []
        self.assertEqual(check_syllables(poem_line, pattern, x), expected, "Did not pass: poem_line = ['Dog'] / pattern = ([1], ['A'])")


    def test_03_incorrect_number_of_syllables_multiple_items(self):
        ''' Tests incorrect syllables on multiple poem lines.
        '''
        poem_line = ['Dog', 'Fog', 'Smolog']
        pattern = ([0, 4, 3], ['*', 'A', '*'])
        expected = ['Fog', 'Smolog']
        self.assertEqual(check_syllables(poem_line, pattern, x), expected, "Did not pass: poem_line = ['Dog', 'Fog', 'Smolog'] / pattern = ([0, 4, 3], ['*', 'A', '*'])")


    def test_04_incorrect_number_of_syllables_one_item(self):
        ''' Tests incorrect syllables on a poem line.
        '''
        poem_line = ['Dog']
        pattern = ([3], ['*'])
        expected = ['Dog']
        self.assertEqual(check_syllables(poem_line, pattern, x), expected, "Did not pass: poem_line = ['Dog'] / pattern = ([3], ['*'])")


    def test_05_check_with_no_syllable_requirements_one_item(self):
        ''' Tests the no syllable requirments (use of 0) on one line.
        '''
        poem_line = ['Farty Mart']
        pattern = ([0], ['A'])
        expected = []
        self.assertEqual(check_syllables(poem_line, pattern, x), expected, "Did not pass: poem_line = ['Farty Mart'] / pattern = ([0], ['A'])")


    def test_06_multiple_no_syllable_requirements_multiple_items(self):
        ''' Tests the no syllable requirments with multiple '0' with multiple lines
        '''
        poem_line = ['mart', 'farty', 'dart MART, Bat!']
        pattern = ([0, 0, 0], ['*', '*', '*'])
        expected = []
        self.assertEqual(check_syllables(poem_line, pattern, x), expected, "Did not pass: poem_line = ['mart', 'farty', 'dart MART, Bat!'] / pattern = ([0, 0, 0], ['*', '*', '*']")
unittest.main(exit=False)
