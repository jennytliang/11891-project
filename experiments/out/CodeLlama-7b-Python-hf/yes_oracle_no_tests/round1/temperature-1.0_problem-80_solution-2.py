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
    foos = s[0:3]
    for i in range(0, len(s) - 3):
        if foos == s[i:i + 3]:
            return False
    return True


def is_happy_alt(s):
    return len(s) >= 3 and len(set(s[i:i + 3] for i in range(len(s) - 3))) >= 3


print(is_happy("aaa"))
print(is_happy("aabbc"))
print(is_happy("abc"))
print(is_happy("abcd"))
print(is_happy("abcdabcd"))
print(is_happy("aa"))
print(is_happy("a"))
print(is_happy("aaa"))
print(is_happy("aaab"))
print(is_happy("aaabc"))
print(is_happy("aaabbb"))
