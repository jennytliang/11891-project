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
    # First, we split the sentence into words, using the space as the delimiter.
    words = sentence.split(" ")
    # Then, we iterate through the words list, checking if the length of the current word is a prime number.
    for i in range(len(words)):
        # If the word's length is a prime number, we add it to a new list.
        if is_prime(len(words[i])):
            prime_words.append(words[i])
    # Finally, we join the list of words that are prime numbers, and return the result.
    return " ".join(prime_words)


def is_prime(n):
    """
    Check if a number is prime.
    """
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
