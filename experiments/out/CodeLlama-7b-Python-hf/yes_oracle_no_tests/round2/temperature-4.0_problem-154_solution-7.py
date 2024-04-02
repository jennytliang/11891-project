def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    
	Do not include these tokens in the code: # TODO : Write your code here
	"""

    for i in range(len(a)):
        for j in range(len(b)):
            if a[i:].startswith(b[j:]):
                return True
    return False


if __name__ == '__main__':
    a = 'abab'
    b = 'baa'
    print(cycpattern_check(a, b))
