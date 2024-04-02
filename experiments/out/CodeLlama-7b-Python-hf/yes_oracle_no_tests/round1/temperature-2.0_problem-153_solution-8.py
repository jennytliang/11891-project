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
    strongest_extension = extensions[0]
    strongest_extension_strength = strength(strongest_extension)
    for extension in extensions:
        strength_extension = strength(extension)
        if strength_extension > strongest_extension_strength:
            strongest_extension = extension
            strongest_extension_strength = strength_extension
    return class_name + '.' + strongest_extension

def strength(s):
    return len(list(filter(lambda c: c.isupper(), s))) - len(list(filter(lambda c: c.islower(), s)))


if __name__ == '__main__':
    print("Example:")
    print(Strongest_Extension('my_class', ['AA', 'Be', 'CC']))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert Strongest_Extension("my_class", ["AA", "Be", "CC"]) == "my_class.AA", "First"
    assert Strongest_Extension("my_class", ["AA", "Be", "Cc"]) == "my_class.CC", "Second"
    assert Strongest_Extension("my_class", ["aA", "be", "cc"]) == "my_class.aA", "Third"
    assert Strongest_Extension("my_class", ["Aa", "be", "cc"]) == "my_class.be", "Four"
    assert Strongest_Extension("my_class", ["aa", "Be", "CC"]) == "my_class.Be", "Fifth"
    print("Coding complete? Click 'Check' to earn cool rewards!")
