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
    
	Include these tokens in the code: ch : str ) -> bool :
	Do not include these tokens in the code: char ):
	"""


    def is_vowel(ch):
        return ch in 'AEIOUaeiou'

    if len(word) < 3:
        return ''

    # Find the last vowel
    last_vowel_pos = -1
    for i in range(len(word)-1, -1, -1):
        if is_vowel(word[i]):
            last_vowel_pos = i
            break

    # Find the last consonant
    last_consonant_pos = -1
    for i in range(len(word)-1, -1, -1):
        if not is_vowel(word[i]):
            last_consonant_pos = i
            break

    # Find the closest vowel between the last consonant and the last vowel
    closest_vowel_pos = -1
    for i in range(last_consonant_pos, last_vowel_pos):
        if is_vowel(word[i]):
            closest_vowel_pos = i
            break

    if closest_vowel_pos == -1:
        return ''
    else:
        return word[closest_vowel_pos]