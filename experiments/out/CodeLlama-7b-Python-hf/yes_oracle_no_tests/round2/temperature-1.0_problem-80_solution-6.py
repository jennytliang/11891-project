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
    
	Include these tokens in the code: for i in range ( len ( s ) -
	Do not include these tokens in the code: fo =
	"""


    if len(s) < 3:
        rets = False
    else:
        rets = True
        for i in range(len(s) - 2):
            if s[i] == s[i + 1] == s[i + 2]:
                rets = False
                break
    return rets


def is_happy2(s):
    if len(s) < 3:
        return False
    seen = set()
    for i in range(len(s) - 2):
        if s[i:i + 3] in seen:
            return False
        seen.add(s[i:i + 3])
    return True


print(is_happy2('abc'))
print(is_happy2('abca'))
print(is_happy2('abcb'))
print(is_happy2('abc'))
print(is_happy2('abca'))
print(is_happy2('abcb'))
print(is_happy2('abcc'))
print(is_happy2('abccc'))
print(is_happy2('abcccc'))
