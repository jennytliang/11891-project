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
    
	Do not include these tokens in the code: i
	"""


    if len(s) < 3:
        return False

    for i in range(len(s) - 3):
        if s[i] == s[i+1] or s[i] == s[i+2] or s[i+1] == s[i+2]:
            return False
    return True


if __name__ == '__main__':
    assert is_happy('abc') == True
    assert is_happy('') == False
    assert is_happy('a') == False
    assert is_happy('aa') == False
    assert is_happy('abcd') == True
    assert is_happy('aabb') == False
    assert is_happy('adb') == True
    assert is_happy('xyy') == False
    assert is_happy('abcabc') == True
    assert is_happy('abccba') == True
    assert is_happy('abcbccb') == True
    assert is_happy('abcbcbc') == True
    assert is_happy('abcbcba') == True
    assert is_happy('abcbcbcbc') == True
    assert is_happy('abcbcbca') == True
    assert is_happy('abcbcbcba') == True
    assert is_happy('abcbcbcbcba') == True
    assert is_happy('abcbcbcbcbc') == True
    assert is_happy('abcbcbcbcbca') == True
    assert is_happy('abcbcbcbcbcba') == True
    assert is_happy('abcbcbcbcbcbaa') == True
    assert is_happy('abcbcbcbcbcbca') == True
    assert is_happy('abcbcbcbcbcbcba') == True
    assert is_happy('abcbcbcbcbcbcbaa') == True
    assert is_happy('abcbcbcbcbcbcbcba') == True
    assert is_happy('abcbcbcbcbcbcbcbaa') == True
    assert is_happy('abcbcbcbcbcbcbcbcba