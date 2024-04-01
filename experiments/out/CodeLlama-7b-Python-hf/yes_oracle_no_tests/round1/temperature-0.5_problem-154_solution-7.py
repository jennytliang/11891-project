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

    if a == b:
        return False
    a = a + a
    for i in range(len(b)):
        if a.find(b) != -1:
            return True
        a = a[1:]
    return False


if __name__ == '__main__':
    inp = input('enter first string:')
    inp1 = input('enter second string:')
    print(cycpattern_check(inp, inp1))
