from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    
	Include these tokens in the code: to _ int = {' zero ':
	"""
    return " ".join(sorted(numbers.split(), key=lambda x: int(x.strip())))


def sort_words(words: str) -> str:
    """ Input is a string of words delimited by single spaces.
    Return the string with the words sorted alphabetically, case insensitive.
    >>> sort_words('alice,bob,Carol')
    'alice,bob,Carol'
    """
    return ",".join(sorted(words.split(",")))


def sort_sentence(sentence: str) -> str:
    """ Input is a sentence delimited by single spaces.
    Return the string with the words sorted alphabetically, case insensitive.
    >>> sort_sentence('Carol the bob alice')
    'alice the bob Carol'
    """
    return " ".join(sorted(sentence.split()))


def sort_shopping_list(items: str) -> str:
    """ Input is a string of items delimited by single spaces.
    Return the string with the items sorted alphabetically, case insensitive.
    Each item is a string with the format:
        <quantity> <item name>
    where <quantity> is an integer and <item name> is a string.
    Return the string with the items sorted first by quantity, from smallest to largest,
    and then by name, case insensitive.
    >>> sort_shopping_list('2 apples, 12 bananas, 8 oranges, 3 pears')
    '2 apples, 3 pears, 8 oranges, 12 bananas'
    """
    return ", ".join(sorted(items.split(", "), key=lambda x: (int(x.split(" ")[0]), x.split(" ")[1])))


def sort_phone_list(numbers: str) -> str:
    """ Input is a string of numbers delimited by single spaces.
    Each number is a string with the format:
        <area code>-<exchange>-<line>
    where <area code> is a three digit integer, <exchange>