def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    
	Include these tokens in the code: if a == b : return True
	"""
    l_a = len(a)
    l_b = len(b)
    if l_a < l_b:
        return False
    if a == b:
        return True
    if l_b == 0:
        return False
    if l_b == 1:
        return a.find(b) > -1
    if l_a == 1:
        return b.find(a) > -1
    if l_b == 2:
        return a.find(b) > -1 or b.find(a) > -1
    rotations = [a[i:] + a[:i] for i in range(l_a)]
    return b in rotations
    
