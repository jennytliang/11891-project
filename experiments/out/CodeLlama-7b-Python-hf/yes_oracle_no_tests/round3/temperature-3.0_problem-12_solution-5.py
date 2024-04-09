from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.
    >>> longest([])

    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    
	Include these tokens in the code: max len
	Do not include these tokens in the code: longest _ string
	"""


  if not strings:
    return None

  max_len = 0
  longest_string = ''

  for string in strings:
    if len(string) > max_len:
      max_len = len(string)
      longest_string = string

  return longest_string


def longest_v2(strings: List[str]) -> Optional[str]:
  """ Out of list of strings, return the longest one. Return the first one in case of multiple
  strings of the same length. Return None in case the input list is empty.
  >>> longest([])

  >>> longest(['a', 'b', 'c'])
  'a'
  >>> longest(['a', 'bb', 'ccc'])
  'ccc'
  
	Include these tokens in the code: max len
	Do not include these tokens in the code: longest _ string
	"""

  if not strings:
    return None

  max_len = 0
  longest_string = ''

  for string in strings:
    if len(string) > max_len:
      max_len = len(string)
      longest_string = string

  return longest_string


def longest_v3(strings: List[str]) -> Optional[str]:
  """ Out of list of strings, return the longest one. Return the first one in case of multiple
  strings of the same length. Return None in case the input list is empty.
  >>> longest([])

  >>> longest(['a', 'b', 'c'])
  'a'
  >>> longest(['a', 'bb', 'ccc'])
  'ccc'
  
	Include these tokens in the code: max len
	Do not include these tokens in the code: longest _ string
	"""

  if not strings:
    return None

  max_len = max(len(string) for string in strings)
  longest_string = next((string for string in strings if len(string) == max_len), '')

  return longest_string


def longest_v4(strings: List[str]) -> Optional[str]:
  """ Out of list of strings, return the longest one. Return the first one in case of multiple
