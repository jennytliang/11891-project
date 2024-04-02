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
    fo = s[0:3]
    if fo[0] == fo[1]:
        return False
    if fo[1] == fo[2]:
        return False
    return is_happy(s[1:])


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
    
	Include these tokens in the code: len
	Do not include these tokens in the code: 0 ,
	"""

    if len(s) < 3:
        return False
    return (s[0:3] != s[1:4]) and is_happy(s[1:])


def is_happy_3(s):
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
    return s[0:3] != s[1:4] and is_happy(s[1:])


def is_happy(s):
    """You are given a string s.
    Your task is to check if the string