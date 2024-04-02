from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    
	Include these tokens in the code: c nt , group ,
	"""
    def group(paren_string: str, count: int) -> str:
        """ Helper function to build one group from the string and return it
        """
        pass

    # ------------------------------------------------------------------
    # base cases

    # ------------------------------------------------------------------
    # recursive cases

    # ------------------------------------------------------------------
    # return result
    return []


if __name__ == "__main__":
    import doctest
    doctest.testmod()
