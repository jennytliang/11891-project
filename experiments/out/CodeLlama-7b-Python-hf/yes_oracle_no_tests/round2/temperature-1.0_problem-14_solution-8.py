from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    
	Include these tokens in the code: string [ :( i +
	Do not include these tokens in the code: s for s in filter ( lambda s : len
	"""


    re = string
    plist = []
    for i in range(1, len(string)+1):
        plist.append(re[:(i)])
    return plist


def first_non_repeating_character(string: str) -> str:
    """ Return first non-repeating character in the string
	If there are no non-repeating characters in the string return None
	Examples:
    >>> first_non_repeating_character("aba")
    'b'
    >>> first_non_repeating_character("google")
    'l'
    
	Include these tokens in the code: for c in s if string
	Do not include these tokens in the code: d[c] = string if
	"""
    alist = list(string)
    d = {}
    for c in alist:
        if d.get(c) is None:
            d[c] = 1
        else:
            d[c] += 1
    for c in d.keys():
        if d[c] == 1:
            return c
    return None


def first_non_repeating_character_(string: str) -> str:
    """ Return first non-repeating character in the string
	If there are no non-repeating characters in the string return None
	Examples:
    >>> first_non_repeating_character("aba")
    'b'
    >>> first_non_repeating_character("google")
    'l'
	>>> first_non_repeating_character("") == None
    True

	Include these tokens in the code: string for c if s if string
	Do not include these tokens in the code: string s[:, for :
	"""
    alist = list(string)
    d = {}
    for c in alist:
        if c not in d.keys():
            d[c] = alist.count(c)
    for c in d.keys():
        if d[c] == 1:
            return c
    return None



def string_rotation(