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
    #############
    # Parameter #
    #############
    words = sentence.split(' ')

    ################
    # Solution Code #
    ################
    # 1. Create a function to check if a number is prime
    def is_prime(a):
        for i in range(2, a):
            if a % i == 0:
                return False
        return True

    # 2. Create a function to generate prime numbers
    def generate_primes(a):
        primes = []
        for i in range(2, a + 1):
            if is_prime(i):
                primes.append(i)
        return primes

    # 3. Create a function to find the words with prime lengths
    def find_words_with_prime_length(words):
        primes = generate_primes(len(words))
        words_with_prime_length = []
        for i in range(len(words)):
            if primes[i] == len(words[i]):
                words_with_prime_length.append(words[i])
        return words_with_prime_length

    # 4. Create a function to find the words with prime length
    def find_words_with_prime(words):
        words_with_prime = []
        for word in words:
            if is_prime(len(word)):
                words_with_prime.append(word)
        return words_with_prime

    # 5. Return the words with prime length
    if len(words) == 1:
        return sentence
    else:
        words_with_prime_length = find_words_with_prime_length(words)
        words_with_prime = find_words_with_prime(words)
        if len(words_with_prime) == 0:
            return ' '.join(words_with_prime_length)
        else:
            return ' '.join(words_with_prime)


# 6. Print the words with prime length
print(words_in_sentence("This is a test"))
print(