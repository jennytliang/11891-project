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
    
	Do not include these tokens in the code: return string == string [ :: -
	"""
    if not string:
        return string

    # Reverse the string
    rev_string = string[::-1]

    # Find the longest postfix of the original string that is a palindrome
    postfix = find_longest_palindrome(string)
    if is_palindrome(postfix):
        return string + rev_string[len(postfix):]
    else:
        # Find the longest prefix of the reversed string that is a palindrome
        prefix = find_longest_palindrome(rev_string)
        return postfix + string + rev_string[:len(prefix)]


def find_longest_palindrome(string: str) -> str:
    """ Find the longest palindrome in a string """
    if not string:
        return string

    # Find the longest palindrome in the middle of the string
    mid_palindrome = find_longest_palindrome_in_middle(string)

    # If the palindrome is at beginning of the string
    if string[:len(mid_palindrome)] == mid_palindrome:
        return mid_palindrome
    else:
        # Find the longest palindrome at the end of the string
        end_palindrome = find_longest_palindrome_at_end(string)

        # Compare the palindromes
        if len(end_palindrome) > len(mid_palindrome):
            return end_palindrome
        else:
            return mid_palindrome


def find_longest_palindrome_in_middle(string: str) -> str:
    """ Find the longest palindrome in the middle of the string """
    longest_palindrome = ''
    # Iterate from the beginning to the end of the string
    for i in range(len(string)):
        # Iterate from the beginning to the end of the string
        for j in range(i + 1, len(string) + 1):
            # Check if the substring is a palindrome
            substring = string[i:j]
            if is_pal