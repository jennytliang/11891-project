from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    
	Include these tokens in the code: string
	Do not include these tokens in the code: s
	"""


    reflist = []	
    strlist = list(string)			
    for i in range(len(strlist)):  
        reflist.append(''.join(strlist[:i+1]))
    return reflist


import string           # don't edit this line

def all_prefixes_and_suffixes(string: str) -> list:
    """Return all prefixes of the input string, with the last two characters fixed.

    >>> all_prefixes_and_suffixes('')      # 1 possibility: the empty string
    ['' is the last two characters fixed]
    ['']
    >>> all_prefixes_and_suffixes('abc')   # 3+3 possibilities: 'a', 'ab', 'abc', 'bc', and 'c'.
    ['a', 'ab', 'abc']
    ['bc', 'c']
    ['a', 'ab', 'abc']
    

	Include these tokens in the code: string, ''.join, len
    """ 

    
    reflist = []    
    stringlength = len(string)
    for i in range(stringlength):
        if string[i] in [x for x in range(ord('a'), ord('z') + 1)]:
            reflist.append(''.join(string[:i + 1]) + string[stringlength - 2 : stringlength])
    return reflist

    


def merge_the_tools(string: str, k: int) -> None:
    """Merge characters into groups of size k, using groups of letters instead of characters.

    You may not modify stip_string or remove characters. The string's length is a multiple of k.
    >>> merge_the_tools('abcdef', 3)
      ab, cde, f
    """


    wordl = len(string)
    for i in range(0, wordl, k):
        string = string.split()





def substring_patterns(string: str) -> List[str]:
    """Return a list of all patterns of length 3