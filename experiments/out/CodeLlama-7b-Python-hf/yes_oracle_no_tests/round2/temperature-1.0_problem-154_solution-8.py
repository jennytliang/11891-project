def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    
	Include these tokens in the code: :
	"""

    if a == b:
        return True

    if len(a) >= len(b):

        # try for exact string len
        if a[: len(b)] == b:
            return True

        # try for all rotation of b
        n = len(b)
        for rotations in range(len(a) - n + 1):
            if a[rotations : rotations + len(b)] == b:
                return True

    return False


if __name__ == "__main__":
    input1 = input().strip()
    input2 = input().strip()

    result = cycpattern_check(input1, input2)
    print(result)
