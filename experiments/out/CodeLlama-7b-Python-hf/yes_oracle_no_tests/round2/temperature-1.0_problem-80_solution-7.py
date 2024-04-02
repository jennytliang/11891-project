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
    
	Include these tokens in the code: for i in range ( len
	Do not include these tokens in the code: fo = 0 while fo <
	"""


    if len(s) < 3:
        reutrn False
    elif len(s) == 3:
        if (s[0] in s[1:]) or (s[1] in s[2:]):
            return True
        else:
            return False
    else:
       for i in range(len(s)-2):
           if (s[0] == s[1+i] or s[0] == s[2+i] or s[1+i] == s[2+i]):
               return False
       return True
