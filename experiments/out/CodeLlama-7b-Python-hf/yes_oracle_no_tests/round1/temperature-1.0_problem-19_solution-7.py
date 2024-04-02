from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    
	Include these tokens in the code: to _ int = {' zero ':
	"""
    return " ".join(sorted(numbers.split(), key=int))


def count_vowels(sentence: str) -> int:
    """ Return the number of vowels in the given sentence.
    A vowel is any lowercase English letter a, e, i, o, u, y.
    >>> count_vowels('Hi there!')
    3
    >>> count_vowels('The quick brown fox jumped over the lazy dog.')
    13
    >>> count_vowels('A dictionary is a collection of unique words sorted
    ... by their keys.')
    10
    """
    vowels = set('aeiouy')
    return sum(s in vowels for s in sentence.lower())


def remove_duplicates(lst: List[str]) -> List[str]:
    """ Return a new list containing the elements of the given list without duplicates.
    >>> remove_duplicates([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])
    [1, 2, 3, 4]
    >>> remove_duplicates(['g', 'o', 'd', 'd', 'o', 'g', 'g'])
    ['g', 'o', 'd']
    """
    return list(set(lst))


def reverse_words(lst: List[str]) -> List[str]:
    """ Return a new list containing the elements of the given list in reverse order.
    >>> reverse_words(['The', 'quick', 'brown', 'fox'])
    ['fox', 'brown', 'quick', 'The']
    >>> reverse_words(['Hello', 'world', '!'])
    ['!', 'world', 'Hello']
    """
    return lst[::-1]


def max_in_list(lst: List[int]) -> int:
    """ Return the maximum value in the given list.
    >>> max_in_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    10
