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
    
	Include these tokens in the code: def strength ( s : str ) -> int :
	"""
    import math
    def strength(s):
        return s.count('A') - s.count('a')

    strongest = extensions[0]
    for extension in extensions:
        if strength(extension) > strength(strongest):
            strongest = extension
    return f'{class_name}.{strongest}'


def test_function():
    assert Strongest_Extension("my_class", ['AA', 'Be', 'CC']) == 'my_class.AA'
    assert Strongest_Extension("my_class", ['AA', 'aa', 'CC']) == 'my_class.AA'
    assert Strongest_Extension("my_class", ['aA', 'aa', 'Aa']) == 'my_class.aA'
    assert Strongest_Extension("my_class", ['aA', 'AA', 'aa']) == 'my_class.aA'
    assert Strongest_Extension("my_class", ['AA', 'aa', 'aA']) == 'my_class.aA'
    assert Strongest_Extension("my_class", ['Aa', 'aA', 'aa']) == 'my_class.Aa'
    assert Strongest_Extension("my_class", ['AA', 'aa', 'aA', 'aA']) == 'my_class.AA'
    assert Strongest_Extension("my_class", ['AA', 'Aa', 'aa']) == 'my_class.AA'
    assert Strongest_Extension("my_class", ['AA', 'Aa', 'Aa']) == 'my_class.Aa'
    assert Strongest_Extension("my_class", ['Aa', 'Aa', 'Aa']) == 'my_class.Aa'
    assert Strongest_Extension("my_class", ['AA', 'aa', 'aa']) == 'my_class.AA'
    assert Strongest_Extension("my_class", ['aa', 'aa', 'aa']) == 'my_class.aa'
    assert Strongest_Extension("my_class", ['aa', 'aa', 'AA']) == 'my_class.AA'
    assert