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
    
	Include these tokens in the code: : str ) -> int : C AP
	Do not include these tokens in the code: ):
	"""

    def stren(x):
        return (x.count('A') + x.count('E') + x.count('I') + x.count('O') + x.count('U')) - (x.count('a') + x.count('e') + x.count('i') + x.count('o') + x.count('u'))
    
    return f"{class_name}.{max(extensions, key=stren)}"


# Do not edit the below lines.
if __name__ == '__main__':
    assert Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'
    assert Strongest_Extension('my_class', ['AA', 'aa', 'aa', 'Be', 'CC']) == 'my_class.AA'
    assert Strongest_Extension('my_class', ['AA', 'aa', 'aa', 'Be', 'CC', 'aa']) == 'my_class.AA'
    assert Strongest_Extension('my_class', ['AA', 'aa', 'aa', 'Be', 'CC', 'aa', 'aa']) == 'my_class.AA'
    assert Strongest_Extension('my_class', ['AA', 'aa', 'aa', 'Be', 'CC', 'aa', 'aa', 'aa']) == 'my_class.AA'
    assert Strongest_Extension('my_class', ['AA', 'aa', 'aa', 'Be', 'CC', 'aa', 'aa', 'aa', 'aa']) == 'my_class.AA'
    assert Strongest_Extension('my_class', ['AA', 'aa', 'aa', 'Be', 'CC', 'aa', 'aa', 'aa', 'aa', 'aa']) == 'my_class.AA'
    assert Strongest_Extension('my_class', ['AA', 'aa', 'aa', 'Be', 'CC', 'aa', 'aa', 'aa', 'aa', 'aa', 'aa']) == 'my_class.AA'
    assert Strongest_Extension('my_class', ['AA', 'aa', 'aa', 'Be', 'CC', 'aa', 'aa