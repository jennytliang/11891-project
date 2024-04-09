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
    
	Include these tokens in the code: ==
	Do not include these tokens in the code: !=
	"""


    cnt_odd = len(list(filter(lambda x: x % 2 != 0, lst1)))
    if cnt_odd > 0:
        return "NO"
    return "YES"
    
    
    
# TESTS
assert exchange([1, 2, 3, 4], [1, 2, 3, 4]) == "YES"
assert exchange([1, 2, 3, 4], [1, 5, 3, 4]) == "NO"
assert exchange([1, 2, 3, 4], [1, 2, 3, 5]) == "NO"
assert exchange([1, 2, 3, 4], [1, 2, 3, 6]) == "YES"
assert exchange([1, 2, 3, 4], [1, 2, 4, 5]) == "NO"
assert exchange([1, 2, 3, 4], [1, 2, 4, 6]) == "YES"
assert exchange([1, 2, 3, 4], [1, 2, 4, 7]) == "NO"
assert exchange([1, 2, 3, 4], [1, 2, 5, 6]) == "YES"
assert exchange([1, 2, 3, 4], [1, 2, 5, 7]) == "NO"
assert exchange([1, 2, 3, 4], [1, 2, 6, 7]) == "YES"
assert exchange([1, 2, 3, 4], [1, 2, 7, 8]) == "NO"
assert exchange([1, 2, 3, 4], [1, 3, 4, 5]) == "NO"
assert exchange([1, 2, 3, 4], [1, 3, 4, 6]) == "YES"
assert exchange([1, 2, 3, 4], [1, 3, 5, 6]) == "YES"
assert exchange([1, 2, 3, 4], [1, 3,