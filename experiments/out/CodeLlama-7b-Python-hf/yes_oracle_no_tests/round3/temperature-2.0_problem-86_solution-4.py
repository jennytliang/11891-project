def anti_shuffle(s):
    """
    Write a function that takes a string and returns an ordered version of it.
    Ordered version of string, is a string where all words (separated by space)
    are replaced by a new word where all the characters arranged in
    ascending order based on ascii value.
    Note: You should keep the order of words and blank spaces in the sentence.

    For example:
    anti_shuffle('Hi') returns 'Hi'
    anti_shuffle('hello') returns 'ehllo'
    anti_shuffle('Hello World!!!') returns 'Hello !!!Wdlor'
    
	Include these tokens in the code: , key = lambda ch : ord ( ch ))
	Do not include these tokens in the code: )),
	"""


    words = s.split(" ")
    return " ".join(map(lambda x: "".join(so(sorted(x))), words))


def so(lst):
    return "".join(map(lambda x: chr(x), sorted(map(lambda y: ord(y), lst))))


if __name__ == '__main__':
    print("Example:")
    print(anti_shuffle('hello'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert anti_shuffle('hello') == 'ehllo'
    assert anti_shuffle('edabba') == 'aabbeD'
    assert anti_shuffle('a b c d e f g h i j k l m n o p q r s t u v w x y z') == 'abcdefghijklmnopqrstuvwxyz'
    assert anti_shuffle('This is a string with    several words') == 'disi      asw    yrs    neev    mbl    gtis'
    assert anti_shuffle('This is a string with    several words and spaces') == 'disi      asw    yrs    neev    sbl    gtis    apes'
    assert anti_shuffle('This is a string with    several words and spaces    and   punctuation, such asCommas andPeriods?') == 'disi      asw    yrs    neev    sbl    gtis    apes    adn    pnuctaion,    s,hcual    asCommas    andPeriods?'
    print("Coding complete? Click 'Check' to earn cool rewards!")
