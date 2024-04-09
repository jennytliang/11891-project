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
    
	Do not include these tokens in the code: # Write your code here .
	"""
    
    # write your code here
    def is_consonant(char):
        return char in 'bcdfghjklmnpqrstvwxyz'
    
    def is_vowel(char):
        return char in 'aeiou'
    
    def is_letter(char):
        return char in 'abcdefghijklmnopqrstuvwxyz'
    
    def is_space(char):
        return char == ' '
    
    def is_word(word):
        return all(is_letter(char) for char in word)
    
    def is_consonant_word(word):
        return all(is_consonant(char) for char in word)
    
    def is_vowel_word(word):
        return all(is_vowel(char) for char in word)
    
    def is_consonant_word(word):
        return all(is_consonant(char) for char in word)
    
    def is_vowel_word(word):
        return all(is_vowel(char) for char in word)
    
    def is_space_word(word):
        return all(is_space(char) for char in word)
    
    def consonant_counter(word):
        return sum(1 for char in word if is_consonant(char))
    
    def vowel_counter(word):
        return sum(1 for char in word if is_vowel(char))
    
    def word_list(string):
        return [word for word in string.split(' ') if is_word(word)]
    
    def consonant_word_list(string):
        return [word for word in string.split(' ') if is_consonant_word(word)]
    
    def vowel_word_list(string):
        return [word for word in string.split(' ') if is_vowel_word(word)]
    
    def space_word_list(string):
        return [word for word in string.split(' ') if is_space_word(word)]
    