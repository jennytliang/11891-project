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
        if a == 1:
            return False
        for x in range(2, a):
            if a % x == 0:
                return False
        return True

    return " ".join(filter(lambda x: is_prime(len(x)), sentence.split()))


if __name__ == "__main__":
    assert words_in_sentence("This is a test") == "is"
    assert words_in_sentence("lets go for swimming") == "go for"
    assert words_in_sentence("This is another test") == "is"
    assert words_in_sentence("lets go for swimming again") == "go for"
