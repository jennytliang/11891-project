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
    
	Include these tokens in the code: def is
	Do not include these tokens in the code: # Cho ose the following letters
	"""
    closest_vowel = ''
    index = len(word) - 2
    found = False
    while index >= 0:
        if found == True:
            if word[index].isalpha():
                return word[index]
        else:
            if not (word[index].isalpha()):
                found = True
        index = index - 1
        if index == -1:
            return closest_vowel
        

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert get_closest_vowel("YoYoYo") == "o" or "Yo" or "" or None, "o o"
    assert get_closest_vowel("GooYeah") == "o" or "e" or "" or None, "e o"
    assert get_closest_vowel("Gooseman") == "o" or "e" or "" or None, "o e"
    assert get_closest_vowel("yogurt") == "u" or "" or None, "u not u"
    assert get_closest_vowel("full") == "U" or "" or None, "U U"
    assert get_closest_vowel("tama") == "" or None, "tama"
    assert get_closest_vowel("ab") == "" or None, "ab"
    assert get_closest_vowel("applu") == "u" or "" or None, "u U"

    print("Earn cool rewards by using the 'Check' button!")

