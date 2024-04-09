from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    
	Include these tokens in the code: to _ int = {' zero ':
	"""
    if numbers == "":
        return ""
    else:
        return " ".join(sorted(numbers.split()))


def sum_numbers(numbers: str) -> int:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the sum of all the numbers in the string
    >>> sum_numbers('three one five')
    9
    
    """
    if numbers == "":
        return 0
    else:
        return sum(int(x) for x in numbers.split())


def count_letters(letters: str) -> int:
    """ Input is a string of lowercase letters.
    Return the count of distinct letters in the string
    >>> count_letters('abcabc')
    3
    
    """
    return len(set(letters))


def count_letters_2(letters: str) -> int:
    """ Input is a string of lowercase letters.
    Return the count of distinct letters in the string
    >>> count_letters('abcabc')
    3
    
    """
    if letters == "":
        return 0
    else:
        return len(set(letters))


def is_pangram(sentence: str) -> bool:
    """ Input is a string.
    Return True if the string is a pangram, False otherwise.
    A pangram is a sentence containing every letter of the alphabet at least once.
    >>> is_pangram('the quick brown fox jumps over the lazy dog')
    True
    
    """
    return len(set("abcdefghijklmnopqrstuvwxyz") - set(sentence.lower())) == 0


def is_pangram_2(sentence: str) -> bool:
    """ Input is a string.
    Return True if the string is a pangram, False otherwise.
    A pangram is a sentence containing