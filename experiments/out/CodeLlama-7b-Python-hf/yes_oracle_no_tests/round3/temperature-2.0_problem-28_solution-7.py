from typing import List


def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    
	Include these tokens in the code: ".
	"""

    ret = ""
    for string in strings:
        ret += string
    return ret


# print(concatenate([]))
# print(concatenate(['a', 'b', 'c']))
# print(concatenate(['a', 'b', 'c', 'd', 'e']))


def concatenate_2(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    
	Include these tokens in the code: ".
	"""
    ret = ""
    for string in strings:
        ret += string
    return ret


def concatenate_3(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
	
	Include these tokens in the code: ".
	"""
    return "".join(strings)


# print(concatenate_2([]))
# print(concatenate_2(['a', 'b', 'c']))
# print(concatenate_2(['a', 'b', 'c', 'd', 'e']))
# print(concatenate_3([]))
# print(concatenate_3(['a', 'b', 'c']))
# print(concatenate_3(['a', 'b', 'c', 'd', 'e']))


def concatenate_4(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
	
	Include these tokens in the code: ".
	"""
    return "".join(strings)


def capitalize(string: str) -> str:
    """ Capitalize first letter of a string
    
	Include these tokens in the code: ".
	"""
    return string.capitalize()


def capitalize_2(string: str) -> str:
    """ Capitalize first letter of a string
    
	Include these tokens in the code: ".
	"""
    return string.capitalize()


def