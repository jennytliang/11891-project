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
    #print(f"words: {words}")
    ordered_words = []
    for word in words:
        #print(f"word: {word}")
        ordered_word = "".join(sorted(word))
        ordered_words.append(ordered_word)
    #print(f"ordered_words: {ordered_words}")
    ordered_s = " ".join(ordered_words)
    return ordered_s


def anti_shuffle_solution(s):
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
    #print(f"words: {words}")
    ordered_words = []
    for word in words:
        #print(f"word: {word}")
        ordered_word = "".join(sorted(word))
        ordered_words.append(ordered_word)
    #print(f"ordered_words: {ordered_words}")
    ordered_s = " ".join(ordered_words)
    return ordered_s


if __name__ == "__main__":
    string = "Hello World"
    print(f"string: {string}")
    print(f"anti_shuffle(string): {anti_shuffle(string)}")
    print(f"anti_shuffle_solution(string): {anti_shuffle_solution(string)}")

    string = "Hi"
    print(f"string: {string}")
    print(f"anti_sh