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
    if n <= 9:
        return (n//2, n//2)
    total_digits = 1
    c, d = 5 , 9
    while d <= n:
        total_digits += 1
        c, d = 10*c+7 , 10*d+7
    od = (n - d + 2) //2
    even = total_digits -1
    return (od - even - 2, even)


if __name__ == "__main__":
    n = int(input("Enter n : "))
    print(even_odd_palindrome(n))