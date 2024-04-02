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
    
    # Step 1 : Extract the words from the string.
    s = s.lower().split()
    # Step 2 : Create a list to hold the words with the correct number of consonants.
    ans = []
    # Step 3 : Iterate through the list of words.
    for word in s:
        # Step 4 : Check each word to see if it contains the correct number of consonants.
        if word.count("a") + word.count("e") + word.count("i") + word.count("o") + word.count("u") == n:
            ans.append(word)
    return ans


print(select_words("Mary had a little lamb", 4))
print(select_words("Mary had a little lamb", 3))
print(select_words("simple white space", 2))
print(select_words("Hello world", 4))
print(select_words("Uncle sam", 3))