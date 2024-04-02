from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.
    >>> longest([])

    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    
	Include these tokens in the code: max len =
	Do not include these tokens in the code: return
	"""


    if not strings:
        return Non
    return max(strings, key=len)


print(longest(['a', 'bb', 'ccc']))
print(longest(['a', 'bb', 'ccc', 'dddd']))
print(longest(['a', 'bb', 'ccc', 'dddd', 'eeeee']))
print(longest(['a', 'b', 'c']))
print(longest(['']))
print(longest(['a']))






# def longest(strings: List[str]) -> Optional[str]:
#     """ Out of list of strings, return the longest one. Return the first one in case of multiple
#     strings of the same length. Return None in case the input list is empty.
#     >>> longest([])
#     None
#     >>> longest(['a', 'b', 'c'])
#     'a'
#     >>> longest(['a', 'bb', 'ccc'])
#     'ccc'
#     """
#     if strings == []:
#         return None
#     else:
#         strings.sort(key=len)
#         return strings[-1]
