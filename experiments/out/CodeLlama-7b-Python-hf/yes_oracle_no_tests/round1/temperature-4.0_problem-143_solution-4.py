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
    ######################
    # PSEUDOCODE
    # 1. Split sentence into list of words
    # 2. For each word in list of words:
    #    if word is prime:
    #        append to list of prime words
    # 3. Return list of prime words
    ######################

    # 1. Split sentence into list of words
    words = sentence.split()

    # 2. For each word in list of words:
    prime_words = []
    for word in words:
        #    if word is prime:
        if is_prime(word):
            #        append to list of prime words
            prime_words.append(word)

    # 3. Return list of prime words
    return prime_words


def is_prime(num):
    """
    Check if num is prime
    """
    if num <= 1:
        return False

    # check for factors
    for i in range(2, num):
        if (num % i) == 0:
            return False

    return True


def test_is_prime():
    assert is_prime(2) == True
    assert is_prime(15) == False
    assert is_prime(51) == True


def test_words_in_sentence():
    assert words_in_sentence("This is a test") == "is"
    assert words_in_sentence("lets go for swimming") == "go for"
    assert words_in_sentence("i love coding") == "love coding"
