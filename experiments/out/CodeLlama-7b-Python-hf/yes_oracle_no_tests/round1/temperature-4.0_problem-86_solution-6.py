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
    anti_shuffled = []
    for word in words:
        if word == "":
            anti_shuffled.append(word)
        else:
            letters = sorted(list(word))
            anti_shuffled.append("".join(letters))
    return " ".join(anti_shuffled)


def test_anti_shuffle():
    assert anti_shuffle("Hi") == "Hi"
    assert anti_shuffle("hello") == "ehllo"
    assert anti_shuffle("Hello World!!!") == "Hello !!!Wdlor"
    assert anti_shuffle("") == ""
    assert anti_shuffle("12345") == "12345"
    assert anti_shuffle("1a2b3c") == "1a2b3c"
    assert anti_shuffle("123 456") == "123 456"
    assert anti_shuffle("1 2 3 4 5") == "1 2 3 4 5"
    assert anti_shuffle("1 2 3 4 5 ") == "1 2 3 4 5 "
    assert anti_shuffle("Hello World!!! 123") == "Hello !!!Wdlor 123"
    assert anti_shuffle("1 2 3 4 5 6 7 8 9 10 11 12 13 14 15") == "1 2 3 4 5 6 7 8 9 10 11 12 13 14 15"
    assert anti_shuffle("1234567890") == "1234567890"
    assert anti_shuffle("1234567890abcdefghijklmnopqrstuvwxyz") == "1234567890abcdefghijklmnopqrstuvwxyz"
    assert anti_shuffle("