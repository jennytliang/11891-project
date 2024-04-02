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

    # Create a list of words in string s.
    word_list = s.split()
    # Create a new list with elements which pass the conditions
    ans = []
    for word in word_list:
        consonant = 0
        for letter in word:
            if letter != 'a' and letter != 'e' and letter != 'i' and letter!= 'o' and letter!= 'u' and letter != ' ':
                consonant += 1
        if consonant == n:
            ans.append(word)
    return ans

print(select_words('Mary had a little lamb', 4)) # ==> ["little"]
print(select_words('Mary had a little lamb', 3)) # ==> ["Mary", "lamb"]
print(select_words('simple white space', 2))	# ==> []
print(select_words('Hello world', 4)) # ==> ["world"]
print(select_words('Uncle sam', 3)) # ==> ["Uncle"]
