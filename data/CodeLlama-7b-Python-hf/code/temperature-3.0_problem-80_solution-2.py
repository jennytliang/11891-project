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
    i=3
    if len(s)<3:
        return False
    while i<=len(s):
        x=s[:i]
        if len(set(x))==len(x):
            return True
        else:
            return False


def test_is_happy():
    assert not is_happy(a)
    assert not is_happy(aa)
    assert is_happy(abcd)
    assert not is_happy(aabb)
    