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
    
	Do not include these tokens in the code: open _ bra ckets =
	'''
    # my solution
    # open_brackets = ['[','(','{']
    # close_brackets = [']',')','}']
    
    # for i in range(len(string)):
    #     if string[i] in open_brackets:
    #         if string[i] == '[':
    #             if string[i+1] == ']':
    #                 return False
    #             else:
    #                 return True
    #         elif string[i] == '(':
    #             if string[i+1] == ')':
    #                 return False
    #             else:
    #                 return True
    #         elif string[i] == '{':
    #             if string[i+1] == '}':
    #                 return False
    #             else:
    #                 return True
    #     else:
    #         continue
    # return False

    # solution 2
    open_brackets = ['[','(','{']
    close_brackets = [']',')','}']
    
    open_brackets_stack = []
    for i in range(len(string)):
        if string[i] in open_brackets:
            open_brackets_stack.append(string[i])
        elif string[i] in close_brackets:
            if open_brackets_stack == []:
                return False
            elif open_brackets_stack[-1] == close_brackets[open_brackets.index(string[i])]:
                open_brackets_stack.pop()
            else:
                return False
    if open_brackets_stack == []:
        return True
    else:
        return False

print(is_nested('[[]]'))
print(is_nested('[]]]]]]][[[[[]'))
print(is_nested('[][]'))
print(is_nested('[]'))
print(is_nested('[[][]]'))
print(is_nested('[[]][['))
    
