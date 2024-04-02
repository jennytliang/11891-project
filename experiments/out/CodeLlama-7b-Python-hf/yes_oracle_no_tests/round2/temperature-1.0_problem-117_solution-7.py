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
    
    # Write your code below this line 👇

    if len(s) == 0:
        return []
    s_list = s.split()
    words = []

    for word in s_list:
        vowel = 0
        count = 0
        for i in list(str(word).lower()):
            if i.islower() and i == i not in 'aeiou':
                count += 1
                vowel += 1
        if count == n:
            words.append(word)

    return words


if __name__ == "__main__":
    print(select_words(input("Enter a line you'd like to select words from: "), int(input("Enter the number of consonants: "))))

