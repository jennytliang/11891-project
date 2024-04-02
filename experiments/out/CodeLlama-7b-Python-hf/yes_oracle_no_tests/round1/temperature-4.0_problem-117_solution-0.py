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
	Do not include these tokens in the code: res
	"""
    # pass # remove this when you write your solution
    # print(s)
    # print(n)
    s = s.split()
    # print(s)
    ans = []
    for word in s:
        count = 0
        for c in word:
            if c.lower() in "aeiou":
                continue
            else:
                count += 1
        if count == n:
            ans.append(word)
    return ans


def select_words2(s, n):
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
	Do not include these tokens in the code: res
	"""
    # pass # remove this when you write your solution
    # print(s)
    # print(n)
    s = s.split()
    # print(s)
    ans = []
    for word in s:
        count = 0
        for c in word:
            if c.lower() in "aeiou":
                continue
            else:
                count += 1
        if count == n:
            ans.append(word)
    return ans


print(select_words2("Mary had a little lamb", 4))
print(select_words2("Mary had a little lamb", 3))
print(select_words