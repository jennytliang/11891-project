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
    ##################
    # PSEUDOCODE
    #
    # 1. split sentence into words
    # 2. create new empty string (sentence_prime)
    # 3. create empty list (words_prime)
    # 4. iterate through words in sentence
    #     a. if word is prime, append to words_prime
    #     b. append word to sentence_prime
    # 5. join words_prime into sentence_prime
    # 6. return sentence_prime

    # 1. split sentence into words
    sentence = sentence.split(" ")

    # 2. create new empty string (sentence_prime)
    sentence_prime = ""

    # 3. create empty list (words_prime)
    words_prime = []

    # 4. iterate through words in sentence
    for word in sentence:
        # a. if word is prime, append to words_prime
        if is_prime(len(word)):
            words_prime.append(word)

        # b. append word to sentence_prime
        sentence_prime = sentence_prime + " " + word

    # 5. join words_prime into sentence_prime
    sentence_prime = " ".join(words_prime)

    # 6. return sentence_prime
    return sentence_prime


def is_prime(num):
    """
    Determines if a number is prime.

    Args:
        num (int): Number to check.

    Returns:
        bool: True if prime, False otherwise.
    """
    # 1. start with a variable to track if num is prime
    is_prime = True

    # 2. loop through all numbers up to the num
    for i in range(2, num):
        # 3. if num is evenly divisible by i, num is not prime
        if num % i == 0:
            is_prime = False
            # 4. exit loop
            break

    # 5. return if num is prime
    return is_prime


def main():
    print(words_in