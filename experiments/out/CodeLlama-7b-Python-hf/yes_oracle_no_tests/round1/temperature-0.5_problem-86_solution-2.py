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
    
	Include these tokens in the code:  words = s . split (" ")
	"""

    if len(s) == 0:
        return s

    words = s.split(" ")
    for i in range(len(words)):
        words[i] = "".join(sorted(list(words[i])))
    return " ".join(words)


def test_anti_shuffle():
    assert anti_shuffle("Hi") == "Hi"
    assert anti_shuffle("hello") == "ehllo"
    assert anti_shuffle("Hello World!!!") == "Hello !!!Wdlor"
    assert anti_shuffle("") == ""
    assert anti_shuffle(" a b ") == " a b "
    assert anti_shuffle(" a b c d e f ") == " a b c d e f "
    assert anti_shuffle("Hello World!!!  ") == "Hello !!!Wdlor  "
    assert anti_shuffle("  Hello World!!!  ") == "  Hello !!!Wdlor  "
    assert anti_shuffle("  Hello World!!!  ") == "  Hello !!!Wdlor  "
    assert anti_shuffle("  Hello World!!!  ") == "  Hello !!!Wdlor  "
    assert anti_shuffle("  Hello World!!!  ") == "  Hello !!!Wdlor  "
    assert anti_shuffle("  Hello World!!!  ") == "  Hello !!!Wdlor  "
    assert anti_shuffle("  Hello World!!!  ") == "  Hello !!!Wdlor  "
    assert anti_shuffle("  Hello World!!!  ") == "  Hello !!!Wdlor  "
    assert anti_shuffle("  Hello World!!!  ") == "  Hello !!!Wdlor  "
    assert anti_shuffle("  Hello World!!!  ") == "  Hello !!!Wdlor  "
    assert anti_shuffle("  Hello World!!!  ") == "  Hello !!!Wdlor  "
    assert anti_shuffle("  Hello World!!!  ") == "  Hello !!!Wdlor  "
    assert anti_shuffle("  Hello World!!!  ") == "  Hello !!!Wdlor  "