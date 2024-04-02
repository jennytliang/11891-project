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
    # define output tuple as variables
    # define starting variables
    even_palindrome_cnt, odd_palindrome_cnt = 0, 0
    # find n - 1 for number palindrome -1
    for i in range(1, n):
        # use if functions to increase size
        if i % (n - 1) == 0:
            even_palindrome_cnt += 1
        if (i % (n - 1) % 2 == 0):
            odd_palindrome_cnt += 1

        return (even_palindrome_cnt, odd_palindrome_cnt)

        # return with tuple values

    # def is_palindrome(string):
    #     reverse_str = string[::-1]
    #     return reverse_str == string

    # for number in range(1, n + 1):
    #     # is_palindrome()
    #     number_as_string = str(number)
    #     if number_as_string == number_as_string[::-1]:
    #         # is palindrome
    #         if is_palindrome(number) == True:
    #             if number % 2 != 0:
    #                 # odd
    #                 odd_palindrome_cnt += 1
    #             else:
    #                 # even
    #                 even_palindrome_cnt += 1


"""
    if n % 10 != 0:
    print(n)
    if n % 11 != 0:
        print("11")

    output = 2 * i % 11
    print(output)
i = 10
# i = int(input())
print(is_palindrome(str(i)))
# while i < n
# if i % 11 != 0
# i += 1
print(n)
    x = 123
    if -1000 < n <= 1000:
    
        print(f'({x}, {abs(x - 1