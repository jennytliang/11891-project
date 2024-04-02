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
    # My and best way solution
    def is_prime(a):
        return a > 1 and all(a % i for i in range(2, int(a ** 0.5) + 1))

    def words_in_sentence(sentence):
        return ' '.join([word for word in sentence.split() if is_prime(len(word))])

    return words_in_sentence(sentence)



def test():
    assert words_in_sentence("This is a test") == "is"
    assert words_in_sentence("lets go for swimming") == "go for"
    assert words_in_sentence("this test this test") == ""
    assert words_in_sentence("go go go go go go go") == "go go go go go go"
    assert words_in_sentence("go go go go go go go go go go go go go go go go go go go go go go") == "go go go go go go go go go go go go go go go go go go go go"
    assert words_in_sentence("go go go go go go go go go go go go go go go go go go go go go go go go go go") == "go go go go go go go go go go go go go go go go go go go go go go go go go"
    assert words_in_sentence("go go go go go go go go go go go go go go go go go go go go go go go go go go go go go") == "go go go go go go go go go go go go go go go go go go go go go go go go go go go go"
    assert words_in_sentence("go go go go go go go go go go go go go go go go go go go go go go go go go go go go go go go") == "go go go go go go go go go go go go go go go go go go go go go go go go go go go go go go"
    assert words_in_sentence("go go go go go go go go go go go go go go go go go go go go go go go go go go go go go go