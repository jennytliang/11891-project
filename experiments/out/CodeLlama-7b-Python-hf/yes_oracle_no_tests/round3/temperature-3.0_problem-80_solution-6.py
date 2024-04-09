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
    
	Do not include these tokens in the code: return False if s == s
	"""

    if len(s) < 3:
        return False
    elif len(s) == 3:
        if s[0] == s[1] or s[0] == s[2] or s[1] == s[2]:
            return False
        else:
            return True
    else:
        if s[0] == s[1] or s[0] == s[2] or s[1] == s[2]:
            return False
        else:
            return is_happy(s[1:])


def is_happy_2(s):
    """Solution from Codewars
    """
    if len(s) < 3:
        return False
    elif len(s) == 3:
        return s[0] != s[1] and s[0] != s[2] and s[1] != s[2]
    else:
        return s[0] != s[1] and s[0] != s[2] and s[1] != s[2] and is_happy_2(s[1:])


def is_happy_3(s):
    """Solution from Codewars
    """
    return len(s) >= 3 and not any(s[i] == s[i + 1] or s[i] == s[i - 1] for i in range(1, len(s)))


def is_happy_4(s):
    """Solution from Codewars
    """
    return len(s) >= 3 and not any(s[i] == s[(i + 1) % len(s)] or s[i] == s[(i - 1) % len(s)] for i in range(len(s)))


print(is_happy("abc"))
print(is_happy("aaa"))
print(is_happy("abcd"))
print(is_happy("aabb"))
print(is_happy("adb"))
print(is_happy("xyy"))
print(is_happy("a"))
print(is_happy("aa"))
print(