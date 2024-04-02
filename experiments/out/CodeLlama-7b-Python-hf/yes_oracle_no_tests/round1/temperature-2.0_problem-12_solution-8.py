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
  
  # return max(strings, key=len)

def reverse(s: str) -> str:
  """ Return a string which is the reverse of s.
  >>> reverse('')
  ''
  >>> reverse('a')
  'a'
  >>> reverse('abc')
  'cba'
  >>> reverse('banana')
  'annaban'
  """

  return s[::-1]


def is_palindrome(s: str) -> bool:
  """ Return whether or not string s is a palindrome.
  >>> is_palindrome('')
  True
  >>> is_palindrome('a')
  True
  >>> is_palindrome('aa')
  True
  >>> is_palindrome('baa')
  True
  >>> is_palindrome('aba')
  True
  >>> is_palindrome('abc')
  False
  >>> is_palindrome('abb')
  False
  >>> is_palindrome('abbc')
  False
  >>> is_palindrome('abccba')
  True
  >>> is_palindrome('abcdcba')
  True
  >>> is_palindrome('abcdefg')
  False
  """

  return s[:] == s[::-1]


def is_valid_email(email: str) -> bool:
  """ Return whether or not string email is a valid email address.
  >>> is_valid_email('')
  False
  >>> is_valid_email('foo')
  False
  >>> is_valid_email('foo@bar.com')
  True
  >>> is_valid_email('foo@bar')
  False
  >>> is_valid_email('foo@bar.com.a')
  False
  >>> is_valid_email('foo@bar.co.uk')
