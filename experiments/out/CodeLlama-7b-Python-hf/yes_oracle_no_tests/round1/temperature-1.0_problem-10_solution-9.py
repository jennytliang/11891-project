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
    # TODO: implement the function
    # return string == string [ :: - 1]
    raise NotImplementedError()


def is_palindrome_stack(string: str) -> bool:
    """ Test if given string is a palindrome using a stack """
    if string == '':
        return True
    stack = []
    for i in range(len(string)):
        stack.append(string[i])

    flag = True

    while flag:
        if len(stack) == 1:
            return True
        if stack.pop() != string[len(stack)]:
            return False
        if len(stack) == 1:
            return True
        if stack.pop() != string[len(stack) - 1]:
            return False


def make_palindrome_stack(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string.
    Algorithm idea is simple:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    >>> make_palindrome_stack('')
    ''
    >>> make_palindrome_stack('cat')
    'catac'
    >>> make_palindrome_stack('cata')
    'catac'
    
	Do not include these tokens in the code: return string == string [ :: -
	"""
    if string == '':
        return string
    string = string + string[::-1]
    stack = []
    for i in range(len(string)):
        stack.append(string[i])
    string = ''
    while len(stack) > 1:
        string = string + stack.pop()

    return string


if __name__ == '__main__':
    import doctest

    doctest.testmod()
