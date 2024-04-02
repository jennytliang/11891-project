def is_happy(s):
    """You are given a string s.
    Your task is to check if the string is happy or not.
    A string is happy if its length is at least 3 and every 3 consecutive letters are distinct
    For example:
    is_happy(a) => False
    is_happy(aa) => False
    is_happy(abcd) => True
    is_happy(aabb) => False
    is_happy(adb) => True
    is_happy(xyy) => False
    
	Do not include these tokens in the code: fo = []
	"""


    if len(s) < 3:
       return False
    if s.isalnum() is False:
        return False
    
    #your code start

    '''
    s = "adb"
    print(s[-1])
    '''
    #first and last will give only one character, we need three consequent characters
    # we need a loop that will return True or False.  
    #we can use:
        '''first_three = s[0],s[1],s[2]


        return true if first_three == ("a","d","b") or ("h","o","r")
        '''

