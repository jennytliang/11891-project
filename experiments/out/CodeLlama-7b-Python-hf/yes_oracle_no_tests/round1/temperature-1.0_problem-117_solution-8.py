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
    # Your code here
    # s = s.lower()
    # ls = s.split(" ")
    # n_consonants = 0
    # ans = []
    # for word in ls:
    #     for letter in word:
    #         if letter.lower() in "aeiou":
    #             n_consonants += 1
    #     if n_consonants == n:
    #         ans.append(word)
    #     n_consonants = 0
    # return ans

    return [word for word in s.split() if len(re.findall('[bcdfghjklmnpqrstvwxz]', word)) == n]


# print(select_words("Mary had a little lamb", 4))
# print(select_words("Mary had a little lamb", 3))
# print(select_words("simple white space", 2))
# print(select_words("Hello world", 4))
# print(select_words("Uncle sam", 3))


def select_words_2(s, n):
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
    # Your code here
    # s