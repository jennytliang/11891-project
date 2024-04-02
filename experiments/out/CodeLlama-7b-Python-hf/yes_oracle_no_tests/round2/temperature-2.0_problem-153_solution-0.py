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
    strongest = 0
    strongest_ext = ''
    for ext in extensions:
        strength_ext = 0
        for c in ext:
            if c.isupper():
                strength_ext += 1
            elif c.islower():
                strength_ext -= 1
        if strength_ext > strongest:
            strongest = strength_ext
            strongest_ext = ext
    return class_name + '.' + strongest_ext


if __name__ == '__main__':
    print("Example:")
    print(Strongest_Extension('my_class', ['AA', 'Be', 'CC']))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert Strongest_Extension("MyClass", ["A", "b", "C"]) == "MyClass.A", "First"
    assert Strongest_Extension("MyClass", ["_", "B", "c", "D", "E"]) == "MyClass._", "Second"
    assert Strongest_Extension("MyClass", ["", "B", "C", "D", "E"]) == "MyClass.B", "Third"
    assert Strongest_Extension("MyClass", ["Z", "B", "C", "D", "E"]) == "MyClass.Z", "Fourth"
    assert Strongest_Extension("MyClass", ["", "", "", "D", "E"]) == "MyClass.D", "Fifth"
    assert Strongest_Extension("MyClass", ["", "B", "C", "", ""]) == "MyClass.B", "Sixth"
    assert Strongest_Extension("MyClass", ["", "a", "A", "b", "c"]) == "MyClass.a", "Seventh"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
