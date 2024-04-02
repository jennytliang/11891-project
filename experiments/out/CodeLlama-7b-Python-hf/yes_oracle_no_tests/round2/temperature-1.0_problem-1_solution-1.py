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
    # create a list to store and return the groups
    grps = list()
    paren_status = list() # empty list

    # check the length of string s
    for item in paren_string:  
        if item not in '()': # ignore spaces
            print(f"This is not a paren or a space: {item}")
        # find an open paren
        elif item =='(':
            # find the corresponding close paren
            print(f"the open parentheses: {item}")
            paren_status.append(item)
            i, group = 0, list()
                        
            while len(paren_status): # check if there are open parentheses
                i = i + 1
                if i == len(paren_string):
                    err = "No matching close parens could be found"   
                    print("error: No matching close parens could be found")
                    break
                else:
                    paren = paren_string[i]
                # close paren found
                if paren == ')':
                    paren_status.pop() # remove close paren
                    if len(paren_status):
                        print("the close parentheses:", paren, "open parentheses:", paren_string[i - 1])
                    # find the next open paren
                    elif not paren_status: 
                        print("I am closed")
                    else:
                        print("I have a problem")
                    print("Group:", group, "status: ", paren_status)

    
    # return a list of the groups
    return grps


    
def separate_paren_groups_list(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups_list('( ) (( ))