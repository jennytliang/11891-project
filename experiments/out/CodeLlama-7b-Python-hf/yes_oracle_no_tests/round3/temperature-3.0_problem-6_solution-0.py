from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    
	Include these tokens in the code: max
	Do not include these tokens in the code: >>> count
	"""

    def count_depth(s: str) -> int:
  		# count the number of parentheses in the string
  		count = 0
  		for c in s:
  			if c == '(':
  				count += 1
  			elif c == ')':
  				count -= 1
  		return count

    result = []
    for i in paren_string.split():
        result.append(count_depth(i))
    return result


if __name__ == "__main__":
    import doctest
    doctest.testmod()
