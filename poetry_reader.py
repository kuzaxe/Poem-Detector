"""
A pronunciation dictionary: dict of {str: list of str}
  - each key is a word (a str)
  - each value is a list of phonemes for that word (a list of str)
"""


def read_pronunciation(pronunciation_file):
    """ (file open for reading) -> pronunciation dictionary

    Read pronunciation_file, which is in the format of the CMU Pronouncing
    Dictionary, and return the pronunciation dictionary.
    """
    pr_dict = {}

    for line in pronunciation_file:
        if not line.strip().startswith(';;;'):
            new_text = line.split('  ')
            pr_dict[new_text[0]] = new_text[1].split()
    return pr_dict 
    

def read_poetry_form_description(poetry_forms_file):
    """ (file open for reading) -> poetry pattern

    Precondition: we have just read a poetry form name from poetry_forms_file.

    Return the next poetry pattern from poetry_forms_file.
    """
    numbers = []
    letters = []    
    while 1:
        temp = poetry_forms_file.readline().split()
        if temp != []:
            numbers.append(temp[0])
            letters.append(temp[1])
        else:
            return (numbers, letters)
        
def read_poetry_form_descriptions(poetry_forms_file):
    """ (file open for reading) -> dict of {str: poetry pattern}

    Return a dictionary of poetry form name to poetry pattern for the
    poetry forms in poetry_forms_file.
    """
    poetry_name_pattern = {}
    line = poetry_forms_file.readline().strip()
    while line != '':
        poetry_name_pattern[line] = read_poetry_form_description(poetry_forms_file)
        line = poetry_forms_file.readline().strip()
        
    return poetry_name_pattern
