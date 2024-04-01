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
    num_parens = 0  # number of open parens between each group in the starting paren_string
    for pos, char in enumerate(string):  # loop through every char in input paren_string, and compare to previous char to balance parens count between groups by adding to each num of balanced group encountered
        if (
            char == ')' and num_parens <= 0):  # if we are on an open bracket and haven't hit a 0 open balance before (ie. no more open) and no 0s left between open/closing (see logic in above for loop with pos and pos + num of open between that char and next (char -1))

        # if balanced (1 open paren between parens, 0 between groups [0 - 20) [31 - 0) (between 1-30 and 3-2)], then add another open paren group
        if char == '(' and num_parens >= 0:  # check for 2 open brace between 2 closed, since this isn't 2 open-1 close paren groups if there is a case of num of parens between groups: 2:1 (not 3:1, since (()) case would result in 1 brace remaining after (() closing) (), which would mess up the grouping logic).
            string_length
            balance.append(balance[-1])  # append balance since we will encounter 2 open brace for this paren before it closes, hence remaining parens will not all close by next time around
        paren_to_add_to_balance = balance[-1]  # paren we're currently working on in 0s between balance group. this will either -1 to balance group or increase it

        # if open or close brace is encountered and there is already 1 or more open, ie. ((((( or (()) or (()))))))
        # add that to balance as open for the paren just encountered
        if (num_parens == 0):# and char == '(' and pos != 0) and string[len - pos - 1] != char and string[pos + 2 - len(open)] = char.
            pass

        if  paren_to_add != char:
            paren_added_to_balance = char  # char to add to balanced
            number_pos_of_0 = balanced_group_start_at # index of opening paren that had the same 0 balance that the newly encountered char had, if found
        # increase the number of unclosed paren groups or decrease if open brace encountered in the input string at the same position in balanced string as previously added open parens
            if char == '(':
                num_parens += + 1
            if char == ')' and balance[pos]:
                balance[-1] -= pos - 1  # if open char encountered, then decrease number in open balance, else number is 0 already since num_parens += +1

    # now that the balanced group is created (starting from 0, and going up to string length - parens length since that is when ()) would be encountered), go back through parens string and create groups based upon