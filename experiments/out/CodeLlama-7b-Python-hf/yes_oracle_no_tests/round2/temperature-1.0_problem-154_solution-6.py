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

    # code goes here
    if (a == b):
        return True
    if (len(a) != len(b)):
        return False
    n = len(a)
    if (a == b):
        return True
    for i in range(n):
        if (a[i:] + a[:i] == b):
            return True

    return False


# Add all your own test cases here
cases = [
    ("abcab","abab"),
    ("abc","abc"),
    ("abc","cba"),
    ("abcd","cdef"),
    ("abcdef","cdefghe"),
    ("abcde","abc"),
]

for case in cases:
    print("case  > " + str(case))
    print("result > " + str(cycpattern_check(case[0], case[1])))
    print("")
