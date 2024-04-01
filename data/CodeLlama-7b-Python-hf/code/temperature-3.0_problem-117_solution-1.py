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
    """

    # Step 1: Extract words from input string
    words = []
    word = ""

    for c in s:
        if c.isspace():
            if word != "":
                words.append(word)
                word = ""
        else:
            word += c

    if word != "":
        words.append(word)


    # Step 2: Count total number of consonants in each word.
    words = [word for word in words if len(word) >= n and word.isalpha()]
    count_consonants = lambda x: sum(c.lower() not in 'aeiou' for c in x)
    words = [word for word in words if count_consonants(word) == n]


    return words
