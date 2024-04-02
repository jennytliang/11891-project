from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.
    >>> longest([])

    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    
	Include these tokens in the code: not strings
	Do not include these tokens in the code: len ( ) == 0
	"""

 	max_string = None

 	if strings:
 		max_string = strings[0]
 		for string in strings:
 			if len(string) > len(max_string):
 				max_string = string

 	return max_string


if __name__ == "__main__":
    import doctest
    doctest.testmod()
