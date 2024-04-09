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
    
	Include these tokens in the code: ans = []
	"""
    # strip() removes the leading and trailing spaces
    s = s.strip()
    # split() splits the string into a list based on the separator
    # in this case, it splits the string into a list of words
    # based on the spaces between the words
    words = s.split()
    # the list comprehension below is a short way of writing the following:
    # for word in words:
    #   if len(word) == n:
    #       ans.append(word)
    ans = [word for word in words if len(word) == n]
    return ans
