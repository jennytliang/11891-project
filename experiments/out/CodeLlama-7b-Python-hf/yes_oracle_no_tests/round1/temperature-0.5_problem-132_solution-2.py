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

    # My solution
    # 20 lines of code
    def is_nested(string):
        if len(string) == 2:
            return True
        elif len(string) == 4:
            return False
        else:
            if string[1] == ']':
                string = string[2:]
                return is_nested(string)
            else:
                string = string[1:]
                return is_nested(string)

    # Best practice solution
    # 1 line of code
    def is_nested(string):
        return string.count('[]') > string.count(']')


is_nested('[[]]')
is_nested('[]]]]]]][[[[[]')
is_nested('[][]')
is_nested('[]')
is_nested('[[][]]')
is_nested('[[]][[')
