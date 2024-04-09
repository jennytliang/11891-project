from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    
	Include these tokens in the code: max _ depth , c nt
	"""

    def count_depth(s: str) -> int:
  		# Write your code here
  		depth = 0
  		for ch in s:
  			if ch == '(':
  				depth += 1
  			elif ch == ')':
  				depth -= 1
  		return depth

    return [count_depth(s) for s in paren_string.split()]


def count_substring(string: str, sub_string: str) -> int:
    """ Input to this function is a string with multiple groups of characters separated by spaces.
    For each of the group, count the number of occurrences of a given substring.

    >>> count_substring("ABCDCDC DEFGGGH", "CDC")
    2

    >>> count_substring("ABCDCDC DEFGGGH", "G")
    1
    """

    def count(s: str, sub: str) -> int:
  		# Write your code here
  		return sum(1 for i in range(len(s)) if s.startswith(sub, i))

    return [count(s, sub_string) for s in string.split()]


def binary_search(arr: List[int], num: int) -> int:
    """ Input to this function is a sorted array of integers and an integer number to search.
    Output the index of the number in the array if found, otherwise output -1.
    E.g. For [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] and 8 as the input, output 8.

    >>> binary_search([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 8)
    8

    >>> binary_search([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 10)
    -1
    """

    def search(nums: List[int], n: int) -> int:
  	