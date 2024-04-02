from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    
	Include these tokens in the code: to _ int = {' zero ':
	"""
    return ' '.join(sorted(numbers.split()))


def sort_sentence(sentence: str) -> str:
    """ Input is a string containing a single word and an integer.
    The word is delimited by a single space and the digit is at the end of the string.
    Return the string with the word sorted based on the integer value.
    >>> sort_sentence('is2 Thi1s T4est 33')
    'Thi1s is2 33 T4est'
    """
    pass


def sort_sentence_case_insensitive(sentence: str) -> str:
    """ Input is a string containing a single word and an integer.
    The word is delimited by a single space and the digit is at the end of the string.
    Return the string with the word sorted based on the integer value, but this time case insensitive.
    >>> sort_sentence_case_insensitive('is2 Thi1s T4est 33')
    'is2 Thi1s 33 T4est'
    """
    pass


def sort_array(source_array: List[int]) -> List[int]:
    """ Input is an array of integers.
    Return the same array with the values sorted from smallest to largest without creating a new array.
    >>> sort_array([5, 3, 2, 1, 4])
    [1, 2, 3, 4, 5]
    """
    pass


def sort_array_case_insensitive(source_array: List[str]) -> List[str]:
    """ Input is an array of strings.
    Return the same array with the values sorted from smallest to largest without creating a new array.
    This time case insensitive.
    >>> sort_array_case_insensitive(['b', 'c', 'A', 'd'])
    ['A', 'b', 'c', 'd']
    """
    pass


if __name__ == "__main__":
    import doctest

    doctest.testmod()
