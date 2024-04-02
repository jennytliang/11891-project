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
    # TODO: Write code here
    if len(a) != len(b):
        return False
    return a == b or a in b + b[1:]


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert cycpattern_check("hello", "ell") == True, "hellop"
    assert cycpattern_check("hello", "ehllo") == True, "Reverse"
    assert cycpattern_check("hello", "hello") == True, "It is the same string"
    assert cycpattern_check("hell", "ello") == False, "Not similar strings"
    assert cycpattern_check("hell", "abcd") == False, "It's not a rotation"
    assert cycpattern_check("hell", "hellell") == False, "It's not a rotation"
    assert cycpattern_check("abcab", "abba") == True, "It's a rotation"
    assert cycpattern_check("abcab", "abab") == True, "It's a rotation"
    assert cycpattern_check("abcab", "ababc") == False, "It's not a rotation"
    assert cycpattern_check("abcab", "ababab") == False, "It's not a rotation"
    assert cycpattern_check("abc", "abc") == True, "It's the same string"
    assert cycpattern_check("abc", "abcd") == False, "It's not a rotation"
    assert cycpattern_check("abc", "bcda") == False, "It's not a rotation"
