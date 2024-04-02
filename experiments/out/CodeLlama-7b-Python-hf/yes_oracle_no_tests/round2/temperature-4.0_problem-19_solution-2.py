from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    
	Include these tokens in the code: to
	Do not include these tokens in the code: # split the numbers into a list
	"""
    return " ".join(sorted(numbers.split(" ")))


def sort_names(names: str) -> str:
    """ Input is a space-delimited string of names.
    Return the string with names sorted from longest to shortest
    >>> sort_names('Ann Maria Laura')
    'Laura Ann Maria'
    """
    return " ".join(sorted(names.split(" "), key=len, reverse=True))


def sort_sentence(sentence: str) -> str:
    """ Input is a sentence.
    Return the sentence with the words sorted from longest to shortest
    >>> sort_sentence('laptop charger battery')
    'battery charger laptop'
    """
    return " ".join(sorted(sentence.split(" "), key=len, reverse=True))


def sort_shopping_list(shopping_list: str) -> str:
    """ Input is a string containing a list of items.
    Return the list with the items sorted from least to most items, breaking ties alphabetically.
    >>> sort_shopping_list('eggs 12 bottled water 2')
    'bottled water 2 eggs'
    """
    return " ".join(sorted(shopping_list.split(" "), key=lambda s: (len(s), s)))


def sort_addresses(addresses: str) -> str:
    """ Input is a string containing a list of address.
    Return the list with the addresses sorted by distance from (0,0)
    >>> sort_addresses('42 Sample St, 32 Sample St, 12 Sample St')
    '12 Sample St, 32 Sample St, 42 Sample St'
    """
    return " ".join(sorted(addresses.split(" "), key=lambda s: (s.count(",") - 2) * 100 + s.count(" ")))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
