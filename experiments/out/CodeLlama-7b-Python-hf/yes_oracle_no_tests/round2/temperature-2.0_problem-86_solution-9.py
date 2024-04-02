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
    for i,word in enumerate(words):
        if word.isalpha():
            words[i] = "".join(sorted(word))
    return " ".join(words)

def test_anti_shuffle():
    assert anti_shuffle("Hi") == "Hi"
    assert anti_shuffle("hello") == "ehllo"
    assert anti_shuffle("Hello World!!!") == "Hello !!!Wdlor"
    assert anti_shuffle("123456789") == "123456789"
    assert anti_shuffle("12 3456789") == "12 3456789"
    assert anti_shuffle("12 345 6789") == "12 345 6789"
    assert anti_shuffle("12 345 678 9") == "12 345 678 9"
    assert anti_shuffle("1234567890") == "1234567890"
    assert anti_shuffle("1234567890") == "1234567890"
    assert anti_shuffle("12345678901") == "12345678901"
    assert anti_shuffle("123456789012") == "123456789012"
    assert anti_shuffle("1234567890123") == "1234567890123"
    assert anti_shuffle("12345678901234") == "12345678901234"
    assert anti_shuffle("123456789012345") == "123456789012345"
   