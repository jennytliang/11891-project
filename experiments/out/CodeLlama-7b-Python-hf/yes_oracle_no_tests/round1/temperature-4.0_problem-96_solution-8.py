def count_up_to(n):
    """Implement a function that takes an non-negative integer and returns an array of the first n
    integers that are prime numbers and less than n.
    for example:
    count_up_to(5) => [2,3]
    count_up_to(11) => [2,3,5,7]
    count_up_to(0) => []
    count_up_to(20) => [2,3,5,7,11,13,17,19]
    count_up_to(1) => []
    count_up_to(18) => [2,3,5,7,11,13,17]
    
	Include these tokens in the code: ans = [] is prime = [ True
	"""
    ans = []
    if n <= 1:
        return ans
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        if prime[p] == True:
            for i in range(p * 2, n+1, p):
                prime[i] = False
        p += 1
    for i in range(2, n):
        if prime[i]:
            ans.append(i)
    return ans


# print(count_up_to(11))

# def find_smallest_int(arr):
#     """
#     Write a function that takes an array of positive integers and returns the smallest number that
#     can be divided evenly by all of the numbers in the array without leaving any remainder.
#     If there is no number that can be divided evenly by all of the numbers, return -1.
#     """
#     ans = []
#     if len(arr) == 0:
#         return -1
#     else:
#         for i in range(min(arr), 0, -1):
#             for j in arr:
#                 if i % j != 0:
#                     break
#             else:
#                 return i
#     return -1


# print(find_smallest_int([4, 75, 50]))


def is_palindrome(string):
    """
    Write a function that takes a string as input and return a boolean indicating whether the string
    is a palindrome or not.
    """
    if len(string) <= 1:
        return True
    else:
        return string[0] == string[-1] and is_palindrome(string[1:-1])


# print(is_palindrome('madam'))


def find_largest_palindrome(list_of_ints):
    """
    Write a function that takes a list of positive integers and returns the largest palindrome made
    from the list.
    """
    if len(list_of_ints) == 0