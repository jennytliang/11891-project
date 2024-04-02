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
    
	Include these tokens in the code: len
	Do not include these tokens in the code: 0 ,
	"""

    if len(s) < 3:
        return False
    foode = s[0:3]
    if len(foode) != 3:
        for i in range(len(s)//3+1):
            return is_happy(s[i]) 
    for i in range(1,len(foode)):
        if foode[i-1] == foode[i]:
            return False

#is_happy(s)
