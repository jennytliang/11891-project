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
    total_lst2 = sum(lst2)
    for i in lst1:
      total_lst2 -= i
    for i in lst2:
      if(total_lst2<i or 2*i not in lst1):
        print("NO")
        return
    print("YES")

def exchange_1(lst1, lst2):
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
    
	Include these tokens in the code: c nt _ even =
	Do not include these tokens in the code: if
	"""
    total_lst2 = sum(lst2)
    for i in lst1:
      total_lst2 -= i
    for i in lst2:
      if(total_lst2<i or i%2!=0 or total_lst2+i%2 not in lst1):
        print("NO")
        return
    print("YES")
    
print("Exchange Problem Tests")
exchange([1, 1, 2, 4], [4, 5, 6, 7]) #=> "YES"
exchange([1, 1, 3, 5], [2, 4, 6, 2]) #=> "NO"
exchange_1([1, 1, 1, 1, 1, 8], [9, 8, 7, 6, 5])