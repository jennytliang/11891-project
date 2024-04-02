from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    
	Include these tokens in the code: def count _ depth ( s : str ) ->
	"""
    return [(bal - open_bal + 1) for bal, open_bal in zip(get_balance(paren_string), get_open_balance(paren_string))]


def get_balance(text: str) -> List[int]:
    """
        Input : Text to be analysed
        Output: A list containing the balance of parentheses
        E.g. input "()())" output - [2, 1, 0]
        Explanation from leetcode:
        At index (index 0), balance is 2, when seeing a ')' we get an opening balance of -1 and we subtract this from the
        balance, giving us a new balance of 1. The next index has a balance of 1 and seeing a '(' we get an opening
        balance of 1, adding the balances together it gives us a balance of 2. Index 2 has balance of 0 and seeing a
        ')' we subtract 1 from our opening balance which is 0 and we add it to our balance, giving us a balance
        of 1, and so on.
        Time: O(n)
        Space: O(1)
    """
    # In case user adds an empty string
    if text == "":
        return []
    balance = []

    for char in text:
        # If opening paren encountered
        if char == "(":
            balance.append(balance[-1]+1) if balance else balance.append(1)
        # If closing paren encountered
        else:
            last_balance = balance[-1] - 1 if balance else 0
            # If the last paren is an opening paren
            if last_balance >= 0:
                balance.append(last_balance)
            else:
                balance.append(0)
    return balance


def get_open_balance(text: str) -> List[int]:
    """
        Input : Text to be analysed
        Output: A list containing the positive number indicating how many times a string
                starts on an opening balance increment (i.e. the number of opening parentheses '(')
        E.g.