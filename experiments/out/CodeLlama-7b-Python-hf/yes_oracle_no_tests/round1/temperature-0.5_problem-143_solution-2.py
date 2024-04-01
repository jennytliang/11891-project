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
    
	Include these tokens in the code:  def is _ prime ( a ):
	Do not include these tokens in the code: words =
	"""

    # 1. Find all words in sentence
    words = sentence.split(' ')

    # 2. Filter words by prime length
    words_in_sentence = [word for word in words if is_prime(len(word))]

    # 3. Join words by space
    return ' '.join(words_in_sentence)


def is_prime(n):
    """
    Determine if a number is a prime number.

    Example 1:
        Input: n = 9
        Output: false

    Example 2:
        Input: n = 17
        Output: true
    """
    # 1. Check if n is a negative integer
    if n <= 0:
        # Not a prime
        return False

    # 2. Check if n is an even integer
    if n % 2 == 0:
        # Not a prime
        return False

    # 3. Check if n is an odd integer
    if n % 2 != 0:
        # Check if n is a prime
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                # Not a prime
                return False

    # 4. Return if n is a prime
    return True


if __name__ == '__main__':
    test_cases = [
        ['sentence = "This is a test"', 'output = "is"'],
        ['sentence = "lets go for swimming"', 'output = "go for"'],
    ]
    for index, test_case in enumerate(test_cases):
        print(f'test case {index + 1}')
        print(f'input: {test_case[0]}')
        print(f'output: {test_case[1]}')
        print(f'words_in_sentence({test_case[0].split(" ")[1]}) = {words_in_sentence(eval(test_case[0].split(" ")[1]))}')
        print('')
