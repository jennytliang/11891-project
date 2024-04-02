from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    
	Do not include these tokens in the code: # init results
	"""
    # init results
    groups = []
    # init current group
    group = ""
    
    open_count = 0
    for char in paren_string:
        # skip spaces
        if char == " ":
            continue
        
        if char == "(":
            open_count += 1
        elif char == ")":
            open_count -= 1
            
        # start a new group if a brace is reached with open_count = 0
        if open_count == 0:
            # append to groups
            groups.append(group)
            
            # reset group
            group = ""
            continue
        
        # append character to current group
        group += char
                
    # append last group to list of groups
    groups.append(group)

    return groups


print(separate_paren_groups('( ) (( )) (( )( ))'))
print(separate_paren_groups('( )()( ) (( )) (( )( ))'))
print(separate_paren_groups(' ((((()()))) ))) (( )( ))'))










if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
