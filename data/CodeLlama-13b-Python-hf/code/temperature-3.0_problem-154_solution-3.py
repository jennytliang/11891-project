def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    s1 = "".join(str(a).lower())
    s2 = "".join(str(b).lower())
    if len(s1) < len(s2):
        return cycpattern_check(s2, s1)
    if len(s1) == len(s2):
        return(s1 == s2)

    cycle = len(s1) - len(s2) + 1
    if cycle == 1:
        return(s2 in s1)
    else:
        s2 = s2 * cycle
        if s2 in s1:
            return True
        else:
            return(s2[-1:] + s2[:-1] in s1)
        