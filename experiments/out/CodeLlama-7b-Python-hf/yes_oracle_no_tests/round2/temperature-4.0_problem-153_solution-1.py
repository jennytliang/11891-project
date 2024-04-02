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
    strongest_ext = ""
    for e in extensions:
        strength = len(e) - e.lower().count("a")
        if strength > strongest:
            strongest = strength
            strongest_ext = e
    return f"{class_name}.{strongest_ext}"


if __name__ == "__main__":
    print("Example:")
    print(Strongest_Extension("my_class", ["AA", "Be", "CC"]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert (
        Strongest_Extension("my_class", ["AA", "Be", "CC"]) == "my_class.AA"
    ), "First"
    assert (
        Strongest_Extension("Weird", ["Aa", "Be", "Cc"]) == "Weird.Be"
    ), "Second"
    assert (
        Strongest_Extension("Class", ["class", "a", "b", "c"]) == "Class.class"
    ), "Third"
    assert (
        Strongest_Extension("Weird", ["class", "A", "b", "C"]) == "Weird.A"
    ), "Fourth"
    print("Coding complete? Click 'Check' to earn cool rewards!")
