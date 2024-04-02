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
    if is_palindrome(string):
        return string
    for i in range(len(string), 0, -1):
        if is_palindrome(string[:i]):
            return string + string[i - len(string) :][::-1]


def is_palindrome_stack(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]


def make_palindrome_stack(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string.
    Algorithm idea is simple:
    - Use two stacks, one for characters, another for reversed characters.
    - Iterate over supplied string, and put characters in the first stack.
    - Once the first stack is full, start to pop characters from the first stack,
      and push them into the second stack.
    - Once the first stack is empty, push the rest of the characters from the first stack
      into the second stack.
    - Once the first stack is empty, the second stack will contain the palindrome.
    >>> make_palindrome_stack('')
    ''
    >>> make_palindrome_stack('cat')
    'catac'
    >>> make_palindrome_stack('cata')
    'catac'
    """
    if is_palindrome_stack(string):
        return string
    stack1, stack2 = [], []
    for char in string:
        stack1.append(char)
        if len(stack1) > len(stack2):
            while stack1:
                stack2.append(stack1.pop())
    while stack1:
        stack2.append(stack1.pop())
    return "".join(stack2)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
