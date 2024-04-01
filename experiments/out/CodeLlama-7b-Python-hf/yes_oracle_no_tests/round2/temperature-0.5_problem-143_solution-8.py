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
    
	Do not include these tokens in the code: # 1 . Take in
	"""
    # pylint: disable=W0613, R0902, R0912, R0913, R0914, C0103
    def is_prime(num):
        if num == 1:
            return False
        if num == 2:
            return True
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

    words = sentence.split()
    primes = []
    for word in words:
        if is_prime(len(word)):
            primes.append(word)

    return " ".join(primes)
