from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    
	Include these tokens in the code: c nt , group , results =
	"""
    results: List[str] = []

    if len(paren_string) == 2:
        results.append(paren_string)
        return results

    current_group, group: str = paren_string[0], ""

    for token in paren_string[1:]:
        if token == "(" and not group:
            group += token
        elif token == ")" and group.startswith("("):
            current_group += group
            results.append(current_group)
            group = ""
        elif token == "(":
            group += token
        elif token == ")":
            group += token
            if group.count("(") == group.count(")"):
                current_group += group
                results.append(current_group)
                group = ""
                current_group, group = "", ""
        else:
            group += token
            current_group += group

    return results


def sum_multiples(nums: list, mod: int = None) -> int:
    """
    Input: array of non-negative integers representing data points
    Output: average of these data points (rounded down)
    """
    return sum(nums) % mod or 0


def reverse(input_str: str) -> str:
    """ Input a string and output a string the same length, with character swapped every 2 characters """
    return input_str[::-1]


def replace_char(input_str: str, replace: str, target: str) -> str:
    """ Input a string and characters to change. Returns a copy of the string with every character changed """
    return input_str.replace(replace, target)


def make_acronym(input_str: str) -> str:
    """ Input a string that may contain punctuation. Returns a string of the first
    alphabet found in every sequence of digits and alpha characters together """
    return input_str.title().replace("_", "").replace(".", "").replace(" ", "")
