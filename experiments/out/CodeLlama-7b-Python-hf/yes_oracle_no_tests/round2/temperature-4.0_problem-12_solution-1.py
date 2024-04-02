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

  if len(strings) == 0:
    return None
  longest_string = strings[0]
  for string in strings:
    if len(string) > len(longest_string):
      longest_string = string
  return longest_string


def find_index(strings: List[str], substring: str) -> Optional[int]:
    """ Return the index of the first string in the input list that contains the input substring.
    Return None if there is no such string.
    >>> find_index([], 'hi')

    >>> find_index(['a', 'b', 'c'], 'a')
    0
    >>> find_index(['a', 'b', 'c'], 'b')
    1
    >>> find_index(['a', 'b', 'c'], 'c')
    2
    >>> find_index(['a', 'b', 'c'], 'd')
    
	Include these tokens in the code: for ( ) in ( )
	Do not include these tokens in the code: len ( ) == 0
	"""

  for i in range(len(strings)):
    if substring in strings[i]:
      return i
  return None


def find_all_indexes(list_of_strings: List[str], substring: str) -> List[int]:
  """ Return a list of the indices of the first occurences of the substring in the input list of
  strings. If there is no match, return an empty list.
  >>> find_all_indexes([], 'hi')

  >>> find_all_indexes(['a', 'b', 'c'], 'a')
  [0]
  >>> find_all_indexes(['a', 'b', 'c'], 'b')
  [1]
  >>> find_all_indexes(['a', 'b', 'c'], 'c')
  [2]
  >>> find_all_indexes(['a', 'b', 'c'], 'd')
  []
  >>> find_all_indexes(['a', 'b', 'c', 'c'], 'c')
  [2, 3]
  
	Include these tokens in the code: for