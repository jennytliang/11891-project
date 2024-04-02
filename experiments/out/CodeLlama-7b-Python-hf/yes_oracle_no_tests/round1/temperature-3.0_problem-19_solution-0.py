from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    
	Include these tokens in the code: to _ int = {' zero ':
	"""
    pass


def sort_names(names: str) -> str:
    """ Input is a space-delimited string of names.
    Return the string with names sorted by last name (alphabetically) and first name (alphabetically)
    >>> sort_names('john smith jane doe')
    'jane doe john smith'
    """
    pass


def sort_addresses(addresses: str) -> str:
    """ Input is a space-delimited string of addresses, where each address is in the format 'ADDRESS CITY STATE ZIPCODE'.
    Return the addresses sorted by zipcode.
    >>> sort_addresses('123 Main St. Seattle WA 98101 456 11th Ave. Seattle WA 98102')
    '11th Ave. Seattle WA 98102 123 Main St. Seattle WA 98101'
    """
    pass


def sort_integers(integers: str) -> str:
    """ Input is a space-delimited string of integers.
    Return the string with integers sorted from smallest to largest.
    >>> sort_integers('1 3 2')
    '1 2 3'
    """
    pass


if __name__ == "__main__":
    import doctest

    doctest.testmod()
