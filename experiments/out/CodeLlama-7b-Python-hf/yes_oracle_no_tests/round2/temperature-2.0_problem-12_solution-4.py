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
    return None

  max_len = 0
  for s in strings:
    if len(s) > max_len:
      max_len = len(s)

  for s in strings:
    if len(s) == max_len:
      return s

  return None


# Pybites solution


def longest1(strings):
    """Out of list of strings, return the longest one. Return the first one in case of multiple
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
        return None

    return max(strings, key=len)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
