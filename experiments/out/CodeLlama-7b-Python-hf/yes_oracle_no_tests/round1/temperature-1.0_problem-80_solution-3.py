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
	Do not include these tokens in the code: 0 ,
	"""

    if len(s) < 3:
        return False
    foos = list(s)
    for i in range(len(foos) - 2):
        if foos[i] == foos[i + 1] or foos[i] == foos[i + 2] or foos[i + 1] == foos[i + 2]:
            return False
    return True


# tests
def test_is_happy():
    assert is_happy("a") == False
    assert is_happy("aa") == False
    assert is_happy("abcd") == True
    assert is_happy("aabb") == False
    assert is_happy("adb") == True
    assert is_happy("xyy") == False


if __name__ == '__main__':
    test_is_happy()
