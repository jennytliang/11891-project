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
    return ' '.join(list(zip(*words))[1])

if __name__ == '__main__':
    print("Example:")
    print(anti_shuffle("hello"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert anti_shuffle("hello") == "ehllo", "First"
    assert anti_shuffle("Here Comes The Sun") == "EchRs tne Comse TsnS", "Second"
    assert anti_shuffle("hi") == "hi", "Third"
    print("Coding complete? Click 'Check' to earn cool rewards!")
