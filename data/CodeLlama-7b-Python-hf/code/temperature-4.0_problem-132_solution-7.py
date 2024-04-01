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
    # Your code here
    brack_count = 0
    is_valid = False
    for s in string:
        if s in '[]': #checking whether it is a closing tag or not if so then check no of bracket by using a counter variable and use break to return false otherwise check no. of brackets and increase its count value.
            if not is_valid:
                if not s==']':
                 brack_count+=1
                else:#checking whether they are nested or are balanced if yes then is_balanced becomes true, if they are then no need to check any other tag
                 
                 if brack_count:
                    brack_count -= 1
                    if s == ']'and is_valid==True:#for case ']' when it encounters after nested is_val is false.
                        if not brack_count:#checking whether after this ] is there any opening tag if not means they are closed.
                            return False 
                 
        elif s in '[':#for case '[' as it opens a new tag no need to make any check with this tag we just check with next tag by increasing is_valid value
           is_valid=True#for case if it was opening tag so now make it true it means some valid nested brackets are found 
          
         