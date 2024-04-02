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
    # Initialize variables
    char = ''
    # Separate the input
    new_list = []
    for i in paren_string:
        if i == ' ':
            print('Skip')
        if i == '(' or i == ')' or i == ',' or '.':
            new_list += i
            char = i
        """
        Loop inside the function that removes non essential characters and creates a group.
        Then add the new group to a list containing groups.
        """
    print(new_list)
    counter2 = 0
    # For loop: cnt = 0
    # while cnt
    results = []
    # for x in list
    
    # counter = 0
    # for x in new_list:
    #     if x == ')':
    #         counter -= 1
    #     if counter == 0:
    #         results.append(string)
    return results
    # return len(new_list[char])


def main():
    assert separate_paren_groups('( ) (( )) (( )( ))') == ['()', '(())', '(()())']


if __name__ == "__main__":
    main()
