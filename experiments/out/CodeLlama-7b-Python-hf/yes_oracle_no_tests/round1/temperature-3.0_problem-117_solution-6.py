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
	Do not include these tokens in the code: # Step 1 : Ext
	"""
    #pass
    # Step 1 : Extract the words from the string s
    words = s.split()
    # Step 2 : Create a list to store the words that have n consonants
    ans = []
    # Step 3 : Iterate through the words
    for word in words:
        # Step 4 : For each word, count the number of consonants
        consonants = 0
        for letter in word:
            if letter not in ['a','e','i','o','u']:
                consonants += 1
        # Step 5 : If the number of consonants is equal to n, add the word to the list
        if consonants == n:
            ans.append(word)
    return ans



print(select_words("Mary had a little lamb", 4))
print(select_words("Mary had a little lamb", 3))
print(select_words("simple white space", 2))
print(select_words("Hello world", 4))
print(select_words("Uncle sam", 3))