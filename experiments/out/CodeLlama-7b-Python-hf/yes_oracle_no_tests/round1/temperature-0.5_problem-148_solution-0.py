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

    planets =  ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

    if planet1 not in planets or planet2 not in planets:
        return ()

    if planets.index(planet1) > planets.index(planet2):
        return ()

    return tuple(planets[planets.index(planet1)+1:planets.index(planet2)])


if __name__ == '__main__':
    print("Example:")
    print(bf('Earth', 'Neptune'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert bf("Earth", "Neptune") == ("Venus",), "Earth Neptune"
    assert bf("Saturn", "Uranus") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn"), "Saturn Uranus"
    assert bf("Venus", "Venus") == (), "Same planets"
    assert bf("Mercury", "Uranus") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn"), "Mercury to Uranus"
    assert bf("Mars", "Earth") == ("Venus",), "Mars to Earth"
    assert bf("Jupiter", "Mars") == (), "Jupiter to Mars"
    print("Coding complete? Click 'Check' to earn cool rewards!")
