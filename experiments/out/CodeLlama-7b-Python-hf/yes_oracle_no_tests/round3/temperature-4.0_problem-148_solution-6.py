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
    
	Include these tokens in the code: une
	Do not include these tokens in the code: u en
	'''


    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    planet_index = {"Mercury": 0, "Venus": 1, "Earth": 2, "Mars": 3, "Jupiter": 4, "Saturn": 5, "Uranus": 6, "Neptune": 7}
    
    if planet1 not in planets or planet2 not in planets:
        return ()
    
    if planet_index[planet1] < planet_index[planet2]:
        return tuple(planets[planet_index[planet1] + 1:planet_index[planet2]])
    else:
        return tuple(planets[planet_index[planet2] + 1:planet_index[planet1]])


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert bf("Jupiter", "Neptune") == ("Saturn", "Uranus"), "Jupiter Neptune"
    assert bf("Saturn", "Uranus") == (), "Saturn Uranus"
    assert bf("Earth", "Mercury") == ("Venus",), "Earth Mercury"
    assert bf("Venus", "Earth") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn"), "Venus Earth"
    assert bf("Mars", "Venus") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn"), "Mars Venus"
    assert bf("Uranus", "Neptune") == ("Saturn",), "Uranus Neptune"
    assert bf("Neptune", "Saturn") == ("Saturn",), "Neptune Saturn"
    assert bf("Saturn", "Mercury") == (), "Saturn Mercury"
    assert bf("Venus", "Mercury") == ("Venus",), "