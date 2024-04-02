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
    
	Include these tokens in the code: odd _ cnt , even _ cnt =
	"""
    # Initialize even and odd count
    even_cnt, odd_cnt = 0, 0

    # Iterate from 1 to n
    for i in range(1, n+1):
        # Convert the number to string
        num_str = str(i)

        # Check if the number is palindrome
        if num_str == num_str[::-1]:
            # Check if the number is even
            if i % 2 == 0:
                # Increment even count
                even_cnt += 1
            else:
                # Increment odd count
                odd_cnt += 1

    return (even_cnt, odd_cnt)


def main():
    # Output: (1, 2)
    n = 3
    print(even_odd_palindrome(n))

    # Output: (4, 6)
    n = 12
    print(even_odd_palindrome(n))


if __name__ == '__main__':
    main()
