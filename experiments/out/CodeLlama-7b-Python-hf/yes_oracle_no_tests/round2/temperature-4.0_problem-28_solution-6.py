from typing import List


def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    
	Do not include these tokens in the code: if __ name __ == " __ main __
	"""

    return "".join(strin for strin in strings)


def concatenate_with_space(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string with spaces between strings
    >>> concatenate_with_space([])
    ''
    >>> concatenate_with_space(['a', 'b', 'c'])
    'a b c'
    
	Do not include these tokens in the code: if __ name __ == " __ main __
	"""

    return " ".join(strin for strin in strings)


def concatenate_with_comma(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string with commas between strings
    >>> concatenate_with_comma([])
    ''
    >>> concatenate_with_comma(['a', 'b', 'c'])
    'a, b, c'
    
	Do not include these tokens in the code: if __ name __ == " __ main __
	"""

    return ", ".join(strin for strin in strings)


def concatenate_with_newline(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string with newlines between strings
    >>> concatenate_with_newline([])
    ''
    >>> concatenate_with_newline(['a', 'b', 'c'])
    'a\\nb\\nc'
    
	Do not include these tokens in the code: if __ name __ == " __ main __
	"""

    return "\n".join(strin for strin in strings)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
