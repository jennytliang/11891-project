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
    
	Do not include these tokens in the code: # s = s . split ("
	"""
    if s == "": return s
    words = s.split()
    return " ".join([sorted(word) for word in words])

if __name__ == '__main__':
    print("Example:")
    print(anti_shuffle("Hi"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert anti_shuffle("Hi") == "Hi", "Hi -> Hi"
    assert anti_shuffle("hello") == "ehllo", "hello -> ehllo"
    assert anti_shuffle("Hello World!!!") == "Hello !!!Wdlor", "Hello World!!! -> Hello !!!Wdlor"
    assert anti_shuffle("aab ccd eee fff ggg") == "aar cdd eee fff ggg", "aab ccd eee fff ggg -> aar cdd eee fff ggg"
    assert anti_shuffle("aa bb cc dd ee ff gg hh ii jj kk ll mm nn") == "aa bb cc dd ee ff gg hh ii jj kk ll mm nn", "aa bb cc dd ee ff gg hh ii jj kk ll mm nn -> aa bb cc dd ee ff gg hh ii jj kk ll mm nn"
    print("Coding complete? Click 'Check' to earn cool rewards!")