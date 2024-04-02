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
    
	Do not include these tokens in the code: ### ######## ## # Solution
	"""
    #####################
    # start coding below #
    #####################
    # check for edge case
    if len(sentence) == 1:
        return sentence

    # split the sentence into a list of words
    words = sentence.split()

    # iterate through the words and check if the length of the word is a prime number
    # if it is a prime number, add it to a new list
    primes = []
    for word in words:
        if is_prime(len(word)):
            primes.append(word)

    # join the list into a single string
    return " ".join(primes)


def is_prime(number):
    """
    You are given a number, you have to check if it is a prime number.

    Example 1:
        Input: number = 12
        Output: False

    Example 2:
        Input: number = 20
        Output: False

    Constraints:
        * 1 <= number <= 20
    
	Do not include these tokens in the code: ### ######## ## # Solution
	"""
    #####################
    # start coding below #
    #####################
    # check for edge case
    if number == 1:
        return False

    # iterate through the numbers from 2 to the number and check if the number is divisible by any of them
    # if it is divisible by any of them, the number is not a prime number
    for i in range(2, number):
        if number % i == 0:
            return False

    # otherwise, the number is a prime number
    return True


def is_palindrome(string):
    """
    You are given a string, you have to check if it is a palindrome.

    Example 1:
        Input: string = "abcdcba"
        Output: True

    Example 2:
        Input: string = "abcd"
        Output: False

    Constraints:
        * 1 <= len(string) <= 20
        * string contains only letters
    
