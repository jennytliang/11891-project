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

    # First, we need to find the position of the last consonant.
    # We can use the `find` function for that.

    # Last consonant position
    last_consonant_position = -1

    # Iterate backwards through the string
    for i in range(len(word)-1, 0, -1):
        # If the character is a consonant, break
        if not is_vowel(word[i]):
            last_consonant_position = i
            break

    # If we didn't find any consonants, return empty string
    if last_consonant_position == -1:
        return ""

    # If we found the last consonant, we need to find the closest vowel before it
    # We can use the `rfind` function for that

    # Closest vowel position
    closest_vowel_position = -1

    # Iterate backwards through the string
    for i in range(last_consonant_position - 1, 0, -1):
        # If the character is a vowel, break
        if is_vowel(word[i]):
            closest_vowel_position = i
            break

    # If we didn't find any vowels, return empty string
    if closest_vowel_position == -1:
        return ""

    # If we found the closest vowel, return the closest vowel
    return word[closest_vowel_position]


def is_vowel(ch):
    return ch in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
