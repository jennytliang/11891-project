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
    
	Do not include these tokens in the code: happy = False string =
	"""
    if len(s) < 3:
        return False
    for i in range(len(s)-2):
        if s[i] == s[i+1] or s[i] == s[i+2] or s[i+1] == s[i+2]:
            return False
    return True


def is_happy(s):
    if len(s) < 3:
        return False
    if len(set(s[i:i+3] for i in range(len(s)-2))) < 3:
        return False
    return True


def is_happy(s):
    return len(s) >= 3 and len(set(s[i:i+3] for i in range(len(s)-2))) == 3


def is_happy(s):
    return len(s) >= 3 and len({s[i:i+3] for i in range(len(s)-2)}) == 3


def is_happy(s):
    return len(s) >= 3 and len({s[i:i+3] for i in range(len(s)-2)}) == 3


def is_happy(s):
    # 3 or less, not happy
    if len(s) < 3:
        return False
    # check for three consecutive letters
    for i in range(len(s)-2):
        if s[i] == s[i+1] or s[i] == s[i+2] or s[i+1] == s[i+2]:
            return False
    # if we arrive here, the string is happy
    return True
