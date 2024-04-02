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
        return a > 1 and all(a % i != 0 for i in range(2, int(a**0.5)+1))
    
    primes = []
    for i in range(len(sentence)):
        if is_prime(len(sentence[i])):
            primes.append(sentence[i])
    return " ".join(primes)