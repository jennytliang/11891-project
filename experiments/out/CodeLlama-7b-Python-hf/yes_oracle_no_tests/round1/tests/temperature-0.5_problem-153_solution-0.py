def Strongest_Extension(class_name, extensions):
    """You will be given the name of a class (a string) and a list of extensions.
    The extensions are to be used to load additional classes to the class. The
    strength of the extension is as follows: Let CAP be the number of the uppercase
    letters in the extension's name, and let SM be the number of lowercase letters 
    in the extension's name, the strength is given by the fraction CAP - SM. 
    You should find the strongest extension and return a string in this 
    format: ClassName.StrongestExtensionName.
    If there are two or more extensions with the same strength, you should
    choose the one that comes first in the list.
    For example, if you are given "Slices" as the class and a list of the
    extensions: ['SErviNGSliCes', 'Cheese', 'StuFfed'] then you should
    return 'Slices.SErviNGSliCes' since 'SErviNGSliCes' is the strongest extension 
    (its strength is -1).
    Example:
    for Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'
    
	Include these tokens in the code:  def strength ( s : str )
	Do not include these tokens in the code: strong est _ extension
	"""

    strongest_extension = None
    strongest_extension_strength = None
    for extension in extensions:
        extension_strength = strength(extension)
        if strongest_extension is None or extension_strength > strongest_extension_strength:
            strongest_extension = extension
            strongest_extension_strength = extension_strength
    return class_name + '.' + strongest_extension


def strength(s):
    return -len([c for c in s if c.islower()]) + len([c for c in s if c.isupper()])




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
    inputs = [['Watashi', ['tEN', 'niNE', 'eIGHt8OKe']], ['Boku123', ['nani', 'NazeDa', 'YEs.WeCaNe', '32145tggg']], ['__YESIMHERE', ['t', 'eMptY', 'nothing', 'zeR00', 'NuLl__', '123NoooneB321']], ['K', ['Ta', 'TAR', 't234An', 'cosSo']], ['__HAHA', ['Tab', '123', '781345', '-_-']], ['YameRore', ['HhAas', 'okIWILL123', 'WorkOut', 'Fails', '-_-']], ['finNNalLLly', ['Die', 'NowW', 'Wow', 'WoW']], ['_', ['Bb', '91245']], ['Sp', ['671235', 'Bb']], ['Test1', ['UPPERCASE', 'uppercase', '1111']], ['Test2', ['capitalLETTERS', 'lowercaseletters', 'mIxEdcAsE']], ['Test3', ['oneUPPERcaseletter', 'TWoUPPERcaseletTErs', 'threeUppercaseletters', 'fourlowercaseletters']], ['Test4', ['ALLUPPERcaseletters', 'ALLlowercaseletters', 'Nolettersatall123', '12345']], ['Test5', ['ZERO', 'one', 'Two', 'THREE', 'four', 'FIVE', 'six', 'seven', 'eight', 'nine', '10']], ['Person', ['TEst', 'Name', 'naMe', 'AGE']], ['Animal', ['CAMel', 'hOrSE', 'DoG']], ['Vehicle', ['Automobile', 'CAR', 'SuPerbIkE', 'Z']], ['Computer', ['Laptop', 'DEsktop', 'TABLET', 'MONITOR', 'MOUSE', 'KEYboard']], ['Book', ['NOVEL', 'picturebook', 'COOkbook', 'Dictionary', 'Encyclopedia']], ['Computer', ['Laptop', 'DEsktop', 'TABLET', 'MONITOR', 'MOUSE', 'KEYboard', 'KEYeightboard']], ['Compter', ['Laptop', 'DEsktop', 'TABLET', 'MONITOR', 'MOUSE', 'KEYboard', 'KEYeightboard']], ['Computer', ['Laptop', 'DEsktop', 'TABLET', 'MONITOR', 'MOUSE', 'KEYeightboard']], ['Vehcice', ['Automobile', 'CAR', 'Vehicle', 'SuPerbIkE', '']], ['VehciceBook', ['Automobile', 'CAR', 'Vehicle', 'SuPerbIkE', '']], ['Animaal', ['CAMel', 'hOrSE', 'DoG']], ['Animal', ['capitalLETTERS', 'lowercaseletters', 'mIxEdcAsE']], ['Test1', ['UPPERCASE', 'uppercase', 'uppercasse', '1111']], ['Test1', ['UPPERCASE', 'uppercase', 'Animal']], ['Vehcice', ['Automobile', 'CAR', 'Vehicele', 'SuPerbIkE', '']], ['T1e1st1', ['UPPERCASE', 'uppercase', '1111']], ['Test3', ['oneUPPERcaseletter', 'threeUppercaseletters', 'fourlowercaseletters', 'threeUppercaseletters']], ['Vehcice', ['bIkE', 'Automobile', 'CAR', 'Vehicle', 'SuPerbIkE', '']], ['eightTeste3', ['UPPERCASE', 'uppercase', 'Animal']], ['AniVehcicemal', ['CAMel', 'hOrSE', 'DoG']], ['Test5', ['ZERO', 'one', 'Two', 'THREE', 'four', 'FIVE', 'six', 'FVIVE', 'seven', 'eight', 'nine', '10']], ['VehciceBo', ['Automobile', 'CAR', 'Vehicle', 'SuPerbIkE', '']], ['Test1', ['UPPERSCASE', 'uppercase', 'Animal']], ['Test1', ['UPPERCASE', 'uppercase', 'uppercasse', '1Test5111']], ['Animal', ['Do', 'CAMel', 'hOrSE', 'ZERO']], ['eightTeste3', ['aAnimal', 'UPPERCASE', 'uppercase', 'Animal']], ['TeTst3CTest3omputer', ['oneUPPERcaseletter', 'TWoUPPERcaseletTErs', 'fourlowercaseletteNamers', 'threeUppercaseletters', 'fourlowercaseletters']], ['Vehcpicturebccookoobk', ['Automobile', 'CAR', 'Vehicle', 'SuPerbIkE', '']], ['Test5', ['ZERO', 'one', 'Two', 'THREE', 'fur', 'four', 'FIVE', 'six', 'FVIVE', 'seven', 'eight', 'nine', '10']], ['AnimAnimaonelal', ['CAMel', 'hOrSE', 'DoG']], ['_', ['yolo', '900000000', 's3cr3tK3y', 'GIMMETH3L00TZ!']], ['ClassName', ['XXXXXXx', 'AAA', 'ffffff', 'Bbcde', 'GHIJKLMN']], ['My_class', ['Aaa', 'ZZZZ', 'ddd', 'E', 'HHHHHH']], ['Another_class', ['AbCdEfG', 'Hijklmno', '12345', 'pqrstuvwxy', 'Z']], ['MYCLASS', ['qwerty', 'asdfgh', 'zxcvbn', 'QWERTY', 'ASDFGHJKL', 'ZXCVBNM']], ['testing1', ['TESTING2', 'TEST', 'test', 'tEstin3g']], ['AnotherClass', ['hello', 'WORLD', 'Python321', 'TEST', 'Extend']], ['MyClass', ['AbcDEFg', 'hIjKlmn', 'OPqrst', 'UVWxYZ']], ['YetAnotherClass', ['1', 'BBB', 'ccc', 'DDDDDD', 'EEEeeeE', 'ffffff']], ['OneMoreClass', ['AAAaA', 'bbBbB', 'CcCcC', 'ddddDDD', 'EEE', 'FgHiJ', 'kLMNop']], ['s3cr3tK3y', ['AbCdEfG', 'Hijklmno', '12345', 'pqrstuvwxy', 'Z']], ['MyCslass', ['hIjKlmn', 'OPqrst', 'UVWxYZ']], ['AnotherClass_', ['hello', 'WORLD', 'Python321', 'TEST', 'Python3yolo21', 'Extend']], ['MExtendy_class', ['Aaa', 'ZZZZ', 'ddd', 'E', 'HHHHHH']], ['MYCLASS', ['qwerty', 'asdfgh', 'zxcvbn', 'QWERTY', 'ASDFGHJKL', 'qweqrty', 'ZXCVBNM']], ['My_classMYCLASS', ['Aaa', 'ZZZZ', 'ddd', 'E', 'HHHHHH', 'ZZZZ']], ['ClassaName', ['XXXXXXx', 'AAA', 'ffffff', 'Bbcde', 'GHIJKLMN']], ['ClassaName', ['XXXXXXx', 'AAA', 'ffffff', 'Bbcde', 'GHIJKLN']], ['otherClahellorss', ['hello', 'WORLD', 'Python321', 'TEST', 'Extend']], ['s3cr3tK3y', ['Hijklmno', 'pqrstuvwxy', 'Z']], ['s3cr3tK3y', ['Hijklmno', '12345', 'pqrstuvwxy', 'Z', 'Hijklmno']], ['ClassaName', ['GHIHJKLN', 'XXXXXXx', 'AAA', 'ffffff', 'Bbcde', 'GHIJKLN']], ['otherClahellorss', ['hello', 'WORLD', 'ExtAbCdEfGend', 'TEST', 'Extend']], ['My_classMYCLASS', ['Aaa', 'ZZZZ', 'dddd', 'E', 'HHHHHH', 'ZZZZ']], ['Python321_', ['yolo', '900000000', 's3cr3tK3y', 'GIMMETH3L00TZ!']], ['My_classLMYCLASS', ['Aaa', 'ZZZZ', 'ddd', 'E', 'HHHHHH', 'ZZZZ']], ['s3cr3tK3y', ['AbCdEfG', 'Hijklmno', '12345', 'pqrstuvwxy']], ['YetAnotherClass', ['1', 'BBB', 'GIMMETH3L00TZ!', 'ccc', 'DDDDDD', 'EEEeeeE', 'ffffff']], ['Another_class', ['AbCdEfG', 'Hijklmno', '12345', 'pqrstuvwxy', 'Z', '12345']], ['MExtendy_class', ['Aaa', 'ddd', 'E', 'HHHHHH']], ['My_class', ['qwerty', 'asdfgh', 'zxcvbn', 'ASDFGHJKL', 'qwewrty', 'ZXCVBNM']], ['Another_class', ['AbCdEfG', 'Hijklmno', '12345', 'AbCdEfASDFGHJKLG', 'pqrstuvwxy', 'Z', '12345']], ['dddd', ['Hijklmno', 'pqrstuvwxy', 'Hijklmno']], ['ClassaNamse', ['XXXXXXx', 'AAA', 'ffffff', 'Bbcde', 'GHIJKLMN', 'XXXXXXx']], ['MyClass', ['AbcDEFg', 'hIjKlmn', 'OPqrst', 'UVotherClahellorssWxYZ']], ['_', ['yolo', '900000000', 's3cr3tKK3y', 'GIMMETH3L00TZ!']], ['My_classLMYCLASS_', ['yolo', '900000000', 's3cr3tK3y', 'GIMMETH3L00TZ!']], ['s3cr3tK3y', ['AbCdEfG', 'Hijklmno', 'My__classMYCLASS', 'pqrstuvwxy', 'Hijklmno']], ['_', ['yolo', '900000000', 's3cr3tK3y']], ['s3cr3tK3y', ['Hijklmno', 'pqrstuvwxy', 'Z', 'pqrstuvwxy']], ['ClassaName', ['XXXXXX', 'AAA', 'ffffff', 'Bbcde', 'GHIJKLN']], ['MYCLASS', ['qwerty', 'zxcvbn', 'QWERTY', 'ASDFGHJKL', 'ZXCVBNM']], ['MyClasss', ['AbcDEFg', 'hIjKlmn', 'OPqrst', 'UVWxYZ']], ['s3cr3tK3y', ['AbCdEfG', 'My__classMYCLASS', 'pqrstuvwxy', 'Hijklmno']], ['otherClahellorss', ['ClassaNamse', 'WORLD', 'ExtAbCdEfGend', 'TEST', 'Extend']], ['My_classMYCLASS', ['Aaa', 'ZZZZ', 'dddd', 'E', 'HHHHHH', 'ZZZZ', 'ZZZZ']], ['MYCLASMyClasssS', ['qwerty', 'asdfgh', 'zxcvbn', 'QWERTY', 'ASDFGHJKL', 'qweqrty', 'ZXCVBNM']], ['Another_class', ['AbCdEfG', 'Hijklmno', '12345', 'pqrstuvwxy', 'Z', '12345', 'AbCdEfG']], ['AnotherClas_', ['hello', 'WORLD', 'Python321', 'TEST', 'Python3nyolo21', 'Extend', 'Python3yolo21']], ['ClassaNamse', ['XXXXXXx', 'AAA', 'bbBbB', 'Bbcde', 'MyClasss', 'XXXXXXx']], ['ddGHIHJKLNdd', ['Hijklmno', 'pqrstuvwxy', 'Hijklmno']], ['qwewrty', ['ylo', 'yolo', '900000000', 's3cr3tK3y']], ['OPqrst', ['AbCdEfG', 'Hijklmno', '12345', 'pqrstuvwxy']], ['MExtendy_class', ['Aaa', 'ZZZZ', 'ddd', 'E', 'HHHHHH', 'ZZZZ']], ['AnotAbCdEfASDFGHJKLGher_class', ['AbCdEfG', 'Hijklmno', '12345', 'AbCdEfASDFGHJKLG', 'pqrstuvwxy', 'Z', '12345']], ['My_class', ['Aaa', 'ZZZzxcvbnZ', 'ddd', 'E', 'HHHHHH']], ['otherClahellorss', ['ClassaNamsse', 'WORLD', 'ExtAbCdEfGend', 'TEST', 'Extend']], ['ys3cr3tK3y', ['Hijklmno', 'pqrstuvwxy', 'Z']], ['YetAnotherClasUVWxYZs', ['1', 'BBB', 'ccc', 'DDDDDD', 'EEEeeeE', 'ffffff', 'EEEeeeE']], ['MnYetAnSlaassYCLASS', ['qwerty', 'zxcvbn', 'QWERTY', 'ASDFGHJKL', 'ZXCVBNM']], ['My_class', ['ddddDDD', 'asdfgh', 'zxcvbn', 'ASDFGHJKL', 'qwewrty', 'ZXCVBNM', 'asdfgh']], ['nYetAnotherCMYCLASSlassnothGIM!METYoetAnoEEErClassH3L00TZ!yoloerClass', ['qwerty', 'zxcvbn', 'QWERTY', 'ASDFGHJKL', 'ZXCVBNM']], ['ClassaName', ['XXXXXX', 'AAA', 'ffffff', 'Bbcde', 'GHIJKLN', 'GHIJKLN']], ['Python321_', ['yolo', 'nYetAnotherCMYCLASSlaass', 's3cr3tK3y', 'GIMMETH3L00TZ!']], ['test', ['AbCdEfG', 'Hijklmno', '12345', 'pqrstuvwxy', 'Z', '12345', 'AbCdEfG']], ['MMy_classMYCLASS', ['Aaa', 'ZZZZ', 'ddd', 'E', 'HHHHHH', 'ZZZZ']], ['x1UXXXXXXxVWxYZ', ['1', 'BBB', 'ccc', 'DDDDDD', 'EEEeeeE', 'ffffff', 'EEEeeeE']], ['Another_css', ['AbCdEfG', 'Hijklmno', '12345', 'pqrstuvwxy', 'Z', '12345']], ['test', ['Hijklmno', '12345', 'pqrstuvwxy', 'Z', '12345', 'AbCdEfG']], ['My_class', ['Aaa', 'ZZZZ', 'ddd', 'E', 'HHHHHH', 'E']], ['MMy_classMYCLASS', ['Aaa', 'ZZZZ', 'ddd', 'HHHHHH', 'ZZZZ']], ['My_class', ['ddddDDD', 'asdfgh', 'Aaa', 'zxcvbn', 'ASDFGHJKL', 'qwewrty', 'ZXCVBNM', 'asdfgh']], ['MYCLASS', ['Aaa', 'ZZZZ', 'ddd', 'E', 'HHHHHH', 'ZZZZ']], ['My_classMYCLASS', ['Aa', 'ZZZZ', 'HHHHHH', 'ZZZZ']], ['Another_class', ['AbCdEfG', 'Hijklmno', '12345', 'pqrstuvwxy', 'Z', 'AbCdEfG']], ['ClassNaMqwertyy_classLMYCLA_e', ['XXXXXXx', 'AAA', 'ffffff', 'Bbcde', 'GHIJKLMN']], ['My__classMYCLASS', ['ZZZZ', 'dddd', 'E', 'HHHHHH', 'ZZZZ', 'ZZZZ', 'ZZZZ']], ['My_class', ['Aaa', 'ZZZZ', 'HHHMeyOneMoreClassClass', 'ddd', 'E', 'HHHHHH', 'E', 'ZZZZ']], ['My_class', ['Aaa', 'ZZZZ', 'ddd', 'E', 'HHHHH', 'HHHHHH']], ['ddGHIHJKLNdd', ['hello', 'WORLD', 'Python321', 'TEST', 'Python3yolo21', 'Extend']], ['OPqrst', ['AbCdEfG', 'Hijklmno', '12345', 'pqrstuvwxy', '12345']], ['ClassaNamse', ['XXXXXX', 'AAA', 'ffffff', 'Bbcde', 'GHIJKLN', 'GHIJKLN']], ['otherClahellorss', ['ClassaNamsse', 'WORLD', 'ExtAbCdEfGend', 'Extend']], ['ClassaNamse', ['Aaa', 'ZZZZ', 'ddd', 'E', 'HHHHHH', 'ZZZZ']], ['MExty_class', ['Aaa', 'ddd', 'E', 'HHYetAnotherClassHHHH']], ['MMExtendy_classy_classMYCLASS', ['Aaa', 'ZZZZ', 'dddd', 'AAaa', 'HHHHHH', 'ZZZZ']], ['s3cr3tKK3y', ['AbCdEfG', 'Hijklmno', '12345', 'pqrstuvwxy', 'Z', '12345']], ['MExtendy_clasAnotherClasss', ['Aaa', 'ZZZZ', 'ddd', 'E', 'HHHHHH', 'ZZZZ']], ['My_class', ['qwerty', 'asdfgh', 'zxcvbHHHMeyOneMoreClassClassn', 'ASDFGHJKL', 'qwewrty', 'ZXCVBNM']], ['JDLRFD', ['AbcDEFg', 'hIjKlmn', 'OPqrst', 'UVotherClahellorssWxYZ', 'hIjKlmn']], ['test', ['AbCdEfG', 'Hijklmno', '12345', 'pqrstuvwxy', 'Z', '12345', 'AbCdEfG', 'pqrstuvwxy']], ['My_classLMYCLASS_nnYetAnotherCMYsCLASSUVWxYZlass', ['yolo', '900000000', 's3cr3tK3y', 'GIMMETH3L00TZ!']], ['YoetAnoEEErClasslassaName', ['XXXXXXx', 'AAA', 'ffffff', 'Bbcde', 'GHIJKLMN']], ['MExtendyc_class', ['Aaa', 'ZZZZ', 'E', 'HHHHHH']], ['MyClasssnYetAnotherCMYsCLASMqwertyy_classLMYCLASS_', ['AbcDEFg', 'hIjKlmn', 'OPqrst', 'UVWxYZ', 'OPqrst']], ['My_class', ['qwerty', 'asdfgCcCcC', 'zxcvbHHHMeyOneMoreClassClassn', 'ASDFGHJKL', 'qwewrty', 'ZXCVBNM']], ['MMy_clasMEAAAaAxtendy_classsMYCLASS', ['Aaa', 'ZZZZ', 'HHHHHH', 'ZZZZ']], ['', ['HhAas', 'okIWILL123']], ['$pecial_&_Cl@ss_name', ['YoUReXt']], ['123ThisIsTheClassName456', ['Ex1', 'ex2', 'ex3', 'EX4']], ['ThisIsTheClassName', ['ThisIsTheExtension']], ['NoExtensionHasUpperCaseOrLowerCase', ['1234', '5678', '9987', 'hello']], ['', ['abc', 'DEF', 'gHi']], ['SampleClass', ['Abc', 'ddD', 'eFG']], ['SampleClass', ['AAA', 'BBB', 'CCC']], ['SampleClass', ['aBc', 'dEf', 'Ghi']], ['SampleClass', ['AbC', 'DeF', 'gHI']], ['UVWxYZ', ['hello', 'WORLD', 'Python321', 'Exteasdfghnd', 'TEST', 'Extend']], ['AAA', ['AbcDEFg', 'hIjKlmn', 'OPqrst', 'UVWxYZ']], ['testing1', ['TESTING2', 'TOPqrstEST', 'test', 'tEstin3g']], ['MyClass', ['AbcDEFg', 'hIjKlmn', 'OPqrst']], ['AbCdEfG', ['AAAaA', 'bbBbB', 'CcCcC', 'ddddDDD', 'EEE', 'FgHiJ', 'kLMNop']], ['UVWxYZ', ['WORLD', 'Python321', 'Exteasdfghnd', 'TEST', 'Extend']], ['YetAnotherClass', ['1', 'BBB', 'ccc', 'DDDDDD', 'ffffff']], ['MyClass', ['AbcDEFg', 'hIjKlmn', 'Bbcde', 'UVWxYZ']], ['My_class', ['Aaa', 'ZZZZ', 'ddd', 'E']], ['AbCdETESTING2fG', ['AAAaA', 'bbBbB', 'CcCcC', 'ddddDDD', 'EEE', 'FgHiJ', 'kLMNop']], ['AbCdEfG', ['AAAaA', 'bbBbB', 'CcCcC', 'ddddDDD', 'EEE', 'FgHiJ', 'kLMNop', 'ddddDDD']], ['MYCLASS', ['hello', 'WORLD', 'Python321', 'TEST', 'Extend']], ['Tg1', ['TESTING2', 'TOPqrstEST', 'TOPqrsttEST', 'test', 'tEstin3g']], ['fffffBbcdeAaaff', ['AAAaA', 'bbBbB', 'CcCcC', 'ass', 'EEE', 'FgHiJ', 'kLMNop', 'ddddDDD']], ['Another_class', ['AbCdEfG', '1235', 'Hijklmno', '12345', 'vpqrstuvwxy', 'Z']], ['Tg', ['TESTING2', 'TOPqrstEST', 'TOPqrsttEST', 'test', 'tEstin3g']], ['TESTING2', ['AAAaA', 'bbBbB', 'CcCcC', 'ddddDDD', 'EEE', 'FgHiJ', 'kLMNop']], ['M1235yClass', ['AbcDEFg', 'hIjKlmn', 'Bbcde', 'UVWxYZ']], ['T1', ['TESTING2', 'TOPqrstESST', 'TOPqrsttEST', 'test', 'tEstin3g']], ['MYCLASS', ['qwerty', 'asdfgh', 'zxcvbn', 'QWERTY', 'MYCLASS', 'ASDFGHJKL', 'ZXCVBNM']], ['1', ['TESTING2', 'TOPqrstEST', 'TOPqrsttEST', 'test', 'tEstin3g']], ['TESTING2', ['AAAaA', 'bbBbB', 'CcCcC', 'ddddDDD', 'EEE', 'hello', 'kLMNop']], ['T1', ['hello', 'WORLD', 'Python321', 'Exteasdfghnd', 'TEST', 'Extend']], ['TESTING2', ['AAAaA', 'bbBbB', 'CcCcC', 'ddddDDD', 'EEE', 'kLMNop']], ['OneMorCassNaame', ['AAAaA', 'bbBbB', 'CcCcC', 'ddddDDD', 'EEE', 'FgHiJ', 'kLMNop']], ['testing1', ['yolo', '900000000', 's3cr3tK3y', 'GIMMETH3L00TZ!']], ['M1235yClas', ['AbcDEFg', 'hIjKlmn', 'Bbcde', 'UVWxYZ']], ['T1', ['TESTING2', 'TOPqrstEST', 'TOPqrsttEST', 'test', 'tEstin3g']], ['T1', ['hello', 'WORLD', 'Python321', 'Exteasdfghnd', 'TEST', 'Extend', 'WORLD']], ['MCyClass', ['AbcDEFg', 'hIjKlmn', 'OPqrst', 'UVWxYZ']], ['_', ['yolo', '900000000', 's3cr3tK3y', 'GIMMETH3L00TZ!', 'GIMMETH3L00TZ!']], ['1234GHIJKLMN5', ['TESTING2', 'TOPqrstEST', 'TOPqrsttEST', 'test', 'tEstin3g']], ['YetAtEstin3gnotherClass', ['1', 'BBB', 'ccc', 'DDDDDD', 'EEEeeeE', 'ffffff']], ['Ye1234GHIJKLMN5tAnotherClass', ['1', 'BBB', 'ccc', 'DDDDDD', 'ffffff']], ['M1235yClass', ['AbcDEFg', 'hIjKlmn', 'Bbcde', 'UVWxYZ', 'AbcDEFg']], ['Tg', ['AbcDEFg', 'hIjKlmn', 'OPqrst', 'UVWxYZ', 'UVWxYZ']], ['Ye1234GHIJKLMN5tAnotherClass', ['HHHHHM1235yClassHExteand1', 'BBB', 'ccc', 'DDDDDD', 'ffffff']], ['TESTINT2G2', ['AAAaA', 'bbBbB', 'CcCcC', 'testiffffffngg1', 'EEE', 'kLMNop', 'bbBbB']], ['_Exteasdfghnd', ['yolo', '900000000', 's3cr3tK3y', 'GIMMETH3L00TZ!']], ['T11', ['hello', 'WORLD', 'Python321', 'Exteasdfghnd', 'TEST', 'Extend']], ['AbCEdEfG', ['AAAaA', 'bbBbB', 'CcCcC', 'ddddDDD', 'EEE', 'FgHiJ', 'kLMNop']], ['YetAtEstin3gnotherClass', ['1', 'BBB', 'ccc', 'DDDDDD', 'bbBbBeeE', 'ffffff']], ['AbCdEfG', ['AAAaA', 'bbBbB', 'CcCcC', 'ddddDDD', 'xcvbnAAAaA', 'EEE', 'FgHiJ', 'kLMNop', 'ddddDDD']], ['MyClMasss', ['1', 'BBB', 'ccc', 'DDDDDD', 'bbBbBeeE', 'ffffff']], ['TgTg1', ['AbcDEFg', 'hIjKlmn', 'OPqrst', 'UVWxYZ', 'UVWxYZ']], ['Another_class', ['AbCdEfG', '1235', 'Hijklmno', '12345', 'vpqrstuvwxy', 'Z', 'Hijklmno']], ['YCBBBLASS', ['1', 'BBB', 'ccc', 'DDDDDD', 'ffffff']], ['T1', ['hello', 'Python321', 'Exteasdfghnd', 'TEST', 'Extend']], ['M12ss', ['AbcDEFg', 'hIjKlmn', 'Bbcde', 'UVWxYZ', 'AbcDEFg']], ['BBBB', ['AAAaA', 'bbBbB', 'CcCcC', 'testiffffffngg1', 'EEE', 'kLMNop', 'bbBbB']], ['_Exteasdfghnd', ['yMCyClassolo', 'yolo', '900000000', 's3cr3tK3y', 'GIMMETH3L00TZ!']], ['T1', ['hello', 'WORLD', 'Python321', 'Exteasdfghnd', 'helHHHHHHEHxteasdkLMNopfBBBghndo', 'TEST', 'Extend']]]
    results = ['Watashi.eIGHt8OKe', 'Boku123.YEs.WeCaNe', '__YESIMHERE.NuLl__', 'K.TAR', '__HAHA.123', 'YameRore.okIWILL123', 'finNNalLLly.WoW', '_.Bb', 'Sp.671235', 'Test1.UPPERCASE', 'Test2.capitalLETTERS', 'Test3.TWoUPPERcaseletTErs', 'Test4.12345', 'Test5.THREE', 'Person.AGE', 'Animal.CAMel', 'Vehicle.CAR', 'Computer.MONITOR', 'Book.NOVEL', 'Computer.MONITOR', 'Compter.MONITOR', 'Computer.MONITOR', 'Vehcice.CAR', 'VehciceBook.CAR', 'Animaal.CAMel', 'Animal.capitalLETTERS', 'Test1.UPPERCASE', 'Test1.UPPERCASE', 'Vehcice.CAR', 'T1e1st1.UPPERCASE', 'Test3.oneUPPERcaseletter', 'Vehcice.CAR', 'eightTeste3.UPPERCASE', 'AniVehcicemal.CAMel', 'Test5.THREE', 'VehciceBo.CAR', 'Test1.UPPERSCASE', 'Test1.UPPERCASE', 'Animal.ZERO', 'eightTeste3.UPPERCASE', 'TeTst3CTest3omputer.TWoUPPERcaseletTErs', 'Vehcpicturebccookoobk.CAR', 'Test5.THREE', 'AnimAnimaonelal.CAMel', '_.GIMMETH3L00TZ!', 'ClassName.GHIJKLMN', 'My_class.HHHHHH', 'Another_class.AbCdEfG', 'MYCLASS.ASDFGHJKL', 'testing1.TESTING2', 'AnotherClass.WORLD', 'MyClass.UVWxYZ', 'YetAnotherClass.DDDDDD', 'OneMoreClass.AAAaA', 's3cr3tK3y.AbCdEfG', 'MyCslass.UVWxYZ', 'AnotherClass_.WORLD', 'MExtendy_class.HHHHHH', 'MYCLASS.ASDFGHJKL', 'My_classMYCLASS.HHHHHH', 'ClassaName.GHIJKLMN', 'ClassaName.GHIJKLN', 'otherClahellorss.WORLD', 's3cr3tK3y.Z', 's3cr3tK3y.Z', 'ClassaName.GHIHJKLN', 'otherClahellorss.WORLD', 'My_classMYCLASS.HHHHHH', 'Python321_.GIMMETH3L00TZ!', 'My_classLMYCLASS.HHHHHH', 's3cr3tK3y.AbCdEfG', 'YetAnotherClass.GIMMETH3L00TZ!', 'Another_class.AbCdEfG', 'MExtendy_class.HHHHHH', 'My_class.ASDFGHJKL', 'Another_class.AbCdEfASDFGHJKLG', 'dddd.Hijklmno', 'ClassaNamse.GHIJKLMN', 'MyClass.AbcDEFg', '_.GIMMETH3L00TZ!', 'My_classLMYCLASS_.GIMMETH3L00TZ!', 's3cr3tK3y.My__classMYCLASS', '_.900000000', 's3cr3tK3y.Z', 'ClassaName.GHIJKLN', 'MYCLASS.ASDFGHJKL', 'MyClasss.UVWxYZ', 's3cr3tK3y.My__classMYCLASS', 'otherClahellorss.WORLD', 'My_classMYCLASS.HHHHHH', 'MYCLASMyClasssS.ASDFGHJKL', 'Another_class.AbCdEfG', 'AnotherClas_.WORLD', 'ClassaNamse.XXXXXXx', 'ddGHIHJKLNdd.Hijklmno', 'qwewrty.900000000', 'OPqrst.AbCdEfG', 'MExtendy_class.HHHHHH', 'AnotAbCdEfASDFGHJKLGher_class.AbCdEfASDFGHJKLG', 'My_class.HHHHHH', 'otherClahellorss.WORLD', 'ys3cr3tK3y.Z', 'YetAnotherClasUVWxYZs.DDDDDD', 'MnYetAnSlaassYCLASS.ASDFGHJKL', 'My_class.ASDFGHJKL', 'nYetAnotherCMYCLASSlassnothGIM!METYoetAnoEEErClassH3L00TZ!yoloerClass.ASDFGHJKL', 'ClassaName.GHIJKLN', 'Python321_.GIMMETH3L00TZ!', 'test.AbCdEfG', 'MMy_classMYCLASS.HHHHHH', 'x1UXXXXXXxVWxYZ.DDDDDD', 'Another_css.AbCdEfG', 'test.Z', 'My_class.HHHHHH', 'MMy_classMYCLASS.HHHHHH', 'My_class.ASDFGHJKL', 'MYCLASS.HHHHHH', 'My_classMYCLASS.HHHHHH', 'Another_class.AbCdEfG', 'ClassNaMqwertyy_classLMYCLA_e.GHIJKLMN', 'My__classMYCLASS.HHHHHH', 'My_class.HHHHHH', 'My_class.HHHHHH', 'ddGHIHJKLNdd.WORLD', 'OPqrst.AbCdEfG', 'ClassaNamse.GHIJKLN', 'otherClahellorss.WORLD', 'ClassaNamse.HHHHHH', 'MExty_class.E', 'MMExtendy_classy_classMYCLASS.HHHHHH', 's3cr3tKK3y.AbCdEfG', 'MExtendy_clasAnotherClasss.HHHHHH', 'My_class.ASDFGHJKL', 'JDLRFD.AbcDEFg', 'test.AbCdEfG', 'My_classLMYCLASS_nnYetAnotherCMYsCLASSUVWxYZlass.GIMMETH3L00TZ!', 'YoetAnoEEErClasslassaName.GHIJKLMN', 'MExtendyc_class.HHHHHH', 'MyClasssnYetAnotherCMYsCLASMqwertyy_classLMYCLASS_.UVWxYZ', 'My_class.ASDFGHJKL', 'MMy_clasMEAAAaAxtendy_classsMYCLASS.HHHHHH', '.okIWILL123', '$pecial_&_Cl@ss_name.YoUReXt', '123ThisIsTheClassName456.EX4', 'ThisIsTheClassName.ThisIsTheExtension', 'NoExtensionHasUpperCaseOrLowerCase.1234', '.DEF', 'SampleClass.eFG', 'SampleClass.AAA', 'SampleClass.aBc', 'SampleClass.AbC', 'UVWxYZ.WORLD', 'AAA.UVWxYZ', 'testing1.TESTING2', 'MyClass.AbcDEFg', 'AbCdEfG.AAAaA', 'UVWxYZ.WORLD', 'YetAnotherClass.DDDDDD', 'MyClass.UVWxYZ', 'My_class.ZZZZ', 'AbCdETESTING2fG.AAAaA', 'AbCdEfG.AAAaA', 'MYCLASS.WORLD', 'Tg1.TESTING2', 'fffffBbcdeAaaff.AAAaA', 'Another_class.AbCdEfG', 'Tg.TESTING2', 'TESTING2.AAAaA', 'M1235yClass.UVWxYZ', 'T1.TESTING2', 'MYCLASS.ASDFGHJKL', '1.TESTING2', 'TESTING2.AAAaA', 'T1.WORLD', 'TESTING2.AAAaA', 'OneMorCassNaame.AAAaA', 'testing1.GIMMETH3L00TZ!', 'M1235yClas.UVWxYZ', 'T1.TESTING2', 'T1.WORLD', 'MCyClass.UVWxYZ', '_.GIMMETH3L00TZ!', '1234GHIJKLMN5.TESTING2', 'YetAtEstin3gnotherClass.DDDDDD', 'Ye1234GHIJKLMN5tAnotherClass.DDDDDD', 'M1235yClass.UVWxYZ', 'Tg.UVWxYZ', 'Ye1234GHIJKLMN5tAnotherClass.DDDDDD', 'TESTINT2G2.AAAaA', '_Exteasdfghnd.GIMMETH3L00TZ!', 'T11.WORLD', 'AbCEdEfG.AAAaA', 'YetAtEstin3gnotherClass.DDDDDD', 'AbCdEfG.AAAaA', 'MyClMasss.DDDDDD', 'TgTg1.UVWxYZ', 'Another_class.AbCdEfG', 'YCBBBLASS.DDDDDD', 'T1.TEST', 'M12ss.UVWxYZ', 'BBBB.AAAaA', '_Exteasdfghnd.GIMMETH3L00TZ!', 'T1.WORLD']
    for i, (inp, exp) in enumerate(zip(inputs, results)):
        assertion(candidate(*inp), exp, 0)


check(Strongest_Extension)