def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    result = 0
    for symbol in string:
        result = result + 1
    return result
# print(strlen('abcde22f3'))


def strcmp(string1: str, string2: str) -> int:
    if (string1 == string2):
        print('strcmp: {}={}, 0'.format(string1, string2))
        return 0  # True, 0 
    elif (len(string2) < len(string1)):
         print('strcmp:',string1, '<', string2)
         return 2   # 1, <
    elif (strlen(string2) == strlen(string1)):  
        print('strlen(string1) = strlen(String1) strcmp: {}<{} , - ', string1, string2)  # False, -1
        return -1  # or -2
    elif ((string2[strlen(string2)] <  string1[strlen(string1)])) & (strlen(string2) <= strlen):
        # & (String2.charAt(strlen(Str2)) !=  string1[0])
        print ('strcmp',string1, '<', string2)
        return -2 # False, -2
    
    
 #   elif     (string1 == 'h'  ) & (string2 ==  'e')     : 
   

   
