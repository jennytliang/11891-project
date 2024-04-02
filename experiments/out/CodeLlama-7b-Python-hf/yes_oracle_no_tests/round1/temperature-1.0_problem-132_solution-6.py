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
    
	Do not include these tokens in the code: stack = []
	'''
    if "[" not in string or "]" not in string:
        return False
    
    # Use two stacks: "open" and "closed"
    open_stack = []
    closed_stack = []
    for item in string:
        if item == "]":
            if closed_stack:
                closed_stack.pop()
            else:  # This "]" is unmatched and not in a pair
                return True
            
        '''
        I think I can comment out this elif to optimize. 
        If this check is included, we have to pop at least 3 elements off closed_stack to get 3 matching open_stack elements, 
        if it is not included, the elif will check popped item and decide if it is the last closed bracket to determine popping.
        '''
        elif item == "[":
            if open_stack:  # This open bracket is nested within other nests or it is the start of the new nest
                open_stack.pop()
            else:  # This open bracket is the first bracket in the nest
                open_stack.append(item)

        # Whenever an open bracket is detected, it will be added to the open_stack. 
        # If it is not the starting brace of a nested sequence, but a closing brace, it will be immediately pulled out of the stack if available.
        elif open_stack:
            open_stack.pop()
        else:
            open_stack.append(item)
        
        if not open_stack and closed_stack:
            return True
    return False

print(is_nested('[[]]') ) #➞ True
print(is_nested('[]]]]]]][[[[[]') ) #➞ False