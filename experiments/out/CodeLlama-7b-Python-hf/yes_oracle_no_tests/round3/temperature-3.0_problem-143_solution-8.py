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
    # 1. Split sentence into words
    # 2. Create a list to store words that are prime
    # 3. For each word in sentence, check if word is prime
    # 4. If so, add to the list
    # 5. Join the list with a space
    ######################

    # 1.
    words = sentence.split()
    # 2.
    prime_words = []
    # 3.
    for word in words:
        # 4.
        if is_prime(word):
            prime_words.append(word)
    # 5.
    return ' '.join(prime_words)


def is_prime(num):
    """
    Determine if a number is prime
    """
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for number in range(3, int(num**0.5)+1, 2):
        if num % number == 0:
            return False
    return True


def test_case(sentence, solution, test_func=words_in_sentence):
    output = test_func(sentence)
    if output == solution:
        print("Passed")
    else:
        print(f"Failed, expected {solution}, got {output}")


test_case("This is a test", "is")
test_case("lets go for swimming", "go for")
test_case("code wars", "")
test_case("code", "code")
test_case("code test test code", "code test code")
test_case("code test test1 code", "")
test_case("code test test1 test code", "test")
