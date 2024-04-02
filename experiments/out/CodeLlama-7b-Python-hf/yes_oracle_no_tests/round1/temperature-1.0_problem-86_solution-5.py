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
    result = []
    for word in words:
        if word == "":
            result.append(word)
        else:
            word = sorted(word)
            word = "".join(word)
            result.append(word)
    return " ".join(result)


def test_anti_shuffle():
    assert anti_shuffle("Hi") == "Hi"
    assert anti_shuffle("hello") == "ehllo"
    assert anti_shuffle("Hello World!!!") == "Hello !!!Wdlor"
    assert anti_shuffle("This is a test") == "dis a ehist etst"
    assert anti_shuffle("This is a test 2") == "dis a ehist etst 2"
    assert anti_shuffle("") == ""
    assert anti_shuffle("a") == "a"
    assert anti_shuffle("ab") == "ab"
    assert anti_shuffle("123") == "123"
    assert anti_shuffle("123 456") == "123 456"
    assert anti_shuffle("123 456 789") == "123 456 789"
    assert anti_shuffle("1 2 3") == "1 2 3"
    assert anti_shuffle("1 2 3 4") == "1 2 3 4"
    assert anti_shuffle("1 2 3 4 5") == "1 2 3 4 5"
    assert anti_shuffle("1 2 3 4 5 6") == "1 2 3 4 5 6"
    assert anti_shuffle("1 2 3 4 5 6 7") == "1 2 3 4 5 6 7"
    assert anti_shuffle("1 2 3 4 5 6 7 8") == "1 2 3 4 5 6 7 8"
    assert anti_