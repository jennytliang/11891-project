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
    
	Include these tokens in the code: def
	Do not include these tokens in the code: # First , we split the sentence
	"""
    # First , we split the sentence
    sentence = sentence.split()

    # Then , we create a list containing all the prime numbers in the range of len(sentence)
    primes = [x for x in range(2, len(sentence)) if all(x % y != 0 for y in range(2, x))]

    # Then , we create a list containing all the words in the sentence
    words = []
    for x in range(len(sentence)):
        words.append(sentence[x])

    # Then , we create a list containing all the prime numbers in the range of len(words)
    primes_words = [x for x in range(2, len(words)) if all(x % y != 0 for y in range(2, x))]

    # Finally , we create a list containing all the prime numbers in the range of len(words)
    # and that are also in the list primes_words
    primes_words_in_primes = [x for x in primes_words if x in primes]

    # Then , we create a list containing all the words in the sentence
    # that are also in the list primes_words_in_primes
    words_in_primes = []
    for x in range(len(words)):
        if x in primes_words_in_primes:
            words_in_primes.append(words[x])

    # Finally , we return a string that contains the words from the original sentence
    # whose lengths are prime numbers
    return " ".join(words_in_primes)
