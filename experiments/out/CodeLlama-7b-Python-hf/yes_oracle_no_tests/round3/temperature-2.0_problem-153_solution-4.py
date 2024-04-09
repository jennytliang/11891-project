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
    strongest = None
    max_strength = 0
    for extension in extensions:
        strength = 0
        for letter in extension:
            if letter.isupper():
                strength += 1
            elif letter.islower():
                strength -= 1
        if strength > max_strength:
            max_strength = strength
            strongest = extension
    return class_name + "." + strongest


if __name__ == '__main__':
    print("Example:")
    print(Strongest_Extension('my_class', ['AA', 'Be', 'CC']))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert Strongest_Extension("MyClass", ["A", "b", "C"]) == "MyClass.A", "First"
    assert Strongest_Extension("MyClass", ["A", "a", "C"]) == "MyClass.C", "Second"
    assert Strongest_Extension("MyClass", ["my", "name", "is", "MyClass"]) == "MyClass.MyClass", "Third"
    assert Strongest_Extension("FIve", ["Five", "five", "fivE", "FiVe", "fIvE", "FiVe"]) == "FIve.Five", "Fourth"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
