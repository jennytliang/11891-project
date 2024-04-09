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
    assert sentence

    words = sentence.split()
    primes = []
    
    for word in words:
        if is_prime(len(word)):
            primes.append(word)

    return ' '.join(primes)


def is_prime(num):
    if num == 1:
        return False
    
    for i in range(2, num):
        if num % i == 0:
            return False
    
    return True


if __name__ == '__main__':
    # Example 1:
    # Input: sentence = "This is a test"
    # Output: "is"
    sentence = "This is a test"
    print(words_in_sentence(sentence))

    # Example 2:
    # Input: sentence = "lets go for swimming"
    # Output: "go for"
    sentence = "lets go for swimming"
    print(words_in_sentence(sentence))

    # Example 3:
    # Input: sentence = "yep"
    # Output: ""
    sentence = "yep"
    print(words_in_sentence(sentence))

    # Example 4:
    # Input: sentence = "This is an empty sentence"
    # Output: ""
    sentence = "This is an empty sentence"
    print(words_in_sentence(sentence))

    # Example 5:
    # Input: sentence = "This is a test sentence"
    # Output: "test"
    sentence = "This is a test sentence"
    print(words_in_sentence(sentence))

    # Example 6:
    # Input: sentence = "This is a test sentence."
    # Output: "test"
    sentence = "This is a test sentence."
    print(words_in_sentence(sentence))

    # Example 7:
    # Input: sentence = "This is a test sentence."
    # Output: "test"
    sentence = "This is a test sentence."
    print(words_in_sentence(sentence))
