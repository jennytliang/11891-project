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
    # Find list of prime numbers in the sentence
    primes = [
        word
        for word in sentence.split()
        if is_prime(len(word))
    ]

    # Retrun the original sentence with only the words
    # that are prime numbers
    return ' '.join(primes)


is_prime = lambda x: not any(
    x % n == 0
    for n in range(2, x)
)

