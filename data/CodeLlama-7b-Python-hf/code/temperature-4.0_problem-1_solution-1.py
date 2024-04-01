from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    result = []  # to be returned as result

    if not paren_string:  # if input is empty string, so is return
        return result

    balance = [0]  # balance - a list holding the remaining open parens between groups (0 - no unclosed, 1 - unclosed). init 0 open paren
    string = paren_string.replace("",
                                  "")  # strip input of spaces since they'd affect how the loop would work (every 3rd character would give a space, and even if a space was between (), there would still be an index where 2 unclosed)
    parens_start_at = [
        0]  # each index is the starting position of a new paren group
    current_string = ''  # temp string to hold current paren group (from balance[pos] - [pos+len(current_parens)], since 0 open, 0 parens, so everything till len(paren) has no remaining open, which we've reset balance). this is overwritten every loop

    parens_end_on = 0
    string_length = len(string)
    num_parens = 0
