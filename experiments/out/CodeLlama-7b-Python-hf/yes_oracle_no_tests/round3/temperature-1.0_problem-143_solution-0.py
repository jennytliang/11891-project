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
    
	Do not include these tokens in the code: ### ######## ## # #
	"""
    ##############
    # PSEUDOCODE #
	##############

    # 1. split the sentence into words
	# 2. get all the words from the sentence
	# 3. filter out the words that are not prime numbers
	# 4. join the words into a single string, separated by a space
	# 5. return the string

    #############
    # EXECUTION #
    #############

    # 1. split the sentence into words
    words = sentence.split(" ")

    # 2. get all the words from the sentence
    # 3. filter out the words that are not prime numbers
    # 4. join the words into a single string, separated by a space
    primes = " ".join([word for word in words if is_prime(len(word))])

    # 5. return the string
    return primes


def is_prime(number):
    """
    Checks if a number is prime.
    """
    if number < 2:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def test_is_prime():
    assert is_prime(2)
    assert is_prime(3)
    assert not is_prime(4)
    assert is_prime(5)
    assert not is_prime(6)
    assert is_prime(7)
    assert not is_prime(8)
    assert not is_prime(9)


def test_words_in_sentence():
    assert words_in_sentence("This is a test") == "is"
    assert words_in_sentence("lets go for swimming") == "go for"
    assert words_in_sentence("lets go for swimming") == "go for"
    assert words_in_sentence("This is a test") == "is"
    assert words_in_sentence("code jam") == "jam"
    assert words_in_sentence("code jam") == "jam"
    assert words_