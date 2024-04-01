def get_closest_vowel(word):
    """You are given a word. Your task is to find the closest vowel that stands between 
    two consonants from the right side of the word (case sensitive).
    
    Vowels in the beginning and ending doesn't count. Return empty string if you didn't
    find any vowel met the above condition. 

    You may assume that the given string contains English letter only.

    Example:
    get_closest_vowel("yogurt") ==> "u"
    get_closest_vowel("FULL") ==> "U"
    get_closest_vowel("quick") ==> ""
    get_closest_vowel("ab") ==> ""
    
	Include these tokens in the code:  def is _ v owel ( ch
	Do not include these tokens in the code: ow els =
	"""

    # First, we'll determine the position of the consonant that's closest to the vowel.
    # We'll do this by iterating through the string backwards.

    # First, we'll check to see if the word is empty.
    if len(word) == 0:
        return ""

    # If the word has only one character, we'll check to see if it's a vowel.
    if len(word) == 1:
        if is_vowel(word[0]):
            return word[0]
        else:
            return ""

    # We'll start at the end of the word and move backwards.
    # If we encounter a vowel, we'll set the vowel position to the current position.
    # If we encounter a consonant, we'll set the consonant position to the current position.
    # We'll keep iterating until we hit a vowel.
    # Once we hit a vowel, we'll compare the vowel position to the consonant position.
    # If the vowel position is greater than the consonant position, we know that the
    # vowel is closer to the right side than the consonant.
    # If the vowel position is less than the consonant position, we know that the
    # consonant is closer to the right side than the vowel.
    # If the vowel position is equal to the consonant position, we know that the
    # vowel and the consonant are on the same side.
    # If the vowel position is greater than the consonant position, we know that the
    # vowel is closer to the right side than the consonant.
    # If the vowel position is less than the consonant position, we know that the
    # consonant is closer to the right side than the vowel.
    # If the vowel position is equal to the consonant position, we know that the
    # vowel and the consonant are on the same side.

    vowel_position = len(word) - 1
    consonant_position = len(word) - 