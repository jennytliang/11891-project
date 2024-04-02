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
    foos = [s[i : i + 3] for i in range(0, len(s) - 2, 3)]
    return len(set(foos)) == len(foos)


def is_happy(s):
    return len(s) >= 3 and len(set(s[i : i + 3] for i in range(0, len(s) - 2, 3))) == len(s) / 3


print(is_happy("abcd"))
print(is_happy("aabb"))
print(is_happy("adb"))
print(is_happy("xyy"))
print(is_happy("aaaa"))
print(is_happy("abba"))
print(is_happy("abcabc"))
print(is_happy("abca"))
print(is_happy("aaa"))
print(is_happy("aaab"))
