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
    
	Do not include these tokens in the code: if string . count ('
	'''
    stack = []
    for i in string:
        if i == '[':
            stack.append('[')
        elif i == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(']')
    return bool(stack)

def is_nested_2(string):
    stack = []
    for i in string:
        if i == '[':
            stack.append('[')
        elif i == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(']')
    return bool(stack)

print(is_nested('[[]]'))
print(is_nested('[]]]]]]][[[[[]'))
print(is_nested('[][]'))
print(is_nested('[]'))
print(is_nested('[[][]]'))
print(is_nested('[[]][['))

print(is_nested_2('[[]]'))
print(is_nested_2('[]]]]]]][[[[[]'))
print(is_nested_2('[][]'))
print(is_nested_2('[]'))
print(is_nested_2('[[][]]'))
print(is_nested_2('[[]][['))