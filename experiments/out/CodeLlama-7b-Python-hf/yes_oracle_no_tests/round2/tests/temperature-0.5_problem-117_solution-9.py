def select_words(s, n):
    """Given a string s and a natural number n, you have been tasked to implement 
    a function that returns a list of all words from string s that contain exactly 
    n consonants, in order these words appear in the string s.
    If the string s is empty then the function should return an empty list.
    Note: you may assume the input string contains only letters and spaces.
    Examples:
    select_words("Mary had a little lamb", 4) ==> ["little"]
    select_words("Mary had a little lamb", 3) ==> ["Mary", "lamb"]
    select_words("simple white space", 2) ==> []
    select_words("Hello world", 4) ==> ["world"]
    select_words("Uncle sam", 3) ==> ["Uncle"]
    
	Do not include these tokens in the code: # write your code here
	"""
    # write your code here
    pass
































































































































































































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
    inputs = [['Mary had a little lamb', 4], ['Mary had a little lamb', 3], ['simple white space', 2], ['Hello world', 4], ['Uncle sam', 3], ['', 4], ['a b c d e f', 1], ['apple banana cherry', 3], ['random words are fun to write', 5], ['the quick brown fox jumps over the lazy dog', 6], ['the cat in the hat', 2], ['jingle bells jingle bells jingle all the way', 8], ['Python is a popular programming language', 3], ['', 1], ['this is a test string with multiple words containing different numbers of consonants', 7], ['quack quack goes the duck', 2], ['ThE qUiCk BrOwN fOx JuMpS oVeR tHe LaZy DoG', 6], ['apple banana cherry', 6], ['random words are fun to write', 2], ['Python isp a popular programming language', 3], ['apple banana chernry', 3], ['random words are fun to write', 8], ['apple banana cherry', 2], ['', 2], ['apple banana cherry', 1], ['apple banana chethe cat in the hatrry', 6], ['the quick brown fox jumps over the lazy dog', 1], ['quack quack goes the duck', 1], ['the quick browan fox jumps over the lazy dog', 0], ['Python isp a popular programming languagePython is a popular progrmming language', 2], ['appna cherry', 2], ['the quick brown fox jumps og', 1], ['this is a test string with multiple words containing different numbers of consonants', 6], ['Python isp a popular programmia popular progrmming language', 2], ['jingle bells jingle bells jingle all the way', 2], ['apple banappna cherryana cherry', 2], ['apple banappna cherryana cherry', 1], ['apple banaapple banana chethe cat in the hatrryppna cherryana cherry', 8], ['Python isp a popular programmia popular progrmming language', 1], ['ThE qUiCk BrOwN fOx JuMpS oVeR tHe LaZy DoG', 5], ['Python isp a popular programming language', 0], ['Python isp a popular programmia popular progrmming language', 3], ['Python isp a popular mprogramming language', 7], ['apple banana cherapple banaapple banana chethe cat ine hatrryppna cherryana cherryry', 2], ['apple banana chernry', 1], ['apple banappna cherryana cherr', 1], ['the quick brown fox jumps over the lazy dog', 0], ['apple banana chethe cat in the hatrry', 3], ['this is a test sThE qUiCk BrOwN fOx JuMpS oVeR tHe LaZy DoGds containing different numbers of consonants', 7], ['Pythion isp a popular programmia popular progrmming language', 2], ['apple banana cherapple banaapple banana chethe cat ine hatrrypypna cherryana cherryry', 2], ['Python isp a popular program ming language', 3], ['apple banana cherapple banaapple banana chethe cat ine hatrrypypna cherryana chcerryry', 2], ['the quick browan fox jumps over the lazy dog', 2], ['Python isp a popular program ming language', 1], ['apple banaapple banana chethe cat in the hatrryppna cherryana cherry', 1], ['the quick brown fox jumps over the lazy dog', 8], ['eapple banana chernry', 8], ['apple banana cherry', 5], ['random words are fun to write', 9], ['Pythion isp a popular programmia popular progrmming language', 1], ['ThE qUiCk BrOwN fOx JuMpS oVPython isp a popular program ming languageeR tHe LaZy DoG', 5], ['this is a test s tring with multiple words containing different numbers of consonants', 5], ['Python isp a popular program ming language', 5], ['this is a test s tring with multiple words containing different numbers of consonants', 6], ['apple banana chernry', 6], ['apple banana cheraptple banaapple banana chethe cat ine hatrrypypna cherryana chcerryry', 2], ['apple banana cherPython isp a popular mprogramming languageapple banaapple banana chethe cat ine hatrrypypna cherryana cherryry', 2], ['Thapple banana cherPython isp a popular mprogramming languageapple banaapple banana chethe cat ine hatrrypypna cherryana cherryryE qUiCk BrOwN fOx JuMpS oVeR tHe LaZy DoG', 6], ['the quick browan fox jumps over the lazy dog', 7], ['the quic k brown fox jumps over the lazy dog', 8], ['apple banaapple banana chethe cat in the hatrryppna cherryana cherry', 5], ['the quick browan fox jgumps over the lazy dog', 3], ['aeppna cherry', 2], ['Python isp a popular program mithe quick browan fox jgumps over the lazy dogng language', 1], ['Python isp a popular program ming language', 0], ['the quick brown fox jumps over the laapanana chethe cat ine hatrrypypna cherryana chcerryryzy dog', 1], ['this is a test string with multiplePython isp a popular program ming language words containing different numbers of consonants', 1], ['ther quick browan fox jumps over the lazy dog', 0], ['the quick brown fox jumps over tvhe lazy dog', 0], ['apple banaThE qUiCk BrOwN fOx JuMpS oVPython isp a popular program ming languageeR tHe LaZy DoGna cherry', 1], ['eapple banana cher nry', 8], ['apple banappna cherryana cherry', 0], ['jingle bells jingle bellthe quick brown fox jumps over the lazy dog all the way', 2], ['this is a test sThE qUiCk BrOwN fOx JuMpS oVeR tHe LaZy DoGds containing different numbers of consonants', 6], ['apple banaapple apple banana cherrybanana chethe cat in the hatrryppna cherryana cherry', 1], ['apple banappna cherryanra cherry', 9], ['apple baanana chernry', 6], ['ThE qUiCk BrOwN fOx JuMpS oVeR tHe LaZy DoG', 9], ['Python isp a popular programming language', 9], ['ThE qUiCk BrOwN fOx JuMpS oVeR tHe LaZy DoGS oVeR tHe LaZy DoG', 6], ['jingle bells jingle bells jingle all the way', 3], ['ThE qUiCk BrOwN fOx JuMpS oVeR tHe LaZy DoG', 2], ['aeppnac cherry', 0], ['jingle bells jingle bells jingle all t he way', 2], ['the quick browan fox jPython isp a popular program mithe qugick browan fox jgumps over the lazy dogng languageumps over the lazy dog', 0], ['Pythapple banappna cherryana cherron isp a popular mprogramming language', 7], ['Python isp a popular programming language', 2], ['Python isp a popular programminPython isp a popular programming languagePython is a popular progrmming languageg language', 0], ['apple banaapple apple banana cherrybanana chethe cat in the hatrryppna cherryana cherry', 6], ['ThE qUiCk BrOwN fOx JuMpS oVPython isp a popular program ming languageeR tHe LaZy DoG', 6], ['the quick browan fox jPython isp a popular program mithe qugick browan fox jgumps over the lazy dogng languageumps over the lazy dog', 1], ['the quick brown fox jumps  og', 1], ['the quick brown fox jumps over tvhe lazy dog', 1], ['eapple banana chernry', 7], ['Python isp a popular programminPython isp a populathis is a test string with multiplePython isp a popular program ming language words containing different numbers of consonants programming  languagePython is a popular progrmming languageg language', 0], ['random words are funy to wrPython isp a popular programming languageite', 5], ['', 5], ['aaa eee iii ooo uuu', 3], ['The quick brown fox jumped over the lazy dog', 6], ['The quick brown fox jumped over the lazy dog', 3], ['The Quick brown fox jUmPed over the lAzY dog', 5], ['ABCDEFGH', 0], ['Mississippi River', 4], ['ab cd ef gh ij', 2], ['the quick brown fox', 3], ['Qwertyuiopasdfghjklzxcvbnm', 10], ['The', 5], ['The Quick brown fox jUmPed over the lAzY dog', 2], ['Qwertyuiopasdfghjklzxcvbnm', 3], ['brown', 4], ['bwrown', 5], ['Thee Quick brown fox jUmPed over the lAzY dog', 2], ['The Quick brown fox jUmPed over the lAzY dog', 4], ['the quick brown fox', 6], ['The', 3], ['uuu', 3], ['uuu', 0], ['The quick brown fox jumped over the lazy dog', 5], ['the quick brown fox', 2], ['ABCDEFGH', 10], ['ab cd ef gh ij', 3], ['ThTe', 3], ['brown', 5], ['Mississippi River', 5], ['River', 3], ['aaa eee iii ooo uuu', 1], ['The quick brown fojx jumped over the lazy dog', 5], ['The quick brown fox jumped over the lazy dog', 0], ['The quick brown fojex jumped over the lazy dog', 5], ['Qwertyuiopasdfghjklzxcvbnm', 4], ['The Quick brown fox jUmPed over the lAzY dog', 9], ['gh', 0], ['The quick brown fojexd jumped over the lazy dog', 5], ['aaa eee iii ooo uuu', 2], ['jumpedABCDEFGH', 10], ['aaa eee iii ooo uuu', 0], ['the quick brown fox', 0], ['Qwertyvbnm', 4], ['aaa eee iii ooo uuuQuick', 6], ['guuuh', 1], ['Thee', 3], ['uuuu', 0], ['Theooo quick brown fox jumped over the lazy dog', 6], ['u', 3], ['Theooo quieck brown fox jumped over the lazy dog', 6], ['the quick brown fox', 1], ['guuuuh', 3], ['wbwrown', 5], ['uuuQuick', 10], ['guuuuh', 2], ['ab cd ef g ij', 2], ['The Quick brown fox jUmPed over the lAzY dog', 8], ['Thee Quick brown fox jUmPed over the lAzY dog', 3], ['Misesissippi River', 1], ['Quick', 6], ['The quick brown fox jumped over the lazy dog', 4], ['The Quick brown fox jUmPed over the lAzY dog', 7], ['Misppi River', 5], ['Thee Quick brown fox jUmPed over the lAzY dog', 4], ['thhe quick buuurown fox', 0], ['u', 2], ['The Quick brown fox jUmPed over the lAzY dog', 6], ['', 3], ['', 9], ['foTheooo quick browjn fox jumped over the lazy dog', 4], ['Thee Quick brown fox jUmPed over the lAzY dog', 8], ['Misppi Riuuuuver', 5], ['aaoa eee iii ooo uuuQuick', 6], ['The Quick bnrown fox jUmPed over the lAzY dog', 9], ['Quick', 5], ['The Quick brown fox jUmPed over the lAzY dog', 10], ['guuuu', 9], ['ThTheooo quieck brown fox jumped over the lazy doge Quick brown fox jUmPed over the lAzY dog', 7], ['iii', 0], ['The Quick bnrown fox jUmPed over the lAzY doggh', 2], ['The Quick brown fox jQuickUmPed over the lAzY dog', 5], ['buuurown', 1], ['the quick brown fox', 10], ['ab cd efb gh ij', 3], ['guuuuh', 9], ['aaoa eee iii oou uuick', 2], ['doggh', 3], ['The quick brown fojx jumped over the lazy dog', 10], ['iii', 6], ['iicdi', 0], ['aadoga eee iii ooo uuu', 2], ['iiiMississippi River', 6], ['braaoa eee iii ooo uuuQuickn', 9], ['the quick brown foxwbwrown', 4], ['ab cdf gh ij', 3], ['Thee Quick brown fox jUmPed over the lAzY dog', 9], ['ab', 4], ['the quick brown fox', 5], ['Qwertyuiopasdfghjklzxcvbnm', 2], ['thhe quick buuurownfox', 1], ['The quick brown fojx jumped over the lazy dog', 3], ['ab cd ef gh ij', 10], ['Thee', 9], ['The Quick bnrown fox jUmPed over the lAzY doggh', 6], ['aaa eee iii ooo uuuQuickguuuuh', 9], ['brown', 0], ['quick', 9], ['ab cd ef g ij', 1], ['The quick brown fox jumped over rthe lanzy dog', 5], ['bnrown', 3], ['Misesissippi River', 0], ['Qwertyuiopasdfghjklzxmcvbnm', 4], ['ab cd ef g ij', 6], ['lAzY', 5], ['quick', 10], ['bnrown', 9], ['iii', 5], ['aadoga eee iii ooo uuu', 5], ['The Quick brown foxaadoga jUmPed over the lAzY dog', 5], ['The quick brown fojx jumped over the lazy dog', 2], ['thjumpede quick brown fox', 0], ['iicdi', 2], ['thher quick buuurownfox', 1], ['ab ij', 10], ['ab cdguuuh ef g ij', 1], ['aaa eee iii ooo uuu', 10], ['The Quick brown foxaadoga jUmPed over the lAzY dog', 10], ['doggh', 6], ['Thab cdf gh ijy dog', 0], ['doge', 9], ['ed over the lazy dog', 5], ['Tee', 9], ['MisesissippiRiver', 0], ['the', 2], ['ab cd h ij', 3], ['ef', 10], ['ab cd ef g ij', 9], ['doggh', 1], ['iiicdi', 2], ['afoxb', 4], ['iii', 1], ['ij', 9], ['guu', 9], ['The', 10], ['Tee', 4], ['uuuQuick', 2], ['ab cddog ef gh ij', 2], ['The Quick brown fox jUmPed over tlanzyhe lAzY dog', 5], ['The Quick brown fox juuuUmPed oveer the lAzY dog', 9], ['aaoa eee iii oou uuick', 1], ['ABCDab cd h ijEFGH', 5], ['aaoathher', 1], ['doghgh', 6], ['ed over the lazy dohg', 5], ['TeThe Quick brown fox jUmPed over the lAzY doge', 4], ['thher quick buuurownfox', 10], ['jumpedABCCDEFGH', 10], ['The Quick brown fox jUmPed over the lAzY dog', 3], ['thher quick buuurowuuuQuickguuuuhnfox', 7], ['ijEFGH', 5], ['ef', 9], ['ef', 11], ['iicdi', 10], ['iij', 9], ['The Quick bnrown fox jUmPed over the lAzY doggh', 8], ['The Quick bnrown fox jUmPed over the lAzY dog', 7], ['Mispspi River', 5], ['iiab cdf gh ij', 2], ['The quick brown fojx jumped oviiiMississippier the lazy dog', 10], ['guuuuab cd ef gh ijh', 2], ['Tee', 0], ['iiafb cdf gh ij', 2], ['The quick brown fox jumped over rthe lyanzy dog', 1], ['aaa eee iii obrownoo uuuQuickguuuuh', 5], ['the quick browab', 2], ['the qquick brown fox', 2], ['cd', 7], ['uu', 3], ['foTheooo quick browjn fox jumped over the lazy dog', 0], ['uuuu', 3], ['doggh', 11], ['ab cd ef g ij', 5], ['Qwertyuiopasdfghjklkzxcvbnm', 6], ['ab cdf gh ij', 2], ['aaa eee iii ooo uuu', 9], ['The Quick brown fox jUmPed over the lAzY afoxbdog', 6], ['The Quick brown fox jUmPed over the lAzY dog', 0], ['foxaadoga', 7], ['thher quick buuurownfox', 11], ['aaacdguuuuh', 5], ['The Quick brown fox jUmPed over the lAzY aab cd ef g ijfoxbdog', 6], ['The quick brown fojx jumped oviiiMississippier the lazy dog', 6], ['iiii', 0], ['Mab cd ef g ijisppi River', 5], ['cddog', 0], ['Thee Quick brown fox jUmPed over the lAzY dog', 5], ['ab cddog ef gh ij', 0], ['Thee Quick brohwn fox jUmPed over the lAzY dog', 10], ['aaoathher', 6], ['aaa eee iii ooo uuuQuick', 4], ['The Quick brown foxaadAoga jUmPed over the lAzY dog', 5], ['lazy', 3], ['Misppi Rsr', 4], ['ab cdf gdh ij', 3], ['The quick brown fox jumped over rthe lyanzy dog', 5], ['MMississippi River', 4], ['thher quick buuurownfox', 9], ['ab cddog ef g', 2], ['guuuuh', 4], ['aaoa eee iii oou uuuick', 7], ['g', 2], ['Misesissippi River', 11], ['wbwrown', 9], ['Theeab cd h ij Quick brown fox jUmPed over the lAzY dog', 9], ['Qwerbtyuiopasdfghjklzxcvbnm', 4], ['aadee iii ooo uuu', 5], ['Misesissippi ooover', 11], ['oviiiMississippier', 6], ['rthe', 6], ['iiab cdf gh ij', 0], ['ab cd h ij', 10], ['MisesssippiRiver', 2], ['iiiMississippi River', 10], ['Thee Quick brown fThab cdf gh ijy dogox jUmPed over the lAzY dog', 9], ['obrownoo', 4], ['guuuuh', 8], ['Misesissippi River', 7], ['iiab cdf gh ij', 1], ['The Quick bnrown fox jUmPed oUver the lAzY dog', 9], ['aadee', 0], ['MisesissippiRiver', 11], ['foxwbwrown', 5], ['aaa eee iii ooo uuu', 5], ['Thee Quick brown fox jUmPed ov dog', 4], ['aiiafbadee iii ooo uuu', 5], ['Theeab cd h ij Quick brown fox jUmPed over the lAzY dog', 10], ['lanzy', 10], ['doggh', 9], ['ab cd ef g ij', 0], ['oviiiMississippier', 10], ['The Quick brown fox Qwertyuiopasdfghjklkzxcvbnmver the lAzY dog', 9], ['ijEFiGH', 5], ['the quick browab', 5], ['iiafb cdf gh ij', 7], ['Misesissippi ooover', 7], ['aadoga eee iii ooo uuu', 1], ['lyanzy', 8], ['ijy', 5], ['The Quick bnrown fox jUmPed oUver the lgAzY dog', 5], ['efab ij', 12], ['thher quick buuuroMisesissippiRiverx', 1], ['quieck', 2], ['juuuUmPed', 5], ['The Quick brown folx jUmPed over tlanzyhe lAzY dog', 5], ['the qudoghghick brown fox', 2], ['aaa eee iii obrownoo uuuQuickguuuuh', 4], ['jumpedABCDQuiQwertyuiopasdfghjklkzxcvbnmverckEFGH', 10], ['The Quick bnrown fox jUmPed oUver the lg', 4], ['The quick brown  fojexd jumped oover the lazy dog', 5], ['oviiiMississippier', 7], ['cd', 12], ['ABCDab cd Gh ijEFGH', 5], ['oviiiMississippier', 4], ['doghggh', 11], ['Thab', 4], ['The Quick Thee Quick brown fThab cdf gh ijy dogox jUmPed over the lAzY dogbrown fox jUmPed over the lAzY aab cd ef g ijfoxbdog', 6], ['iicd', 1], ['MisesissippiRiver', 4], ['TeThe Quick berown fox jUmPed over the lAzY doge', 6], ['aaoathher', 5], ['aadoga eee iii ooo uu', 2], ['Mab cd ef g ijisppi RrtheiveQwertyuiopasdfghjklkzxcvbnmverr', 13], ['The Quick brown folx jUmPed over tlanzyhe lAzY dog', 4], ['braaoa eee iii ooo uuuQuickn', 5], ['rthe', 3], ['quick', 12], ['guuuu', 2], ['MisesssippiTeeRiver', 2], ['Qwertyuiopasdfghjklzxmcvbnm', 6], ['The Quick brown fox jUmPed eover the lAzY dog', 0], ['dh', 6], ['foxwbrwron', 5], ['doggh', 7], ['thhe quick buuhurownfox', 1], ['QwertyuiopasdfQwertyuiopasdfghjklkzxcvbnmverghjklzxcvbnm', 10], ['bwrown', 0], ['dogghh', 9], ['The quick d over the lazy dog', 6], ['ij', 10], ['ThTe', 11], ['thher quick buuurownfox', 6], ['uu', 5], ['aaa eee iii obrowunoo uuuQuickguuuuh', 5], ['Thee Quick brown fox jUmPed over the lAzY dog', 7], ['guuuu', 7], ['thhe', 3], ['The quick brown fojx jumped oviiiMississippier the lazy dog', 5], ['buuuroMisesissippiRiverx', 8], ['aaa eeeThe Quick brown fox jQuickUmPed over the lAzY dog iii ooo uuuQuick', 4], ['t he quick brown fox', 3], ['ab cad ef gh ij', 10], ['thher quick buuurownfox', 13], ['MisesissippiRiverQwerbtyuiopasdfghjklzxcvbnm', 0], ['TeThe Quick brown fox jUmPed oab cddog ef gver the lAzY doge', 4], ['The Quick brownThTheooo over the lAzY afoxbdog', 6], ['Misppi Riuuuuver', 7], ['bwrown', 12], ['Thee Quick brown fox jUmP ed over the lAzY dog', 9], ['Qwertyuiopasdfghjklzxcvbnm', 9], ['iiab cdf gch ij', 1], ['iijy', 5], ['thher quick buuurownfox', 8], ['tlanzyhe', 5], ['t he quick brown fox', 12], ['guuuuh', 11], ['gownuh', 3], ['ab ij', 6], ['brrowwn', 4], ['ga', 7], ['bwrown', 4], ['aaa eee iii obrownoo uuuQuickguuuuh', 1], ['uu', 7], ['Misesissippi River', 12], ['aadoga eee iii ooo uuu', 0], ['browThee', 5], ['guu', 8], ['ABCDab cd Gh ijEFGH', 4], ['MisppMi Rsr', 4], ['the qrown fox', 7], ['bworon', 5], ['rthe', 2], ['iiii', 4], ['Misesssipaaoa eee iii ooo uuuQuickpiRiver', 2], ['TeThe', 0], ['uuuQuickTheooo quieck brown fox jumped over the lazy dogpiRiveruuu', 0], ['iijiii', 6], ['e', 12], ['ThTheooo quieck brown fox jumped over the lazy doge Quick brown fox jUmPed over the lAzY dog', 5], ['the quick bthjumpedeown fox', 10], ['the quick brown foxwbwrown', 0], ['gaa', 7], ['Mab cd ef g ijisppi RrtheiveQwertyuiopasdfghjklkzxcvbnmverrThe', 5], ['ab cad ef gh ijthe quick brothherown foxwbwrown', 0], ['aaoa eee iii oou uuobrowunooick', 7], ['Mab', 5], ['ijEFiGH', 3], ['ThTe', 4], ['aadberownoga eee iii ooo uuu', 2], ['iiTheooo quieck brown fox jumped over the lazy dogicdi', 10], ['The Quickab cddog ef g brown fox jQuickUmPed over the lAzY dog', 5], ['Thee Quick brown fThab cdf gh ijy dogox jUmPed over the lAzY dog', 4], ['uuobrowunooick', 2], ['iicdi', 3], ['uuThe Quick brown fox jQuickUmPed over the lAzY dog', 5], ['The Quick brown fox jUmPed over iicdithe lAzY dog', 7], ['Misesissippi', 10], ['The quick brown fox jumped over rthe lyanzy  dog', 5], ['ee', 9], ['Theeab', 2], ['guthe quick bthjumpedeown foxuuuh', 3], ['aadoga eee iii ooo uuu', 10], ['doge', 5], ['MMississippi River', 3], ['Misesissippi River', 8], ['pjumpDEFGH', 10], ['ab cd h ij', 4], ['QweTeThe Quick brown fox jUmPed over the lAzY dogertyuiopasdfghjklzxmcvbnm', 6], ['TeThe Quick berown fox jUmPed over the lAzY doge', 7], ['juuuUmPed', 10], ['euuue', 9], ['lanlzy', 10], ['bnrown', 11], ['The Quick brown fox juuuUmPed oveer the lAzY dogaaoa eee iii oou uuick', 2], ['jUmP', 5], ['bworon', 10], ['Qwertyuiopasdfghjklzxcvberownbnm', 4], ['The Quick brown fox juuuUmPed oveer the lAzY dogaaoa eee iii oou uuick', 3], ['ab ij', 9], ['ooover', 12], ['aaaab', 4], ['bwrrown', 0], ['ed over the lazy dog', 2], ['ABCDab cd h ijEFGH', 2], ['RrtheiveQwertyuiopasdfghjklkzxcvbnmverrThe', 4], ['MisesissipipiRiver', 0], ['guuuu', 11], ['uuuQuick', 8], ['Theeab cd h ij Quick brown fox jUmPed over the lAzY dog', 7], ['RrtheiveQwertyuiopasdfghjklkzxcvbnmverrThe', 3], ['aadoga eee iii oab cddog ef gh ijoo uuu', 0], ['The Quick brown fox jUmPed over the lAzY dog', 12], ['RrtheiveQwertyuiopasdfghjklkzxcvbnmverrThe', 5], ['jumpedABCCDEFGH', 4], ['The quick brown fojex jumped over theg', 5], ['MisppMi Rsr', 10], ['cc', 7], ['e quick brown foxwbwrown', 3], ['ABCDEFGH', 4], ['cc', 13], ['eQwerbtyuiopasdfghjklzxcvbnm', 1], ['Misppi River', 9], ['The Quick brown fox jUmPed over tlanzyhe lAzY dog', 12], ['thjumpede quick brown fox', 7], ['e quick brown foxwbwrown', 12], ['RrtheiveQwertyuiopasdfghjklkzxcvbnmverr', 4], ['The Quick brown folx jUmPed over tlanzyhe lAzY do', 4], ['guuuuab cd ef gh ijh', 6], ['lanlzy', 11], ['thhe quick buuurownfox', 0], ['iicd', 4], ['RrtheiveQwerityuiopasdfghjklkzxcvbnmverrThe', 4], ['aadoga eee iiid ooo uuu', 5], ['eTee', 4], ['guuuuab cd ef gh ijh', 1], ['efab ijgownuh', 3], ['abaaa eeeThe Quick brown fox jQuickUmPed over the lAzY dog iii ooo uuuQuick cd h ij', 3], ['Gh', 11], ['Thee Quick brohwn fox jUmPed over the lAzY dog', 4], ['lanlzy', 9], ['dogicdi', 7], ['ab ij', 7], ['aaa eeeef iii obrownoo uuuQuickguuuuh', 5], ['obrowunoo', 5], ['doge', 12], ['aadoga eee iii ooo uuu', 7], ['ThTheooo quieck brown fox jumped over the lazy doge Quick brown fox jUmPed over the lAzY dog', 8], ['aaoa eee iii  oou uuick', 7], ['cd', 5], ['ov', 9], ['guuuuuh', 8], ['The Quick brown fox jUmPed over the lAijthegchdog', 4], ['quieck', 8], ['oab', 5], ['e quick brown foxwbwrown', 11], ['eaaacdguuuuhrown foxwbwrown', 4], ['folx', 6], ['ABCDab cd Gh ijEFGH', 12], ['folx', 12], ['thher quick buuuroMisesissippiRiverx', 4], ['TheTheooo Quick brown fox jUmPed over the lAzY dog', 5], ['guuuuuh', 11], ['ThTe', 8], ['Mab cd ef gThe Quick brown fox jUmPed over the lAzY aab cd ef g ijfoxbdog ijisppi RrtheiveQwertyuiopasdfghjklkzxcvbnmverr', 13], ['c', 10], ['Qwertiyuiopasdfghjklzxcvbnm', 3], ['iiTheooo', 9], ['ddogicdi', 7], ['jUmPed', 7], ['jumpedABCCDE', 10], ['t he quick brown fox', 13], ['ABCDEFGH', 5], ['MMississippi', 2], ['thhe quick buuhurownfox', 5], ['dbrownThTheooooge', 11], ['ijthe', 8], ['ab cd ef g ij', 10], ['ab ddog ef g', 12], ['The Quick brown fox jUmPed over tlanzyhe lAzY dog', 10], ['e quick brown foxwbwrown', 4], ['ed', 0], ['ab cd ef  ij', 6], ['dogghh', 6], ['aiiafbadee iii ooo uuulyanzy', 11], ['ab cddog ef aiiafbadee iii ooo uuulyanzygh ij', 0], ['Te', 9], ['doggh', 8], ['eTeafoxbdoge', 4], ['iiiMississipp', 6], ['Mispspi', 5], ['The Quick brown fox jUmPed over tbuuurownhe lAzY dog', 8], ['dijy', 13], ['MisppiijEFGH Riuuuuver', 7], ['Theetbuuurownhe', 3], ['aaoa eee iii  oou uuick', 9], ['The quick brown fox jumped over the lazy dog', 1], ['t xhe quick brown fox', 11], ['gouwnuh', 3], ['ooab', 5], ['Theeab cd h ij Quoverh the lAzY dog', 10], ['ijEFiGH', 7], ['uuab cdf gdh iju', 0], ['brown', 3], ['guuiiab cdf gch ijuu', 7], ['Thee Quick brown fox jUmPed over the lAzY dog', 12], ['uuuQuickTheooo quieck brown fox jumped over the lazy dogpiRiveruuu', 3], ['ThTheooo quieck brown fox jumped over th e lazy doge Quick brown fox jUmPed over the lAzY dog', 7], ['bthjumpedeown', 4], ['tdbrownThTheoooogehe qquick brorwn fox', 2], ['iiTheooo quieck brown fox jumped over the lazy dogicdi', 2], ['The Quick bnrown fox jUmPed oUver the lAzY dog', 8], ['cdddog', 7], ['the qudoghghick brown fox', 5], ['The Quick brown folx jUmPed over tlanzyhe lAzY do', 2], ['gdh', 5], ['brorwn', 5], ['The', 0], ['aoou brorwnuuuick', 7], ['dooeoveroggTheeabh', 6], ['MisebrowTheesissippi River', 6], ['iiii', 9], ['ij', 3], ['fox', 10], ['MisesisaoousippiRiver', 0], ['c', 9], ['wdobwrown', 5], ['oooaob', 8], ['The quick brown fox jumped over rthe lyanzy dog', 4], ['MisebrowTheepsissippi River', 6], ['the quick browno fox', 7], ['thher quck buuurownfox', 11], ['      ', 3], ['', 0], ['aaa euee iii ooo uuu', 3], ['Quick', 3], ['Quick', 4], ['aaa eee iiai oo', 3], ['aaa eeMissefissippie iiaia oo', 3], ['Quicck', 4], ['The quick brown fox jumped over tzy dog', 3], ['quick', 3], ['ABCDEFGH', 6], ['the quick browcd fox', 3], ['aaa eee iiii ooo uuu', 3], ['iiiThe quick brown fox jumped over tzy dogi', 3], ['quicqk', 3], ['The quick brown fox jumped overQwertyuiopasdfghjklzxcvbnm tzy dog', 3], ['aaa eee iiai oo', 2], ['', 6], ['ABCDEFGH', 9], ['aaa', 5], ['rRiver', 6], ['ABCDEFGH', 2], ['ABCDEFG', 0], ['the quick browcd fox', 9], ['the quAjUmPedBCDEFQuicckGick browcd fox', 10], ['aadoguu', 5], ['The', 4], ['over', 5], ['ABCDEFGH', 3], ['Toohe quick brown fox jumped overQwertyuiopasdfghjklzxcvbnm tzy dog', 3], ['oo', 3], ['the quAjUmPedBCDEFQuicowcd fox', 3], ['The quick brown fox jumped over tzy dog', 0], ['cd', 3], ['the quAjUmPedBCDEFQuicowcd fox', 4], ['the quAjUmPedBCDEFQuicckGick browcd fox', 0], ['overQwertyuiopasdfghjklzxcvbnm', 0], ['the quick browcd fox', 0], ['the quAjUmPedBCDEFQuicckGick browcd fox', 11], ['MississiThe quick brown fox jumped over the lazy  dog River', 4], ['MississiThe qujUmPedick brown fox jumped over the lazy  dog River', 4], ['MississiThe qujUmPedick brown fox jumped over the lazy  dog River', 3], ['the quAjUmPedBCDEFQuicckGick browcd fox', 12], ['QQuick', 4], ['MississiThe quick rbrown fox jumped over the lazy  dog River', 4], ['overxQwertyuiopasdfghjklzxcvbnm', 9], ['ABCDEFGH', 11], ['aaa', 3], ['dogEABCDEFGH', 2], ['tzyk', 5], ['aaa eee  oo', 3], ['The quick brown fox jumped over the lazy dog', 10], ['The quick brown fox jumped over tz y dog', 0], ['lazy', 5], ['quick', 0], ['quAjUmPedBCDEFQuicckGick', 0], ['aaa euee iii ooo uuu', 2], ['aaa eee iiii ooo uuu', 4], ['the quAjUmPedBCDEFQuicowcd fox', 10], ['aaa eee  oo', 4], ['Toohe quick brown fox jumped overrbrownQwertyuiopasdfghjklzxcvbnm tzy dog', 3], ['aaa eee iiai oo', 5], ['the quAjUmPedBCDEFQuicckGick browcdfox', 2], ['the quick browcd fox', 10], ['MississiThe qujUmPedick brown fox jumped over the lazy  dog River', 0], ['the quAjUmPedBDCDEFQuicckGick browcdfox', 1], ['the quAjUmPedBCDEFQuicckGick browcd fox', 6], ['The quickiiii brown fox jumped over tz y dog', 0], ['the quick browcd fox', 11], ['overQwuiopasdfghjklzxcvbnm', 2], ['aaa eee iiii ooo uuu', 0], ['Quick', 12], ['MississiThe quick rbrown fox jumped over the lazy  dog River', 11], ['iiiThe quick brownr tzy dogi', 9], ['aaaa', 3], ['qukick', 3], ['Toohe quick brown fox jumped overrbrownQwertyuiopasdfghjklzxcvbnm tzy dog', 4], ['aaaaa', 3], ['QQuicThe quickiiii brown fox jumped over tz y dogk', 12], ['aadogu', 5], ['overrbrownQwertyuiopasdfghjklzxcvbnm', 1], ['aadoguu', 3], ['QQuicThe quickiiii brown fox jumped over tz y dogk', 1], ['QQuicThe quickiiii brown fox jumped over tz y dogk', 11], ['overthexQwertyuiopasdfghjklzxcvbnm', 9], ['the quAjUmPedBCDEFQuifcox', 4], ['the quAjUmPedBCDEFQuicckGick browcd fox', 7], ['brownr', 3], ['QQuicThe quickiiii brown fox jumped over tz y dogk', 13], ['Missisthe quick browcd foxsiThe quick brown fox jumped over the lazy  dog River', 4], ['Toohe quick brown fox jumped overQwertyuiopasdfghjklzxcvbnm tzy dog', 2], ['ABCDEFGAH', 6], ['iiiThe quick brownr tzy dogi', 10], ['the', 11], ['Qwertyuiopasdfghjklzxcvbnm', 11], ['the quAjUmPedBCDEFQuicckGick browcd fox', 3], ['Quick', 1], ['rer', 8], ['the quick browcd fox', 6], ['quAjUmPedBCDEFQuicowcd', 3], ['browcdfox', 3], ['Toohe quick brown fox jumped overQwertyuiopasdfghjklzxcvbnm tzoverQwuiopasdfghjklzxcvbnmy dog', 2], ['brownr', 11], ['ab cd ef gh iquickiiiij', 3], ['aaarbrownaa', 3], ['brown', 1], ['qujUmPedick', 11], ['', 11], ['re', 8], ['oo', 4], ['nthe quick brox', 3], ['quuick', 3], ['The quick brown fox jumped over tz y dog', 3], ['bo', 1], ['quick', 1], ['The quick brown fox jumped overQwertyuiopasdfghjklzxcvbnm tzy dog', 12], ['QQuicThe quickiiii brown fox jumped over tz y dogk', 6], ['qujUmiiiiPedick', 11], ['aaa euee iii ooo uuucd', 12], ['dogiquick', 3], ['The quick brown fox jumped over tzy dog', 6], ['ABCBDEFGHoverQwuiopasdfghjklzxcvbnm', 2], ['overQwuiopasdfghjklzxcvbnm', 9], ['quicqk', 4], ['QQuicThe quickiiii brown fox jumped over tz y dogk', 7], ['brownr', 4], ['overQwuiopasdfghhjklzxcvbnm', 9], ['lazy', 7], ['The Quick brown fox jUmPed over the lAzY dog', 11], ['Qaaa eee iiai oouick', 1], ['aadoaaaguu', 3], ['Theaadoaaaguu', 0], ['Toohe quick xbrown fox jumped overQwertyuiopasdfghjklzxcvbnm tzy dog', 4], ['The quick brown fox jumpedover the lazy dog', 6], ['quAjUmPEedBCDEFQuicowcd', 4], ['rer', 3], ['quAjUmPedBCDEFQuifcox', 3], ['the quAjUmPedBCDEFQuicckthe quAjUmPedBCDEFQuicckGick browcd foxwcd fox', 7], ['wn fox jumped over the lazy  dog River', 13], ['ABCBDEFGHovwuiopasdfghjklzxcvbnm', 2], ['browonr', 3], ['the quick browcdx', 0], ['lazy', 2], ['Quiick', 4], ['the quAjUmPedBCDEFQuicowcd fox', 0], ['aaaaaa', 3], ['ABCDEFGAH', 0], ['ABCDEFGA', 6], ['rRiver', 2], ['ab', 3], ['a aa euee iii ooo uuucd', 0], ['ethe quAjUmPedBCtheDEFQuicowcd foxbrowonr', 3], ['the quAjUmPedBCDEFQuicowcd fox', 1], ['euee', 0], ['foxbrowonr', 10], ['browcdfox', 12], ['T he quick brown fox jumped over tzy dog', 3], ['cd', 10], ['aaa eee iiii ooo uuu', 2], ['re', 2], ['rRnthever', 2], ['browonABCDEFGHr', 12], ['ab cd ef gh ij', 8], ['aaaaa', 0], ['over', 9], ['ABCDEFGA', 3], ['the quicktzoverQwuiopasdfghjklzxcvbnmybrowcdx', 0], ['aaa eee iiii ooo uuu', 1], ['T he quick brown fox jumped over tzy dog', 4], ['lazzy', 2], ['aaa eee  oo', 12], ['River', 8], ['Toohe quick xbrown fox jumped overQwertyuiopasdfghjklzxcvbnm tzy dog', 0], ['lazzy', 1], ['The quick brown fox jumped over tzy dog', 1], ['MississiThe quick rbrown fox jumped over the lazy  dog River', 2], ['the quick browcdx', 7], ['theMississiThe quick rbrown fox jumped over the lazy  dog River', 11], ['MississiThe', 4], ['quAPEedBCDEFQuicowcd', 7], ['the', 8], ['uuu', 2], ['oever', 9], ['lazy', 10], ['lazzy', 4], ['Qaaa', 5], ['QQuick', 3], ['aaa eee iiiABCDEFGAi ooo uuu', 2], ['rer', 12], ['ab cd ef glazyh ij', 2], ['wn fox jumped over the lazy  dog River', 14], ['Quick', 8], ['he', 1], ['ABCFDEFGH', 9], ['uuucd', 4], ['QQuick', 1], ['ab cthe quAjUmPedBCDEFQuicckthe quAjUmPedBCDEFQuicckGick browcd foxwcd foxd ef glazyh ij', 2], ['MississiThe quick brown fox jumped over the lazy  dog River', 5], ['aaa eee reriiii ooo uuu', 2], ['the quAjUmPedBCDEFQuicowcd fox', 9], ['ucd', 7], ['qukick', 8], ['Qick', 1], ['aaa eee iiii', 2], ['ABCDEFGH', 8], ['aaa eee iiii ooo u', 4], ['the quAjUmPedoBCDEFQuicowcd fox', 10], ['the quAjUmPedBCDEFQuicckthe quAjUAmPedBCDEFQuicckGick browcd foxwcd fox', 7], ['lazz', 2], ['the quAjUmPedBCDEFQuicowcd fox', 2], ['Mississippi', 6], ['lazzMissisthe quick browcd foxsiThe quick brown fox jumped over the lazy  dog Rivery', 1], ['over', 2], ['The quick brown fox jumped over tzy dog', 5], ['foxwcd', 4], ['the quAjUmPedoBCDEFQuicoox', 10], ['overQwertyuiopasdfghjklzxcvbnm', 3], ['bo', 2], ['quick', 5], ['reriiii', 5], ['the quAjUmPedBCDEthe quAjUmPedBCDEFQuicckGick browcd foxFQuicowcd fox', 11], ['browonr', 6], ['Qaaa', 10], ['The quick brown fox jumpedover the lazy dog', 1], ['the quAjUmPedBCDEFQuicckGiMississippick browcd fox', 12], ['rRnnthever', 2], ['quAjUmPeudBCDEFQuicowcd', 2], ['QuiQcck', 4], ['MississippiquAjUmPedBCtheDEFQuicowcdver', 4], ['BABCDEFGH', 11], ['ulazyuucd', 4], ['r', 8], ['QQuiucThe quickiiii brown fox jumped over tz y dogk', 1], ['theMississiThe quick rbrown fox jumped over ththe quAjUmPedBCDEFQuicckGick browcd fox lazy  dog River', 9], ['wn', 11], ['MississiThe qujUmPedick brown fox jumped over the lazy  dog River', 2], ['River', 10], ['ethe quAjUmPedBCtheDEFQuicowcd foxbrowonr', 4], ['ucd', 6], ['quAjUmPEedBCDEFQduicowcd', 4], ['dogiquick', 7], ['Quick', 11], ['ethe quAjUmPedBCtheDEFQuicowcd foxbrowonr', 11], ['browonABCDEFGHr', 11], ['QutzoverQrwuiopasdfghjklzxcvbnmyick', 4], ['ab cd ef glazyh ij', 13], ['The quick brown fox jumped overQwertyuiopasdfghjklzxcvbnm tzy dog', 6], ['qucicquk', 3], ['Toohe quick brown fox jumped overQwertyuiopasdfghjklzxcvbnm tzoverQwuiopasdfghjklzxcvbnmy dog', 3], ['The quick brownRivery fox jumped over the lazy dog', 10], ['lAzY', 2], ['he', 2], ['brownonr', 6], ['the quAjUmPe', 10], ['tzoverQwuiopasdfghjklzxcvbnmy', 4], ['quAjUmPedBCDEFQuicowcd', 11], ['aadoguu', 9], ['ABCDEFGH', 14], ['The quick brown fox jumped overQwernm tzy dog', 3], ['foxbrowonr', 1], ['overQwuiopasdfghjklzxzcvbnm', 2], ['dogEABCDEFGH', 3], ['oo', 1], ['the quAjUmPedBCDEFQuicckGick browcd fx', 10], ['QQuicThe quickiiii brown fox jumped over tz y dogk', 3], ['ucd', 4], ['aaoguu', 10], ['ABCDEFdogiquick', 0], ['The quick brown fox jumped over tzy dog', 9], ['the quAjUmPedBCDEFQuicckGick browcdfox', 10], ['browonr', 7], ['fx', 3], ['aaa eee iiai oo', 1], ['quicqk', 9], ['QQuickquick', 0], ['The', 6], ['overxQwertyuiopasdfghjklzxcvbnm', 10], ['overthexQwertyuiopasdfghjklzxcvbnm', 8], ['a aa euee iii ooo uuucd', 11], ['cQuiick', 4], ['ABCBDEFGHoverQwuiopajsdfghjklzxcvbnm', 2], ['the quAjUmPedBCDEFQuicckthe quAjUmPedBCDEFQuicckGick browcd foxwcd fox', 9], ['qtheMississiThe quick rbrown fox jumped over the lazy  dog Riverck', 5], ['overthexQwertyuiopasdfghjklzxcvbnm', 11], ['Toohe quick xbrown fox jumped overQwertyuiopasdfghjklzxcvbnm tzy dog', 1], ['qucicuk', 0], ['rquickiiiiRiver', 2], ['aaa eee iii ouoo uuu', 1], ['fox', 8], ['lAzAY', 2], ['dogEABCDEFGH', 6], ['The quick browRnRivery fox jumped over the lazy dog', 10], ['ABCDEFdogiquick', 3], ['dgogi', 11], ['ctheABCDEFGH', 2], ['ABCBDEFGHovijerQABCDEFGAwuiopasdfghjklzxcvbnm', 2], ['aaa eee iiii o uuu', 3], ['overQwuiopasdfghjklzxcvbnm', 1], ['tfoxFQuicowcdhe quick browcd fox', 6], ['tfoxFQuicowcdhe quick browcd fox', 2], ['quAoeverPEedBCDEFQuicowcd', 7], ['aa', 0], ['the ouooquAjUmPedoBCDEFQuicoox', 10], ['overthexQwertyuiopasdfghjklzxcvbnm', 1], ['reriiii', 4], ['he', 13], ['ABCDEFG', 5], ['ABCBDEFGHoverQwuiopajsdfghjklzxcvbnm', 10], ['QuiQcckQuick', 4], ['foxwcdy', 5], ['the quick browcd fox', 8], ['ab', 1], ['the quickwn fox jumped over the lazy  dog Riverbrowcdx', 0], ['aaa eee iii overthexQwertyuiopasdfghjklzxcvbnmooo uuu', 2], ['Quiick', 5], ['overrbrownQwertyuiopasdfghjklzxcvbnm', 12], ['dog', 4], ['overxQwertyuiopasdfghjklzxcvbnm', 2], ['iii', 9], ['rRntheve', 2], ['overrbrownQwertyuiopabsdfghjklzxcvbnm', 12], ['wn fox jumped over the lazy  dog River', 11], ['QwertyuiopasdfghjklzxcvQQuiucThe quickiiii brown fox jumped over tz y dogkbnm', 10], ['quuick', 6], ['ucd', 9], ['the quAjUmPedBCDEFQuicckGick browcdfox', 12], ['re', 3], ['the quAjUmPedBCDEFQuricckGick browcdfox', 2], ['Qaaaa', 5], ['the quAjUmPedBDCDEFQuicckGick browcdfox', 12], ['browonABCDEF', 12], ['aaa eee iiii ooou uuu', 2], ['browcodfox', 12], ['The quick brown fox jumped over tzy dog', 10], ['the', 12], ['tPhe quAjUmPe', 7], ['cd', 2], ['MississippiquAjUmPedBCtheDEFQuicowcdver', 0], ['aaa erRnnthevero', 10], ['the quick brown fox', 12], ['The quick brown fox jumped overQwernm tzy dog', 2], ['QQuick', 13], ['y', 11], ['ABCBDEFGHovijerQABCDEFGAwuiopasdfghjklzxcvbnm', 7], ['AG', 11], ['quioverrbrownQwertyuiopabsdfghjklzxcvbnmck', 5], ['the quAjUmPedBCDEFQuicckthe quAjUmPedBCDEFQuicckGick browcd foxwcd fox', 8], ['aaa euee iii o uuu', 3], ['The quick brown fox jumped over the lazy dg', 6], ['qujUmPedick', 12], ['ooo', 3], ['Mississippi River', 0], ['iiaia', 10], ['ethe', 6], ['browoFnABCDthe quAjUmPedBCDEFQuicckGiMississippick browcd foxGHr', 3], ['quAjUmPedBDCDEFQuicckGick', 4], ['quioverrbrownQwertyuiopabsdfghjklzxcvbnmck', 12], ['the quictzk browcd fox', 0], ['TheQQuiucThe quick brown fox jumped over tzy dog', 9], ['quAjUmPedBCDEthe', 1], ['overQwuiopasdfghjklzxcvbnm', 0], ['oo', 0], ['the quAjUmPedBCDEFQuicowcd fox', 5], ['aaa eee iiii', 11], ['ulazyuucd', 12], ['QQuick', 14], ['ABCFDEFGHhe', 10], ['MississiThe', 3], ['ABCBDEFGHovijerQABCDEFGAwuiopasdfBghjklzxcvbnm', 8], ['T he quick brown fox jumped over tzy dog', 2], ['dgab', 1], ['a', 11], ['aadogu', 4], ['quicqk', 11], ['the quAjUmPedBCDEFQufoxwcdifcox', 4], ['qucicuk', 5], ['the qoverQwertyuiopasdfghjklzxcvbnmuick browcdx', 7], ['ab cd efToohe quick brown fox jumped overQwertyuiopasdfghjklzxcvbnm tzy dog gh ij', 8], ['ethhe', 6], ['lazzMissisthe quick browcd foxsiThe quick brown fox jumped over the lazy  dog Rivery', 12], ['iiiThe quick brownr tzy dogi', 11], ['overthexQwertyuopasdfghjklzxcvbnm', 11], ['quAjUmPedBDCDEFQuicckGick', 3], ['browcdfoerRnntheverox', 3], ['aaa eee iii overthexQwertyuiopasdfghjklzxcvbnmooo uuu', 3], ['quAjUmPEedBCDEFQuicowcd', 12], ['lQuiQcckQuickAzY', 2], ['the quAjUmoouickPedBCDEFQuicowcd fox', 10], ['dgab', 9], ['quAjUmPedBCDEFQuicckGick', 1], ['tfioxFQuicowcdhe quick browcd fox', 6]]
    results = [['little'], ['Mary', 'lamb'], [], ['world'], ['Uncle'], [], ['b', 'c', 'd', 'f'], ['apple', 'banana'], [], [], ['the', 'cat', 'the', 'hat'], [], [], [], ['consonants'], ['goes', 'the'], [], [], ['fun'], [], ['apple', 'banana'], [], [], [], [], [], [], [], [], ['isp'], [], ['og'], ['containing', 'different'], ['isp'], ['all', 'the', 'way'], [], [], ['hatrryppna'], [], [], ['a'], [], [], ['cat'], [], [], [], ['apple', 'banana'], ['consonants'], ['isp'], ['cat'], ['ming'], ['cat'], ['the', 'fox', 'over', 'the', 'dog'], [], ['in'], [], [], ['cherry'], [], [], ['program', 'languageeR'], ['multiple', 'numbers'], ['Python', 'program'], ['containing', 'different'], ['chernry'], ['cat'], ['isp', 'cat'], ['cherryana'], [], [], ['banaapple', 'cherry'], ['quick', 'lazy'], [], [], ['a'], ['ine'], ['is', 'of'], [], [], [], [], [], ['fox', 'over', 'the', 'dog', 'all', 'the', 'way'], ['containing', 'different'], ['in'], [], ['chernry'], [], [], [], [], ['ThE', 'fOx', 'oVeR', 'tHe', 'DoG'], [], ['all', 'way'], ['a'], ['Pythapple'], ['isp'], ['a', 'a', 'a'], ['cherryana'], ['oVPython'], [], ['og'], [], [], ['a', 'a', 'a', 'a', 'a'], ['languageite'], [], [], [], ['quick', 'lazy'], [], [], [], ['cd', 'gh'], ['quick'], [], [], ['The', 'fox', 'over', 'the', 'dog'], [], ['brown'], ['bwrown'], ['Thee', 'fox', 'over', 'the', 'dog'], ['brown', 'jUmPed'], [], [], [], ['uuu'], [], ['the', 'fox'], [], [], ['ThTe'], [], [], ['River'], [], [], [], [], [], [], [], [], [], ['jumpedABCDEFGH'], ['aaa', 'eee', 'iii', 'ooo', 'uuu'], [], [], [], [], [], ['uuuu'], [], [], [], [], [], [], [], ['guuuuh'], ['cd'], [], ['Quick', 'lAzY'], [], [], ['brown', 'jumped'], [], [], ['brown', 'jUmPed'], [], [], [], [], [], ['jumped'], [], [], [], [], [], [], [], [], ['iii'], ['The', 'fox', 'over', 'the'], [], [], [], [], [], ['uuick'], [], [], [], [], ['aadoga'], [], [], ['brown'], ['cdf'], [], [], [], [], [], ['quick', 'fojx', 'lazy'], [], [], [], [], [], [], ['ab', 'ef', 'g', 'ij'], [], [], [], [], [], [], [], [], [], [], [], ['The', 'over', 'the', 'dog'], [], ['iicdi'], [], [], ['ab', 'ef', 'g', 'ij'], [], [], [], [], [], [], [], [], ['the'], [], [], [], [], ['iiicdi'], [], [], [], [], [], [], [], ['gh'], [], [], [], [], [], [], [], ['brown', 'jUmPed'], [], [], ['Quick', 'lAzY'], [], [], [], [], [], [], [], [], ['Mispspi'], ['gh'], [], ['guuuuab', 'cd', 'gh', 'ijh'], [], ['iiafb', 'gh'], [], ['uuuQuickguuuuh'], ['the'], ['the', 'fox'], [], [], [], [], [], [], [], ['gh'], [], [], [], [], [], [], ['ijfoxbdog'], [], ['iiii'], [], [], [], [], [], [], [], [], ['lazy'], ['Misppi'], ['cdf', 'gdh'], ['lyanzy'], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], ['obrownoo'], [], ['Misesissippi'], ['iiab', 'ij'], [], [], [], [], [], ['brown', 'jUmPed'], [], [], [], [], [], [], [], [], [], [], ['Misesissippi'], [], [], [], ['bnrown'], [], [], [], [], [], ['the', 'fox'], ['obrownoo'], [], ['jUmPed'], [], [], [], [], [], [], [], ['dogbrown', 'ijfoxbdog'], [], [], [], [], ['aadoga'], [], ['brown', 'jUmPed'], [], ['rthe'], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], ['buuurownfox'], [], ['uuuQuickguuuuh'], [], [], ['thhe'], [], [], ['brown'], ['quick'], [], [], [], ['brown', 'jUmPed', 'cddog'], [], [], [], [], [], ['iiab', 'ij'], [], [], [], [], [], [], [], [], [], [], [], [], [], ['eee', 'iii', 'ooo', 'uuu'], ['browThee'], [], ['ABCDab', 'ijEFGH'], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], ['brown', 'fThab', 'jUmPed'], [], [], [], [], [], ['lyanzy'], [], [], ['guthe', 'quick', 'foxuuuh'], [], [], ['River'], [], [], [], [], [], [], [], [], [], ['The', 'fox', 'oveer', 'the', 'dogaaoa', 'uuick'], [], [], [], ['Quick', 'lAzY'], [], [], [], [], ['over', 'the', 'dog'], ['cd'], [], [], [], [], [], [], ['eee', 'iii', 'uuu'], [], [], [], [], [], [], ['quick'], [], [], [], [], [], [], [], [], ['brown', 'jUmPed'], [], [], [], [], [], [], [], ['ef'], [], ['Quick', 'lAzY', 'uuuQuick'], [], ['jUmPed'], [], [], [], ['uuuQuickguuuuh'], [], [], [], [], [], [], [], [], ['brown', 'jUmPed'], [], [], [], [], [], [], [], ['thher'], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], ['brown'], [], [], [], [], ['iii', 'ooo'], [], [], [], [], ['Mispspi'], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], ['quieck', 'lazy'], [], [], ['fox'], ['iiTheooo', 'fox', 'over', 'the'], [], [], [], ['The', 'over'], [], ['brorwn'], [], ['brorwnuuuick'], [], [], [], [], [], [], [], [], [], ['brown', 'jumped'], [], [], [], [], [], [], ['Quick'], [], [], [], ['Quicck'], ['quick', 'tzy'], ['quick'], ['ABCDEFGH'], ['quick'], [], ['quick', 'tzy'], [], ['quick', 'tzy'], [], [], [], [], [], [], [], [], [], [], [], [], [], ['quick', 'tzy'], [], [], [], [], [], [], [], [], [], ['brown', 'jumped'], ['brown', 'jumped'], ['lazy', 'River'], [], ['QQuick'], ['jumped'], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], ['quick', 'tzy'], [], ['the'], [], [], [], [], [], [], [], ['aaa', 'eee', 'iiii', 'ooo', 'uuu'], [], [], [], [], [], ['brown', 'jumped'], [], [], [], [], [], ['y'], [], [], [], [], [], [], ['brown', 'jumped'], ['Toohe', 'fox', 'dog'], ['ABCDEFGAH'], [], [], [], [], [], [], [], [], [], ['Toohe', 'fox', 'dog'], [], [], [], [], [], [], [], [], ['nthe', 'quick', 'brox'], ['quuick'], ['quick'], ['bo'], [], [], [], [], [], [], [], [], [], ['quicqk'], [], [], [], [], [], ['Qaaa'], [], [], ['jumped'], ['jumpedover'], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], ['a', 'aa', 'euee', 'iii', 'ooo'], [], [], ['euee'], [], [], ['quick', 'tzy'], [], [], [], [], [], [], ['aaaaa'], [], [], [], [], ['brown', 'jumped'], [], [], [], [], [], [], ['fox', 'over', 'the', 'dog'], [], [], [], [], [], [], [], [], ['lazzy'], [], [], [], [], ['cd'], [], [], ['he'], [], [], [], [], [], ['reriiii'], [], [], [], [], [], [], [], [], [], [], ['the', 'fox'], [], [], ['over'], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], ['y'], ['theMississiThe'], [], ['fox', 'over', 'the', 'dog'], [], [], [], [], [], [], [], ['browonABCDEFGHr'], [], [], [], [], ['quick'], [], [], [], ['brownonr'], [], [], [], [], [], ['quick', 'tzy'], [], [], [], [], [], ['quickiiii', 'dogk'], [], [], [], [], [], [], [], [], [], [], [], [], [], [], ['cQuiick'], [], [], ['rbrown', 'Riverck'], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], ['fox'], [], ['aa'], [], [], [], [], ['ABCDEFG'], [], [], [], [], ['ab'], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], ['the'], [], [], [], [], [], [], [], [], ['cd'], [], [], [], ['The', 'fox', 'dog'], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], ['oo'], [], [], [], [], [], [], [], ['fox', 'over', 'dog'], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
    for i, (inp, exp) in enumerate(zip(inputs, results)):
        assertion(candidate(*inp), exp, 0)


check(select_words)