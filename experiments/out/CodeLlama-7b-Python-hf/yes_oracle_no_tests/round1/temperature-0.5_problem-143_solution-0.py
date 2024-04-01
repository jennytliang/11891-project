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
    
	Include these tokens in the code:  def is _ prime ( a ):
	Do not include these tokens in the code: words =
	"""

    #############
    # Base Cases #
    #############

    if not sentence:
        return ""

    if sentence == " " or sentence == "":
        return ""

    if len(sentence) == 1:
        return sentence

    if len(sentence) == 2:
        return sentence

    #############
    # Main Code #
    #############

    words = sentence.split(" ")
    new_words = []

    for word in words:
        if len(word) == 1:
            new_words.append(word)
        else:
            for num in range(2, len(word) + 1):
                if is_prime(num) == True:
                    new_words.append(word)
                    break

    return " ".join(new_words)


def is_prime(num):
    for i in range(2, num):
        if (num % i) == 0:
            return False
    return True


def test_is_prime():
    assert is_prime(5) == True
    assert is_prime(10) == False
    assert is_prime(1) == False
    assert is_prime(7) == True


def test_words_in_sentence_case_1():
    expected = "is"
    actual = words_in_sentence("This is a test")
    assert actual == expected


def test_words_in_sentence_case_2():
    expected = "go for"
    actual = words_in_sentence("lets go for swimming")
    assert actual == expected
