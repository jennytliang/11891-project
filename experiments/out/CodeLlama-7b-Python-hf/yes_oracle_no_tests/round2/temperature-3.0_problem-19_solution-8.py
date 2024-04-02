from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    
	Include these tokens in the code: to _ int = {' zero ':
	"""
    # TODO: write your solution here
    return ' '.join(sorted(numbers.split(), key=lambda x: int(x.strip())))


def sort_names(names: str) -> str:
    """ Input is a string of names, separated by a single space.
    Return the string with names sorted from last name to first name,
    ignoring middle initials.
    >>> sort_names('Bart Simpson Krusty The Clown')
    'Clown Krusty Simpson Bart'
    
	Include these tokens in the code: to _ int = {' zero ':
	"""
    # TODO: write your solution here
    return ' '.join(sorted(names.split(), key=lambda x: x.split()[-1] + ' ' + x.split()[0]))


def sort_addresses(addresses: str) -> str:
    """ Input is a string of addresses, separated by a single newline character.
    Each address consists of an optional first name or last name,
    followed by a street number, followed by a street name, followed by a city name,
    followed by a state abbreviation, followed by a five digit zip code.
    Separate address components are separated by a single space.
    Return the string with addresses sorted by street name,
    followed by street number, followed by city name, followed by state, followed by zip.
    Ignore middle initials.
    >>> sort_addresses('123 Main Street\\n456 1st Street\\n789 Broadway\\n101 Centre Street')
    '101 Centre Street\\n456 1st Street\\n123 Main Street\\n789 Broadway'
    
	Include these tokens in the code: to _ int = {' zero ':
	"""
    # TODO: write your solution here
    return '\n'.join(sorted(addresses.split('\n'), key=lambda x: (x.split()[-1], x.split()[-2], x.split()[-3], x.split()[-4], x.split()[-5])))


def sort_dates(dates: str) -> str:
