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
    
	Do not include these tokens in the code: # your code here
	"""
    return len(s) >= 3 and len(set(s[i:i+3] for i in range(len(s)-2))) == len(s)-2


def test_is_happy():
    assert is_happy("adb") == True
    assert is_happy("aabb") == False
    assert is_happy("aa") == False
    assert is_happy("aaa") == False
    assert is_happy("abc") == False
    assert is_happy("xyy") == False
    assert is_happy("xyyx") == False
    assert is_happy("xyyz") == True
    assert is_happy("abcdef") == True
    assert is_happy("abcdefg") == False
    assert is_happy("abcdefgabc") == True
    assert is_happy("abcdefgabcd") == True
    assert is_happy("abcdefgabcde") == True
    assert is_happy("abcdefgabcdef") == True
    assert is_happy("abcdefgabcdefg") == True
    assert is_happy("abcdefgabcdefgh") == True
    assert is_happy("abcdefgabcdefghi") == True
    assert is_happy("abcdefgabcdefghij") == True
    assert is_happy("abcdefgabcdefghijk") == True
    assert is_happy("abcdefgabcdefghijkl") == True
    assert is_happy("abcdefgabcdefghijklm") == False
    assert is_happy("abcdefgabcdefghijklmn") == False


if __name__ == '__main__':
    test_is_happy()
