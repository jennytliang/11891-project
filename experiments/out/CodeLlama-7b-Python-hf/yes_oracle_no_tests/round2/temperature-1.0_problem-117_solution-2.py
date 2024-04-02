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
    
	Do not include these tokens in the code: words = s . split ()
	"""
    
    # Write your code here.
    
    string = s.split()
    lst = []
    count = 0
    for i in string:
        count += 1
        lst.append(i)
        if count % 2 == 0:
            k = i
        if len(k) == n and k.isalpha() and k.islower() == False:
            lst = lst[-1]
        if len(lst) != 0:
            return lst
        else:
            return []
        
select_words("Mary had a little lamb", 4)
select_words("Mary had a little lamb", 3)
select_words("simple white space", 2)
select_words("Hello world", 4)
select_words("Uncle sam", 3)