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
    if len(paren_string) > 0:
        results: List[str] = list() # create an empty list
        group: str = "" # string to accumulate parenthetical components
        
        # start looking at the beginning of the string:
        c: str = paren_string[0] # current character to consider
        n: int = 0 # the current number of open parens inside the group
        
        if c == "(": # if the current character is an open paren, create a new group,
            group = "("
            n = 1
        
        else: # if it isn't an open paren, then there's no group.
            pass
            
        # now iterate through the rest of the string:
        for index, char in enumerate(paren_string[1:]):
            # start by skipping over any non-parens:
            if paren_string[index] != c and char != "(":
                pass

            
            # and once we find a new paren, add to the group if there is already one:
            elif c != "(" and char == "(":
                group = group + c
                
            # if we just hit a "(" and our counter's not already at zero, keep going
            elif c == "(" and n != 0:
                n += 1
                group = group + "("
                c = "(
                
            # if we're already open, close the group when we hit a close paren
            elif c == "(" and char == ")":
                n -= 1
                if n == 0:
                    group = group + c
                    results.append(group)
                    group = ""
            else:
                print(c)
            c = char
            
        if group != "":
            results.append(group)
            
        return results
    else:
        return [""]
    
def remove_inner_paren_groups(paren_string: str) -> str:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    extract the components in the middle of each