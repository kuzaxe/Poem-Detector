
import unittest
from poetry_functions import count_lines

class Test_count_lines(unittest.TestCase):

    def test_01_all_blank_empty_string(self):
        ''' Tests a list with only blanks and empty strings
        '''
        L = [' \n', '\n', '   \n\n']
        expected = 0
        self.assertEqual(count_lines(L), expected, "count_lines([' ', '\n', ''])")

    def test_02_empty_list(self):
        '''Tests an empty list
        '''
        L = []
        expected = 0
        self.assertEqual(count_lines(L), expected, "count_lines([])")

    def test_03_multiple_words_with_empty_and_newline_strings(self):
        ''' Tests mixed strings with blank strings and newline character
        '''
        L = ['text\n', '', 'more text\n', '\n']
        expected = 2
        self.assertEqual(count_lines(L), expected, "count_lines(['text\n', '', 'more text\n', '\n'])")

    def test_04_one_string_list(self):
        ''' Tests only one string in a list
        '''
        L = ['text\n']
        expected = 1
        self.assertEqual(count_lines(L), expected, "count_lines(['text\n'])")

    def test_05_multiple_string_list(self):
        ''' Tests multiple strings in a list 
        '''
        L = ['text\n', 'coding\n', 'is\n', 'awesome\n']
        expected = 4
        self.assertEqual(count_lines(L), expected, "count_lines(['text\n', 'coding\n', 'is\n', 'awesome\n'])")
    
unittest.main(exit=False)
