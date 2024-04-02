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
    sentence = sentence.split()
    return " ".join(
        word for word in sentence if is_prime(len(word))
    )


def is_prime(n):
    is_prime = True
    if n == 1 or n == 2:
        return is_prime
    elif n % 2 == 0 or n % 3 == 0:
        is_prime = False
    else:
        i = 5
        while i * i <= n and is_prime:
            if n % i == 0 or n % (i+2) == 0:
                is_prime = False
            i += 6
    return is_prime


def test_words_in_sentence():
    assert words_in_sentence("This is a test") == "is"
    assert words_in_sentence("lets go for swimming") == "go for"
    assert words_in_sentence("Thisis a test"), "", ""
    assert words_in_sentence(2), "", ""


if __name__ == '__main__':
    test_words_in_sentence()
