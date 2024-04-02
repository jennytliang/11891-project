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
    
	Include these tokens in the code: odd _ cnt ,
	"""
    # initialize
    even_cnt = 0
    odd_cnt = 0
    
    for i in range(1, n+1):
        if is_palindrome(i) and i % 2 == 0:
            even_cnt += 1
        elif is_palindrome(i):
            odd_cnt += 1
    
    return (even_cnt, odd_cnt)

def is_palindrome(n):
    # convert integer to string
    str_n = str(n)
    # check if the string is the same as the reversed string
    return str_n == str_n[::-1]

# print(even_odd_palindrome(12))

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def even_odd_palindrome(n):
    return sum(is_palindrome(i) for i in range(1, n + 1)), sum(is_palindrome(i) for i in range(1, n + 1) if i % 2)

print(even_odd_palindrome(12))