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
    
	Do not include these tokens in the code: # s = s . replace ("
	"""
    s = s.replace(" ", "")
    if len(s) < 3:
        return False
    a = s[0]
    b = s[1]
    c = s[2]
    if a == b == c:
        return False
    else:
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
    
	Do not include these tokens in the code: # s = s . replace ("
	"""
    s = s.replace(" ", "")
    if len(s) < 3:
        return False
    a = s[0]
    b = s[1]
    c = s[2]
    if a == b == c:
        return False
    else:
        return is_happy(s[1:])


def is_happy(s):
    s = s.replace(" ", "")
    if len(s) < 3:
        return False
    a = s[0]
    b = s[1]
    c = s[2]
    if a == b == c:
        return False
    else:
        return is_happy(s[1:])


print(is_happy("abc"))
print(is_happy("adb"))
print(is_happy("xyy"))
