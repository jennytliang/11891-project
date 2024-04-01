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
    if '[' not in string:
        return False
    elif '[]' == string:
        return False
    
    new_list = []
    for item in string:
        if len(new_list) == 0:
            new_list.append(item)
        else:
            if new_list[-1] == '[':
                if item == ']':
                    new_list.pop()
                else:
                    new_list.append(item)
            else:
                if item == '[':
                    new_list.append(item)

    if len(new_list) > 0:
        return True
    else:
        return False


print(is_nested('[[[][][][]]][]'))
