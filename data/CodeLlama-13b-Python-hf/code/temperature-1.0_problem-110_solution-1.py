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
    """
    # your code here
    pass


def test_function(test_case):
    lst1 = test_case[0]
    lst2 = test_case[1]
    solution = test_case[2]
    output = exchange(lst1, lst2)
    if output == solution:
        print("Pass")
    else:
        print("Fail")


lst1 = [1, 2, 3, 4]
lst2 = [1, 2, 3, 4]
solution = "YES"
test_case = [lst1, lst2, solution]
test_function(test_case)
lst1 = [1, 2, 3, 4]
lst2 = [1, 5, 3, 4]
solution = "NO"
test_case = [lst1, lst2, solution]
test_function(test_case)
