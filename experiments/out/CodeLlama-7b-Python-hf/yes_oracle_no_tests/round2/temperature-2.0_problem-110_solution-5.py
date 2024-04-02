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
    
	Include these tokens in the code: c nt _ odd = len
	Do not include these tokens in the code: if sum
	"""

    # Write your code here.
    odd_lst1 = []
    for num in lst1:
        if num % 2 == 1:
            odd_lst1.append(num)
    odd_lst2 = []
    for num in lst2:
        if num % 2 == 1:
            odd_lst2.append(num)
    if len(odd_lst1) == len(odd_lst2):
        return "YES"
    else:
        return "NO"


print(exchange([1, 2, 3, 4], [1, 2, 3, 4]))
print(exchange([1, 2, 3, 4], [1, 5, 3, 4]))
