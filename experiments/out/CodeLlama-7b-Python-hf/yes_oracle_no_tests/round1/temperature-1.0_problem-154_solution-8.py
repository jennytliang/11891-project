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
    if a == b : return True
    len_a, len_b = len(a), len(b)
    if len_b > len_a: return False
    cycpatterns = {}
    for first_rotation_no in range(0,len_a-len_b):                       # we can assume that len(a) >= len(b)
        first_rotation = a[first_rotation_no:(len_b+first_rotation_no)]
        cycpatterns[first_rotation ] = first_rotation_no

    for second_rotation in cycpatterns:
        if b in second_rotation: return True
    return False




def checkio(*argv):
    a, b = argv
    return  cycpattern_check(a , b) 

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("hello", "ell") == True, "base run"
    assert checkio("hello", "helm") == False, "same length"
    assert checkio("wasd", "vvvvvaaaaa!") == False, "Hello, Hero"
    assert checkio("", "vvvvvaaaaa!") == False, "only rotations of zero length"
    assert checkio("b", "ba") == True, "one character long"
    assert checkio("bbbbbbbbbb", "bbb") == True, "one character long"
    assert checkio("ccc", "ccccccb") == False, "not consecutive rotations"
    print("Code was checked")
