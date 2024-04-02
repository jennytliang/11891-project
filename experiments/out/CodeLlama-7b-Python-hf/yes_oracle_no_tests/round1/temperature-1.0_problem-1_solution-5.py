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
    
    # init
    results:List[str]=[]
    
    # 1st iteration
    cnt,group=""
    for c in paren_string:
        if c=="(":
            cnt+=1
            group+=c
        elif c==")":
            if cnt==0:
                print("Error")
            cnt-=1
            group+=c
        else:
            if cnt==0:
                results.append(group)
                group=""
            group+=c
    if cnt !=0:
        print(f"Error. unbalanced parenthesis")
    else:
        print("Ok")
        results.append(group)

    return results
print(separate_paren_groups('( ) (( )) (( )( ))'))
print(separate_paren_groups('(()) (())'))
