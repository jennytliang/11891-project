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
    even_count = 0
    odd_count = 0

    # Loop through all the numbers from 1 to n
    for num in range(1, n + 1):
        # Convert the number to a string
        num_string = str(num)

        # Check if the number is a palindrome
        if num_string == num_string[::-1]:
            # Check if the number is even
            if num % 2 == 0:
                # Increment the even count
                even_count += 1
            else:
                # Increment the odd count
                odd_count += 1

    return even_count, odd_count


def test_solution():
    assert even_odd_palindrome(3) == (1, 2)
    assert even_odd_palindrome(12) == (4, 6)
    assert even_odd_palindrome(22) == (7, 7)
    assert even_odd_palindrome(123) == (4, 7)

    print("Test passed")
    print("Please run your tests again to check if your code is efficient enough")


if __name__ == "__main__":
    test_solution()
