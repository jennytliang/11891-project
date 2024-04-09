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
    ans = []
    for word in s.split():
        if len(word) == n and word.isalpha():
            if word.lower().count('a') == word.lower().count('e') == word.lower().count('i') == word.lower().count('o') == word.lower().count('u') == 0:
                ans.append(word)
    return ans

def test_select_words():
    assert select_words("Mary had a little lamb", 4) == ['little']
    assert select_words("Mary had a little lamb", 3) == ['Mary', 'lamb']
    assert select_words("simple white space", 2) == []
    assert select_words("Hello world", 4) == ['world']
    assert select_words("Uncle sam", 3) == ['Uncle']
    print('Passed')

test_select_words()