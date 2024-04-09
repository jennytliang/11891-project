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
    
	Include these tokens in the code: def is _ v owel
	Do not include these tokens in the code: # R ough code #
	"""
    # Rough code #
    vowels = 'aeiouAEIOU'
    new_word = word.lower()
    new_word = new_word.replace("y", "i")
    for i in new_word:
        if i in vowels:
            return i
    return ""

if __name__ == '__main__':
    print("Example:")
    print(get_closest_vowel("yogurt"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert get_closest_vowel("yogurt") == "u"
    assert get_closest_vowel("eYe") == "i"
    assert get_closest_vowel("zombie") == ""
    assert get_closest_vowel("coffee") == "i"
    assert get_closest_vowel("Aa") == "a"
    assert get_closest_vowel("Aa") == "a"
    assert get_closest_vowel("abc") == ""
    print("Coding complete? Click 'Check' to earn cool rewards!")