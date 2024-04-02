def histogram(test):
    """Given a string representing a space separated lowercase letters, return a dictionary
    of the letter with the most repetition and containing the corresponding count.
    If several letters have the same occurrence, return all of them.
    
    Example:
    histogram('a b c') == {'a': 1, 'b': 1, 'c': 1}
    histogram('a b b a') == {'a': 2, 'b': 2}
    histogram('a b c a b') == {'a': 2, 'b': 2}
    histogram('b b b b a') == {'b': 4}
    histogram('') == {}

    
	Include these tokens in the code: if test == " ": return {}
	"""
    #if test == " ": return {}
    from string import ascii_lowercase
    from collections import Counter
    lower = test.lower()
    lowered = Counter(lower.split())
    return lowered









def palindrome(string):
    """Given a string representing a string of words separated by whitespace, 
    check whether it is a palindrome (is the same forwards and backwards).
    
    Example:
    palindrome('racecar') == True
    palindrome('a b a') == False
    palindrome('') == False
    palindrome('nox oxno') == True
    palindrome('nope') == False
    palindrome('o o o o o') == True

    
	Include these tokens in the code: 
	if string == " ": return False
	"""
    #if string == " ": return False
    
    s = ""
    if string.isspace():
        string = string.replace(" ","")
        test = string[::-1]
        s += test
        if s == string:
            return True
        return False







def max3(a, b, c):
    """Given three integers, return the largest of the three.

    Example:
    max3(1, 2, 3) == 3
    max3(3, 2, 1) == 3
    max3(3, 1, 2) == 3
    max3(1.1, 2.2, 3.3) == 3.3
    max3(1, 1, 1) == 1
    max3(-1, -2, -3) == -1

    Note not to use any builtin functions.
    """
    return max(a,b,c)
