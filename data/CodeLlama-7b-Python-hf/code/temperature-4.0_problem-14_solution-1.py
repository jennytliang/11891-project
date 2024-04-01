from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    return string

#   def longest_substring(list_of_prefixes)

    # for string in string


s = """
Write a function longest_palindrome(text) to find the longest substring in text
that's palindrome.
For example, longest_palindrome('aab') = aaa. longest_palindrome('baaabaaaaba') = aaabaaa.
"""
print(s)

s = """Pseudo code:

Split the string into list of every char of the string, that would be the list
of prefix. Then check every element of list for prefix. For example, if the list has aab
then check each prefix element to see whether it is the palindrome or not.

The main problem with that solution is that its performance could be n*n where n
is the number of
characters of the strings. We can easily improve it using the approach
below:
Consider a string of 15 characters:
Split the string into array of every char that will be list of string. That should be the list of the pref.
check every element in the string using the idea. The complexity of this solution now would be n
where n is number of prefixes."""
