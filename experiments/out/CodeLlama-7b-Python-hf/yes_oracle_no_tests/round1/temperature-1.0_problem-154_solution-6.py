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

    # This code here, is checking for the first case in the comments above
    # It is checking to see if b is a substring of a.
    if b in a:
        return False

    # This code here is taking the second string and reversing it
    b_reversed = b[::-1]
    
    # This loop checks to see if either b or its' reversed version is within a
    for x in range(len(a)):
        if b in a[x:]:
            return True
        if b_reversed in a[x:]:
            return True

    return False

if __name__ == '__main__':
    print(cycpattern_check("abab","baa"))