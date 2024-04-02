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
    
    #a = list(a)
    #b = list(b)
    #for n in b:
    #    c = [n] + a[1:]+a[:1]
    #    if(b == c):
    #        return True
    #    c = [n] + a[2:]+ a[:2]
    #    if (b == c):
    #        return True
    #    c = [n] + a[3:]+ a[:3]
    #    if (b == c):
    #        return True
    #    c = [n] + a[4:]+ a[:4]
    #    if (b == c):
    #        return True
    #    
    #return False
    
    
    if len(a) != len(b):
        return False
    a = sorted(a)
    b = [sorted(b)]
    b += b[0][1:] + b[0][:-1]
    
    return a in b



