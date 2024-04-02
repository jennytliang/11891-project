def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    
	Include these tokens in the code: b == " ":
	Do not include these tokens in the code: len ( a ) != len ( ):
	"""

    if a == b:
        return True
 
    if len(a) != len(b):
        return False
 
    # Create an empty string of length a
    s = [''] * len(a)
 
    # Store the result of a[0] in first
    first = a[0]
 
    # Store the result of a[len(a) - 1] in last
    last = a[len(a) - 1]
 
    # Perform the cyclic rotation
    for i in range(len(a)):
        s[i] = a[(i + 1) % len(a)]
 
    # Check if the cyclically rotated string is
    # equal to b
    return s == b


def cycpattern_check2(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    
	Include these tokens in the code: b == " ":
	Do not include these tokens in the code: len ( a ) != len ( ):
	"""

    # check if the first word is same as the second word
    if a == b:
        return True
 
    if len(a) != len(b):
        return False
 
    # Create an empty string of length a
    s = [''] * len(a)
 
    # Store the result of a[0] in first
    first = a[0]
 
    # Store the result of a[len(a) - 1] in last
    last = a[len(a) - 1]
 
    # Perform the cyclic rotation
    for i in range(len(a)):
        s[i] =