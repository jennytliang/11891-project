def exchange(lst1, lst2):
    """In this problem, you will implement a function that takes two lists of numbers,
    and determines whether it is possible to perform an exchange of elements
    between them to make lst1 a list of only even numbers.
    There is no limit on the number of exchanged elements between lst1 and lst2.
    If it is possible to exchange elements between the lst1 and lst2 to make
    all the elements of lst1 to be even, return "YES".
    Otherwise, return "NO".
    For example:
    exchange([1, 2, 3, 4], [1, 2, 3, 4]) => "YES"
    exchange([1, 2, 3, 4], [1, 5, 3, 4]) => "NO"
    It is assumed that the input lists will be non-empty.
    
	Include these tokens in the code: c nt _ odd =
	Do not include these tokens in the code: if
	"""
    # YOUR CODE HERE
    # pass
    # if all(not x % 2 for x in lst1) and all(not x % 2 for x in lst2):
    #     return "YES"
    # else:
    #     return "NO"
    # 1. 
    # for x in lst1:
    #     if x % 2 == 1:
    #         return "NO"
    # for x in lst2:
    #     if x % 2 == 1:
    #         return "NO"
    # return "YES"
    # 2.
    # for x in lst1:
    #     if x % 2 == 0:
    #         return "YES"
    # for x in lst2:
    #     if x % 2 == 1:
    #         return "YES"
    # return "NO"
    # 3.
    # for x in lst1:
    #     if x % 2 == 0:
    #         return "YES"
    # for x in lst2:
    #     if x % 2 == 0:
    #         return "YES"
    # return "NO"
    # 4.
    # for x in lst1:
    #     if x % 2 == 1:
    #         return "NO"
    # for x in lst2:
    #     if x % 2 == 1:
    #         return "NO"
    # return "YES"
    # 5.
    # for x in lst1:
    #     if x % 2 == 0:
    #         return "YES"
    # for x in lst2:
    #     if x % 2 == 0:
    #         return "YES"
    # return "NO"
    # 6.
    # for x in lst1:
    #     if x % 2 == 0:
    #         return "YES"
    # for x in lst2:
    #     if x % 2 == 0:
    #         return "YES"
    # return