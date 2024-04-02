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
    prefix = ''
    suffix = ''
    while string:
        if is_palindrome(string):
            break
        string = string[:-1]
    if string:
        prefix = string
        suffix = string[::-1]
    return prefix + suffix


def make_palindrome_dynamic(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string.
    Algorithm idea is simple:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    >>> make_palindrome_dynamic('')
    ''
    >>> make_palindrome_dynamic('cat')
    'catac'
    >>> make_palindrome_dynamic('cata')
    'catac'
    
	Do not include these tokens in the code: return string == string [ :: -
	"""
    prefix = ''
    suffix = ''
    for i in range(len(string)):
        for j in range(i + 1, len(string) + 1):
            if is_palindrome(string[i:j]):
                break
        if is_palindrome(string[i:j]):
            prefix = string[:i]
            suffix = string[i:j][::-1]
            break
    return prefix + suffix


def main():
    print(make_palindrome(''))
    print(make_palindrome('cat'))
    print(make_palindrome('cata'))
    print(make_palindrome_dynamic(''))
    print(make_palindrome_dynamic('cat'))
    print(make_palindrome_dynamic('cata'))


if __name__ == '__main__':
    main()
