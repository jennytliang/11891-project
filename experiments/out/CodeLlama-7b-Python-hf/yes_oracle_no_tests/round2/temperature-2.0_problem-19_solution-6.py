from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    
	Include these tokens in the code: to _ int
	"""
    # split input into a list of tokens
    tokens = numbers.split()
    # convert to numbers
    numbers = [int(token) for token in tokens]
    # sort the numbers
    numbers.sort()
    # convert back to strings
    tokens = [str(number) for number in numbers]
    # rejoin the tokens
    return " ".join(tokens)


def sort_names(names: str) -> str:
    """ Input is a space-delimited string of names.
    Return the string with names sorted alphabetically
    >>> sort_names('Carolina Fayer Grethe')
    'Fayer Grethe Carolina'
    
    Include these tokens in the code: to _ str
    """
    # split input into a list of tokens
    tokens = names.split()
    # sort the tokens
    tokens.sort()
    # rejoin the tokens
    return " ".join(tokens)


def sort_names_numbers(names_numbers: str) -> str:
    """ Input is a space-delimited string of names and numbers.
    Return the string with names and numbers sorted alphabetically
    >>> sort_names_numbers('Alice 10 Bob 1 charlie 2')
    'Alice 10 charlie 2 Bob 1'
    
    Include these tokens in the code: to _ str
    """
    # split input into a list of tokens
    tokens = names_numbers.split()
    # split tokens in two, one list of names, the other of numbers
    names = []
    numbers = []
    for token in tokens:
        try:
            int(token)
            numbers.append(token)
        except ValueError:
            names.append(token)
    # sort the names
    names.sort()
    # sort the numbers
    numbers.sort()
    # rejoin the tokens
    return " ".join(names + numbers)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
