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
    ######################
    # PSEUDOCODE
    # 1. Split sentence into a list
    # 2. Create a new list to store words
    # 3. Loop through each word
    # 4. Check if the length of the word is prime
    # 5. If it is, add it to the new list
    # 6. Join the new list back into a string
    ######################

    # 1. Split sentence into a list
    sentence = sentence.split()

    # 2. Create a new list to store words
    new_sentence = []

    # 3. Loop through each word
    for word in sentence:

        # 4. Check if the length of the word is prime
        if is_prime(len(word)):

            # 5. If it is, add it to the new list
            new_sentence.append(word)

    # 6. Join the new list back into a string
    return ' '.join(new_sentence)


def is_prime(num):
    """
    Check if a number is prime
    """
    for i in range(2, num):
        if (num % i) == 0:
            return False
    return True


print(words_in_sentence("This is a test"))
print(words_in_sentence("lets go for swimming"))
