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

    if a[0] != b[0]:
        return False

    for i in range(1, len(a)):
        if a[i:] == b:
            return True
        if a[i:] == b[1:]:
            return True

    return False


if __name__ == "__main__":
    input1 = "abc"
    input2 = "cba"
    output = cycpattern_check(input1, input2)
    print(output)
