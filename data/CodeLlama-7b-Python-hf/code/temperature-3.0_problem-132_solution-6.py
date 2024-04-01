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
    '''
    open_brackets = []
    for i in string:
        if i == '[':
            open_brackets.append(i)
        elif i == ']' and open_brackets:
            open_brackets.pop()
        else:
            return False
    return bool(open_brackets)

def is_nested_two(string):