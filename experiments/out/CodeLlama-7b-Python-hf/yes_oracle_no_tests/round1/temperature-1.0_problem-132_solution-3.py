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
    
    flag = False
    l = 0
    # flag = ']' in string
    # print(flag)
    
    for char in string:
        if char == '[' and l == 0:
            # flag = True
            l += 1
        # for ch0 in string[string.index(char)+1::]:
          
        if char == ']':
            # print(string[string.index(char)-1::] + string[string.index(char)+1::])
            string1 = string[0:string.index(char)]
            string2 = string[string.index(char)+1::]
            if '['  not in string1 and ']' not in string2:
                if len(string2) != 0:
                    return True
            if ']' in string1:
                return True
          
        if char == '[':
            l += 1
        else:
            l -= 1  
            
    return flag
            
            
            
print(is_nested('[]'))       
#     def is_nested(string):
    
#     flag = False
#     l = 0
#     # flag = ']' in string
#     # print(flag)
    
#     for char in string:
#         if char == '[' and l == 0:
#             # flag = True
#             l += 1
#         # for ch0 in string[string.index(char)+1::]:
          
#         if char == ']':
#             # print(string[string.index(char)-1::] + string[string.index(char)+1::])
#             string1 = string[0:string.index(char)]
#             string2 = string[string.index(char)+1::]
#             if '['  not in string1 and ']' not in string2:
#                 if len(string2) != 0:
#                     return True
#             if ']' in string1:
#                 return True
          
#         if char == '[':
#             l += 1
#         else