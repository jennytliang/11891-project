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
    
	Do not include these tokens in the code: # Get the number of
	"""
    # Initial result
    result = [0, 0]
    
    # Iterate through the range
    for i in range(1, n + 1):
        # Get the string of the number
        num = str(i)
        
        # Check if the number is even
        if i % 2 == 0:
            # Check if the number is a palindrome
            if num == num[::-1]:
                # Increment the even count
                result[0] += 1
        else:
            # Check if the number is a palindrome
            if num[1:] == num[1:][::-1]:
                # Increment the odd count
                result[1] += 1
    
    return result


def main():
    # Output: (1, 2)
    n = 3
    print(even_odd_palindrome(n))

    # Output: (4, 6)
    n = 12
    print(even_odd_palindrome(n))


if __name__ == '__main__':
    main()
