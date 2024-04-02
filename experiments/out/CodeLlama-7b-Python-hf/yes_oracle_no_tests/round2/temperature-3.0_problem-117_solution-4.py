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
    # Write your code here.
    ans = []
    if len(s) == 0:
        return ans
    if n < 0:
        return ans
    if s.isalpha() == False:
        return ans
    if len(s.split()) == 1:
        if len(s) == n:
            return [s]
        else:
            return ans
    if n > len(s):
        return ans
    if n == len(s):
        return [s]
    if n == 0:
        return [s]
    if n >= 1:
        for i in s.split():
            if len(i) == n:
                ans.append(i)
        return ans


def select_words_2(s, n):
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
    # Write your code here.
    ans = []
    if len(s) == 0:
        return ans
    if n < 0:
        return ans
    if s.isalpha() == False:
        return ans
    if len(s.split()) == 1:
        if len(s) == n:
            return [s]
        else:
            return ans
    if n > len(s):
        return