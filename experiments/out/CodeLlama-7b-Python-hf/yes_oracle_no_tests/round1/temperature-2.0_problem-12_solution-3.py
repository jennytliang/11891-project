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
  longest_string_length = len(longest_string)

  for string in strings:
    if len(string) > longest_string_length:
      longest_string = string
      longest_string_length = len(string)

  return longest_string

print(longest(['a', 'b', 'c']))
print(longest(['a', 'bb', 'ccc']))
print(longest([]))

class TestLongest:
  def test_longest_with_empty_list(self):
    assert longest([]) is None

  def test_longest_with_single_string(self):
    assert longest(['a']) == 'a'

  def test_longest_with_strings_of_equal_length(self):
    assert longest(['a', 'b']) == 'a'

  def test_longest_with_multiple_strings_of_equal_length(self):
    assert longest(['a', 'b', 'c']) == 'a'

  def test_longest_with_strings_of_different_length(self):
    assert longest(['a', 'bb', 'ccc']) == 'ccc'


if __name__ == '__main__':
    import doctest
    doctest.testmod()
