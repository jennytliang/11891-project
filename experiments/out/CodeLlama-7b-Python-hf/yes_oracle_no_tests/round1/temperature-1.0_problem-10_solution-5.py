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
    suffix = find_longest_palindrome(string)
    if suffix == -1:
        return string
    return string + string[-suffix : : -1]


def find_longest_palindrome(string: str) -> int:
    """ Find the length of the longest palindromic suffix in a supplied string """
    if string == "":
        return 0
    if string == string[::-1]:
        return len(string)
    for i in range(len(string), 0, -1):
        prefix = string[:i]
        suffix = string[-i:]
        if suffix == suffix[::-1] and prefix == prefix[::-1]:
            return i
    return -1


def main():
    example = "nursesrun"
    print(f"Example {example} => {make_palindrome(example)}")


if __name__ == "__main__":
    main()
