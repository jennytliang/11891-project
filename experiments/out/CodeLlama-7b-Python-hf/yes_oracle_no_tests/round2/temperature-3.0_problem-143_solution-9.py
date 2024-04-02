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
	Do not include these tokens in the code: words = sentence . split ()
	"""
    words = sentence.split(" ")
    result = ""
    for word in words:
        if len(word) in list_of_prime_numbers(len(word)):
            result += word + " "
    return result.strip()


def list_of_prime_numbers(num):
    """
    Returns a list of prime numbers
    """
    primes = []
    for i in range(2, num + 1):
        if not any(i % j == 0 for j in range(2, i)):
            primes.append(i)
    return primes
