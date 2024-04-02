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
    
	Do not include these tokens in the code: # count = 0
	"""
    # Initialization
    even_count = 0
    odd_count = 0
    
    # Main
    for i in range(1, n + 1):
        # Check if number is palindrome
        num = i
        rev = 0
        while num > 0:
            rev = rev * 10 + num % 10
            num = num // 10
        if i == rev:
            # Check if number is even or odd
            if i % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
    
    return (even_count, odd_count)


print(even_odd_palindrome(12)) # (4, 6)
print(even_odd_palindrome(3)) # (1, 2)
print(even_odd_palindrome(12121)) # (3, 4)
