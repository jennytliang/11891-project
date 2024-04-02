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
	Do not include these tokens in the code: result = [] for word
	"""
    ######################
    # PSEUDOCODE
    # split the sentence into words
    # create a list to store the words
    # loop through the words
    #   if the word length is prime, add it to the list
    # return the list
    #####################

    # split the sentence into words
    words = sentence.split()

    # create a list to store the words
    prime_words = []

    # loop through the words
    for word in words:
        # if the word length is prime, add it to the list
        if is_prime(len(word)):
            prime_words.append(word)

    # return the list
    return " ".join(prime_words)


def is_prime(n):
    """
    Check if a number is prime
    """
    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True
