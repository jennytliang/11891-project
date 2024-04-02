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
    word = word.replace("Q", "U")
    word = word.replace("q", "u")
    # print(word)
    for i in range(len(word)-1, 0, -1):
        if word[i].isupper():
            if word[i].isalpha() and word[i].lower() in "aeiou":
                for j in range(i-1, 0, -1):
                    if word[j].isalpha() and word[j].lower() in "aeiou":
                        if word[j+1].isupper():
                            return word[j]
                        if word[j+1].islower():
                            return word[j].upper()
    return ""


if __name__ == '__main__':
    print(get_closest_vowel("yogurt"))
    print(get_closest_vowel("FULL"))
    print(get_closest_vowel("quick"))
    print(get_closest_vowel("ab"))
