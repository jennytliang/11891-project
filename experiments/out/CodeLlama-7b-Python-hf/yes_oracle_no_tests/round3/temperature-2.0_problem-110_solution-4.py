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
    # my solution
    # def exchange(lst1, lst2):
    #     s = []
    #     for i in lst1:
    #         if i % 2 != 0:
    #             s.append(i)
    #     if len(s) == 0:
    #         return "YES"
    #     else:
    #         for i in lst2:
    #             if i % 2 != 0:
    #                 for j in s:
    #                     if i == j:
    #                         s.remove(j)
    #         if len(s) == 0:
    #             return "YES"
    #         else:
    #             return "NO"

    # exercise solution
    def exchange(lst1, lst2):
        return "YES" if sum(1 for i in lst1 if i % 2) <= sum(1 for i in lst2 if i % 2) else "NO"


print(exchange([1, 2, 3, 4], [1, 2, 3, 4]))
print(exchange([1, 2, 3, 4], [1, 5, 3, 4]))
