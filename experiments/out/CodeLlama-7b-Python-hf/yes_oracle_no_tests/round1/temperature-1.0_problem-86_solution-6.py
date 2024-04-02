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
    if s is None or s == "":
        return ""
    else:
        words = s.split(" ")
        new_words = []
        for word in words:
            if len(word) == 0:
                new_words.append(word)
            else:
                new_words.append("".join(sorted(list(word))))
        return " ".join(new_words)


def test_anti_shuffle():
    assert anti_shuffle("Hi") == "Hi"
    assert anti_shuffle("hello") == "ehllo"
    assert anti_shuffle("Hello World!!!") == "Hello !!!Wdlor"
    assert anti_shuffle("") == ""
    assert anti_shuffle(None) == ""
    assert anti_shuffle("Hi Hello") == "HHi ello"
    assert anti_shuffle("Hi Hello World") == "HHi ello Worlld"
    assert anti_shuffle("Hi Hello World!!!") == "HHi ello !!!Wdlor"
    assert anti_shuffle("Hi Hello World!!! How are you?") == "HHi ello !!!Wdlor ???aer oyu"
