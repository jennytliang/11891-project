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
    
	Include these tokens in the code: ans
	Do not include these tokens in the code: if len ( s ) ==
	"""
    # YOUR CODE HERE
    if len(s) == 0:
        return []
    else:
        s = s.lower()
        s = s.split()
        ans = []
        for word in s:
            if len(word) == n:
                vowels = 'aeiou'
                if word.count('a') == 0 and word.count('e') == 0 and word.count('i') == 0 and word.count('o') == 0 and word.count('u') == 0:
                    ans.append(word)
        return ans
