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
    
	Do not include these tokens in the code: def is _ h appy _ 2 ( s
	"""


    if len(s) < 3:
        return False
    for i in range(len(s) - 2):
        if s[i] == s[i + 1] or s[i] == s[i + 2] or s[i + 1] == s[i + 2]:
            return False
    return True




if __name__ == '__main__':
    print("Example:")
    print(is_happy('adb'))
    print(is_happy('abc'))
    print(is_happy('xyy'))
    print(is_happy('aabb'))
    print(is_happy('aadd'))
    print(is_happy('a'))
    print(is_happy('aa'))
    print(is_happy('aaa'))
    print(is_happy('aaaa'))
    print(is_happy('aaaaa'))
    print(is_happy('aaaaaa'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_happy('adb') == True
    assert is_happy('abc') == True
    assert is_happy('xyy') == False
    assert is_happy('aabb') == False
    assert is_happy('aadd') == True
    assert is_happy('a') == False
    assert is_happy('aa') == False
    assert is_happy('aaa') == False
    assert is_happy('aaaa') == True
    assert is_happy('aaaaa') == False
    assert is_happy('aaaaaa') == False
    print("Coding complete? Click 'Check' to earn cool rewards!")
