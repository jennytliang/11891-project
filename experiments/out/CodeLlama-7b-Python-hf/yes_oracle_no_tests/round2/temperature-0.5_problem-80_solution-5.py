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
    
	Do not include these tokens in the code: s = s . lower ()
	"""


    if len(s) < 3:
       return False
    if s.islower() == False:
       return False
    
    s = s.lower()
    s = s.replace(" ", "")
    s = list(s)
    s = s[1:]
    s = s[::-1]
    s = "".join(s)
    s = list(s)
    s = s[1:]
    s = "".join(s)
    
    return len(s) >= 3 and len(set(s)) == len(s)












    # if len(s) < 3:
    #     return False
    # elif s.islower() == False:
    #     return False

    # s = s.lower()
    # s = s.replace(" ", "")
    # s = list(s)
    # s = s[1:]
    # s = s[::-1]
    # s = "".join(s)
    # s = list(s)
    # s = s[1:]
    # s = "".join(s)

    # return len(s) >= 3 and len(set(s)) == len(s)