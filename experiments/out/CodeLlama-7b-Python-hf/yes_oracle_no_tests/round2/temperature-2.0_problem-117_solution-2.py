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
    
	Do not include these tokens in the code: # Y OUR CO DE H ERE
	"""
    # WRITE YOUR SOLUTION BELOW THIS LINE
    def get_consonants(s):
        consonants = []
        for c in s:
            if c not in ['a', 'e', 'i', 'o', 'u']:
                consonants.append(c)
        return consonants
    
    def get_words(s):
        words = []
        temp = ""
        for c in s:
            if c == ' ':
                if temp != "":
                    words.append(temp)
                    temp = ""
            else:
                temp += c
        if temp != "":
            words.append(temp)
        return words
    
    def get_words_with_consonants(s, n):
        words = []
        consonants = get_consonants(s)
        if len(consonants) == n:
            words.append(s)
        for word in get_words(s):
            temp = get_consonants(word)
            if len(temp) == n:
                words.append(word)
        return words
    
    return get_words_with_consonants(s, n)
    
    # WRITE YOUR SOLUTION ABOVE THIS LINE
# End of solution

# Below are given tests that will check what happens when you run your code.
# The are not related to what the assignment asks you to do.
# You can safely ignore them.

if __name__ == "__main__":
    # Do not edit this code
    s = "Mary had a little lamb"
    n = 4
    assert select_words(s, n) == ["little"]
    s = "Mary had a little lamb"
    n = 3
    assert select_words(s, n) == ["Mary", "lamb"]
    s = "simple white space"
    n = 2
    assert select_words(s, n) == []
    s = "Hello world"
    n = 4
    assert select_words(s,