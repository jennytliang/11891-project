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
    
	Include these tokens in the code: if
	'''



    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptun"]
    planet1_index = planets.index(planet1)
    planet2_index = planets.index(planet2)

    if planet1_index == -1 or planet2_index == -1:
        return ()

    return planets[planet1_index+1:planet2_index]


print(bf("Jupiter", "Neptune"))
print(bf("Earth", "Mercury"))
print(bf("Mercury", "Uranus"))


# test.assert_equals(bf("Jupiter", "Neptune"), ("Saturn", "Uranus"))
# test.assert_equals(bf("Earth", "Mercury"), ("Venus"))
# test.assert_equals(bf("Mercury", "Uranus"), ("Venus", "Earth", "Mars", "Jupiter", "Saturn"))
# test.assert_equals(bf("Mercury", "Mercury"), ())
# test.assert_equals(bf("Jupiter", "Jupiter"), ())