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
    
	Do not include these tokens in the code: def cons _ count ( s
	"""
    arr = select_words_helper(s.split(), n)
    return arr
    
def find_consonants(s):
    s = s.lower()
    vowels = ['a', 'e', 'i', 'o', 'u']
    return s[1:] if s[0] in vowels else s


def select_words_helper(s, n):
    """Given a string s and a natural number n, you have been tasked to implement 
    a function that returns a list of all words from string s that contain exactly 
    n consonants, in order they words apper in s.
    You have to use the helper function:
    cons _count ( s )
    where:
    - cons_count can return number of consomnants in s or any string (in this task)
    - s: is the string you need to check
    
    Examples:
    find_consonants("little") == 4
   """     
    arr = []
    for i in s:
        if cons_count(i) == n:
            arr.append(i)
    return arr

def cons_count(s):
    """
    cons_count function will return number of consomnants (c) in s (s string)
    """
    arr = []
    c = 0
    for i in s:
        if i in ['a', 'e', 'i', 'o', 'u']:
            c += 1
    return len(s) - c

