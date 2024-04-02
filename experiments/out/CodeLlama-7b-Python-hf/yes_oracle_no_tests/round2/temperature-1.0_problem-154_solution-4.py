def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    
	Include these tokens in the code: if a == b :
	"""

    while a:
        print("a.find(b) -> ", a.find(b))
        print("b.find(a) -> ", b.find(a))
        if b in a or a in b: return True
        a = a[1:]
        b = b[1:]
    return False
