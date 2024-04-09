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
    #split the string into a list of words
    word_list = s.split()
    #go through each word
    for word in word_list:
        #if the word has the right number of consonants, add it to the answer
        if consonant_count(word) == n:
            ans.append(word)
    return ans
    
def consonant_count(s):
    """Given a string s, return the number of consonants in the string.
    Note: you may assume the input string contains only letters.
    Examples:
    consonant_count("Mary had a little lamb") ==> 7
    consonant_count("a u c") ==> 2
    consonant_count("x") ==> 1
    consonant_count("") ==> 0
    """
    #count the number of consonants
    consonants = 0
    #go through each letter in the string
    for letter in s:
        #if the letter is not a vowel, add it to the consonant count
        if letter not in ['a', 'e', 'i', 'o', 'u']:
            consonants += 1
    return consonants

ans = select_words("Mary had a little lamb", 4)
print(ans)
