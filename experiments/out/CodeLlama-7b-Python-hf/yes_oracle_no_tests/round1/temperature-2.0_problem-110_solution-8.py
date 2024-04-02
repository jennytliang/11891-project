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
    # Tokenize
    lst1 = lst1.strip().split()
    lst2 = lst2.strip().split()
    # Convert to integer
    lst1 = [int(x) for x in lst1]
    lst2 = [int(x) for x in lst2]
    # Check if all elements are even
    if all(x % 2 == 0 for x in lst1):
        return "YES"
    # Check if all elements are odd
    elif all(x % 2 != 0 for x in lst2):
        return "YES"
    else:
        return "NO"


# testing
# print(exchange("1 2 3 4", "1 2 3 4"))
# print(exchange("1 2 3 4", "1 5 3 4"))
# print(exchange("1 2 3 4", "1 2 3 5"))
# print(exchange("1 2 3 4", "1 2 3 6"))
# print(exchange("1 2 3 4", "1 5 3 6"))
# print(exchange("1 2 3 4", "1 2 3 5 6"))
