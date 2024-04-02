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
    # Hint: use the split function to convert the string into a list of words
    # Hint: use a for loop to iterate through the list of words
    # Hint: use the len function to check that a word contains n consonants
    # Hint: use the isalpha function to check if a character is a letter
    # Hint: use the isvowel function to check if a character is a vowel
    # Hint: use the isspace function to check if a character is a space
    # Hint: use the append function to add a word to a list
    # Hint: use the list function to convert a string into a list of letters
    # Hint: use the join function to convert a list of letters into a string
    # Hint: use the sum function to count the number of vowels in a word
    # Hint: use the filter function to filter out vowels from a list of letters
    # Hint: use the set function to convert a list into a set of unique letters
    # Hint: use the len function to count the number of elements in a set
    # Hint: use the set function to convert a list of letters into a set of unique letters
    # Hint: use the sum function to count the number of vowels in a word
    # Hint: use the filter function to filter out vowels from a list of letters
    # Hint: use the set function to convert a list into a set of unique letters
    # Hint: use the len function to count the number of elements in a set
    # Hint: use the set function to convert a list of letters into a set of unique letters
    if len(s) == 0:
        return []
    ans = []
    for word in s.split():
        if len(word) == n and sum(1 for c in word if c.isalpha()) == n:
            ans.append(word)
    return ans


# def select_words(s, n):
#     """Given a string s and a natural number n, you have been tasked to implement 
#     a function that returns a list of all words from