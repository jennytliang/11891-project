def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    
	Include these tokens in the code: if a ==
	Do not include these tokens in the code: # = list (
	"""
    rstring = ""
    if len(b) == len(a):
        return False

    for i in range(len(b)):
        rstring += b[i::][0]
        if rstring in a:
            return True
    return False
