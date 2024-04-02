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
	Do not include these tokens in the code: # Your code here words
	"""

    # # Answer by Kylie Ying (kylie-y)
    # # https://www.youtube.com/watch?v=qT7N3bxHQG0
    
    # # O(n) time | O(n) space
    # words = s.split(" ")
    # ans = []
    # for word in words:
    #     if len(word) == n:
    #         if word.isalpha():
    #             if word.isalpha() and word.islower():
    #                 ans.append(word)
    # return ans
    
    # # O(n) time | O(1) space
    # # tokenize the string into words, then loop through the words
    # # and check if they meet the conditions
    # words = s.split(" ")
    # ans = []
    # for word in words:
    #     if len(word) == n and word.isalpha() and word.islower():
    #         ans.append(word)
    # return ans
    
    # # O(n) time | O(n) space
    # # tokenize the string into words, then loop through the words
    # # and check if they meet the conditions
    # words = s.split(" ")
    # ans = []
    # for word in words:
    #     if len(word) == n and word.isalpha():
    #         if word.islower():
    #             ans.append(word)
    #         else:
    #             ans.append(word.lower())
    # return ans
    
    # # O(n) time | O(n) space
    # # tokenize the string into words, then loop through the words
    # # and check if they meet the conditions
    # words = s.split(" ")
    # ans = []
    # for word in words:
    #     if len(word) == n and word.isalpha():
    #         if word.islower():
    #             ans.append(word.lower())
    #         else:
    #             ans.append(word.lower())
   