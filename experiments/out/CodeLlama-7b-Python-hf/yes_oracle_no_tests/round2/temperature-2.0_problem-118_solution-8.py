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
    
	Include these tokens in the code: def is _ v owel ( ch : str )
	"""
    # RW 06/07/2020
    if len(word) <= 1:
        return ""
    vowels = "AEIOUaeiou"
    i = len(word) - 2
    while i >= 0:
        if word[i] in vowels:
            if (word[i+1] not in vowels) and (word[i+2] in vowels):
                return word[i]
        i -= 1
    return ""

def main():
    print(get_closest_vowel("yogurt")) # "u"
    print(get_closest_vowel("FULL")) # "U"
    print(get_closest_vowel("quick")) # ""
    print(get_closest_vowel("ab")) # ""

if __name__ == "__main__":
    main()
