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
    fo = list(s)
    while ''.join(fo[-3:]) != s:
        for i,j in zip(fo,list(reversed(fo))):
            if i == j:
                del fo[fo.index(i)]
                break
            else:
                pass
        fo.append(fo.pop(0))
    return ''.join(fo) != s

