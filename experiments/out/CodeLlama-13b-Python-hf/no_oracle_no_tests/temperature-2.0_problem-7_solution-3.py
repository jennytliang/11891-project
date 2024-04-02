from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring
    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    """
    return [string for string in strings if substring in string]


if __name__ == "__main__":
    import doctest
    doctest.testmod()




import numpy as np

def is_floats(x) -> bool:
    # check if it is float; List[float]; Tuple[float]
    if isinstance(x, float):
        return True
    if isinstance(x, (list, tuple)):
        return all(isinstance(i, float) for i in x)
    if isinstance(x, np.ndarray):
        return x.dtype == np.float64 or x.dtype == np.float32
    return False


def assertion(out, exp, atol):
    exact_match = out == exp

    if atol == 0 and is_floats(exp):
        atol = 1e-6
    if not exact_match and atol != 0:
        np.testing.assert_allclose(out, exp, atol=atol)
    else:
        assert exact_match


def check(candidate):
    inputs = [[[], 'john'], [['xxx', 'asd', 'xxy', 'john doe', 'xxxAAA', 'xxx'], 'xxx'], [['xxx', 'asd', 'aaaxxy', 'john doe', 'xxxAAA', 'xxx'], 'xx'], [['grunt', 'trumpet', 'prune', 'gruesome'], 'run'], [['banana', 'apple', 'kiwi', 'peach'], 'a'], [['hello', 'world', 'python', 'numpy', 'pandas'], 'py'], [[], ''], [['abc', 'bcd', 'cbd', 'dbc', 'cda'], 'bc'], [['a', 'ab', 'abc', 'abcd', 'abcde', 'bcde', 'cde'], 'cd'], [['123', '456', '789', '101112'], '12'], [['cat', 'dog', 'elephant', 'rhinoceros', 'seagull'], 'e'], [['supercalifragilisticexpialidocious', 'antidisestablishmentarianism', 'floccinaucinihilipilification'], 'ili'], [['moon', 'stars', 'sun', 'planets'], 's'], [['earth', 'mars', 'jupiter', 'saturn', 'uranus'], 's'], [['hello', 'world', 'python', 'numpy', 'pandas', 'numpy'], 'py'], [['supercalifragilisticexpialidocious', 'antidisestablishmentarianism', 'floccinaucinihilipilification', 'floccinaucinihilipilificatnion'], 'ili'], [['hello', 'world', 'python', 'numpy', 'pandas'], 'antidisestablishmentarianismpy'], [['supercalifragilisticexpialidocious', 'antidisestablishmentarianism', 'floccinaucinihilipilification', 'floccinaucinihilipilificatnion'], 'ili12'], [['supercalifragilisticexpialidocious', 'antidisesshmentarianism', 'floccinaucinihilipilification', 'floccinaucinihilipilificatnion', 'floccinaucinihilipilificatilinion'], 'ili'], [['supercalifragilisticexpialidocious', 'sun', 'floccinaucinihilipilificatioearthn'], 'ili'], [['123', '456', '789', '101112'], '122'], [['supercalifragilisticexpialidocious', 'antidisestablishementarianism', 'floccinaucinihilipilification'], 'ili'], [['abc', 'bcd', 'cbd', 'dbc', 'cda', 'cfloccinaucinihilipilificatilinionda'], 'bc'], [['earth', 'mars', 'jupiter', 'saturn', 'uranus'], 'numpuranusys'], [['supercalifragilisticexpialidocious', 'antidisestablishementarianism', 'floccinaucinihilipilification', 'supercalifragilisticexpialidocious'], 'ili'], [['hello', 'world', 'python', 'numpy', 'pandas'], 'antidisestablishmentariasaturnnismpy'], [['supercalifragilisticexpialidocious', 'antidisesshmentarianism', 'floccinaucinihilipilification', 'floccinaucinihilipilificatnion', 'floccinaucinihilipilificatilinion', 'floccinaucinihilipilifi101112cation'], 'ili'], [['supercalifragilisticexpialidocious', 'antidisestablishmentarianism', 'floccinaucinihilipilification', 'floccinaucinihilipilificatnion'], 'floccinaucinihilipilificatioearthn'], [['hello', 'world', 'python', 'numpy', 's'], 'antidisestablishmentariasaturnnismpy'], [['hello', 'world', 'python', 'numpy'], 'antidisestablishmentarianismpy'], [['antidisesshmentarianism', 'floccinaucinihilipilification', 'floccinaucinihilipilificatnion', 'floccinaucinihilipilificatilinion'], 'ili'], [['hello', 'world', 'python', 'numpy', 'pandas', 'numpy'], 'antidisestablishmentarianismpy'], [['abc', 'bcd', 'cbd', 'dbc', 'cda', 'cfloccinaucinihilipilificatilinionda', 'dcbd'], 'bbc'], [['abc', 'bcd', 'cbd', 'dbc', 'cda', 'cfloccinaucinihilipilificatilinionda', 'dcbd', 'cfloaccinaucinihilipilificatilinionda'], 'bbc'], [['123', '456', '789', '101112', '456'], '12'], [['Washington', 'DC', 'New York City', 'Boston', 'Los Angeles', 'San Francisco', 'Miami'], 'an'], [['The quick brown fox jumps over the lazy dog', 'Pack my box with five dozen liquor jugs', 'How vexingly quick daft zebras jump', 'Jackdaws love my big sphinx of quartz'], 'ox'], [['The cat in the hat', 'Green eggs and ham', 'One fish two fish', 'Red fish blue fish'], 'fish'], [['The Shawshank Redemption', 'The Godfather', 'The Dark Knight', 'The Lord of the Rings', 'Star Wars', 'Inception', 'Forrest Gump'], 'he'], [['We the people of the United States of America, in order to form a more perfect union, establish justice, insure domestic tranquility, provide for the common defense, promote the general welfare, and secure the blessings of liberty to ourselves and our posterity, do ordain and establish this Constitution for the United States of America.', 'To be or not to be, that is the question.', 'It is a truth universally acknowledged, that a single man in possession of a good fortune, must be in want of a wife.', 'I have a dream that one day this nation will rise up and live out the true meaning of its creed: "We hold these truths to be self-evident, that all men are created equal."', 'Four score and seven years ago our fathers brought forth on this continent, a new nation, conceived in Liberty, and dedicated to the proposition that all men are created equal.'], 'equal.'], [['abcdefg'], ''], [['abc(d)e', 'ba%cd', 'cde', 'array', '12345'], '(d)'], [['wsrefgtrh', 'zxyvtru', 'asxwaqzx', 'kjbncxz'], 'tr'], [['The Shawshank Redemption', ' The Godfather ', 'The Dark Knight', '  The Lord of the Rings   ', '   Star Wars', ' Inception     ', 'Forrest Gump'], ' '], [['The Shawshank Redemption', ' The Godfather ', 'The Dark Knight', '  The Lord of the Rings   ', '   Star Wars', ' Inception     ', 'Forrest Gump', ' Inception     '], ' '], [['Washington', 'DC', 'New York City', 'Boston', 'Los Angeles', 'San Francisco', 'Miami', 'Washington'], 'an'], [['Washington', 'DC', 'New York City', 'Boston', 'Los Angeles', 'San Francisco', 'Miami'], 'York'], [['The quick brown fox jumps over the lazy dog', 'Pack my box with five dozen liquor jugs', 'How vexingly quick daft zebras jump', 'Jackdaws love my big sphinx of quartz'], 'oConstitutionx'], [['The quick brown fox jumps over the lazy dog', 'Pack my box with five dozen liquor jugs', 'Jackdaws love my big sphinx of quartz'], 'created'], [['Pack my box with five dozen liquor jugs', 'Jackdaws love my big sphinx of quartz'], 'creeated'], [['abcdefg'], 'universally'], [['The quick brown fox jumps over the lazy dog', 'Pack my box with five dozen liquor jugs', 'Jackdaws love my big sphinx of quartz'], 'creataed'], [['We the people of the United States of America, in order to form a more perfect union, establish justice, insure domestic tranquility, provide for the common defense, promote the general welfare, and secure the blessings of liberty to ourselves and our posterity, do ordain and establish this Constitution for the United States of America.', 'To be or not to be, that is the question.', 'It is a truth universally acknowledged, that a single man in possession of a good fortune, must be in want of a wife.', 'I have a dream that one day this nation will rise up and live out the true meaning of its creed: "We hold these truths to be self-evident, that all men are created equal."', 'Four score and seven years ago our fathers brought forth on this continent, a new nation, conceived in Liberty, and dedicated to the proposition that all men are created equal.', 'I have a dream that one day this nation will rise up and live out the true meaning of its creed: "We hold these truths to be self-evident, that all men are created equal."'], 'equal.'], [['We the people of the United States of America, in order to form a more perfect union, establish justice, insure domestic tranquility, provide for the common defense, promote the general welfare, and secure the blessings of liberty to ourselves and our posterity, do ordain and establish this Constitution for the United States of America.', 'To be or not to be, that is the question.', 'It is a truth universally acknowledged, that a single man in possession of a good fortune, must be in want of a wife.', 'I have a dream that one day this nation will rise up and live out the true meaning of its creed: "We hold these truths to be self-evident, that all men are created equal."', 'Four score and seven years ago our fathers brought forth on this continent, a new nation, conceived in Liberty, and dedicated to the proposition that all men are created equal.'], 'ordain'], [['abcdefg', 'abcdefg'], 'universally'], [['Washington', 'New York City', 'Boston', 'Los Angeles', 'San Francisco', 'Miami', 'Washington'], 'nan'], [['Washington', 'Boston', 'Los Angeles', 'San Francisco', 'Miami', 'Washington'], 'nan'], [['Washington', 'The cat in the hat', 'New York City', 'Boston', 'Los Angeles', 'San Francisco', 'Miami', 'Washington'], 'nation,'], [['Washington', 'New York City', 'Boston', 'Los Angeles', 'San Francisco', 'Miami', 'Washington'], 'nabc(d)e'], [['abcdeits'], 'universally'], [['We the people of the United States of America, in order to form a more perfect union, establish justice, insure domestic tranquility, provide for the common defense, promote the general welfare, and secure the blessings of liberty to ourselves and our posterity, do ordain and establish this Constitution for the United States of America.', 'To be or not to be, that is the question.', 'It is a truth universally acknowledged, that a single man in possession of a good fortune, must be in want of a wife.', 'I have a dream that one day this nation will rise up and live out the true meaning of its creed: "We hold these truths to be self-evident, that all men are created equal."', 'Four score and seven years ago our fathers brought forth on this continent, a new nation, conceived in Liberty, and dedicated to the proposition that all men are created equal.'], 'equ'], [['abcdefg', 'abcdefg'], 'upromoteniversally'], [['The cat in the hat', 'Green eggs and ham', 'One fish two fish', 'Red fish blue fish'], 'ffis'], [['Washington', 'New York City', 'Los Angeles', 'San Francisco', 'Miami', 'Washington'], 'nabc(d)e'], [['abcdefg', 'abcdefg', 'abcdefg'], 'universally'], [['The quick brown fox jumps over the lazy dog', 'Pack my box with five dozen liquor jugs', 'How vexingly quick daft zebras jump', 'Jackdaws love my big sphinx of quartz'], 'oConstituti'], [['Washington', 'New York Ciity', 'The cat in the hat', 'New York City', 'Boston', 'Los Angeles', 'Miami', 'Washington'], 'nation,'], [['Pack my box with five dozen liqugor jugs', 'The quick brown fox jumps ove  zy dog', 'The quick brown fox jumps over the lazy dog', 'Pack my box with five dozen liquor jugs', 'Jackdaws love my big sphinx of quartz'], 'created'], [['Washington', 'New York City', 'Boston', 'Los Angeles', 'San Francisco', 'Miami', 'Washington'], 'want'], [['The quick brown fox jumps over the lazy dog', 'Pack my box with five dozen liquor jugs', 'Pack my box with five dozen lisevenquor jugs', 'How vexingly quick daft zebras jump', 'Jackdaws love my big sphinx of quartz'], 'ox'], [['The q uick brown fox jumps over the lazy dog', 'Pack my box with five dozen liquor jugs', 'How vexingly quick daft zebras jump', 'Jackdaws love my big sphinx of quartz'], 'oConstitutionx'], [['The quick brown fox jumps over the lazy dog', 'San Francisco', 'Pack my box with five dozen liquor jugs', 'How vexingly quick daft zebras jump', 'Jackdaws love my big sphinx of quartz'], 'oConstitutionx'], [[], 'It is a truth universally acknowledged, that a single man in possession of a good fortune, must be in want of a wife.'], [['The quick brown fox jumps over the lazy dog', 'Pack my box with five dozen liquor jugs', 'Pack my box with five dozen lisevenquor jugs', 'forth', 'Jackdaws love my big sphinx of quartz'], 'ox'], [['Washington', 'New York City', 'Los Angeles', 'San Francisco', 'zebras', 'Washington'], 'nabc(d)e'], [['We the people of the United States of America, in order to form a more perfect union, establish justice, insure domestic tranquility, provide for the common defense, promote the general welfare, and secure the blessings of liberty to ourselves and our posterity, do ordain and establish this Constitution for the United States of America.', 'To be or not to be, that is the question.', 'It is a truth universally acknowledged, that a single man in possession of a good fortune, must be in want of a wife.', 'I have a dream that one day this nation will rise up and live out the true meaning of its creed: "We hold these truths to be self-evident, that all men are created equal."', 'Four score and seven years ago our fathers brought forth on this continent, a new nation, conceived in Liberty, and dedicated to the proposition that all men are created equal.', 'I have a dream that one day this nation will rise up and live out the true meaning of its creed: "We hold these truths to be self-evident, that all men are created equal."'], 'eaqual.'], [[], 'universally'], [['Washington', 'New York City', 'Boston', 'Los Angeles', 'San Francisco', 'Miami', 'Washington', 'Miami'], 'want'], [['Washington', 'New York City', 'Boston', 'Los Angeles', 'San Francisco', 'Miami', 'Washington'], 'New York Citywant'], [[], 'Star'], [['The Shawshank Redemption', 'The Godfather', 'The Dark Knight', 'The Lord of the Rings', 'Star Wars', 'Inception', 'universally'], 'he'], [['Washington', 'cRedemptionread', 'New York City', 'Boston', 'Los Angeles', 'San Francisco', 'Miami', 'Washington'], 'nation,'], [['abcgdefg', 'aasxwaqzxbcdefg', 'want', 'abcdefg', 'abcdefg', 'abcdefg'], 'universally'], [['Washington', 'New York City', 'Boston', 'Los Angeles', 'San Francisco', 'Miami', 'Washington'], 'New York Citywan'], [['Washington', 'New York City', 'nWashington', 'Los Angeles', 'San Francisco', 'zebras', 'Washington'], 'nabc(d)e'], [['abcdeits'], 'fortune,'], [['B"Weoston', 'Washington', 'DC', 'New York City', 'Boston', 'Los Angeles', 'San Francisco', 'Miami'], 'York'], [['abcgdefg', 'aasxwaqzxbcdefg', 'want', 'abcdefg', 'abcdefg', 'abcdefg'], 'box'], [['peoplbige', 'abcdefg', 'abcdefg'], 'universally'], [['We the people of the United States of America, in order to form a more perfect union, establish justice, insure domestic tranquility, provide for the common defense, promote the general welfare, and secure the blessings of liberty to ourselves and our posterity, do ordain and establish this Constitution for the United States of America.', 'To be or not to be, that is the question.', 'It is a truth universally acknowledged, that a single man in possession of a good fortune, must be in want of a wife.', 'I have a dream that one day this nation will rise up and live out the true meaning of its creed: "We hold these truths to be self-evident, that all men are created equal."', 'Four score and seven years ago our fathers brought forth on this continent, a new nation, conceived in Liberty, and dedicated to the proposition that all men are created equal.'], 'for'], [['Pack my box with five dozen liqugor jugs', 'The quick brown fkjbncxzox jumps ove  zy dog', 'The quick brown fox jumps over the lazy dog', 'Pack my box with five dozen liquor jugs', 'Jackdaws love my big sphinx of quartz', 'Jackdaws love my big sphinx of quartz'], 'createdd'], [['We the people of the United States of America, in order to form a more perfect union, establish justice, insure domestic tranquility, provide for the common defense, promote the general welfare, and secure the blessings of liberty to ourselves and our posterity, do ordain and establish this Constitution for the United States of America.', 'To be or not to be, that is the question.', 'It is a truth universally acknowledged, that a single man in possession of a good fortune, must be in want of a wife.', 'I have a dream that one day this nation will rise up and live out the true meaning of its creed: "We hold these truths to be self-evident, that all men are created equal."', 'Four score and seven years ago our fathers brought forth on this continent, a new nation, conceived in Liberty, and dedicated to the proposition that all men are created equal.'], 'Citywan'], [['The Shawshank Redemption', ' The Godfather ', 'The Dark Knight', '  The Lord of the Rings   ', '   Star Wars', ' Inception     ', 'Forrest Gump'], 'nation'], [['Washington', 'DC', 'New York City', 'ton', 'Boston', 'Los Angeles', 'San Francisco', 'Miami'], 'York'], [['The quick brown fox jumps over the lazy dog', 'Pack my box with five dozen liquor jugs', 'Jackdaws love my big sphinx of quartz'], 'tthese'], [['The quick brown fox jumps over the lazy dog', 'San Francisco', 'Pack my box with five dozen liquor jugs', 'How vexingly quick daft zebras jump', 'Jackdaws love my big sphinx of quartz'], 'oConstitStar Warsutionx'], [['Washington', 'New York City', 'Los Angeles', 'San Francisco', 'Miami', 'Washington'], 'nab(((The Dark Knightdthese)cc(d)e'], [['Washington', 'New York City', 'San Francisco', 'Miami', 'New York Cicreateddty', 'Washington', 'New York Cicreateddty'], 'nabc(d)e'], [['Washington', 'MMiami', 'New York City', 'San Francisco', 'Miami', 'New York Cicreateddty', 'Washington', 'New York Cicreateddty'], 'nabc(d)e'], [['an', 'abcdeits'], 'universally'], [['The Shawshank Redemption', ' The Godfather ', 'The Dark Knight', '  The Lord of the Rings   ', '   Star Wars', ' Inception     ', 'Forrest Gump'], ' l.'], [['We the people of the United States of America, in order to form a more perfect union, establish justice, insure domestic tranquility, provide for the common defense, promote the general welfare, and secure the blessings of liberty to ourselves and our posterity, do ordain and establish this Constitution for the United States oef America.', 'To be or not to be, that is the question.', 'It is a truth universally acknowledged, that a single man in possession of a good fortune, must be in want of a wife.', 'I have a dream that one day this nation will rise up and live out the true meaning of its creed: "We hold these truths to be self-evident, that all men are created equal."', 'Four score and seven years ago our fathers brought forth on this continent, a new nation, conceived in Liberty, and dedicated to the proposition that all men are created equal.'], 'City'], [['th'], '(((The Dark Knightdtmeaninghese)'], [['abcdefg', 'abcdefg', 'abcdefg'], 'univerhavely'], [['We the people of the United States of America, in order to form a more perfect union, establish justice, insure domestic tranquility, provide for the common defense, promote the general welfare, and secure the blessings of liberty to ourselves and our posterity, do ordain and establish this Constitution for the United States of America.', 'To be or not to be, that is the question.', 'It is a truth universally acknowledged, that a single man in possession of a good fortune, must be in want of a wife.', 'I have a dream that one day this nation will rise up and live out the true meaning of its creed: "We hold these truths to be self-evident, that all men are created equal."', 'Four score and seven years ago our fathers brought forth on this continent, a new nation, conceived in Liberty, and dedicated to the proposition that all men are created equal.', 'I have a dream that one day this nation will rise up and live out the true meaning of its creed: "We hold these truths to be self-evident, that all men are created equal."'], 'Star Wars'], [['daft', 'UEZ', '(((The Dark Knightdthese)', 'of', 'New York Ciitypcerfefct'], 'RRed fish blue fish'], [['Pack my box with five dozen liqugor jugs', 'The quick brown fkjbncxzox jumps ove  zy dog', 'The quick brown fox jumps over the lazy dog', 'Pack my box with five dozen liquor jugs', 'Jackdaws love my big sphinx of quartz'], 'The quick b over the lazy dog'], [['The quick brown fox jumps ove  zy dog', 'The quick brown fox jumps over the lazy dog', 'Pack my box with five dozen liquor jugs', 'Jackdaws love my big sphinx of quartz', 'The quick brown fox jumps ove  zy dog'], 'oxx'], [['We the people of the United States of America, in order to form a more perfect union, establish justice, insure domestic tranquility, provide for the common defense, promote the general welfare, and secure the blessings of liberty to ourselves and our posterity, do ordain and establish this Constitution for the United States of America.', 'To be or not to be, that is the question.', 'It is a truth universally acknowledged, that a single man in possession of a good fortune, must be in want of a wife.', 'I have a dream that one day this nation will rise up and live out the true meaning of its creed: "We hold these truths to be self-evident, that all men are created equal."', 'Four score and seven years ago our fathers brought forth on this continent, a new nation, conceived in Liberty, and dedicated to the proposition that all men are created equal.', 'To be or not to be, that is the question.'], 'ordain'], [['Washington', 'New York City', 'Boston', 'Los Angeles', 'San Francisco', 'Miami', 'Washington', 'Miami'], 'daft'], [['Pack my box with five dozen liqugor jugs', 'The quick brown fox jumps ove  zy dog', 'The quick brown fox jumps over the lazy dog', 'Pack my box with five dozen liquor jugs', 'Redemption'], 'created'], [['Washington', 'Boston', 'Los Angeles', 'San Francisco', 'Miami', 'Washington'], 'nann'], [['The quick brown fox jumps over the lazy dog', 'Pack my box with five dozen liquor jugs', 'Jackdaws love my big sphinx of quartz', 'Pack my box with five dozen liquor jugs'], 'createt'], [['Washington', 'MMiami', 'New York City', 'San Francisco', 'Miami', 'New York Cicreateddty', 'Washington', 'New York Cicreateddty'], 'nabc)e'], [['The Shawshank Redemption', 'The Godfather', 'The Lord of the Rings', 'Star Wars', 'Inception', 'Forrest Gump'], 'he'], [['The quick brown fox jumps over the lazy dog', 'Pack my box with five dozen liquor jugs', 'Pack my box with five dozen lisevenquor jugs', 'How vexingly quick daft zebras jump', 'Jackdaws love my big sphinx of quartz'], 'quiickox'], [['The quick brown fox jumps over the lazy dog', 'Pack my box with five dozen liquor jugs', 'Jackdaws love my big sphinx of quartz'], 'propmtr'], [['The quick brown fox jumps over tPacFour score and seven years ago our fathers brought forth on this continent, a new nation, conceived in Liberty, and dedicated to the proposition that all men are crzyeated equal.he lazy dog', 'San Francisco', 'Pack my box with five dozen liquor jugs', 'How vexingly quick daft zebras jump', 'Jackdaws love my big sphinx of quartz'], 'oConstittutionx'], [['Thee quick brown fox jumps ove  zy dog', 'The quick brown fox jumps over the lazy dog', 'Pack my box with five dozen liquor jugs', 'Jackdaws love my big sphinx of quartz', 'The quick brown fox jumps ove  zy dog'], 'oxxNew York Citywan'], [[], 'abc'], [[], 'substring'], [['', '', ''], 'substring'], [['substring', 'substring', 'substring'], 'substring'], [['string', 'bingo', 'frost', 'parka'], 'substring'], [['', '', ''], ''], [['', 'a', '', 'b'], ''], [[''], ''], [['abc', 'bcd', 'cde', 'def'], 'a'], [['The Godfather', 'The Dark Knight', 'The Lord of the Rings', 'Star Wars', 'posterity,', 'Forrest Gump'], 'he'], [['abcdefg'], 'form'], [[], 'Green'], [['The quick brown fox jumps over the lazy dog', 'Pack my box with five dozen liquor jugs', 'How vexingly quick daft zebras jump', 'Jackdaws love my big sphinx of quartz'], 'tranquility,ox'], [['abcdefg'], 'fom'], [['Washington', 'DC', 'New York City', 'Boston', 'Los Angeles', 'San Francisco', 'Miami'], 'liberty'], [['The Godfather', 'The Dark Knight', 'The Lord of the Rings', 'union,', 'posterity,', 'Forrest Gump', 'union,'], 'h'], [['abcdefg', 'abcdefg'], 'm'], [['fom', 'abcdefg'], 'fom'], [['We the people of the United States of America, in order to form a more perfect union, establish justice, insure domestic tranquility, provide for the common defense, promote the general welfare, and secure the blessings of liberty to ourselves and our posterity, do ordain and establish this Constitution for the United States of America.', 'To be or not to be, that is the question.', 'It is a truth universally acknowledged, that a single man in possession of a good fortune, must be in want of a wife.', 'I have a dream that one day this nation will rise up and live out the true meaning of its creed: "We hold these truths to be self-evident, that all men are created equal."', 'Four score and seven years ago our fathers brought forth on this continent, a new nation, conceived in Liberty, and dedicated to the proposition that all men are created equal.'], 'eqal.'], [['abcdbefg'], 'form'], [['abbcdefg', 'fom', 'abcdefg'], 'fom'], [['The Shawshank Redemption', 'The Godfather', 'The Dark Knight', 'Star Wars', 'Inception', 'Forrest Gump'], 'he'], [['Washington', 'DC', 'New York City', 'Boston', 'Los Angeles', 'San Francisco', 'Miami'], 'libertequal.y'], [['The Shawshank Redemption', ' The Godfather ', 'The Dark Knight', '  The Lord of the Rings   ', '   Star Wars', ' Inception     ', 'Forrest Gump'], 'Angeles'], [['Washington', 'DC', 'New York City', 'Boston', 'Los Angeles', 'San Francisco', 'Miami', 'New York City'], 'an'], [['The Godfather', 'The Dark Knight', 'The Lord of the Rings', 'Star Wars', 'posterity,', 'Forrest Gump'], 'h'], [['Washington', 'DC', 'New York City', 'Boston', 'San Francisco', 'Miami'], 'libertequal.y'], [['abcdefg'], 'fofm'], [['Washington', 'DC', 'New York City', 'Boston', 'Los Angeles', 'San Francisco', 'Miami', 'New York City'], 'aan'], [['The Shawshank Redemption', 'The Godfather', 'The Dark Knight', 'Star Wars', 'Inception', 'Forrest Gump'], 'hhe'], [['abbcdefg', 'fom', 'abcdefg', 'abbcdefg'], 'fom'], [['abcdefg', 'abcdefg'], 'To be or not to be, that is the question.'], [['The Godfatosacknowlledged,phinxxher', 'The Dark Knight', 'The Lord of the Rings', 'union,', 'tranquility,oxunion,', 'posterity,', 'Forrest Gump', 'union,'], 'h'], [['osafortune,cknowlledged,p', 'abcdefg', 'abcdefg'], 'fom'], [['The Shawshank Redemption', 'The Godfather', 'justice,The Dark Knight', 'The Lord of the Rings', 'and', 'Inception', 'Forrest Gump'], 'he'], [['abc(d)e', 'ba%cd', 'cde', 'array', '12345'], 'dozen'], [['The Godfather', 'The Dark Knight', 'DCt', 'The Lord of the Rings', 'union,', 'posterity,', 'Forrest Gump', 'union,'], 'h'], [['osafortune,cknowlledged,p', 'abcdefg'], 'fom'], [['wsrefgtrh', 'zxyvtru', 'asxwaqzx', 'zxyvtConstitutionru', 'kjbncxz'], 'tr'], [['kQEHdzw', 'for', 'asxwaqzx', '  The Lord of the Rings   ', 'Mi', 'its', 'kZWuN'], 'Green'], [['abc(d)e', 'ba%cd', 'cde', 'array', '12345', '12345'], 'Saabc(d)en'], [['abc(d)e', 'ba%cd', 'cde', 'array', 'dog'], 'doquartuzzen'], [['The Shawshank Redemption', 'The Godfather', 'justice,The Dark Knight', 'The Lord of the Rings', 'and', 'Inception', 'Forrest Gump'], 'hhate'], [['Washinestablishon', 'DC', 'New York City', 'Boston', 'Los Angeles', 'San Francisco', 'Miami', 'New York City'], 'an'], [['abcdefg'], 'rtr'], [['The Dark Knight', 'The Lord of the Rings', 'union,', 'posterity,', 'Forrest Gump', 'union,'], 'h'], [['The Godfatosacknowlledged,phinxxher', 'The Dark Knight', 'The Lord of the Rings', 'union,', 'tranquility,oxunion,', 'posterity,', 'Forrest Gump', 'union,'], 'ourselvesh'], [['Washinestablishon', 'DC', 'New York City', 'Boston', 'Los Angeles', 'San Francisco', 'Miami', 'New York City'], 'aan'], [['We the people of the United States of America, in order to form a more perfect union, establish justice, insure domestic tranquility, provide for the common defense, promote the general welfare, and secure the blessings of liberty to ourselves and our posterity, do ordain and establish this Constitution for the United States of America.', 'To be or not to be, that is the question.', 'It is a truth universally acknowledged, that a single man in possession of a good fortune, must be in want of a wife.', 'I have a dream that one day this nation will rise up and live out the true meaning of its creed: "We hold these truths to be self-evident, that all men are created equal."', 'Four score and seven years ago our fathers brought forth on this continent, a new nation, conceived in Liberty, and dedicated to the proposition that all men are created equal.'], 'eqal.osacknsowlledged,phinxx'], [['Washinestablishon', 'DC', 'New York City', 'Boston', 'Los Angeles', 'San Francisco', 'Miami', 'DCC', 'New York City'], 'an'], [['fI have a dream that one day this nation will rise up and live out the true meaning of its creed: "We hold these truths to be self-evident, that all men are created equal."om', 'abcdefg'], 'fom'], [['We the people of the United States of America, in order to form a more perfect union, establish justice, insure domestic tranquility, provide for the common defense, promote the general welfare, and secure the blessings of liberty to ourselves and our posterity, do ordain and establish this Constitution for the United States of America.', 'To be or not to be, that is the question.', 'I have a dream that one day this nation will rise up and live out the true meaning of its creed: "We hold these truths to be self-evident, that all men are created equal."', 'Four score and seven years ago our fathers brought forth on this continent, a new nation, conceived in Liberty, and dedicated to the proposition that all men are created equal.'], 'eqal.'], [['Washington', 'DC', 'New York City', 'Boston', 'Los Angeles', 'San Francisco', 'Miami'], 'nan'], [['Washinestablishon', 'DC', 'New York City', 'Boston', 'Los Angeles', 'San Francisco', 'Miami', 'DCC', 'New York City'], 'Guoxxplibertequal.yan'], [[], 'form'], [['Washington', 'DC', 'New York City', 'Boston', 'Los Angeles', 'San Francisco', 'Miami'], 'tranquility,oxunion,doquartuzzen'], [['Washington', 'DC', 'New York CitYy', 'Boston', 'Los Angeles', 'San Francisco', 'Miami'], 'liberty'], [['abcdefg', 'abcdefg'], 'To be or not to be,  that is the question.'], [['The Godfather', 'The Dark Knight', 'The Lord of the Rings', 'union,', 'pyeathesersrity,', 'Forrest Gump', 'union,'], 'h'], [['The Shawshank Redemption', 'The Godfather', 'justice,The Dark Knight', 'The Lord of the Rings', 'and', 'Inception', 'Forrest Gump'], 'hhatethThe'], [['The Shawshank Redemption', 'To be or not to be, that is the quesetion. Godfather', 'The Godfather', 'justice,The Dark Knight', 'The Lord of the Rings', 'and', 'Inception', 'Forrest Gump'], 'hhatetmyhThe'], [['osafortune,cknowlledged,p', 'abcdefg', 'orm', 'abcdefg'], 'fom'], [['Washington', 'DC', 'New York City', 'Boston', 'Los Angeles', 'San Francisco', 'Miami'], 'tranquility,oxunion,doquartuzLoszen']]
    results = [[], ['xxx', 'xxxAAA', 'xxx'], ['xxx', 'aaaxxy', 'xxxAAA', 'xxx'], ['grunt', 'prune'], ['banana', 'apple', 'peach'], ['python', 'numpy'], [], ['abc', 'bcd', 'dbc'], ['abcd', 'abcde', 'bcde', 'cde'], ['123', '101112'], ['elephant', 'rhinoceros', 'seagull'], ['supercalifragilisticexpialidocious', 'floccinaucinihilipilification'], ['stars', 'sun', 'planets'], ['mars', 'saturn', 'uranus'], ['python', 'numpy', 'numpy'], ['supercalifragilisticexpialidocious', 'floccinaucinihilipilification', 'floccinaucinihilipilificatnion'], [], [], ['supercalifragilisticexpialidocious', 'floccinaucinihilipilification', 'floccinaucinihilipilificatnion', 'floccinaucinihilipilificatilinion'], ['supercalifragilisticexpialidocious', 'floccinaucinihilipilificatioearthn'], [], ['supercalifragilisticexpialidocious', 'floccinaucinihilipilification'], ['abc', 'bcd', 'dbc'], [], ['supercalifragilisticexpialidocious', 'floccinaucinihilipilification', 'supercalifragilisticexpialidocious'], [], ['supercalifragilisticexpialidocious', 'floccinaucinihilipilification', 'floccinaucinihilipilificatnion', 'floccinaucinihilipilificatilinion', 'floccinaucinihilipilifi101112cation'], [], [], [], ['floccinaucinihilipilification', 'floccinaucinihilipilificatnion', 'floccinaucinihilipilificatilinion'], [], [], [], ['123', '101112'], ['San Francisco'], ['The quick brown fox jumps over the lazy dog', 'Pack my box with five dozen liquor jugs'], ['One fish two fish', 'Red fish blue fish'], ['The Shawshank Redemption', 'The Godfather', 'The Dark Knight', 'The Lord of the Rings'], ['I have a dream that one day this nation will rise up and live out the true meaning of its creed: "We hold these truths to be self-evident, that all men are created equal."', 'Four score and seven years ago our fathers brought forth on this continent, a new nation, conceived in Liberty, and dedicated to the proposition that all men are created equal.'], ['abcdefg'], ['abc(d)e'], ['wsrefgtrh', 'zxyvtru'], ['The Shawshank Redemption', ' The Godfather ', 'The Dark Knight', '  The Lord of the Rings   ', '   Star Wars', ' Inception     ', 'Forrest Gump'], ['The Shawshank Redemption', ' The Godfather ', 'The Dark Knight', '  The Lord of the Rings   ', '   Star Wars', ' Inception     ', 'Forrest Gump', ' Inception     '], ['San Francisco'], ['New York City'], [], [], [], [], [], ['I have a dream that one day this nation will rise up and live out the true meaning of its creed: "We hold these truths to be self-evident, that all men are created equal."', 'Four score and seven years ago our fathers brought forth on this continent, a new nation, conceived in Liberty, and dedicated to the proposition that all men are created equal.', 'I have a dream that one day this nation will rise up and live out the true meaning of its creed: "We hold these truths to be self-evident, that all men are created equal."'], ['We the people of the United States of America, in order to form a more perfect union, establish justice, insure domestic tranquility, provide for the common defense, promote the general welfare, and secure the blessings of liberty to ourselves and our posterity, do ordain and establish this Constitution for the United States of America.'], [], [], [], [], [], [], ['I have a dream that one day this nation will rise up and live out the true meaning of its creed: "We hold these truths to be self-evident, that all men are created equal."', 'Four score and seven years ago our fathers brought forth on this continent, a new nation, conceived in Liberty, and dedicated to the proposition that all men are created equal.'], [], [], [], [], [], [], [], [], ['The quick brown fox jumps over the lazy dog', 'Pack my box with five dozen liquor jugs', 'Pack my box with five dozen lisevenquor jugs'], [], [], [], ['The quick brown fox jumps over the lazy dog', 'Pack my box with five dozen liquor jugs', 'Pack my box with five dozen lisevenquor jugs'], [], [], [], [], [], [], ['The Shawshank Redemption', 'The Godfather', 'The Dark Knight', 'The Lord of the Rings'], [], [], [], [], [], ['New York City'], [], [], ['We the people of the United States of America, in order to form a more perfect union, establish justice, insure domestic tranquility, provide for the common defense, promote the general welfare, and secure the blessings of liberty to ourselves and our posterity, do ordain and establish this Constitution for the United States of America.', 'It is a truth universally acknowledged, that a single man in possession of a good fortune, must be in want of a wife.', 'Four score and seven years ago our fathers brought forth on this continent, a new nation, conceived in Liberty, and dedicated to the proposition that all men are created equal.'], [], [], [], ['New York City'], [], [], [], [], [], [], [], [], [], [], [], [], [], [], ['We the people of the United States of America, in order to form a more perfect union, establish justice, insure domestic tranquility, provide for the common defense, promote the general welfare, and secure the blessings of liberty to ourselves and our posterity, do ordain and establish this Constitution for the United States of America.'], [], [], [], [], [], ['The Shawshank Redemption', 'The Godfather', 'The Lord of the Rings'], [], [], [], [], [], [], [], ['substring', 'substring', 'substring'], [], ['', '', ''], ['', 'a', '', 'b'], [''], ['abc'], ['The Godfather', 'The Dark Knight', 'The Lord of the Rings'], [], [], [], [], [], ['The Godfather', 'The Dark Knight', 'The Lord of the Rings'], [], ['fom'], [], [], ['fom'], ['The Shawshank Redemption', 'The Godfather', 'The Dark Knight'], [], [], ['San Francisco'], ['The Godfather', 'The Dark Knight', 'The Lord of the Rings'], [], [], [], [], ['fom'], [], ['The Godfatosacknowlledged,phinxxher', 'The Dark Knight', 'The Lord of the Rings'], [], ['The Shawshank Redemption', 'The Godfather', 'justice,The Dark Knight', 'The Lord of the Rings'], [], ['The Godfather', 'The Dark Knight', 'The Lord of the Rings'], [], ['wsrefgtrh', 'zxyvtru'], [], [], [], [], ['San Francisco'], [], ['The Dark Knight', 'The Lord of the Rings'], [], [], [], ['San Francisco'], [], [], [], [], [], [], [], [], ['The Godfather', 'The Dark Knight', 'The Lord of the Rings', 'pyeathesersrity,'], [], [], [], []]
    for i, (inp, exp) in enumerate(zip(inputs, results)):
        assertion(candidate(*inp), exp, 0)


check(filter_by_substring)