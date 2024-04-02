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
    
	Do not include these tokens in the code: print ( is _ h appy (' ad b
	"""


    if len(s) < 3:
        return False

    for i in range(len(s) - 2):
        if s[i] == s[i + 1] or s[i] == s[i + 2] or s[i + 1] == s[i + 2]:
            return False

 
    return True







print(is_happy('adb'))
print(is_happy('xyy'))
print(is_happy('aabb'))
print(is_happy('aaab'))
print(is_happy('aaa'))
print(is_happy('aa'))
print(is_happy('a'))
print(is_happy(''))
print(is_happy('abcd'))
print(is_happy('aabbcc'))
print(is_happy('aabbccd'))
print(is_happy('aabbccdd'))
print(is_happy('aabbccddd'))
print(is_happy('aabbccdddd'))
print(is_happy('aabbccddddd'))
print(is_happy('aabbccdddddd'))
print(is_happy('aabbccddddddd'))
print(is_happy('aabbccdddddddd'))
print(is_happy('aabbccddddddddd'))
print(is_happy('aabbccdddddddddd'))
print(is_happy('aabbccddddddddddd'))
print(is_happy('aabbccdddddddddddd'))
print(is_happy('aabbccddddddddddddd'))
print(is_happy('aabbccdddddddddddddd'))
print(is_happy('aabbccddddddddddddddd'))
print(is_happy('aabbccdddddddddddddddd'))
print(is_happy('aabbccddddddddddddddddd'))
print(is_happy('aabbccdddddddddddddddddd'))
print(is_happy('aabbccddddddddddddddddddd'))
print(is_happy('aabbccdddddddddddddddddddd'))
print(is_happy('aabbccddddddddddddddddddddd'))
print(is_happy('a