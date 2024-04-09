from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    
	Include these tokens in the code: to _ int = {' zero ':
	"""
    numbers_list = numbers.split()
    numbers_list.sort()
    return " ".join(numbers_list)


def count_letters(string: str) -> str:
    """ Input is a string.
    Return a string with the number of letters in the string followed by the letter 's'.
    If the string is empty, return the string "0 letters"
    >>> count_letters("")
    '0 letters'
    >>> count_letters("zero")
    '5 letters'
    """
    if string == "":
        return "0 letters"
    else:
        return str(len(string)) + " letters"


def reverse_string(string: str) -> str:
    """ Input is a string.
    Return the string reversed.
    >>> reverse_string('zero')
    'roze'
    >>> reverse_string('one')
    'eno'
    >>> reverse_string('')
    ''
    """
    return string[::-1]


def sort_list(list_of_numbers: List[int]) -> List[int]:
    """ Input is a list of numbers.
    Return the list sorted from smallest to largest
    >>> sort_list([3,1,5])
    [1, 3, 5]
    >>> sort_list([])
    []
    >>> sort_list([1,2,3,4,5])
    [1, 2, 3, 4, 5]
    """
    list_of_numbers.sort()
    return list_of_numbers


def count_vowels(string: str) -> str:
    """ Input is a string.
    Return the string with the number of vowels in the string followed by the letter 's'.
    If the string is empty, return the string "0 vowels"
    >>> count_vowels("")
    '0 vowels'
    >>> count_vowels("zero")
    '3 vowels'
    """
    vowels = "aeiou"
    counter = 0
    for char in string:
        if char