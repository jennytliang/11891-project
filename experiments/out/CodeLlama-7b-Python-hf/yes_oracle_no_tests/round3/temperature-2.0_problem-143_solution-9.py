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
    
	Do not include these tokens in the code: " ". lower () "
	"""
    words = sentence.split()
    result = []
    for word in words:
        if len(word) == 0:
            continue
        if len(word) == 1:
            result.append(word)
            continue

        if is_prime(len(word)):
            result.append(word)
    return ' '.join(result)


def is_prime(n: int) -> bool:
    """
    Check if n is prime
    """
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
