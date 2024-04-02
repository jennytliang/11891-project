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
    strongest_extension = ''
    strongest_strength = 0
    for extension in extensions : 
        extension_name = extension[-1::-1]
        cnt_capital = sum(char.isupper() for char in extension_name)
        cnt_small_letter = sum(char.islower() for char in extension_name)
        strength_extension = (cnt_capital - cnt_small_letter)
        if strength_extension >= strongest_strength : 
            strongest_strength = strength_extension
            strongest_extension = extension
    return class_name + "." + strongest_extension



if __name__ == '__main__':
    print("Example:")
    print(Strongest_Extension('my_class', ['SErviNGSliCes', 'Cheese', 'StuFfed']))
    print(Strongest_Extension('class', ['Class', 'Papa','Classroom',  'Paracetamol']))
    print(Strongest_Extension("my_class", ["aBC", "MyClass", "Awesome_class", "ABCClass"]))
  
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert Strongest_Extension("MyClass",
        ["Awesome", "A", "Also", "ASASASA", "Myclass", "AMC", "MyClass"]) == "Myclass.AMC"
    assert Strongest_Extension("Z", ["A"]) == "Z.A"
    assert Strongest_Extension("A", ["Z"]) == "A.Z"
