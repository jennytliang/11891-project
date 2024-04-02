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
    words = sentence.split()
    primes = [num for num in range(2, len(words)+1) if is_prime(num)]
    return " ".join([words[i] for i in primes])


def is_prime(num):
    """
    Check if num is a prime number
    """
    for i in range(2, num):
        if num % i == 0:
            return False
    return True