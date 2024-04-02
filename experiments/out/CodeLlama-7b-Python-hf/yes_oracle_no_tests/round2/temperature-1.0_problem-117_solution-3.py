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
	Do not include these tokens in the code: print (" s
	"""
    s=s.split(" ")
    
    l=[]
    for word in s:
        sum=0
        for i in word:
            if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
                continue
            else:
                sum = sum+1
        if sum==n:
            l.append(str(word))
    print(l)
select_words(str(input()), int(input()))
    
    