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
    # your code here
    strongest = 0
    strongest_name = ""
    for extension in extensions:
        cap = 0
        sm = 0
        for c in extension:
            if c.isupper():
                cap += 1
            elif c.islower():
                sm += 1
            else:
                continue
        strength = cap - sm
        if strength > strongest:
            strongest = strength
            strongest_name = extension
    return class_name + "." + strongest_name


if __name__ == '__main__':
    print("Example:")
    print(Strongest_Extension('my_class', ['AA', 'Be', 'CC']))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert Strongest_Extension("my_class", ["AA", "Be", "CC"]) == "my_class.AA", "First"
    assert Strongest_Extension("my_class", ["AAA", "Be", "CC"]) == "my_class.AAA", "Second"
    assert Strongest_Extension("my_class", ["BA", "Be", "CA"]) == "my_class.BA", "Third"
    assert Strongest_Extension("my_class", ["A", "a"]) == "my_class.A", "Strength"
    assert Strongest_Extension("my_class", ["Aa", "aa", "A"]) == "my_class.Aa", "Equal"
    print("Coding complete? Click 'Check' to earn cool rewards!")