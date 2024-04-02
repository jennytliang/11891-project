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

    planet1_idx = planets.index(planet1)
    planet2_idx = planets.index(planet2)

    if planet1_idx < planet2_idx:
        return tuple(planets[planet1_idx + 1: planet2_idx])
    else:
        return tuple(planets[planet2_idx + 1: planet1_idx])


assert (bf("Jupiter", "Neptune") == ("Saturn", "Uranus"))
assert (bf("Earth", "Mercury") == ("Venus",))
assert (bf("Mercury", "Uranus") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn"))
assert (bf("Jupiter", "Earth") == ())
assert (bf("Mercury", "Neptune") == ())
