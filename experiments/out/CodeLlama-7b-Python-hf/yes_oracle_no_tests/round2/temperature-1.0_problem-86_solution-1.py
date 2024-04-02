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
    
	Include these tokens in the code: words
	Do not include these tokens in the code: if s == " ":
	"""
    result = []     
    # iterate over all the words in the given string
    for word in s.strip().split(" "):
        sorted_word = sorted(word)  # ascending order
        result.append("".join(sorted_word))
    
    return " ".join(result)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert anti_shuffle("Hi") == "Hi", "Hi"
    assert anti_shuffle("hello") == "ehllo", "hello"
    assert anti_shuffle("Hello World!!!") == "Hello !!!Wdlor", "Hello World!!!"
    assert anti_shuffle("Race Car") == "ace CarR", "Race Car"
    assert anti_shuffle("hello World") == "hello Word", "hello World"
    assert anti_shuffle("34 567 32 544656") == "34 32 456 544656", "34 567 32 544656"
    assert anti_shuffle("That's it bro!") == "abd  ihi Itr!!!", "That's it bro!"
    assert anti_shuffle("one") == "eono", "one"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
