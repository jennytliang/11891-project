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
    # split the string into list of words
    # split the words into list of letters
    # filter the list of letters to only include vowels
    # if the length of the list is n, add the word to the result list
    # return the result list
    s = s.split()
    result = []
    for word in s:
        letters = list(word)
        vowels = filter(lambda letter: letter in "aeiou", letters)
        if len(vowels) == n:
            result.append(word)
    return result
