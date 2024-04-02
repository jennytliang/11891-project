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
    
	Do not include these tokens in the code: new _ words = [] for word in
	"""

    words = s.split(" ")[::-1]
    # words = s.split()[::-1]
    word_list = []
    for word in words:
        word_list.append("".join(sorted(list(word))))

    return " ".join(word_list)


if __name__ == "__main__":
    print("Example:")
    print(anti_shuffle("hello"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert anti_shuffle("hello") == "ehllo"
    assert anti_shuffle("aabbc") == "abcb"
    assert anti_shuffle("aabBc") == "abcb"
    assert anti_shuffle("aAaA") == "aaaa"
    assert anti_shuffle("Hlllo") == "Hlllo"
    assert anti_shuffle("Hllllo") == "Lhllo"
    assert anti_shuffle("Hhllo") == "Hhllo"
    assert anti_shuffle("Hhhllo") == "Hhhllo"
    assert anti_shuffle("Heeellooo") == "Helloooe"
    assert anti_shuffle("Hi Mom") == "Hi Mom"
    assert anti_shuffle("Hi! Mom") == "Hi! Mom"
    assert anti_shuffle("Hi! Mom!") == "Hi! Mom!"
    assert anti_shuffle("Hi! Mom!?") == "Hi! Mom!?"
    assert anti_shuffle("Hi?! Mom?!") == "Hi?! Mom?!"
    assert anti_shuffle("Hello World!!!") == "Hello !!!Wdlor"
    assert anti_shuffle("Hello World!!!") == "Hello !!!Wdlor"
    print("Coding complete? Click 'Check' to earn cool rewards!")
