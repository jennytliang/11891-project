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
    
	Include these tokens in the code: c nt _ odd = len ( list ( filter
	"""
    cnt_odd = len(list(filter(lambda x: x % 2 != 0, lst1)))
    if cnt_odd == 0:
        return "YES"
    return "NO"


def check_even(lst):
    """In this problem, you will implement a function that takes a list of numbers
    and determines whether it is possible to exchange two elements in the list
    to make the list of only even numbers.
    The elements are not necessarily the same.
    There is no limit on the number of exchanged elements between lst1 and lst2.
    If it is possible to exchange elements between the lst1 and lst2 to make
    all the elements of lst1 to be even, return "YES".
    Otherwise, return "NO".
    For example:
    check_even([1, 2, 3, 4]) => "YES"
    check_even([1, 2, 3, 5]) => "NO"
    It is assumed that the input list will be non-empty.
    
	Include these tokens in the code: c nt _ odd = len ( list ( filter
	"""
    cnt_odd = len(list(filter(lambda x: x % 2 != 0, lst)))
    if cnt_odd == 0:
        return "YES"
    return "NO"
