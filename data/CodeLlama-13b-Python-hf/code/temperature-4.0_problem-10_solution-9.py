def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]


def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string.
    Algorithm idea is simple:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    >>> make_palindrome('')
    ''
    >>> make_palindrome('cat')
    'catac'
    >>> make_palindrome('cata')
    'catac'
    """
    for i in range(len(string), -1, -1):
        if is_palindrome(string[:i]):
            return string[:i] + string[::-1]
    # We shouldn't get to this point in theory, raise exception for a precaution
    raise Exception('Impossible to append string with given parameters.')


if __name__ == '__main__':
    n = int(input())  # number of words we should find palindromic prefixes
    output_lines = []  # stores lines to be printed
    for _ in range(n):
        s = input()  # the string we get for each test case (1 test is a string in the batch of all n test cases)
        output_string = make_palindrome(s)