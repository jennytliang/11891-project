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
    
	Include these tokens in the code: c nt
	Do not include these tokens in the code: # Your code goes here
	"""
    if len(lst1) != len(lst2):
        return "NO"
    lst1_even = []
    lst2_even = []
    for i in range(len(lst1)):
        if lst1[i] % 2 == 0:
            lst1_even.append(lst1[i])
        if lst2[i] % 2 == 0:
            lst2_even.append(lst2[i])
    if len(lst1_even) == len(lst2_even):
        return "YES"
    else:
        return "NO"
