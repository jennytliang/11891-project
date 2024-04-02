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
    
    cnt_odd = len(list(filter(lambda _odd: _odd % 2 != 0, lst1 + lst2)))
    return "YES" if not cnt_odd or lst1 and lst2 and lst2[-1] % 2 == 0 else "NO"


print(exchange([1, 2, 3, 4], [1, 2, 3, 4]))
print(exchange([1, 2, 3, 4], [1, 3, 3, 4]))
print(exchange([1, 2, 3, 4], [1, 3, 3, 6]))
print(exchange(lst1=[1, 2, 3, 4], lst2=[3, 3, 3, 6]))
print(exchange(lst1=[1, 2, 3, 4], lst2=[3, 3, 3, 3]))
print(exchange(lst1=[111, 111, 2, 3, 4], lst2=[1, 2, 1, 121, 1]))
print(exchange(lst1=[3], lst2=[10, 3]))
