def words_in_sentence(sentence):
    """
    You are given a string representing a sentence,
    the sentence contains some words separated by a space,
    and you have to return a string that contains the words from the original sentence,
    whose lengths are prime numbers,
    the order of the words in the new string should be the same as the original one.

    Example 1:
        Input: sentence = "This is a test"
        Output: "is"

    Example 2:
        Input: sentence = "lets go for swimming"
        Output: "go for"

    Constraints:
        * 1 <= len(sentence) <= 100
        * sentence contains only letters
    
	Include these tokens in the code: def is _ prime ( a ): return
	"""
    
    def is_prime(a):
        return a == 2 or a == 3 or a == 5 or a == 7 or a == 11 or a == 13 or a == 17
    
    words = sentence.split()
    result = []
    for word in words:
        if len(word) == 1:
            continue
        if is_prime(len(word)):
            result.append(word)
    
    return " ".join(result)


if __name__ == "__main__":
    assert words_in_sentence("This is a test") == "is"
    assert words_in_sentence("lets go for swimming") == "go for"
