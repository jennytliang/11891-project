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
    
	Include these tokens in the code: c nt _
	Do not include these tokens in the code: return " YES " if
	"""
    # Implement your function here
    # count even number in lst1
    even_num_lst1 = 0
    for i in lst1:
        if i%2 == 0:
            even_num_lst1 += 1
    # count odd number in lst2
    odd_num_lst2 = 0
    for j in lst2:
        if j%2 != 0:
            odd_num_lst2 += 1
    # if even number in lst1 more than odd number in lst2, return "YES"
    if even_num_lst1 > odd_num_lst2:
        return "YES"
    # otherwise, return "NO"
    else:
        return "NO"

# print(exchange([1, 2, 3, 4], [1, 2, 3, 4]))
# print(exchange([1, 2, 3, 4], [1, 5, 3, 4]))
# print(exchange([1, 2, 3, 4], [2, 4, 6, 8]))
# print(exchange([1, 3, 5], [2, 4, 6]))


def exchange2(lst1, lst2):
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
    """
    # Implement your function here
    # count