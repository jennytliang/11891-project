from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    
	Include these tokens in the code: to _ int = {' zero ':
	"""
    tokens = numbers.lower().split()  # split on whitespace
    numbers = [int(token) for token in tokens]  # convert to int
    numbers.sort()  # sort the numbers
    return ' '.join(str(number) for number in numbers)  # convert back to string


def count_letters(sentence: str) -> str:
    """ Input is a string of lowercase letters.
    Return a string of the letters in the string and their count.
    >>> count_letters('abcdef')
    'a1b1c1d1e1f1'
    """
    letters = {}  # initialize dictionary
    for char in sentence:  # iterate over input
        if char in letters:  # if char is in dictionary, increment value
            letters[char] += 1
        else:  # if char is not in dictionary, add char and set value to 1
            letters[char] = 1
    return ''.join(f'{char}{count}' for char, count in letters.items())  # convert dictionary to string


def is_pangram(sentence: str) -> bool:
    """ Input is a string of lowercase letters.
    Return True if the string is a pangram, and False otherwise.
    >>> is_pangram('abcdefghijklmnopqrstuvwxyz')
    True
    """
    letters = set(sentence.lower())  # convert to set to remove duplicates
    return len(letters) == 26  # if letters contains all 26 letters of the alphabet, return True


def sum_digits(number: int) -> int:
    """ Input is a positive integer.
    Return the sum of the digits in the integer.
    >>> sum_digits(123)
    6
    """
    return sum(int(digit) for digit in str(number))  # convert number to string and iterate over digits


def has_duplicates(sentence: str) -> bool:
    """ Input is a string of lowercase letters.
    Return True if the string has any repeated letters, and False otherwise.
    >>> has_