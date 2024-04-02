def is_palindrome(text: str):
    """
    Checks if given string is a palindrome
    >>> is_palindrome('')
    True
    >>> is_palindrome('aba')
    True
    >>> is_palindrome('aaaaa')
    True
    >>> is_palindrome('zbcd')
    False
    
	Do not include these tokens in the code: if __ name __ == ' __ main __
	"""

    return text == text[::-1]

print("Is 311 a palindrome: {answer}".format(answer="yes" if is_palindrome('311') else "no"))
print("Is 1a3 a palindrome: {answer}".format(answer="yes" if is_palindrome('1a3') else "no"))
print("Is -33 a palindrome: {answer}".format(answer="yes" if is_palindrome('-33') else "no"))
print("Is -333 a palindrome: {answer}".format(answer="yes" if is_palindrome('-333') else "no"))
print("Is A man aplanada? No palindrome!: {answer}".format(answer="yes" if is_palindrome('A man aplanada? No palindrome!') else "no"))
