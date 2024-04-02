def anti_shuffle(s):
    """
    Write a function that takes a string and returns an ordered version of it.
    Ordered version of string, is a string where all words (separated by space)
    are replaced by a new word where all the characters arranged in
    ascending order based on ascii value.
    Note: You should keep the order of words and blank spaces in the sentence.

    For example:
    anti_shuffle('Hi') returns 'Hi'
    anti_shuffle('hello') returns 'ehllo'
    anti_shuffle('Hello World!!!') returns 'Hello !!!Wdlor'
    
	Include these tokens in the code: words = s . split (" ")
	"""
    words = s.split(" ")
    #print(words)
    new_words = []
    for word in words:
        if word == "":
            new_words.append(word)
        else:
            new_word = ""
            for char in word:
                new_word = char + new_word
            new_words.append(new_word)
    #print(new_words)
    new_s = ""
    for word in new_words:
        new_s = new_s + word + " "
    return new_s[:-1]


def test_anti_shuffle():
    assert anti_shuffle("Hi") == "Hi"
    assert anti_shuffle("hello") == "ehllo"
    assert anti_shuffle("Hello World!!!") == "Hello !!!Wdlor"
