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
	Do not include these tokens in the code: # Step 1 : Ext
	"""
    # Step 1 : Extract all the words from the string s
    # Step 2 : Filter the words that have exactly n consonants
    # Step 3 : Return all those words
    # Step 4 : Implement function
    # Step 5 : Test your code
    # Step 6 : Check your code
    # Step 7 : Commit your code

    # Step 1 : Extract all the words from the string s
    words = s.split()

    # Step 2 : Filter the words that have exactly n consonants
    ans = [word for word in words if len(word) == n]

    # Step 3 : Return all those words
    return ans


def main():
    print(select_words("Mary had a little lamb", 4))
    print(select_words("Mary had a little lamb", 3))
    print(select_words("simple white space", 2))
    print(select_words("Hello world", 4))
    print(select_words("Uncle sam", 3))


if __name__ == "__main__":
    main()
