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
    
	Do not include these tokens in the code: ### ######## ## 1 0 lines
	"""
    ######################
    # PSEUDOCODE
    # 1. split sentence into list of words
    # 2. create empty list for prime words
    # 3. for each word in list of words:
    #    a. check if word length is prime
    #    b. if so, add to list of prime words
    # 4. join list of prime words with a space
    # 5. return list of prime words
    ######################
    words = sentence.split()
    prime_words = []
    for word in words:
        if len(word) in get_prime_numbers():
            prime_words.append(word)
    return ' '.join(prime_words)


def get_prime_numbers(number=100):
    """
    Return all prime numbers between 1 and number
    """
    primes = []
    for i in range(2, number + 1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            primes.append(i)
    return primes


if __name__ == '__main__':
    print(words_in_sentence(input()))
