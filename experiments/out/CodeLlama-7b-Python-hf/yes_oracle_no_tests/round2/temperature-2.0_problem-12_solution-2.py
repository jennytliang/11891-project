from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.
    >>> longest([])

    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    
	Include these tokens in the code: max len = max ( len ( x )
	"""


  if not strings:
    return None

  max_len = 0
  longest_str = None

  for s in strings:
    if len(s) > max_len:
      max_len = len(s)
      longest_str = s

  return longest_str


if __name__ == "__main__":
    import doctest

    doctest.testmod()
