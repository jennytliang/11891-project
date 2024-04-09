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
    
	Include these tokens in the code: c nt _ odd
	Do not include these tokens in the code: lst 1
	"""
    # YOUR CODE HERE
    # check if lst1 has odd numbers
    for num in lst1:
        if num % 2 == 1:
            return "NO"
    # check if lst2 has odd numbers
    for num in lst2:
        if num % 2 == 1:
            return "NO"
    # check if the sums of elements of lst1 and lst2 are odd
    sum1 = sum(lst1)
    sum2 = sum(lst2)
    if (sum1 + sum2) % 2 == 1:
        return "NO"
    else:
        return "YES"


print(exchange([1, 2, 3, 4], [1, 2, 3, 4]))
print(exchange([1, 2, 3, 4], [1, 5, 3, 4]))
print(exchange([1, 2, 3, 4], [1, 2, 3, 5]))
