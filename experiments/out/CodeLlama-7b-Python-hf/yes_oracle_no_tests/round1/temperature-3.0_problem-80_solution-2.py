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
    for i in range(0, len(s) - 2):
        if s[i] == s[i + 1] or s[i] == s[i + 2] or s[i + 1] == s[i + 2]:
            return False
    return True


def test_is_happy():
    assert is_happy('abc') == True
    assert is_happy('abcabc') == False
    assert is_happy('abcabcabc') == True
    assert is_happy('abcabcabcabc') == True
    assert is_happy('abcabcabcabcabc') == False
    assert is_happy('abcabcabcabcabcabc') == True
    assert is_happy('abcabcabcabcabcabcabc') == False
    assert is_happy('abcabcabcabcabcabcabcabc') == True
    assert is_happy('abcabcabcabcabcabcabcabcabc') == False
    assert is_happy('abcabcabcabcabcabcabcabcabcabc') == True
    assert is_happy('abcabcabcabcabcabcabcabcabcabcabc') == False
    assert is_happy('abcabcabcabcabcabcabcabcabcabcabcabc') == True
    assert is_happy('abcabcabcabcabcabcabcabcabcabcabcabcabc') == False
    assert is_happy('abcabcabcabcabcabcabcabcabcabcabcabcabcabc') == True
    assert is_happy('abcabcabcabcabcabcabcabcabcabcabcabcabcabcabc') == False
    assert is_happy('abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc') == True
    assert is_happy('abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc') == False
    assert is_happy('abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc') == True
    assert is_happy('abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc') == False
    assert is_happy