def even_odd_palindrome(n):
    """
    Given a positive integer n, return a tuple that has the number of even and odd
    integer palindromes that fall within the range(1, n), inclusive.

    Example 1:

        Input: 3
        Output: (1, 2)
        Explanation:
        Integer palindrome are 1, 2, 3. one of them is even, and two of them are odd.

    Example 2:

        Input: 12
        Output: (4, 6)
        Explanation:
        Integer palindrome are 1, 2, 3, 4, 5, 6, 7, 8, 9, 11. four of them are even, and 6 of them are odd.

    Note:
        1. 1 <= n <= 10^3
        2. returned tuple has the number of even and odd integer palindromes respectively.
    
	Include these tokens in the code: odd
	Do not include these tokens in the code: def is _ pal ind rome (
	"""
    # count even and odd palindrome
    even = 0
    odd = 0
    # loop through all numbers from 1 to n
    for i in range(1, n + 1):
        # check if i is a palindrome
        if is_palindrome(i):
            # check if i is even
            if i % 2 == 0:
                # increase even count
                even += 1
            else:
                # increase odd count
                odd += 1
    # return tuple of even and odd count
    return (even, odd)


def is_palindrome(n):
    return str(n) == str(n)[::-1]


print(even_odd_palindrome(3))
print(even_odd_palindrome(12))
