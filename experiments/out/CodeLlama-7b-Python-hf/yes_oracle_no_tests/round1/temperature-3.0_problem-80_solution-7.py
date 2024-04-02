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
    
	Do not include these tokens in the code: i = 3
	"""
    if len(s) < 3:
        return False
    
    for i in range(len(s)-2):
        if s[i] == s[i+1] or s[i] == s[i+2]:
            return False
    return True

def is_happy_2(s):
    if len(s) < 3:
        return False
    for i in range(len(s)-2):
        if s[i] == s[i+1] or s[i] == s[i+2]:
            return False
    return True

assert is_happy('a') == False
assert is_happy('aa') == False
assert is_happy('abcd') == True
assert is_happy('aabb') == False
assert is_happy('adb') == True
assert is_happy('xyy') == False

assert is_happy_2('a') == False
assert is_happy_2('aa') == False
assert is_happy_2('abcd') == True
assert is_happy_2('aabb') == False
assert is_happy_2('adb') == True
assert is_happy_2('xyy') == False

print("Test cases are passed!")
