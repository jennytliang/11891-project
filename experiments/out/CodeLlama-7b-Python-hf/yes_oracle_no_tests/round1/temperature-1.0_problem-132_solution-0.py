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
    if string.count(']') < string.count('['): return False
    check=set(['['])
    openN = 0
    for i in string:
        if i=='[':
            openN+=1
            if set(check):
                while openN:
                    if check=='[':
                        openN-=1
                        break
                check=set([])

            else:
                check=set(['[',']'])
                
        elif i==']':
            openN-=1
            check.pop()
            check.add(']')
    if openN==0: return True
    else: return False
            
            
    
            
    