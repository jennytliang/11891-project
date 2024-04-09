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
    
	Include these tokens in the code: def is _ prime
	Do not include these tokens in the code: ### ################ ## # start
	"""
    ##############################
    # start
    ##############################
    # Write your code here
    words = sentence.split()
    output = []
    for word in words:
        if len(word) == 1:
            output.append(word)
        else:
            is_prime = True
            for i in range(2, int(len(word)**0.5)+1):
                if word % i == 0:
                    is_prime = False
                    break
            if is_prime:
                output.append(word)
    return " ".join(output)
    ##############################
    # end
    ##############################
