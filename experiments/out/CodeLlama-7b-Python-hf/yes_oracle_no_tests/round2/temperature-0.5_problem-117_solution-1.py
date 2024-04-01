def select_words(s, n):
    """Given a string s and a natural number n, you have been tasked to implement 
    a function that returns a list of all words from string s that contain exactly 
    n consonants, in order these words appear in the string s.
    If the string s is empty then the function should return an empty list.
    Note: you may assume the input string contains only letters and spaces.
    Examples:
    select_words("Mary had a little lamb", 4) ==> ["little"]
    select_words("Mary had a little lamb", 3) ==> ["Mary", "lamb"]
    select_words("simple white space", 2) ==> []
    select_words("Hello world", 4) ==> ["world"]
    select_words("Uncle sam", 3) ==> ["Uncle"]
    
	Do not include these tokens in the code: # write your code here
	"""
    return [w for w in s.split() if len([c for c in w if c.lower() in "aeiou"]) == n]


if __name__ == '__main__':
    print("Example:")
    print(select_words("Mary had a little lamb", 4))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert select_words("Mary had a little lamb", 4) == ["little"]
    assert select_words("Mary had a little lamb", 3) == ["Mary", "lamb"]
    assert select_words("simple white space", 2) == []
    assert select_words("Hello world", 4) == ["world"]
    assert select_words("Uncle sam", 3) == ["Uncle"]
    print("Coding complete? Click 'Check' to earn cool rewards!")
