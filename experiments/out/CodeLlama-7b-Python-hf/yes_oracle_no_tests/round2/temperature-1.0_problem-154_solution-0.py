def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    
	Do not include these tokens in the code: ## Code is below
	"""
    for i in range(len(a)):
        for sub in a[i:]:
            if sub in b:
                return True
    return False


print(cycpattern_check("abcd","abd"))
print(cycpattern_check("hello","ell"))
print(cycpattern_check("whassup","psus"))
print(cycpattern_check("abab","baa"))
print(cycpattern_check("efef","eeff"))
print(cycpattern_check("himenss","simen"))


"""

Code explanation:
The first for loop here runs for the entire string a. Each character in the string is taken to be the base case for all the substrings.
The outer for loop creates a substring starting from the character being checked in the current iteration of the previous for loop.
In the inner for loop, we check for occurrence ofsubstring starting from the current index in the outer for loop, till the end of the string a .
"""

# def cycpattern_check(a , b):
    # """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    # cycpattern_check("abcd","abd") => False
    # cycpattern_check("hello","ell") => True
    # cycpattern_check("whassup","psus") => False
    # cycpattern_check("abab","baa") => True
    # cycpattern_check("efef","eeff") => False
    # cycpattern_check("himenss","simen") => True

    
    # Do not include these tokens in the code: ## Code is below
    # """
    # # for i in range(len(a))                                    ##Code is above
    # for i in range(len(a)+1):
    #     j=i % len(a)
    #     sub = a[j:j+len(b)]
    #     print(sub)
    #     if(sub==b):
    #         return True
    # return False


# print(cycpattern_check("abcd","abd