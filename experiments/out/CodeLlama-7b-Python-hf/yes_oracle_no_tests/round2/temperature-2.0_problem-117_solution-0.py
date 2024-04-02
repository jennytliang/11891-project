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
    
	Do not include these tokens in the code: if len ( s ) ==
	"""
    # Your code here
    # s.split() splits the string into a list of strings
    # list comprehension to create a new list with the words that have the right number of characters
    # filter out words with 0 characters
    # filter out words with 1 characters
    # filter out words with 2 characters
    # filter out words with 3 characters
    # filter out words with 4 characters
    # filter out words with 5 characters
    # return all words with 6 characters
    return [word for word in s.split() if len(word) == n]


select_words("Mary had a little lamb", 4)
