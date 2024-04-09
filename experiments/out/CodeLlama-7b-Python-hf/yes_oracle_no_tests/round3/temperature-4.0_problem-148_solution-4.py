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
	Do not include these tokens in the code: ['
	'''


    pla = [
        "Mercury",
        "Venus",
        "Earth",
        "Mars",
        "Jupiter",
        "Saturn",
        "Uranus",
        "Neptune",
    ]
    pos = [
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
    ]
    planet1 = planet1.lower()
    planet2 = planet2.lower()
    if planet1 not in pla or planet2 not in pla:
        return ()
    else:
        for i in range(len(pla)):
            if pla[i] == planet1:
                planet1 = pos[i]
            if pla[i] == planet2:
                planet2 = pos[i]
        if planet1 > planet2:
            planet1, planet2 = planet2, planet1
        pla = pla[planet1:planet2]
        return tuple(pla)


print(bf("Jupiter", "Neptune"))
print(bf("Earth", "Mercury"))
print(bf("Mercury", "Uranus"))

