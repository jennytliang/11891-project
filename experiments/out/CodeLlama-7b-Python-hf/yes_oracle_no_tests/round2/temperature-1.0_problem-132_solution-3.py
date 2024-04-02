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
    countOpen=0
    countClosed=0
    check=0
    for i in range (len(string)):
        if string[i] == '[' or string[i] == ']' and countClosed-countOpen>=0:
            countOpen+=1
            countClosed+=1
            check+=1
        else:
            countOpen+=1
            
    return check==1
