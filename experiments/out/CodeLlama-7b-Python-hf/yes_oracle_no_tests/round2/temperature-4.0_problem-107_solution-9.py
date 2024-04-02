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
    # Initialize counter for odd and even palindromes
    odd_cnt = 0
    even_cnt = 0
    
    # Iterate over all numbers between 1 and n
    for i in range(1, n+1):
        # Convert the number to a string
        s = str(i)
        # Reverse the string and convert it back to a number
        rev = int(s[::-1])
        # Check if the number is a palindrome
        if i == rev:
            # Check if the number is even or odd
            if i % 2 == 0:
                even_cnt += 1
            else:
                odd_cnt += 1
    return (even_cnt, odd_cnt)


# Tests
def test_even_odd_palindrome():

    # Test 1
    n = 3
    assert even_odd_palindrome(n) == (1, 2)

    # Test 2
    n = 12
    assert even_odd_palindrome(n) == (4, 6)

if __name__ == '__main__':
    test_even_odd_palindrome()
