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

    # First we need to find the words that are prime.
    # We can do this by checking if the length of the word is prime.
    # We can use the is_prime function to check if a number is prime.
    # We can use the split function to split a string into a list of words.
    # Then we can use the filter function to filter the list of words.
    # We can use the join function to join the list of words back into a string.
    return " ".join(list(filter(is_prime, sentence.split())))


def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True
