"""
A poetry pattern:  tuple of (list of int, list of str)
  - first item is a list of the number of syllables required in each line
  - second item is a list describing the rhyme scheme rule for each line
"""

"""
A pronunciation dictionary: dict of {str: list of str}
  - each key is a word (a str)
  - each value is a list of phonemes for that word (a list of str)
"""

# ===================== Helper Functions =====================


def clean_up(s):
    """ (str) -> str

    Return a new string based on s in which all letters have been
    converted to uppercase and punctuation characters have been stripped
    from both ends. Inner punctuation is left untouched.

    >>> clean_up('Birthday!!!')
    'BIRTHDAY'
    >>> clean_up('"Quoted?"')
    'QUOTED'
    """

    punctuation = """!"'`@$%^&_-+={}|\\/,;:.-?)([]<>*#\n\t\r"""
    result = s.upper().strip(punctuation)
    return result


# Add your helper functions here.

# function taken from Darshan Mehta Assignment 2
def list_of_words(text):
    r""" (list of str) -> list of str

    Return a new list of string containing only words that have been converted
    to lowercase and punctuation characters have been stripped from both ends
    of the word.

    >>> list_of_words(['Hey, how are you?', 'Great!!'])
    ['HEY', 'HOW', 'ARE', 'YOU', 'GREAT']
    >>> list_of_words(['\n', '', '"!AMAZING!'])
    ['AMAZING']
    """
    index = 0
    lst_of_words = []

    for line in text:
        lst_of_words.extend(line.split())

    # clean_up each string in lst_of_words
    while index < len(lst_of_words):
        lst_of_words[index] = clean_up(lst_of_words[index])
        index += 1

    while '' in lst_of_words:
        lst_of_words.remove('')
    while ' ' in lst_of_words:
        lst_of_words.remove(' ')

    return lst_of_words


def vowel_finder(phoneme):
    r''' (list of str) -> list of str

    Return the last syllable of a word's phoneme.

    >>> vowel_finder(['A', 'HI0', 'D'])
    ['D', 'HI0']
    >>> vowel_finder(['DH1'])
    ['DH1']
    '''
    reverse_list = []

    for i in range(1, len(phoneme) + 1):
        if not(phoneme[-i][-1] in '012'):
            reverse_list.append(phoneme[-i])
        else:
            reverse_list.append(phoneme[-i])
            return reverse_list


def pattern_index(pattern, letter):
    r""" (lst of str, str) -> lst of int

    Return the index locations of where the letter appears in pattern.

    >>> pattern_index(['A', 'B', 'A'], 'A')
    [0, 2]
    >>> pattern_index(['B', 'A', '*', 'B'], 'B')
    [0, 3]
    """
    rhyme_index = []
    i = 0
    while i < len(pattern):
        if letter in pattern[i:]:
            i = pattern.index(letter, i, len(pattern))
            rhyme_index.append(i)
            i += 1
        else:
            i = len(pattern)
    return rhyme_index


def check_rhyme_helper(rhymes, word_to_phonemes):
    r''' ([list of str], pronunciation dictionary) -> bool

    Return True if and only if the words in rhymes
    match according to word_to_phonemes.
    
    >>> check_rhyme_helper(['Apple'], {'Apple': ['a', 'b', 'd2', 's']})
    True
    >>> check_rhyme_helper(['A', 'D'], {'A': ['d2', 's'], 'D': ['d2', 's']})
    True
    >>> check_rhyme_helper(['A', 'D'], {'A': ['d2', 's'], 'D': ['d2', 'f']})
    False
    '''
    result = []
    base_case = vowel_finder(word_to_phonemes[rhymes[0]])

    for word in rhymes[1:]:
        if not(base_case == vowel_finder(word_to_phonemes[word])):
            result.append(0)

    return len(result) == 0

# ===================== Required Functions =====================

def count_lines(lst):
    r""" (list of str) -> int

    Precondition: each str in lst[:-1] ends in \n.

    Return the number of non-blank, non-empty strings in lst.

    >>> count_lines(['The first line leads off,\n', '\n', '  \n',
    ... 'With a gap before the next.\n', 'Then the poem ends.\n'])
    3
    >>> count_lines(['\n', '  \n', '', ' ',
    ... 'With a gap before the next.\n', 'Then the poem ends.\n'])
    2
    """
    lines = 0
    for line in lst:
        if line.strip() != '':
            lines += 1
    return lines


def get_poem_lines(poem):
    r""" (str) -> list of str

    Return the non-blank, non-empty lines of poem, with whitespace removed
    from the beginning and end of each line.

    >>> get_poem_lines('The first line leads off,\n\n\n' + 'With a gap before the past.\nThen the poem ends.\n')
    ['The first line leads off,', 'With a gap before the past.', 'Then the poem ends.']
    >>> get_poem_lines('The first line leads off')
    ['The first line leads off']
    """

    poem_lines = poem.split('\n')

    i = 0
    while i < len(poem_lines):
        if poem_lines[i].strip() == '':
            poem_lines.remove(poem_lines[i])
        else:
            poem_lines[i] = poem_lines[i].strip()
            i += 1
    return poem_lines


def check_syllables(poem_lines, pattern, word_to_phonemes):
    r""" (list of str, poetry pattern, pronunciation dictionary) -> list of str

    Precondition: len(poem_lines) == len(pattern[0])

    Return a list of lines from poem_lines that do not have the right number of
    syllables for the poetry pattern according to the pronunciation dictionary.
    If all lines have the right number of syllables, return the empty list.

    >>> poem_lines = ['The first line leads off,', 'With a gap before the next.', 'Then the poem ends.']
    >>> pattern = ([5, 5, 4], ['*', '*', '*'])
    >>> word_to_phonemes = {'NEXT': ['N', 'EH1', 'K', 'S', 'T'],
    ...                     'GAP': ['G', 'AE1', 'P'],
    ...                     'BEFORE': ['B', 'IH0', 'F', 'AO1', 'R'],
    ...                     'LEADS': ['L', 'IY1', 'D', 'Z'],
    ...                     'WITH': ['W', 'IH1', 'DH'],
    ...                     'LINE': ['L', 'AY1', 'N'],
    ...                     'THEN': ['DH', 'EH1', 'N'],
    ...                     'THE': ['DH', 'AH0'], 
    ...                     'A': ['AH0'], 
    ...                     'FIRST': ['F', 'ER1', 'S', 'T'], 
    ...                     'ENDS': ['EH1', 'N', 'D', 'Z'],
    ...                     'POEM': ['P', 'OW1', 'AH0', 'M'],
    ...                     'OFF': ['AO1', 'F']}
    >>> check_syllables(poem_lines, pattern, word_to_phonemes)
    ['With a gap before the next.', 'Then the poem ends.']
    >>> poem_lines = ['The first line leads off,']
    >>> check_syllables(poem_lines, ([0], ['*']), word_to_phonemes)
    []
    >>> poem_lines = ['The first line leads off,', 'Before the first poem.', 'A gap ends a line']
    >>> check_syllables(poem_lines, ([0, 0, 5], ['*', '*', '*']), word_to_phonemes)
    []
    """

    store = []
    resulted_syllables = 0
    incorrect_lines = []
    phonemes = ''

    for line in poem_lines:
        store.append(list_of_words([line]))

    for i in range(len(pattern[0])):
        expected_syllables = int(pattern[0][i])
        
        # counts the number of syllables in a poem line.
        if expected_syllables != 0:
            for word in store[i]:
                phonemes += str(word_to_phonemes[word])
            resulted_syllables += phonemes.count('0') + phonemes.count('1') + phonemes.count('2')
            if expected_syllables != resulted_syllables:
                incorrect_lines.append(poem_lines[i])

            phonemes = []
            resulted_syllables = 0
    return incorrect_lines


def check_rhyme_scheme(poem_lines, pattern, word_to_phonemes):
    r""" (list of str, poetry pattern, pronunciation dictionary) -> list of list of str

    Precondition: len(poem_lines) == len(pattern[1])

    Return a list of lists of lines from poem_lines that should rhyme with 
    each other but don't. If all lines rhyme as they should, return the empty 
    list.

    >>> poem_lines = ['The first line leads off,', 'With a gap before the next.', 'Then the poem ends.']
    >>> pattern = ([5, 7, 5], ['A', 'B', 'A'])
    >>> word_to_phonemes = {'NEXT': ['N', 'EH1', 'K', 'S', 'T'],
    ...                     'GAP': ['G', 'AE1', 'P'],
    ...                     'BEFORE': ['B', 'IH0', 'F', 'AO1', 'R'],
    ...                     'LEADS': ['L', 'IY1', 'D', 'Z'],
    ...                     'WITH': ['W', 'IH1', 'DH'],
    ...                     'LINE': ['L', 'AY1', 'N'],
    ...                     'THEN': ['DH', 'EH1', 'N'],
    ...                     'THE': ['DH', 'AH0'],
    ...                     'A': ['AH0'],
    ...                     'FIRST': ['F', 'ER1', 'S', 'T'],
    ...                     'ENDS': ['EH1', 'N', 'D', 'Z'],
    ...                     'POEM': ['P', 'OW1', 'AH0', 'M'],
    ...                     'OFF': ['AO1', 'F']}
    >>> check_rhyme_scheme(poem_lines, pattern, word_to_phonemes)
    [['The first line leads off,', 'Then the poem ends.']]
    >>> pattern = ([5, 7, 5], ['A', 'B', '*'])
    >>> check_rhyme_scheme(poem_lines, pattern, word_to_phonemes)
    []
    """

    checked_letters = ""
    rhyming_lines = [] 
    last_words = []
    rhymes = []
    result = []
    
    for letter in pattern[1]:
        
        if letter not in checked_letters and letter != "*":
            checked_letters += letter
            poem_line_idx = pattern_index(pattern[1], letter)

            # Append lines that rhyme to rhyming_lines
            for num in poem_line_idx:
                rhyming_lines.append(poem_lines[num])
                
            for line in rhyming_lines:
                rhymes.append(list_of_words([line]))

            for item in rhymes:
                last_words.append(item[-1])

            if not check_rhyme_helper(last_words, word_to_phonemes):
                result.append(rhyming_lines)

        rhyming_lines = []
        last_words = []
        rhymes = []

    return result



if __name__ == '__main__':
    import doctest
    doctest.testmod()
