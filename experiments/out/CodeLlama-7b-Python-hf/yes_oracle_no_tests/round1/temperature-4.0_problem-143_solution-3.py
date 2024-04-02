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
    # First, we create a dictionary where the keys are the length of the words and the values are the words with that
    # length.
    words = sentence.split()
    primes = {}
    for word in words:
        if len(word) not in primes:
            primes[len(word)] = []
        primes[len(word)].append(word)

    # Then, we create a list containing the words with prime length
    result = []
    for key in primes:
        if is_prime(key):
            result.extend(primes[key])

    return " ".join(result)


def is_prime(n):
    """
    Check if a number is prime
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
