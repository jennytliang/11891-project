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
    
	Include these tokens in the code: ")
	Do not include these tokens in the code: " )[ :: - 1 ]
	"""


    words = s.s.split(" ")
    new_words = []
    for word in words:
        new_word = ""
        for letter in word:
            new_word += chr(ord(letter) + 1)
        new_words.append(new_word)
    return " ".join(new_words)


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert anti_shuffle("Hi") == "Hi", "Hi"
    assert anti_shuffle("hello") == "ehllo", "ehllo"
    assert anti_shuffle("a b c d e f g h i k l") == "abcdefghikl", "abcdefghikl"
    assert anti_shuffle("How are you?") == "Hnow ae uoy?", "Hnow ae uoy?"
    assert anti_shuffle("Hello World!!!") == "Hello !!!Wdlor", "Hello !!!Wdlor"
    assert anti_shuffle("1 2 3 4 5 6 7 8 9 0") == "1234567890", "1234567890"
    assert anti_shuffle("Lorem ipsum") == "Lrem ipmsu", "Lrem ipmsu"
    assert anti_shuffle("Hello World") == "Hello World", "Hello World"
    assert anti_shuffle("A quick brown fox jumped over the lazy dog.") == "A cuqk owb nraf epxje terevo lystad.","A  cuqk owb nraf epxje terevo lystad."
