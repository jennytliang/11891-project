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
    
	Do not include these tokens in the code: if __ name __ == " __ main __
	"""


    return text == text[:len(text)//2][::-1] + text[len(text)//2 + 1:] 
  
print(is_palindrome('abba')) #true  


