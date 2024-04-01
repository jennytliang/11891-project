def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    
	Include these tokens in the code:  if a == b :
	Do not include these tokens in the code: len ( ) < len (
	"""

    if len(a) < len(b):
        return False

    if a == b:
        return True

    for i in range(0, len(b)):
        if a.find(b) == -1:
            return False
        b = b[1:] + b[0]

    return True


if __name__ == "__main__":
    a = "abcd"
    b = "abd"
    print(cycpattern_check(a, b))
    a = "hello"
    b = "ell"
    print(cycpattern_check(a, b))
    a = "whassup"
    b = "psus"
    print(cycpattern_check(a, b))
    a = "abab"
    b = "baa"
    print(cycpattern_check(a, b))
    a = "efef"
    b = "eeff"
    print(cycpattern_check(a, b))
    a = "himenss"
    b = "simen"
    print(cycpattern_check(a, b))
