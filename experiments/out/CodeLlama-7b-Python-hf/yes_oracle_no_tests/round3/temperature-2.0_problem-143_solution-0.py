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
    ## EDGE CASES ##
    if sentence == "" or sentence == " ":
        return ""
    if sentence == None:
        return None
    if not sentence.isalpha():
        return None
    ## MAIN BODY ##

    words = sentence.split(" ")
    length = len(words)
    output = []
    for word in words:
        if len(word) == 1:
            output.append(word)
        if len(word) > 1:
            if is_prime(len(word)) == True:
                output.append(word)
    return " ".join(output)


def is_prime(number):
    """
    Given a number, returns True if it is a prime number,
    otherwise returns False
    """
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True
