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
    
	Do not include these tokens in the code: list _ of _ words = s
	"""
    
    # split the string into a list of words
    words = s.split()
    
    # count the number of consonants in each word
    consonant_counts = []
    for word in words:
        count = 0
        for letter in word:
            if letter not in ['a','e','i','o','u']:
                count += 1
        consonant_counts.append(count)
    
    # return the list of words with the correct number of consonants
    return [word for word, count in zip(words, consonant_counts) if count == n]

if __name__ == '__main__':
    print(select_words("Mary had a little lamb", 4)) # ==> ["little"]
    print(select_words("Mary had a little lamb", 3)) # ==> ["Mary", "lamb"]
    print(select_words("simple white space", 2)) # ==> []
    print(select_words("Hello world", 4)) # ==> ["world"]
    print(select_words("Uncle sam", 3)) # ==> ["Uncle"]