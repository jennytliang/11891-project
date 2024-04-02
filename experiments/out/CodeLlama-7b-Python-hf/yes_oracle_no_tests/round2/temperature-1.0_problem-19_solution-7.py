from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    
	Include these tokens in the code: to _ int = {' zero ':
	"""
    numbers = numbers.split()
    numbers.sort(key=lambda x: int(x))
    return " ".join(numbers)


def sort_names(names: str) -> str:
    """ Input is a space-delimited string of names.
    Return the string with names sorted alphabetically, lowercase before uppercase.
    >>> sort_names('ann jen ker')
    'ann jen ker'
    """
    names = names.split()
    names.sort()
    return " ".join(names)


def sort_sentence(sentence: str) -> str:
    """ Input is a sentence with the words delimited by a single space.
    Return the sentence with the words sorted alphabetically from shortest to longest.
    If words are the same length, sort them alphabetically.
    >>> sort_sentence('happy birthday')
    'birthday happy'
    """
    sentence = sentence.split()
    sentence.sort(key=lambda x: (len(x), x))
    return " ".join(sentence)


def sort_address(address: str) -> str:
    """ Input is lines with an address.
    Return the address sorted by lines in the following order: City, State, Zip, Street.
    If the same line is repeated, it is sorted alphabetically.
    >>> sort_address('''
    123 Main Street
    Anytown NC
    12345
    ''')
    'Anytown NC\n12345\n123 Main Street'
    """
    address = address.splitlines()
    address.sort()
    return "\n".join(address)


def sort_the_time(time: str) -> str:
    """ Input is a 24-hour time in the format of HH:MM.
    Return the time in 12-hour format with leading zeros removed (so midnight is 0:00am) and minutes passed to 12 hours.
    >>> sort_the_time('09:00')
    '9:00am'
    """
    time = time.