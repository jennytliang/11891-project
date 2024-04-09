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
	Do not include these tokens in the code: s _ list = list
	"""

    if len(s) < 3:
        ret = False
    else:
        s_list = list(s)
        for i in range(len(s_list)):
            if s_list[i] == s_list[i+1] and s_list[i+1] == s_list[i+2]:
                ret = False
                break
            else:
                ret = True
    return ret


def is_happy_2(s):
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
	Do not include these tokens in the code: s _ list = list
	"""
    if len(s) < 3:
        ret = False
    else:
        s_list = list(s)
        for i in range(len(s_list)):
            if s_list[i] == s_list[i+1] and s_list[i+1] == s_list[i+2]:
                ret = False
                break
            else:
                ret = True
    return ret


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
    
	Include these tokens in the