def bf(planet1, planet2):
    '''
    There are eight planets in our solar system: the closerst to the Sun 
    is Mercury, the next one is Venus, then Earth, Mars, Jupiter, Saturn, 
    Uranus, Neptune.
    Write a function that takes two planet names as strings planet1 and planet2. 
    The function should return a tuple containing all planets whose orbits are 
    located between the orbit of planet1 and the orbit of planet2, sorted by 
    the proximity to the sun. 
    The function should return an empty tuple if planet1 or planet2
    are not correct planet names. 
    Examples
    bf("Jupiter", "Neptune") ==> ("Saturn", "Uranus")
    bf("Earth", "Mercury") ==> ("Venus")
    bf("Mercury", "Uranus") ==> ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
    
	Include these tokens in the code: ["
	Do not include these tokens in the code: ("
	'''


    pla1 = planet1
    pla2 = planet2
    if pla1 == "Mercury":
        if pla2 == "Venus":
            return ("Mercury", "Venus")
        elif pla2 == "Earth":
            return ("Mercury", "Venus", "Earth")
        elif pla2 == "Mars":
            return ("Mercury", "Venus", "Earth", "Mars")
        elif pla2 == "Jupiter":
            return ("Mercury", "Venus", "Earth", "Mars", "Jupiter")
        elif pla2 == "Saturn":
            return ("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn")
        elif pla2 == "Uranus":
            return ("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")
        elif pla2 == "Neptune":
            return ("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")
        else:
            return tuple()
    elif pla1 == "Venus":
        if pla2 == "Earth":
            return ("Venus", "Earth")
        elif pla2 == "Mars":
            return ("Venus", "Earth", "Mars")
        elif pla2 == "Jupiter":
            return ("Venus", "Earth", "Mars", "Jupiter")
        elif pla2 == "Saturn":
            return ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
        elif pla2 == "Uranus":
            return ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")
        elif pla2 == "Neptune":
            return ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "U