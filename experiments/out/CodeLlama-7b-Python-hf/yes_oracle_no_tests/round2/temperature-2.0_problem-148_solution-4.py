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
    
	Include these tokens in the code: tuple ()
	'''


    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

    if planet1 not in planets or planet2 not in planets:
        return ()
    else:
        planet1index = planets.index(planet1)
        planet2index = planets.index(planet2)

        if planet1index > planet2index:
            planet1index, planet2index = planet2index, planet1index

        return tuple(planets[planet1index+1:planet2index])


print(bf("Jupiter", "Neptune"))  # ("Saturn", "Uranus")
print(bf("Earth", "Mercury"))  # ("Venus")
print(bf("Mercury", "Uranus"))  # ("Venus", "Earth", "Mars", "Jupiter", "Saturn")











































































