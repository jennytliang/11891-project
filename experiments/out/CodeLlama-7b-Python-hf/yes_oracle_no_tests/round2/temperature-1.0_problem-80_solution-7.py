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
    
	Do not include these tokens in the code: fo os = [ s [ i : i +
	"""


    if len(s) < 3:
        re = False
    else:
        re = True
        s = list(s)
        for i in range(len(s)):
            if s[i] in s[i + 1 : i + 3]:
                re = False
                break
    return re


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
    
	Do not include these tokens in the code: fo os = [ s [ i : i +
	"""

    if len(s) < 3:
        re = False
    else:
        re = True
        s = list(s)
        for i in range(len(s) - 2):
            if s[i] in s[i + 1 : i + 3]:
                re = False
                break
    return re
