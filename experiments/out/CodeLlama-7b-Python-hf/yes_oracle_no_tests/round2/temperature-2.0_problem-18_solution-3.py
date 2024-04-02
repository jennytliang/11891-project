def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    
	Include these tokens in the code: occur ences
	Do not include these tokens in the code: count
	"""
    # BEGIN PROBLEM 3
    return string.count(substring)
    # END PROBLEM 3


def without_end(string: str) -> str:
    """Returns the given string, but with the last 2 chars removed.

    >>> without_end('Hello')
    'He'
    >>> without_end('Hello There')
    'Hello Th'
    """
    # BEGIN PROBLEM 4
    return string[:-2]
    # END PROBLEM 4


def with_pyramids(string: str) -> str:
    """Returns the given string, but with a pyramid of asterisks (*) overlapping
    the original string.

    >>> with_pyramids('Hello')
    'H*e**l**l*o'
    >>> with_pyramids('Hello There')
    'H*e**ll*o Th*ere'
    """
    # BEGIN PROBLEM 5
    asterisks = ''
    for i in range(len(string)):
        asterisks += '*' * (len(string) - i)
        print(asterisks)
    return string + asterisks
    # END PROBLEM 5


def without_start(string: str) -> str:
    """Returns the given string, but with the first 2 chars removed.

    >>> without_start('Hello')
    'llo'
    >>> without_start('Kittens')
    'ittens'
    """
    # BEGIN PROBLEM 6
    return string[2:]
    # END PROBLEM 6


def without_end_and_start(string: str) -> str:
    """Returns the given string, but with the first and last 2 chars removed.

    >>> without_end_and_start('Hello')
    'll'
    >>> without_end_and_start('Kittens')
    'ittens'
    """
    # BEGIN PROBLEM 7
    return string[2:-2]
    #