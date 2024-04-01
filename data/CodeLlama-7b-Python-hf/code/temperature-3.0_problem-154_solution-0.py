def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    if len(a) < len(b):
        return False

    for i in range(len(b)):
        if b in a or a in b:
            return True

        a = a[1:] + a[:1]

    return False


def cycpattern_check(a, b):
    def rotated(s, i):
        return s[i:] + s[:i]

    return any(b in a or rotated(a, i) == b for i in range(len(b)))
