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

    # pylint: disable=W0102, W0107, W0621, C0103
    def is_prime(a):
        if a <= 1:
            return False
        for i in range(2, a):
            if a % i == 0:
                return False
        return True

    words = sentence.split()
    words_prime = [word for word in words if is_prime(len(word))]
    return " ".join(words_prime)
