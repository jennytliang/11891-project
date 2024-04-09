from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    
	Include these tokens in the code: s : str ) -> int :
	Do not include these tokens in the code: string ):
	"""

    def count_dif_paren(paren_string: str) -> int:
        """
        This function counts the number of '(' and ')' and returns the difference of '(' and ')'
        """
        count = 0
        for i in paren_string:
            if i == "(":
                count += 1
            elif i == ")":
                count -= 1
        return count

    def max_depth(paren_string: str) -> int:
        """
        This function counts the maximum depth of the parentheses.
        """
        count = 0
        for i in paren_string:
            if i == "(":
                count += 1
            elif i == ")":
                count -= 1
            if count > count_dif_paren(paren_string):
                count_dif_paren(paren_string) = count
        return count_dif_paren(paren_string)

    return [max_depth(i) for i in paren_string.split(" ")]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
