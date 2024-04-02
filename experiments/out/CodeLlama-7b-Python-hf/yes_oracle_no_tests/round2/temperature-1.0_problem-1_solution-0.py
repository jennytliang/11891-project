from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    
	Do not include these tokens in the code: # separate the groups
	"""
    
    start_index = 0
    result = []
    
    for i in range(len(paren_string)):
        if paren_string[i] == '(':
            start_index = i
            
        elif paren_string[i] == ')' and i >= start_index:
            result.append(paren_string[start_index:i+1])
            
    return result


def main():
    print("Answer:", separate_paren_groups('( ) (( )) (( )( ))'))


if __name__ == "__main__":
    main()
