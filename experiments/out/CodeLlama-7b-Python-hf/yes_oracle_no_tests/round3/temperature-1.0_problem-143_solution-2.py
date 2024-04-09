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
    #####################
    # PSEUDOCODE
    # 1. split sentence into words
    # 2. for each word, convert to int
    # 3. check if word is prime
    # 4. if prime, add to list
    # 5. join list into string
    # 6. return string
    #####################

    # 1. split sentence into words
    words = sentence.split()

    # 2. for each word, convert to int
    prime_words = []
    for word in words:
        word_int = int(word)
        # 3. check if word is prime
        if is_prime(word_int):
            # 4. if prime, add to list
            prime_words.append(word)

    # 5. join list into string
    prime_words_string = ' '.join(prime_words)

    # 6. return string
    return prime_words_string


def is_prime(number):
    """
    Check if number is prime
    """
    is_prime = True

    # 1. check if number is divisible by 1 and itself
    # 2. if divisible, return False
    for divisor in range(2, number):
        if number % divisor == 0:
            is_prime = False
            break

    return is_prime


print(words_in_sentence("This is a test"))
print(words_in_sentence("lets go for swimming"))
