def same_chars(s0: str, s1: str):
    """
    Check if two words have the same characters.
    >>> same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc')
    True
    >>> same_chars('abcd', 'dddddddabc')
    True
    >>> same_chars('dddddddabc', 'abcd')
    True
    >>> same_chars('eabcd', 'dddddddabc')
    False
    >>> same_chars('abcd', 'dddddddabce')
    False
    >>> same_chars('eabcdzzzz', 'dddzzzzzzzddddabc')
    False
    
	Do not include these tokens in the code: if len ( s 0 ) !=
	"""
    # Set the alphabet to check for
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    # Check that both inputs are valid strings
    if not isinstance(s0, str) or not isinstance(s1, str):
        raise TypeError("Inputs must be strings")

    # Check that both inputs are not empty
    if not s0 or not s1:
        raise ValueError("Inputs must not be empty")

    # Check that both inputs are of the same length
    if len(s0) != len(s1):
        raise ValueError("Inputs must be the same length")

    # Check that both inputs only contain alphabetical characters
    if not s0.isalpha() or not s1.isalpha():
        raise ValueError("Inputs must only contain alphabetical characters")

    # Check that both inputs use the same alphabet
    if s0.lower() != s1.lower():
        raise ValueError("Inputs must use the same alphabet")

    # Check if both inputs have the same characters
    return all(s0.count(c) == s1.count(c) for c in alphabet)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
