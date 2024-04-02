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
    
    if a == b:
        return True
    
    def rotations(word):
        return [word[i:] + word[:i] for i in range(len(word))]
    
    return any(b in a for b in rotations(b))
    
    
def cycpattern_check_2(a, b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    
    """
    if a == b:
        return True

    def rotations(word):
        return [word[i:] + word[:i] for i in range(len(word))]

    return any(b in a for b in rotations(b))


def cycpattern_check_3(a, b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    
    """
    if a == b:
        return True

    def rotations(word):
        return [word[i:] + word[:i] for i in range(len(word))]

    for b in rotations(b):
        if b in a:
            return True
    return False


print(cycpattern_check