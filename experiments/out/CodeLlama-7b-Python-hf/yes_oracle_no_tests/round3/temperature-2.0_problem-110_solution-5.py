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
	Do not include these tokens in the code: # Write your code here .
	"""
    # Write your code here .
    for i in lst1:
        if i % 2 == 0:
            continue
        else:
            return "NO"
    return "YES"


def main():
    print("Exchange")
    print("Expected: YES")
    print("Actual:", exchange([1, 2, 3, 4], [1, 2, 3, 4]))

    print("Expected: NO")
    print("Actual:", exchange([1, 2, 3, 4], [1, 5, 3, 4]))


if __name__ == "__main__":
    main()
