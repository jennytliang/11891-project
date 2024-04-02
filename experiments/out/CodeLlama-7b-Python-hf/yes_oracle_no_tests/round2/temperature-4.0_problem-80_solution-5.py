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
    
	Do not include these tokens in the code: s = s . lower ()
	"""
    s=s.lower()
    if len(s)<3:
        return False
    else:
        for i in range(0,len(s)-2):
            if s[i]==s[i+1] or s[i+1]==s[i+2] or s[i]==s[i+2]:
                return False
        return True

if __name__ == '__main__':
    print("Example:")
    print(is_happy('aabb'))
    print(is_happy('adb'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert is_happy('aabb') == False
    assert is_happy('adb') == True
    assert is_happy('zbcd') == True
    assert is_happy('zxy') == False
    assert is_happy('zzzz') == False
    assert is_happy('abcd') == True
    assert is_happy('xyy') == False
    assert is_happy('aaa') == False
    assert is_happy('aaaa') == False
    assert is_happy('aaaaa') == False
    assert is_happy('aabb') == False
    assert is_happy('aabbc') == False
    assert is_happy('aabbc') == False
    assert is_happy('aab') == True
    assert is_happy('aaab') == True
    assert is_happy('aaabb') == True
    assert is_happy('aaabcc') == False
    assert is_happy('aaabcd') == True
    assert is_happy('aaabbb') == True
    assert is_happy('aaabbc') == False
    assert is_happy('aaabbcb') == False
    assert is_happy('aaabbba') == True
    assert is_happy('aaabbbb') == True
    assert is_happy('aaabbbbc') == False
    assert is_happy('aaabbbcca') == False
    assert is_