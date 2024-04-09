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
    
	Do not include these tokens in the code: ### ################ ## # #
	"""
    #############
    # Solution 1 #
    #############
    # assert sentence == 'This is a test'
    # assert result == 'is'
    # return result
    #
    # assert sentence == 'lets go for swimming'
    # assert result == 'go for'
    # return result

    #############
    # Solution 2 #
    #############
    result = []
    for word in sentence.split():
        if is_prime(len(word)):
            result.append(word)
    return ' '.join(result)


def is_prime(number):
    if number == 2:
        return True
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


if __name__ == '__main__':
    # s = input()
    s = 'This is a test'
    result = words_in_sentence(s)
    print(result)