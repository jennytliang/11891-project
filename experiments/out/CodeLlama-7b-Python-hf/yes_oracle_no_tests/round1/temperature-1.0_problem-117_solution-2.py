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
    words =  s.split()
    
    def check_word(word):
        # Checks if a word contains exactly n consonants
        check = ["a","e","i","o","u","y"]
        count = 0
        
        vowels = 0
        for c in word:
            if c not in check:
                count += 1
            else:
                vowels += 1
            
        if count == n and vowels == len(word) - count:
            return True
        else:
            return False
        
    ans = []
    for word in words:
        if check_word(word) == True:
            ans.append(word)
    
    return ans
    