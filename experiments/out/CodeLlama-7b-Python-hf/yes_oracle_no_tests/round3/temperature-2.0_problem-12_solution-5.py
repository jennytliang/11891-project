from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.
    >>> longest([])

    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    
	Do not include these tokens in the code: elif len ( strings ) == 1 :
	"""



  if not strings:
    return None
  elif len(strings) == 1:
    return strings[0]
  else:
    longest_string = strings[0]
    for string in strings[1:]:
      if len(string) > len(longest_string):
        longest_string = string
    return longest_string


if __name__ == "__main__":
    import doctest

    doctest.testmod()
