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
        if a in [2, 3, 5, 7]:
            return True
        if a % 2 == 0 or a % 3 == 0 or a % 5 == 0 or a % 7 == 0:
            return False
        for i in range(2, int(a ** 0.5) + 1):
            if a % i == 0:
                return False
        return True

    def get_prime_words(sentence):
        words = sentence.split()
        return [word for word in words if is_prime(len(word))]

    return ' '.join(get_prime_words(sentence))


if __name__ == "__main__":
    print(words_in_sentence("This is a test"))
    print(words_in_sentence("lets go for swimming"))
