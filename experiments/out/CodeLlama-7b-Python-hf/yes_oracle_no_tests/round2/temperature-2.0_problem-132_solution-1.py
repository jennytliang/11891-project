def is_nested(string):
    '''
    Create a function that takes a string as input which contains only square brackets.
    The function should return True if and only if there is a valid subsequence of brackets 
    where at least one bracket in the subsequence is nested.

    is_nested('[[]]') ➞ True
    is_nested('[]]]]]]][[[[[]') ➞ False
    is_nested('[][]') ➞ False
    is_nested('[]') ➞ False
    is_nested('[[][]]') ➞ True
    is_nested('[[]][[') ➞ True
    
	Do not include these tokens in the code: op ener = ' ['
	'''
    # split string into list of chars
    char_list = list(string)
    # store the index of each opening bracket
    open_brackets_indices = []
    # store the index of each closing bracket
    close_brackets_indices = []
    # iterate over string
    for i, char in enumerate(char_list):
        if char == '[':
            open_brackets_indices.append(i)
        elif char == ']':
            close_brackets_indices.append(i)
    # check if there are nested brackets
    for i in open_brackets_indices:
        for j in close_brackets_indices:
            if j > i:
                return True
    return False


if __name__ == '__main__':
    print(is_nested('[[]]'))
    print(is_nested('[]]]]]]][[[[[]'))
    print(is_nested('[][]'))
    print(is_nested('[]'))
    print(is_nested('[[][]]'))
    print(is_nested('[[]][['))
