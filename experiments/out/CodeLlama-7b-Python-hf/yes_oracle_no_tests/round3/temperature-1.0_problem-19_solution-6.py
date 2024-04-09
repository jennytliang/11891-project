from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    
	Include these tokens in the code: to _ int = {' zero ':
	"""
    return ' '.join(sorted(numbers.split(), key=lambda x: int(x)))


def sort_vowels(string: str) -> str:
    """ Input is a string.
    Return the string with vowels sorted from smallest to largest
    >>> sort_vowels('hello')
    'ehllo'
    """
    vowels = set('aeiou')
    return ''.join(sorted(string, key=lambda x: 'aeiou'.index(x) if x in vowels else 99))


def sort_sentence(sentence: str) -> str:
    """ Input is string that ends with a period.
    Return the string with words sorted by length, shortest to longest
    >>> sort_sentence('sentences.')
    'e.nstces'
    """
    return ' '.join(sorted(sentence.split(), key=lambda x: len(x)))


def sort_array(array: List[int]) -> List[int]:
    """ Input is an array of integers.
    Return the array with the integers sorted from smallest to largest
    >>> sort_array([5, 10, 15, 1, 2])
    [1, 2, 5, 10, 15]
    """
    return sorted(array)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
