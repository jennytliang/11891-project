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
    assert type(sentence) in [list, tuple, str], (
        f"sentence type is {type(sentence)},"
        " It should be of type list, tuple, or str."
    )
    
    words = sentence.split(" ") if isinstance(sentence, str) else sentence
    result = None

    if any((word.isdigit() for word in words)):
        digits = [int(word) for word in words if word.isdigit()]

        if (len(digits) == len(words) and
            min(set(range(len(digits))) - set(digits)) == max(digits)):
            
            result = words
        else:
            return "".join([word for word in words
                              if ((word.isdigit() and int(word) in digits)
                                  or not word.isdigit())])
    
    result = "".join((word for word in words 
                        if not word.isdigit()) if result is None else result)
    
    return result if any((is_prime(i) for i in words)) else \
        "".join([word for word in words
                  if ((int(word) in prime_digits) 
                      or not word.isdigit())])


def is_prime(number):
    assert str(number) == number, f"{number} is not a prime number"
    for i in range(2, int(number ** 0.5)):
        if number % i == 0:
            return False
    return True


prime_digits = [i for i in range(2,101) if is_prime(i)]



assert type(words_in_sentence(["This", "is", "a","test"])) == str, \
    f"words_in_sentence returned {type(words_in_sentence(["This", "is", "a","test"]))}," \
    f" should be of type str"
assert type(words_in_sentence(("lets", "go", "for", "swimming"))) == str, \
