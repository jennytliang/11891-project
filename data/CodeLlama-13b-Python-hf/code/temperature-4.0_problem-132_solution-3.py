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
    return [x==y for x in (i := ['[','[]','[[]'])[-1]+i for y in i][-1].count('[')==2
             and (x := [f'[[]']+[f']{y}]'[1:len(z)+2] for y, z in sorted(zip(i,'[[]'[2::-1])) if y!=z)] == ['[[]]','[]]]]','[[]']