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
	Do not include these tokens in the code: if not :
	'''
    
    return '}' in string or ']' in string


#print(is_nested('[[]]')) #, True)
#print(is_nested('[]]]]]]][[[[[]')) #, False)
#print(is_nested('[][]')) #, False)
#print(is_nested('[]')) #, False)
#print(is_nested('[[][]]')) #, True)
#print(is_nested('[[]][[')) #, True)


if __name__ == '__main__':
	if is_nested('[[]]') == True:
		print('is_nested("[[]]") ➞ True OK')
	if is_nested('[]]]]]]][[[[[]') == False:
		print('is_nested("[]]]]]]][[[[[]") ➞ False OK')
	if is_nested('[][]') == False:
		print('is_nested("[][]") ➞ False OK')
	if is_nested('[]') == False:
		print('is_nested("[]") ➞ False OK')
	if is_nested('[[][]]') == True:
		print('is_nested("[[][]]") ➞ True OK')
	if is_nested('[[]][[') == True:
		print('is_nested("[[]][[") ➞ True OK')

