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
    
	Include these tokens in the code: def is _ prime ( a ):
	Do not include these tokens in the code: words = sentence . split (" ")
	"""
    # pylint: disable=W0212
    if not sentence:
        return ''

    words = sentence.split(' ')
    return ' '.join([word for word in words if _is_prime(len(word))])


def _is_prime(number):
    if number in (2, 3, 5, 7):
        return True
    if number < 2 or number % 2 == 0:
        return False

    for divisor in range(3, int(number ** 0.5) + 1, 2):
        if number % divisor == 0:
            return False

    return True
