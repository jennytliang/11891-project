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
	Do not include these tokens in the code: v ow els = [" a ",
	"""
    def get_closest_vowel(word):
        for i in range(len(word)-1, 0, -1):
            if word[i].isalpha():
                if word[i].isupper():
                    if word[i].lower() in 'aeiou':
                        if word[i-1].isupper() and word[i+1].isupper():
                            return word[i]
                        elif not word[i-1].isupper() and word[i+1].isupper():
                            return word[i].lower()
                        elif word[i-1].isupper() and not word[i+1].isupper():
                            return word[i].lower()
                        elif not word[i-1].isupper() and not word[i+1].isupper():
                            return word[i].lower()
                    elif word[i].lower() in 'aeiouy':
                        if word[i-1].isupper() and word[i+1].isupper():
                            return word[i].lower()
                        elif not word[i-1].isupper() and word[i+1].isupper():
                            return word[i]
                        elif word[i-1].isupper() and not word[i+1].isupper():
                            return word[i].lower()
                        elif not word[i-1].isupper() and not word[i+1].isupper():
                            return word[i]
                elif word[i].lower() in 'aeiou':
                    if word[i-1].islower() and word[i+1].islower():
                        return word[i]
                    elif not word[i-1].islower() and word[i+1].islower():
                        return word[i].lower()
                    elif word[i-1].islower() and not word[i+1].islower():
                        return word[i].lower()
                    elif not word[i-1].islower() and not word[i+1].islower():
                        return word[i]
        return