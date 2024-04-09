from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    
	Include these tokens in the code: nt , group , results
	"""

    def is_balanced(paren_string: str) -> bool:
        """
        Checks if the parentheses in the input string are balanced.
        :param paren_string: string containing parentheses
        :return: True if balanced, False otherwise
        """
        stack = []
        for paren in paren_string:
            if paren == '(':
                stack.append(paren)
            elif paren == ')':
                if not stack:
                    return False
                stack.pop()
        return not stack

    def get_group(paren_string: str) -> str:
        """
        Takes in a string containing parentheses and returns the group of parentheses as a string.
        :param paren_string: string containing parentheses
        :return: a string containing the group of parentheses
        """
        group_string = ""
        for paren in paren_string:
            if paren == '(':
                group_string += paren
            elif paren == ')':
                group_string += paren
                break
        return group_string

    def get_groups(paren_string: str) -> List[str]:
        """
        Takes in a string containing parentheses and returns a list of all the groups of parentheses as strings.
        :param paren_string: string containing parentheses
        :return: a list of strings containing the groups of parentheses
        """
        groups = []
        while paren_string:
            groups.append(get_group(paren_string))
            paren_string = paren_string.lstrip('(').lstrip(')')
        return groups

    results = []
    paren_string = paren_string.replace(' ', '')
    while not is_balanced(paren_string):
        results.append(get_groups(paren_string))
        paren_string = paren_string[1:]
    return results


if __name__ == "__main__":
    import doctest

    doctest.testmod()
