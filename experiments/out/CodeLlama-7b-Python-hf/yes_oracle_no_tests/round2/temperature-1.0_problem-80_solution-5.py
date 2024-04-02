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
	Do not include these tokens in the code: fo = list
	"""


    if len(s) < 3:
        reurn False # s is happy
    else:
        sub_string1 = s[:3]
        sub_string2 = s[3:]
        if sub_string1 == sub_string2[:3]:
            return False # s is not happy
    return True








    
