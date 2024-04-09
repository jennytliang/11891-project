def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    
	Include these tokens in the code: string )):
	Do not include these tokens in the code: s ) - len ( substring ) + 1
	"""


    occurences = 0
    for i in rang(len(string) - len(substring) + 1):
        if string[i:i + len(substring)] == substring:
            occurences += 1
    return occurences



def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    
	Include these tokens in the code: string )):
	Do not include these tokens in the code: s ) - len ( substring ) + 1
	"""


    return sum(string[i:i+len(substring)] == substring for i in range(len(string) - len(substring) + 1))


def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    
	Include these tokens in the code: string )):
	Do not include these tokens in the code: s ) - len ( substring ) + 1
	"""


    return len([i for i in range(len(string) - len(substring) + 1) if string[i:i+len(substring)] == substring])


def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    
	Include these tokens in the code: string )):
	Do