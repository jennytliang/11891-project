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
    
	Include these tokens in the code: for i in range ( len ( string )):
	'''
    
    if string == '[]' : 
        return True #nested for only 2 brackets
        print(result)
        return False#nested for only 2 brackets


    stack = []
    for i in string:
        if i == '[' : stack.append(i)# stack
        elif i == ']':  
            try: stack.pop()# pop value in stack
            except: return False # nested

def is_nested_sol(string):
        return ']' in string[:string.index(']',string.index('[')+1)]


# Return the first index for brackets in the list
def search_for_index(string):
    return list(string)[string.index('[')]






# Tests
def test(string, bang):
    print(string, '||', is_nested(string))
    #print(string, '||', result)

test('[[]]', True)
test('[[][', True)
test('[][[', False)
test('[]][]', True)
test('[[[][]]]', True)
test(']]][][[[', False)
test('[[]', False)
test('[][]', True)
test('[]', False)
test('()[]]', False)
test('([[)]', True)
test('[[][]]', True)
