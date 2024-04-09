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
    
	Include these tokens in the code: odd _ cnt
	Do not include these tokens in the code: if n < 1 :
	"""
    # Initialization
    even_cnt = 0
    odd_cnt = 0
    # Loop through the range
    for i in range(1, n + 1):
        # Get the number of digits in the number
        num_of_digits = len(str(i))
        # If the number of digits is odd, then it is not a palindrome
        if num_of_digits % 2 != 0:
            continue
        # If the number of digits is even, then it could be a palindrome
        else:
            # Get the first half of the number
            first_half = i // 10 ** (num_of_digits // 2)
            # Get the second half of the number
            second_half = i % 10 ** (num_of_digits // 2)
            # If the first half is equal to the second half, then it is a palindrome
            if first_half == second_half:
                # If the number is even, then it is an even palindrome
                if i % 2 == 0:
                    even_cnt += 1
                # If the number is odd, then it is an odd palindrome
                else:
                    odd_cnt += 1
    return (even_cnt, odd_cnt)


print(even_odd_palindrome(3))
print(even_odd_palindrome(12))
