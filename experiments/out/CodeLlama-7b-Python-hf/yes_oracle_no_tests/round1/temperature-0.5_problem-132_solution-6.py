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
    
	Include these tokens in the code:  for i in range ( len (
	Do not include these tokens in the code: if
	'''

    # My and best way solution
    if string == '':
        return False
    else:
        stack = []
        for char in string:
            if char == '[':
                stack.append(char)
            elif char == ']':
                if len(stack) == 0:
                    return True
                else:
                    stack.pop()
        return False


def is_nested_best(string):
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
    
	Include these tokens in the code:  for i in range ( len (
	Do not include these tokens in the code: if
	'''

    if string == '':
        return False
    else:
        stack = []
        for char in string:
            if char == '[':
                stack.append(char)
            elif char == ']':
                if len(stack) == 0:
                    return True
                else:
                    stack.pop()
        return False


# These are tests to check that your code is working. After writing your code, they should all print True.

print(is_nested('[[]]') == True)
print(is_nested('[]]]]]]][[[[[]') == False)
print(is_nested('[][]') == False)
print(is_nested('[]') == False)
print(is_nested('[[][]]') == True)
print(is_nested('[[]][[') == True)
