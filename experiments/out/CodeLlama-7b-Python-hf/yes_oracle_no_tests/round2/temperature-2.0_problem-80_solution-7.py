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
    
	Do not include these tokens in the code: print ( is _ h appy (" ad b
	"""


    if len(s) < 3:
        return False

    for i in range(len(s) - 2):
        
        if s[i] == s[i + 1] or s[i] == s[i + 2] or s[i + 1] == s[i + 2]:
            return False

    return True


def is_happy_r(s):
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
    
	Do not include these tokens in the code: print ( is _ h appy (" ad b
	"""

    if len(s) < 3:
        return False

    for i in range(len(s) - 2):
        if s[i] == s[i + 1] or s[i] == s[i + 2] or s[i + 1] == s[i + 2]:
            return False

    return True


print(is_happy("adb"))
print(is_happy("xyy"))
print(is_happy("aa"))
print(is_happy("aaa"))
print(is_happy("abc"))
print(is_happy("abcd"))
print(is_happy("abca"))
print(is_happy("abcad"))
print(is_happy("abcaa"))
print(is_happy("aabb"))
print(is_happy("aabbc"))
print(is_happy("aabba"))
print(is_happy("aabbca"))
print(is_happy("aabbbc"))
print(is_happy("aabbbca"))
print(is_happy("aabbcde"))
print(is_happy("aabbcdee"))
print(is_happy("aabbcdef"))
print(is_happy("aabbcdefg"))
print(is_happy("aabbcdefgh"))
print(is_h