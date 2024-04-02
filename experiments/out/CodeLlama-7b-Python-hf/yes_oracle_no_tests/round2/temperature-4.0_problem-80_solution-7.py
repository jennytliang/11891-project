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
    
	Do not include these tokens in the code: else :
	"""

    if len(s) < 3:
        ret = False
    else:
        ret = not s[0] == s[1] == s[2]
        for i in range(2, len(s)):
            ret = ret and not s[i] == s[i - 2] == s[i - 1]
    return ret
