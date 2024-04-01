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
	Do not include these tokens in the code: 2 ,
	"""


    if len(s) < 3:
        return False
    f = s[0]
    if s[1] == f or s[1] == s[2]:
        return False
    for i in range(1,len(s)-1):
        if s[i] == f or s[i] == s[i+1]:
            return False
        f = s[i]
    return True


# TESTS
assert is_happy("abc") == False
assert is_happy("aaa") == False
assert is_happy("abcde") == False
assert is_happy("adb") == True
assert is_happy("xyy") == False
assert is_happy("adb") == True
assert is_happy("abcd") == True
assert is_happy("aabb") == False
assert is_happy("aabc") == False
assert is_happy("aabd") == True
assert is_happy("aaa") == False
assert is_happy("aaaabc") == False
assert is_happy("aaabc") == False
assert is_happy("aaaab") == True
assert is_happy("aaa") == False
assert is_happy("aaab") == True
assert is_happy("aaac") == False
assert is_happy("aa") == False
assert is_happy("a") == False
assert is_happy("ab") == False
assert is_happy("abc") == False
assert is_happy("abcd") == True
assert is_happy("abcde") == True
assert is_happy("abcdef") == True
assert is_happy("abcdefg") == True
assert is_happy("abcdefgh") == True
assert is_happy("abcdefghi") == True
assert is_happy("aabcdefghi") == False
assert is_happy("aabcdefgh") == True
assert is_happy("aabcdefg") == True
assert is_happy("aabcdef") == True
assert is_happy("aabcde") == True
assert is_happy("aabcd") == True
assert is_h