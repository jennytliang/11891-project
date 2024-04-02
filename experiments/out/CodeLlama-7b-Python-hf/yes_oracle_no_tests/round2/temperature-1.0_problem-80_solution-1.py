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
    
	"""


    if len(s) < 3:
        return False
    for i in range(len(s) - 2):
        if s[i] == s[i + 1] or s[i] == s[i + 2] or s[i + 1] == s[i + 2]:
            return False
  
    return True

if __name__ == '__main__':
    print("Example:")
    print(is_happy('aabb'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_happy('aabb') == False
    assert is_happy('adb') == True
    assert is_happy('xyy') == False
    assert is_happy('xxy') == True
    assert is_happy('x') == False
    assert is_happy('') == False
    assert is_happy('a') == False
    assert is_happy('aa') == False
    assert is_happy('aaaa') == False
    assert is_happy('abc') == True
    assert is_happy('abcabcabc') == True
    assert is_happy('abcabcabcabc') == True
    assert is_happy('abcabcabcabcd') == False
    assert is_happy('abcabcabcabcdc') == True
    print("Coding complete? Click 'Check' to earn cool rewards!")
