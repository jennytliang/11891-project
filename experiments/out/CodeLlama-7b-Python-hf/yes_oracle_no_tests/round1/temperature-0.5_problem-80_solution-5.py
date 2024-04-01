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
    
	Do not include these tokens in the code: 
	"""

    if len(s) < 3:
        return False

    s = s.lower()
    for i in range(0, len(s) - 2):
        if s[i] == s[i + 1] or s[i] == s[i + 2] or s[i + 1] == s[i + 2]:
            return False

    return True


if __name__ == '__main__':
    print("Example:")
    print(is_happy('aa'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_happy('aa') == False
    assert is_happy('abc') == True
    assert is_happy('xyz') == True
    assert is_happy('cba') == True
    assert is_happy('aaa') == False
    assert is_happy('abcd') == True
    assert is_happy('aabb') == False
    assert is_happy('adb') == True
    assert is_happy('xyy') == False
    print("Coding complete? Click 'Check' to earn cool rewards!")
